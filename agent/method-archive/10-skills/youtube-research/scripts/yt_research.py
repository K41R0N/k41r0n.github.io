#!/usr/bin/env python3
"""
yt_research.py — collect, enrich, score and export YouTube videos for a query.

Ranks videos by *trust and engagement quality*, not raw view counts:
  relevance (R) · channel authority (A) · tier-normalised engagement (E)
  · reach (V, damped) · recency (T) · format fit (F)
with mode-specific weights (topic | learn | expert | brand) and a curated
trusted-channel layer (boost / block lists) on top of the algorithmic score.

Data engine: yt-dlp (no API key). Optional accelerator: the official YouTube
Data API v3 is used automatically when YOUTUBE_API_KEY is set (--provider auto).

Sub-commands
  run          search → enrich → channel-enrich → score → export (+ optional transcripts/comments)
  rescore      re-score an existing run folder offline (new mode / weights / lists)
  transcripts  fetch transcripts for the top N videos of a run
  comments     fetch + pre-analyse comments for the top N videos of a run
  doctor       check yt-dlp, network reachability, cookies, API key

Everything is written to a run folder so collection can happen on one machine
(e.g. Claude Code on a laptop) and analysis on another (e.g. Cowork / claude.ai).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import os
import random
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
DEFAULT_TRUSTED = SKILL_ROOT / "references" / "trusted-channels.json"
USER_TRUSTED = Path(os.environ.get("YT_RESEARCH_TRUSTED", Path.home() / ".config" / "youtube-research" / "trusted-channels.json"))
DEFAULT_OUT_ROOT = Path(os.environ.get("YT_RESEARCH_RUNS", Path.cwd() / "youtube-research-runs"))

# --------------------------------------------------------------------------- #
# Methodology constants (see references/scoring.md for the rationale)
# --------------------------------------------------------------------------- #
MODES = ("topic", "learn", "expert", "brand")

MODE_WEIGHTS = {
    #        R     A     E     V     T     F
    "topic":  dict(R=0.30, A=0.25, E=0.20, V=0.10, T=0.10, F=0.05),
    "learn":  dict(R=0.30, A=0.25, E=0.20, V=0.05, T=0.05, F=0.15),
    "expert": dict(R=0.25, A=0.35, E=0.15, V=0.05, T=0.10, F=0.10),
    "brand":  dict(R=0.35, A=0.10, E=0.15, V=0.15, T=0.20, F=0.05),
}
HALF_LIFE_DAYS = {"topic": 365, "learn": 730, "expert": 540, "brand": 180}

# Median (likes+comments)/views by subscriber tier — SociaVault 2026 study of 75k channels.
ER_BENCHMARK_PCT = {"nano": 5.23, "micro": 3.74, "mid": 2.81, "macro": 2.12, "mega": 1.41, "unknown": 3.06}
TIER_BOUNDS = [("nano", 10_000), ("micro", 50_000), ("mid", 100_000), ("macro", 500_000), ("mega", float("inf"))]

VARIANT_TEMPLATES = {
    "topic":  ["{q}", "{q} explained", "{q} analysis", "{q} {year}"],
    "learn":  ["{q}", "{q} explained", "what is {q}", "{q} tutorial", "{q} deep dive", "{q} for beginners"],
    "expert": ["{q}", "{q} talk", "{q} conference", "{q} interview", "{q} panel", "{q} podcast"],
    "brand":  ["{q}", "{q} review", "{q} explained", "{q} vs", "{q} risks", "{q} news"],
}
# Modes where a date-sorted search is added to surface fresh content the relevance sort hides.
DATE_SORT_MODES = {"topic", "brand"}

STOPWORDS = set("""a an and are as at be by for from how in into is it its of on or that the this to vs with what
why when where who which will would should could can does do did your you we our us they them their than then
best top new latest guide tutorial explained review 2024 2025 2026""".split())

SHILL_PATTERNS = [r"\b100x\b", r"\bgiveaway\b", r"\bairdrop\b", r"\bguaranteed\b", r"\bget rich\b", r"\bto the moon\b",
                  r"\bfree money\b", r"\bpump\b", r"\bnext bitcoin\b", r"\b1000x\b", r"\bmillionaire\b", r"🚀🚀"]
INSTITUTION_PATTERNS = [r"\buniversity\b", r"\binstitute\b", r"\bfoundation\b", r"\bconference\b", r"\bsummit\b",
                        r"\bdevcon\b", r"\bschool of\b", r"\bresearch\b", r"\bofficial\b", r"\bcentral bank\b"]

# tiny sentiment lexicons for the *heuristic* comment pre-pass (Claude does the real reading)
POS_WORDS = set("""great amazing love excellent best helpful clear thanks thank awesome fantastic brilliant good
useful insightful solid legit trust trustworthy recommend recommended impressive bullish safe reliable easy""".split())
NEG_WORDS = set("""scam rug fraud bad worst hate terrible awful misleading shill paid wrong lie lies lying fake
risky dangerous warning avoid loss lost dump bearish confusing boring broken clickbait ponzi unsafe sketchy""".split())
NEGATORS = {"not", "no", "never", "isn't", "isnt", "don't", "dont", "doesn't", "doesnt", "wasn't", "wasnt", "hardly"}


# --------------------------------------------------------------------------- #
# Small utilities
# --------------------------------------------------------------------------- #
def log(msg: str) -> None:
    print(f"[yt-research] {msg}", file=sys.stderr, flush=True)


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def slugify(s: str, n: int = 40) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n] or "query"


def tokenize(s: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9$]+", (s or "").lower()) if len(t) > 1 and t not in STOPWORDS]


def term_in(term: str, tokens: set[str]) -> bool:
    if term in tokens:
        return True
    if len(term) >= 4:  # crude stemming: prefix match both ways
        return any(t.startswith(term) or term.startswith(t) for t in tokens if len(t) >= 4)
    return False


def parse_iso_duration(s: str | None) -> int | None:
    if not s:
        return None
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s)
    if not m:
        return None
    d, h, mi, se = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def iso_date_from_yyyymmdd(s: str | None) -> str | None:
    if not s or len(str(s)) != 8:
        return None
    s = str(s)
    return f"{s[:4]}-{s[4:6]}-{s[6:]}"


def age_days(published: str | None, today: dt.date | None = None) -> float | None:
    if not published:
        return None
    try:
        d = dt.date.fromisoformat(published[:10])
    except ValueError:
        return None
    return max(0.0, ((today or dt.date.today()) - d).days + 0.5)


def tier_for(subs: int | None) -> str:
    if subs is None:
        return "unknown"
    for name, bound in TIER_BOUNDS:
        if subs < bound:
            return name
    return "mega"


def fmt_int(n) -> str:
    return f"{n:,}" if isinstance(n, (int, float)) and n is not None else "—"


def fmt_dur(sec) -> str:
    if sec is None:
        return "—"
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def norm_name(s: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def norm_handle(s: str | None) -> str:
    s = (s or "").strip().lower()
    return s if s.startswith("@") else ("@" + s if s else "")


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Trusted-channel layer
# --------------------------------------------------------------------------- #
class TrustedLists:
    """Loads the skill's seed list plus the user's override file; matches by handle or normalised name."""

    def __init__(self, paths: list[Path], domains: list[str] | None):
        self.by_handle: dict[str, tuple[str, str]] = {}   # handle -> (tier, domain)
        self.by_name: dict[str, tuple[str, str]] = {}
        self.blocked_handles: dict[str, str] = {}
        self.blocked_names: dict[str, str] = {}
        self.shill_patterns = list(SHILL_PATTERNS)
        self.loaded_from: list[str] = []
        self.entries_total = 0
        self.matched: set[str] = set()
        for p in paths:
            data = read_json(p)
            if not data:
                continue
            self.loaded_from.append(str(p))
            self.shill_patterns += data.get("shill_patterns", [])
            for dom, lists in (data.get("domains") or {}).items():
                if domains and dom not in domains:
                    continue
                for tier_key, tier in (("tier_a", "A"), ("tier_b", "B")):
                    for e in lists.get(tier_key, []):
                        self.entries_total += 1
                        h, n = norm_handle(e.get("handle")), norm_name(e.get("name"))
                        if h:
                            self.by_handle.setdefault(h, (tier, dom))
                        if n:
                            self.by_name.setdefault(n, (tier, dom))
                for e in lists.get("blocked", []):
                    self.entries_total += 1
                    h, n = norm_handle(e.get("handle")), norm_name(e.get("name"))
                    if h:
                        self.blocked_handles[h] = dom
                    if n:
                        self.blocked_names[n] = dom

    def lookup(self, handle: str | None, name: str | None) -> tuple[str | None, str | None]:
        """Returns (status, domain) where status in {'A','B','blocked',None}."""
        h, n = norm_handle(handle), norm_name(name)
        if h and h in self.blocked_handles:
            self.matched.add(h)
            return "blocked", self.blocked_handles[h]
        if n and n in self.blocked_names:
            self.matched.add(n)
            return "blocked", self.blocked_names[n]
        if h and h in self.by_handle:
            self.matched.add(h)
            return self.by_handle[h]
        if n and n in self.by_name:
            self.matched.add(n)
            return self.by_name[n]
        return None, None

    def shill_hits(self, *texts: str) -> list[str]:
        blob = " ".join(t for t in texts if t).lower()
        return [p for p in self.shill_patterns if re.search(p, blob)]


# --------------------------------------------------------------------------- #
# Providers
# --------------------------------------------------------------------------- #
class BlockedError(RuntimeError):
    """Raised when YouTube is unreachable (egress policy) or demands a sign-in / bot check."""


def _is_bot_check(msg: str) -> bool:
    m = msg.lower()
    return "sign in to confirm" in m or "not a bot" in m or "confirm you’re not a bot" in m


def _is_network_block(msg: str) -> bool:
    m = msg.lower()
    return any(s in m for s in ("403", "tunnel", "proxy", "unable to download webpage", "failed to resolve",
                                "connection refused", "name or service not known", "network is unreachable"))


class _QuietLogger:
    """Swallows yt-dlp's console chatter but keeps the last error so a failure can be explained."""

    def __init__(self):
        self.last_error = None
        self.warnings: list[str] = []

    def debug(self, msg):  # yt-dlp routes info through debug when quiet
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        self.warnings.append(str(msg))

    def error(self, msg):
        self.last_error = str(msg)


class YtdlpProvider:
    name = "ytdlp"

    def __init__(self, cookies_from_browser: str | None = None, cookie_file: str | None = None, sleep: float = 0.5):
        try:
            import yt_dlp  # noqa: F401
        except ImportError as e:  # pragma: no cover
            raise SystemExit("yt-dlp is not installed. Run: pip install -U yt-dlp") from e
        self.cookies_from_browser = cookies_from_browser
        self.cookie_file = cookie_file
        self.sleep = sleep
        self.logger = _QuietLogger()

    def _opts(self, **extra) -> dict:
        # ignoreerrors must stay False: with True, yt-dlp logs a block/bot-check and returns an
        # empty result, which would look like "no videos" instead of "YouTube is unreachable".
        opts = {
            "quiet": True, "no_warnings": True, "noprogress": True, "skip_download": True,
            "ignoreerrors": False, "ignore_no_formats_error": True, "noplaylist": True,
            "sleep_interval_requests": self.sleep, "logger": self.logger,
            "extractor_args": {"youtube": {"skip": ["dash", "hls", "translated_subs"]}},
        }
        if self.cookies_from_browser:
            opts["cookiesfrombrowser"] = tuple(self.cookies_from_browser.split(":"))
        if self.cookie_file:
            opts["cookiefile"] = self.cookie_file
        opts.update(extra)
        return opts

    def _extract(self, url: str, **extra):
        import yt_dlp
        from yt_dlp.utils import DownloadError
        try:
            with yt_dlp.YoutubeDL(self._opts(**extra)) as ydl:
                return ydl.extract_info(url, download=False)
        except DownloadError as e:
            msg = str(e)
            if _is_bot_check(msg):
                raise BlockedError("YouTube asked for a sign-in / bot check. Re-run with --cookies-from-browser "
                                   "chrome (or firefox/edge/brave), lower --workers, or run from a residential IP.") from e
            if _is_network_block(msg):
                raise BlockedError("YouTube is unreachable from this machine (network/egress policy). Run the "
                                   "collection locally (Claude Code) and analyse the run folder here.") from e
            raise

    # -- search -----------------------------------------------------------
    def search(self, query: str, n: int, sort: str = "relevance") -> list[dict]:
        prefix = "ytsearchdate" if sort == "date" else "ytsearch"
        info = self._extract(f"{prefix}{n}:{query}", extract_flat="in_playlist", noplaylist=False)
        out = []
        for i, e in enumerate((info or {}).get("entries") or []):
            if not e or not e.get("id"):
                continue
            out.append({
                "id": e["id"], "rank": i, "title": e.get("title"), "channel": e.get("channel") or e.get("uploader"),
                "channel_id": e.get("channel_id"), "channel_handle": e.get("uploader_id") if str(e.get("uploader_id", "")).startswith("@") else None,
                "duration_s": e.get("duration"), "views": e.get("view_count"), "live_status": e.get("live_status"),
                "url": e.get("url") or f"https://www.youtube.com/watch?v={e['id']}",
            })
        return out

    # -- video details ------------------------------------------------------
    def video_details(self, ids: list[str], workers: int = 4) -> list[dict]:
        results: list[dict] = []
        errors = 0

        def one(vid: str):
            time.sleep(random.uniform(0, 0.4))
            return self._extract(f"https://www.youtube.com/watch?v={vid}")

        with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
            futs = {ex.submit(one, v): v for v in ids}
            for f in as_completed(futs):
                vid = futs[f]
                try:
                    info = f.result()
                except BlockedError:
                    raise
                except Exception as e:  # noqa: BLE001
                    errors += 1
                    log(f"  ! {vid}: {type(e).__name__}: {str(e)[:120]}")
                    continue
                if info:
                    results.append(self._normalise_video(info))
        if errors:
            log(f"  {errors} video(s) failed extraction")
        return results

    @staticmethod
    def _normalise_video(i: dict) -> dict:
        subs_manual = list((i.get("subtitles") or {}).keys())
        subs_auto = list((i.get("automatic_captions") or {}).keys())
        dur = i.get("duration")
        url = i.get("webpage_url") or f"https://www.youtube.com/watch?v={i.get('id')}"
        handle = i.get("uploader_id") if str(i.get("uploader_id", "")).startswith("@") else None
        return {
            "id": i.get("id"), "url": url, "title": i.get("title"), "description": (i.get("description") or "")[:1500],
            "channel": i.get("channel") or i.get("uploader"), "channel_id": i.get("channel_id"), "channel_handle": handle,
            "channel_subs": i.get("channel_follower_count"), "channel_verified": i.get("channel_is_verified"),
            "duration_s": dur, "views": i.get("view_count"), "likes": i.get("like_count"), "comments_count": i.get("comment_count"),
            "published": iso_date_from_yyyymmdd(i.get("upload_date")) or (dt.datetime.utcfromtimestamp(i["timestamp"]).date().isoformat() if i.get("timestamp") else None),
            "tags": (i.get("tags") or [])[:30], "categories": i.get("categories") or [],
            "chapters": [{"title": c.get("title"), "start_s": c.get("start_time")} for c in (i.get("chapters") or [])][:60],
            "language": i.get("language"), "live_status": i.get("live_status"), "was_live": bool(i.get("was_live")),
            "is_short": bool(dur and dur <= 60) or "/shorts/" in url,
            "has_captions": bool(subs_manual), "has_auto_captions": bool(subs_auto),
            "caption_langs": sorted(set(subs_manual + subs_auto))[:12],
            "_caption_tracks": {"manual": i.get("subtitles") or {}, "auto": i.get("automatic_captions") or {}},
        }

    # -- channel recent uploads -------------------------------------------------
    def channel_recent(self, channel_id: str, n: int = 20) -> dict | None:
        info = self._extract(f"https://www.youtube.com/channel/{channel_id}/videos",
                             extract_flat="in_playlist", noplaylist=False, playlist_items=f"1:{n}")
        if not info:
            return None
        entries = [e for e in (info.get("entries") or []) if e]
        return {
            "id": channel_id, "name": info.get("channel") or info.get("uploader"),
            "handle": info.get("uploader_id") if str(info.get("uploader_id", "")).startswith("@") else None,
            "subs": info.get("channel_follower_count"), "verified": info.get("channel_is_verified"),
            "video_count": info.get("playlist_count"), "description": (info.get("description") or "")[:400],
            "recent": [{"id": e.get("id"), "title": e.get("title"), "views": e.get("view_count"),
                        "duration_s": e.get("duration"), "live_status": e.get("live_status")} for e in entries],
        }

    # -- comments -------------------------------------------------------------
    def comments(self, video_id: str, n: int = 60) -> list[dict]:
        info = self._extract(f"https://www.youtube.com/watch?v={video_id}", getcomments=True,
                             extractor_args={"youtube": {"skip": ["dash", "hls", "translated_subs"],
                                                         "max_comments": [str(n), str(n), "0", "0"],
                                                         "comment_sort": ["top"]}})
        out = []
        for c in (info or {}).get("comments") or []:
            out.append({"id": c.get("id"), "text": c.get("text"), "likes": c.get("like_count") or 0,
                        "author": c.get("author"), "author_is_uploader": bool(c.get("author_is_uploader")),
                        "author_is_verified": bool(c.get("author_is_verified")), "time_text": c.get("time_text"),
                        "timestamp": c.get("timestamp")})
        return out

    # -- transcript -------------------------------------------------------------
    def transcript(self, video: dict, lang: str = "en") -> dict | None:
        import yt_dlp
        tracks = video.get("_caption_tracks")
        if not tracks:
            info = self._extract(f"https://www.youtube.com/watch?v={video['id']}")
            if not info:
                return None
            tracks = {"manual": info.get("subtitles") or {}, "auto": info.get("automatic_captions") or {}}
        chosen, kind = None, None
        for k in ("manual", "auto"):
            pool = tracks.get(k) or {}
            key = pick_lang(pool.keys(), lang, video.get("language"))
            if key:
                for fmt in pool[key]:
                    if fmt.get("ext") == "json3" and fmt.get("url"):
                        chosen, kind = (fmt["url"], key), k
                        break
            if chosen:
                break
        if not chosen:
            return None
        url, key = chosen
        with yt_dlp.YoutubeDL(self._opts()) as ydl:
            raw = ydl.urlopen(url).read()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return None
        segs = json3_to_segments(data)
        return {"video_id": video["id"], "lang": key, "kind": kind, "segments": segs,
                "text": segments_to_text(segs), "words": sum(len(s["text"].split()) for s in segs)}


def pick_lang(keys, wanted: str, original: str | None) -> str | None:
    keys = list(keys)
    if not keys:
        return None
    wanted = (wanted or "en").lower()
    for k in keys:
        if k.lower() == wanted:
            return k
    for k in keys:
        if k.lower().startswith(wanted + "-") or k.lower() == wanted + "-orig":
            return k
    if original:
        for k in keys:
            if k.lower().startswith(original.lower()):
                return k
    return keys[0]


def json3_to_segments(data: dict, block_s: int = 30) -> list[dict]:
    """Collapse YouTube json3 caption events into ~30-second blocks with a start timestamp."""
    segs, cur_start, cur_words = [], None, []
    for ev in data.get("events") or []:
        t = (ev.get("tStartMs") or 0) / 1000.0
        text = "".join(s.get("utf8", "") for s in (ev.get("segs") or [])).replace("\n", " ").strip()
        if not text:
            continue
        if cur_start is None:
            cur_start = t
        if t - cur_start >= block_s and cur_words:
            segs.append({"start_s": round(cur_start, 1), "text": " ".join(cur_words)})
            cur_start, cur_words = t, []
        cur_words.append(text)
    if cur_words:
        segs.append({"start_s": round(cur_start or 0, 1), "text": " ".join(cur_words)})
    return segs


def segments_to_text(segs: list[dict]) -> str:
    return "\n".join(f"[{fmt_dur(int(s['start_s']))}] {s['text']}" for s in segs)


class ApiProvider:
    """YouTube Data API v3 — used when YOUTUBE_API_KEY is set. 100 search calls/day; other calls 1 unit per batch."""
    name = "api"
    BASE = "https://www.googleapis.com/youtube/v3/"

    def __init__(self, key: str, ytdlp_fallback: YtdlpProvider | None = None):
        self.key = key
        self.ytdlp = ytdlp_fallback

    def _get(self, method: str, **params) -> dict:
        params["key"] = self.key
        url = self.BASE + method + "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "ignore")[:400]
            if e.code == 403 and "quota" in body.lower():
                raise BlockedError("YouTube API quota exhausted for today (resets midnight Pacific). Use --provider ytdlp.") from e
            raise BlockedError(f"YouTube API HTTP {e.code}: {body}") from e
        except urllib.error.URLError as e:
            raise BlockedError(f"Cannot reach googleapis.com ({e.reason}). Ask your admin to whitelist www.googleapis.com.") from e

    def search(self, query: str, n: int, sort: str = "relevance", published_after: str | None = None) -> list[dict]:
        data = self._get("search", part="snippet", q=query, type="video", maxResults=min(50, n),
                         order="date" if sort == "date" else "relevance",
                         publishedAfter=(published_after + "T00:00:00Z") if published_after else None)
        out = []
        for i, it in enumerate(data.get("items", [])):
            vid = (it.get("id") or {}).get("videoId")
            if not vid:
                continue
            sn = it.get("snippet", {})
            out.append({"id": vid, "rank": i, "title": sn.get("title"), "channel": sn.get("channelTitle"),
                        "channel_id": sn.get("channelId"), "channel_handle": None, "duration_s": None, "views": None,
                        "live_status": sn.get("liveBroadcastContent"), "url": f"https://www.youtube.com/watch?v={vid}"})
        return out

    def video_details(self, ids: list[str], workers: int = 4) -> list[dict]:
        out = []
        for i in range(0, len(ids), 50):
            data = self._get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]), maxResults=50)
            for it in data.get("items", []):
                sn, st, cd = it.get("snippet", {}), it.get("statistics", {}), it.get("contentDetails", {})
                dur = parse_iso_duration(cd.get("duration"))
                out.append({
                    "id": it["id"], "url": f"https://www.youtube.com/watch?v={it['id']}", "title": sn.get("title"),
                    "description": (sn.get("description") or "")[:1500], "channel": sn.get("channelTitle"),
                    "channel_id": sn.get("channelId"), "channel_handle": None, "channel_subs": None, "channel_verified": None,
                    "duration_s": dur, "views": int(st["viewCount"]) if st.get("viewCount") else None,
                    "likes": int(st["likeCount"]) if st.get("likeCount") else None,
                    "comments_count": int(st["commentCount"]) if st.get("commentCount") else None,
                    "published": (sn.get("publishedAt") or "")[:10] or None, "tags": (sn.get("tags") or [])[:30],
                    "categories": [sn.get("categoryId")] if sn.get("categoryId") else [], "chapters": [],
                    "language": sn.get("defaultAudioLanguage") or sn.get("defaultLanguage"),
                    "live_status": sn.get("liveBroadcastContent"), "was_live": False,
                    "is_short": bool(dur and dur <= 60), "has_captions": cd.get("caption") == "true",
                    "has_auto_captions": None, "caption_langs": [],
                })
        # channel stats in one batch
        cids = sorted({v["channel_id"] for v in out if v.get("channel_id")})
        chan = {}
        for i in range(0, len(cids), 50):
            data = self._get("channels", part="snippet,statistics", id=",".join(cids[i:i + 50]), maxResults=50)
            for it in data.get("items", []):
                st = it.get("statistics", {})
                chan[it["id"]] = {"subs": None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0) or 0),
                                  "handle": (it.get("snippet", {}).get("customUrl") or None)}
        for v in out:
            c = chan.get(v.get("channel_id"))
            if c:
                v["channel_subs"], v["channel_handle"] = c["subs"], c["handle"]
        return out

    def channel_recent(self, channel_id: str, n: int = 20) -> dict | None:
        data = self._get("channels", part="snippet,statistics,contentDetails", id=channel_id)
        items = data.get("items", [])
        if not items:
            return None
        it = items[0]
        st, sn = it.get("statistics", {}), it.get("snippet", {})
        uploads = it.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads")
        recent = []
        if uploads:
            pl = self._get("playlistItems", part="contentDetails", playlistId=uploads, maxResults=min(50, n))
            vids = [p["contentDetails"]["videoId"] for p in pl.get("items", []) if p.get("contentDetails", {}).get("videoId")]
            if vids:
                vd = self._get("videos", part="snippet,statistics,contentDetails", id=",".join(vids), maxResults=50)
                for v in vd.get("items", []):
                    recent.append({"id": v["id"], "title": v.get("snippet", {}).get("title"),
                                   "views": int(v.get("statistics", {}).get("viewCount", 0) or 0),
                                   "duration_s": parse_iso_duration(v.get("contentDetails", {}).get("duration")),
                                   "live_status": v.get("snippet", {}).get("liveBroadcastContent")})
        return {"id": channel_id, "name": sn.get("title"), "handle": sn.get("customUrl"),
                "subs": None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0) or 0),
                "verified": None, "video_count": int(st.get("videoCount", 0) or 0) or None,
                "created": (sn.get("publishedAt") or "")[:10] or None, "description": (sn.get("description") or "")[:400],
                "recent": recent}

    def comments(self, video_id: str, n: int = 60) -> list[dict]:
        out, token = [], None
        while len(out) < n:
            data = self._get("commentThreads", part="snippet", videoId=video_id, order="relevance",
                             maxResults=min(100, n - len(out)), textFormat="plainText", pageToken=token)
            for it in data.get("items", []):
                c = it.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
                out.append({"id": it.get("id"), "text": c.get("textOriginal") or c.get("textDisplay"),
                            "likes": c.get("likeCount") or 0, "author": c.get("authorDisplayName"),
                            "author_is_uploader": False, "author_is_verified": False,
                            "time_text": (c.get("publishedAt") or "")[:10], "timestamp": None})
            token = data.get("nextPageToken")
            if not token:
                break
        return out[:n]

    def transcript(self, video: dict, lang: str = "en") -> dict | None:
        if self.ytdlp:
            return self.ytdlp.transcript({k: v for k, v in video.items() if k != "_caption_tracks"}, lang)
        return None


def make_provider(args) -> YtdlpProvider | ApiProvider:
    key = os.environ.get("YOUTUBE_API_KEY")
    yt = None
    try:
        yt = YtdlpProvider(args.cookies_from_browser, args.cookies, sleep=args.sleep)
    except SystemExit:
        if args.provider in ("ytdlp",) or not key:
            raise
    if args.provider == "api" or (args.provider == "auto" and key):
        if not key:
            raise SystemExit("--provider api requires YOUTUBE_API_KEY in the environment.")
        log("provider: YouTube Data API v3 (YOUTUBE_API_KEY found)" + (" + yt-dlp for transcripts" if yt else ""))
        return ApiProvider(key, yt)
    log("provider: yt-dlp")
    return yt


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #
def relevance(video: dict, qterms: list[str], phrase: str, hits: list[tuple[str, int]], mode: str) -> tuple[float, list[str]]:
    flags = []
    title_tokens = set(tokenize(video.get("title")))
    desc_tokens = set(tokenize(video.get("description"))) | set(tokenize(" ".join(video.get("tags") or [])))
    if qterms:
        t_cov = sum(term_in(t, title_tokens) for t in qterms) / len(qterms)
        d_cov = sum(term_in(t, desc_tokens | title_tokens) for t in qterms) / len(qterms)
    else:
        t_cov = d_cov = 1.0
    coverage = 0.65 * t_cov + 0.35 * d_cov
    if mode == "brand" and phrase:
        blob_title = (video.get("title") or "").lower()
        blob_desc = ((video.get("description") or "") + " " + " ".join(video.get("tags") or [])).lower()
        if phrase in blob_title:
            coverage = max(coverage, 1.0)
        elif phrase in blob_desc:
            coverage = max(coverage, 0.7)
        elif t_cov < 1.0:
            flags.append("brand-not-in-metadata")
            coverage = min(coverage, 0.3)
    best = max((1.0 / (1.0 + r / 8.0) for _, r in hits), default=0.3)
    multi = min(0.3, 0.1 * (len(hits) - 1))
    rank_signal = clamp(best + multi)
    return clamp(0.6 * coverage + 0.4 * rank_signal), flags


def authority(video: dict, chan: dict | None, trusted: TrustedLists, qterms: list[str]) -> tuple[float, list[str], dict]:
    flags, parts = [], {}
    subs = video.get("channel_subs") if video.get("channel_subs") is not None else (chan or {}).get("subs")
    parts["subs_score"] = clamp(math.log10((subs or 0) + 1) / 7.0) if subs is not None else 0.45
    if subs is None:
        flags.append("subs-unknown")
    verified = video.get("channel_verified")
    if verified is None and chan:
        verified = chan.get("verified")
    parts["verified"] = 1.0 if verified else 0.0
    recent = (chan or {}).get("recent") or []
    if recent:
        views = sorted(v["views"] for v in recent if isinstance(v.get("views"), (int, float)))
        med = views[len(views) // 2] if views else 0
        ratio = (med / subs) if (subs and med) else None
        parts["audience_health"] = clamp((math.log10(ratio) + 2.5) / 2.0) if ratio else 0.4
        parts["recent_median_views"] = med
        parts["topical_focus"] = sum(any(term_in(t, set(tokenize(r.get("title")))) for t in qterms) for r in recent) / len(recent) if qterms else 0.5
        durs = [r.get("duration_s") for r in recent if r.get("duration_s")]
        parts["longform_ratio"] = (sum(d > 480 for d in durs) / len(durs)) if durs else 0.6
        parts["shorts_ratio"] = (sum(d <= 60 for d in durs) / len(durs)) if durs else 0.0
    else:
        parts.update(audience_health=0.5, topical_focus=0.5, longform_ratio=0.6, shorts_ratio=0.0, recent_median_views=None)
    a = (0.40 * parts["subs_score"] + 0.25 * parts["audience_health"] + 0.15 * parts["topical_focus"]
         + 0.10 * parts["longform_ratio"] + 0.10 * parts["verified"])
    name = video.get("channel") or (chan or {}).get("name") or ""
    if any(re.search(p, name.lower()) for p in INSTITUTION_PATTERNS):
        a = min(1.0, a + 0.05)
        flags.append("institutional-pattern")
    shill = trusted.shill_hits(name, " ".join(r.get("title") or "" for r in recent))
    if shill:
        a *= 0.5
        flags.append("shill-pattern")
    status, dom = trusted.lookup(video.get("channel_handle") or (chan or {}).get("handle"), name)
    if status == "A":
        a = max(a, 0.92); flags.append(f"trusted:A:{dom}")
    elif status == "B":
        a = max(a, 0.78); flags.append(f"trusted:B:{dom}")
    elif status == "blocked":
        a = min(a, 0.08); flags.append(f"blocked:{dom}")
    parts["trusted"] = status
    return clamp(a), flags, parts


def engagement(video: dict, tier: str) -> tuple[float, list[str], dict]:
    flags, parts = [], {}
    views, likes, comments = video.get("views") or 0, video.get("likes"), video.get("comments_count") or 0
    if not views:
        return 0.4, ["no-views"], {"er_pct": None, "er_vs_benchmark": None}
    if likes is None:
        flags.append("likes-hidden")
        parts.update(er_pct=None, er_vs_benchmark=None)
        return 0.5, flags, parts
    er = (likes + comments) / views
    bench = ER_BENCHMARK_PCT.get(tier, 3.06) / 100.0
    ratio = er / bench if bench else 1.0
    e_er = clamp(0.5 + 0.25 * math.log2(ratio)) if ratio > 0 else 0.0
    depth = clamp((comments / likes) / 0.08) if likes else 0.0
    e = 0.75 * e_er + 0.25 * depth
    if views < 500:
        e = min(e, 0.6); flags.append("low-sample")
    parts.update(er_pct=round(er * 100, 2), er_vs_benchmark=round(ratio, 2), discussion_depth=round(comments / likes, 3) if likes else None)
    return clamp(e), flags, parts


def reach(video: dict) -> float:
    return clamp(math.log10((video.get("views") or 0) + 1) / 7.0)


def recency(video: dict, mode: str, today: dt.date | None = None) -> tuple[float, float | None]:
    a = age_days(video.get("published"), today)
    if a is None:
        return 0.5, None
    return 0.5 ** (a / HALF_LIFE_DAYS[mode]), a


def format_fit(video: dict, mode: str) -> tuple[float, list[str]]:
    flags = []
    d = (video.get("duration_s") or 0) / 60.0
    if video.get("is_short"):
        flags.append("shorts")
    if video.get("was_live") or video.get("live_status") in ("was_live", "is_live", "post_live"):
        flags.append("live")
    if mode == "learn":
        f = 1.0 if 6 <= d <= 45 else 0.7 if 3 <= d < 6 or 45 < d <= 90 else 0.5 if d > 90 else 0.3
        if "live" in flags:
            f *= 0.8
    elif mode == "expert":
        f = 1.0 if 15 <= d <= 120 else 0.8 if d > 120 else 0.7 if 6 <= d < 15 else 0.3
    elif mode == "topic":
        f = 1.0 if 4 <= d <= 60 else 0.4 if d < 1.05 else 0.7
    else:  # brand — every format is perception, shorts slightly less
        f = 0.6 if d < 1.05 else 1.0
    return clamp(f), flags


def score_run(run: dict, mode: str, trusted: TrustedLists, top_n: int, max_per_channel: int, today: dt.date | None = None) -> dict:
    query = run["meta"]["query"]
    qterms = tokenize(query)
    phrase = query.lower().strip()
    hits_by_id: dict[str, list[tuple[str, int]]] = {}
    for s in run.get("search", []):
        for e in s["entries"]:
            hits_by_id.setdefault(e["id"], []).append((s["variant"], e["rank"]))
    chans = {c["id"]: c for c in run.get("channels", []) if c and c.get("id")}
    w = MODE_WEIGHTS[mode]
    owned = {norm_handle(o) for o in (run["meta"].get("owned") or [])} | {norm_name(o) for o in (run["meta"].get("owned") or [])}
    # --require: for ambiguous brand words (the client, a service agent, a client…) insist that a disambiguating
    # pattern appears somewhere in title / description / tags, otherwise drop the video entirely.
    videos_in = run["videos"]
    require = run["meta"].get("require")
    require_dropped = 0
    if require:
        rx = re.compile(require, re.IGNORECASE)
        kept = []
        for v in videos_in:
            blob = " ".join([v.get("title") or "", v.get("description") or "", " ".join(v.get("tags") or []), v.get("channel") or ""])
            if rx.search(blob):
                kept.append(v)
            else:
                require_dropped += 1
        videos_in = kept
    scored = []
    for v in videos_in:
        chan = chans.get(v.get("channel_id"))
        subs = v.get("channel_subs") if v.get("channel_subs") is not None else (chan or {}).get("subs")
        tier = tier_for(subs)
        R, fR = relevance(v, qterms, phrase, hits_by_id.get(v["id"], []), mode)
        A, fA, pA = authority(v, chan, trusted, qterms)
        E, fE, pE = engagement(v, tier)
        V = reach(v)
        T, age = recency(v, mode, today)
        F, fF = format_fit(v, mode)
        flags = fR + fA + fE + fF
        if mode == "brand" and ((phrase and phrase in (v.get("channel") or "").lower())
                                or norm_handle(v.get("channel_handle")) in owned or norm_name(v.get("channel")) in owned):
            flags.append("official-or-affiliated")
        total = 100 * (w["R"] * R + w["A"] * A + w["E"] * E + w["V"] * V + w["T"] * T + w["F"] * F)
        vpd = (v.get("views") or 0) / age if age else None
        scored.append({**{k: val for k, val in v.items() if not k.startswith("_")},
                       "score": round(total, 1), "components": dict(R=round(R, 3), A=round(A, 3), E=round(E, 3), V=round(V, 3), T=round(T, 3), F=round(F, 3)),
                       "channel_tier": tier, "channel_subs": subs, "age_days": round(age) if age is not None else None,
                       "views_per_day": round(vpd) if vpd else None, "flags": flags, "hits": hits_by_id.get(v["id"], []),
                       "engagement": pE, "authority_parts": {k: (round(x, 3) if isinstance(x, float) else x) for k, x in pA.items()}})
    scored.sort(key=lambda x: x["score"], reverse=True)
    # diversity cap: at most `max_per_channel` videos per channel inside the top N
    per_chan: dict[str, int] = {}
    rank = 0
    for v in scored:
        cid = v.get("channel_id") or v.get("channel")
        if rank < top_n and per_chan.get(cid, 0) < max_per_channel:
            rank += 1
            per_chan[cid] = per_chan.get(cid, 0) + 1
            v["rank"] = rank
        else:
            v["rank"] = None
    # channel landscape
    landscape = {}
    for v in scored:
        cid = v.get("channel_id") or v.get("channel")
        L = landscape.setdefault(cid, {"channel_id": v.get("channel_id"), "channel": v.get("channel"), "handle": v.get("channel_handle"),
                                       "subs": v.get("channel_subs"), "tier": v["channel_tier"], "verified": v.get("channel_verified"),
                                       "trusted": v["authority_parts"].get("trusted"), "videos_in_pool": 0, "videos_in_top": 0,
                                       "best_score": 0, "total_views": 0, "authority": v["components"]["A"],
                                       "recent_median_views": v["authority_parts"].get("recent_median_views"),
                                       "audience_health": v["authority_parts"].get("audience_health"),
                                       "topical_focus": v["authority_parts"].get("topical_focus"),
                                       "flags": sorted({f for f in v["flags"] if f.split(":")[0] in ("trusted", "blocked", "shill-pattern", "institutional-pattern", "official-or-affiliated")})})
        L["videos_in_pool"] += 1
        L["videos_in_top"] += 1 if v["rank"] else 0
        L["best_score"] = max(L["best_score"], v["score"])
        L["total_views"] += v.get("views") or 0
    channels = sorted(landscape.values(), key=lambda c: (c["videos_in_top"], c["best_score"]), reverse=True)
    return {"meta": {**run["meta"], "mode": mode, "weights": w, "half_life_days": HALF_LIFE_DAYS[mode], "top_n": top_n,
                     "max_per_channel": max_per_channel, "scored_at": dt.datetime.now().isoformat(timespec="seconds"),
                     "trusted_lists": trusted.loaded_from, "trusted_entries": trusted.entries_total,
                     "trusted_matched": sorted(trusted.matched), "require": require, "require_dropped": require_dropped},
            "videos": scored, "channels": channels}


# --------------------------------------------------------------------------- #
# Export
# --------------------------------------------------------------------------- #
CSV_COLS = ["rank", "score", "title", "url", "channel", "channel_handle", "channel_tier", "channel_subs", "channel_verified", "trusted",
            "flags", "published", "age_days", "duration", "views", "likes", "comments_count", "er_pct", "er_vs_benchmark", "views_per_day",
            "R", "A", "E", "V", "T", "F", "hits", "has_captions", "has_auto_captions", "caption_langs", "transcript_file", "comments_file", "id"]


def export(results: dict, out: Path) -> None:
    write_json(out / "results.json", results)
    with (out / "videos.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=CSV_COLS)
        wr.writeheader()
        for v in results["videos"]:
            wr.writerow({"rank": v.get("rank") or "", "score": v["score"], "title": v.get("title"), "url": v.get("url"), "channel": v.get("channel"),
                         "channel_handle": v.get("channel_handle"), "channel_tier": v["channel_tier"], "channel_subs": v.get("channel_subs"),
                         "channel_verified": v.get("channel_verified"), "trusted": v["authority_parts"].get("trusted") or "",
                         "flags": ";".join(v["flags"]), "published": v.get("published"), "age_days": v.get("age_days"),
                         "duration": fmt_dur(v.get("duration_s")), "views": v.get("views"), "likes": v.get("likes"), "comments_count": v.get("comments_count"),
                         "er_pct": v["engagement"].get("er_pct"), "er_vs_benchmark": v["engagement"].get("er_vs_benchmark"), "views_per_day": v.get("views_per_day"),
                         **v["components"], "hits": ";".join(f"{a}#{r}" for a, r in v["hits"]), "has_captions": v.get("has_captions"),
                         "has_auto_captions": v.get("has_auto_captions"), "caption_langs": ";".join(v.get("caption_langs") or []),
                         "transcript_file": v.get("transcript_file") or "", "comments_file": v.get("comments_file") or "", "id": v["id"]})
    with (out / "channels.csv").open("w", newline="", encoding="utf-8") as f:
        cols = ["channel", "handle", "channel_id", "subs", "tier", "verified", "trusted", "videos_in_top", "videos_in_pool", "best_score",
                "total_views", "authority", "recent_median_views", "audience_health", "topical_focus", "flags"]
        wr = csv.DictWriter(f, fieldnames=cols)
        wr.writeheader()
        for c in results["channels"]:
            wr.writerow({**{k: c.get(k) for k in cols if k != "flags"}, "flags": ";".join(c.get("flags") or [])})
    (out / "report.md").write_text(render_report(results), encoding="utf-8")


def render_report(res: dict) -> str:
    m = res["meta"]
    vids = [v for v in res["videos"] if v.get("rank")]
    L = [f"# YouTube research — “{m['query']}”", "",
         f"Mode **{m['mode']}** · provider {m.get('provider', '?')} · collected {m.get('collected_at', '?')[:16]} · "
         f"{len(res['videos'])} videos enriched from {m.get('pool_size', '?')} candidates across {len(m.get('variants', []))} query variants · "
         f"top {m['top_n']} shown (≤{m['max_per_channel']}/channel)", "",
         f"Weights: " + ", ".join(f"{k} {v:.2f}" for k, v in m["weights"].items()) + f" · recency half-life {m['half_life_days']}d", ""]
    if m.get("provider_notes"):
        L += [f"> {n}" for n in m["provider_notes"]] + [""]
    L += ["## Top videos", "", "| # | Score | Video | Channel | Tier | Published | Length | Views | ER vs tier | R / A / E / V / T / F | Flags |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for v in vids:
        c = v["components"]
        er = v["engagement"].get("er_vs_benchmark")
        trusted = v["authority_parts"].get("trusted")
        chan = f"{v.get('channel')}" + (f" ✓" if v.get("channel_verified") else "") + (f" **[{trusted}]**" if trusted else "")
        L.append(f"| {v['rank']} | {v['score']} | [{(v.get('title') or '')[:80].replace('|', '/')}]({v['url']}) | {chan} | {v['channel_tier']} ({fmt_int(v.get('channel_subs'))}) | "
                 f"{v.get('published') or '—'} | {fmt_dur(v.get('duration_s'))} | {fmt_int(v.get('views'))} | {('%.1fx' % er) if er else '—'} | "
                 f"{c['R']:.2f}/{c['A']:.2f}/{c['E']:.2f}/{c['V']:.2f}/{c['T']:.2f}/{c['F']:.2f} | {', '.join(v['flags']) or '—'} |")
    L += ["", "## Channel landscape", "", "| Channel | Subs | Tier | Trusted | In top | In pool | Best | Authority | Median recent views | Health | Focus | Flags |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in res["channels"][:40]:
        L.append(f"| {c.get('channel')}{' ✓' if c.get('verified') else ''} | {fmt_int(c.get('subs'))} | {c['tier']} | {c.get('trusted') or '—'} | {c['videos_in_top']} | {c['videos_in_pool']} | "
                 f"{c['best_score']} | {c['authority']:.2f} | {fmt_int(c.get('recent_median_views'))} | "
                 f"{('%.2f' % c['audience_health']) if isinstance(c.get('audience_health'), float) else '—'} | "
                 f"{('%.2f' % c['topical_focus']) if isinstance(c.get('topical_focus'), float) else '—'} | {', '.join(c.get('flags') or []) or '—'} |")
    counts = {}
    for v in res["videos"]:
        for f in v["flags"]:
            counts[f.split(":")[0]] = counts.get(f.split(":")[0], 0) + 1
    L += ["", "## Data quality & caveats", ""]
    L.append(f"- Trusted lists loaded: {len(m.get('trusted_lists', []))} file(s), {m.get('trusted_entries', 0)} entries; matched in this run: "
             f"{', '.join(m.get('trusted_matched', [])) or 'none'}.")
    if m.get("require"):
        L.append(f"- `--require {m['require']}` dropped {m.get('require_dropped', 0)} enriched video(s) whose title/description/tags/channel did not match.")
    for k in sorted(counts):
        L.append(f"- `{k}`: {counts[k]} video(s)")
    if not any(v.get("channel_subs") for v in res["videos"]):
        L.append("- Subscriber counts missing for all videos — authority relies on neutral defaults; check the provider.")
    L += ["", "Scores are a research prioritisation aid, not a verdict on content quality. Read `references/scoring.md` for the method.", ""]
    rest = [v for v in res["videos"] if not v.get("rank")]
    if rest:
        L += ["## Remaining candidates (not in top list)", "", "| Score | Video | Channel | Views | Flags |", "|---|---|---|---|---|"]
        for v in rest[:60]:
            L.append(f"| {v['score']} | [{(v.get('title') or '')[:70].replace('|', '/')}]({v['url']}) | {v.get('channel')} | {fmt_int(v.get('views'))} | {', '.join(v['flags']) or '—'} |")
        L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Comments pre-analysis (heuristic — Claude does the qualitative reading)
# --------------------------------------------------------------------------- #
def analyse_comments(video: dict, comments: list[dict], compare_terms: list[str]) -> dict:
    pos = neg = neu = q = 0
    kw: dict[str, int] = {}
    mentions = {t.lower(): 0 for t in compare_terms}
    for c in comments:
        text = (c.get("text") or "").lower()
        toks = re.findall(r"[a-z0-9$']+", text)
        p = n = 0
        for i, t in enumerate(toks):
            negated = i > 0 and toks[i - 1] in NEGATORS
            if t in POS_WORDS:
                if negated:
                    n += 1
                else:
                    p += 1
            elif t in NEG_WORDS:
                if negated:
                    p += 1
                else:
                    n += 1
            if t not in STOPWORDS and len(t) > 3 and t not in NEGATORS:
                kw[t] = kw.get(t, 0) + 1
        if "?" in text:
            q += 1
        if p > n:
            pos += 1
        elif n > p:
            neg += 1
        else:
            neu += 1
        for term in mentions:
            if term and term in text:
                mentions[term] += 1
    top = sorted(comments, key=lambda c: c.get("likes") or 0, reverse=True)[:8]
    return {"video_id": video["id"], "title": video.get("title"), "url": video.get("url"), "n": len(comments),
            "heuristic_sentiment": {"positive": pos, "negative": neg, "neutral_or_mixed": neu, "questions": q},
            "uploader_replies": sum(1 for c in comments if c.get("author_is_uploader")),
            "top_keywords": sorted(kw.items(), key=lambda x: x[1], reverse=True)[:25],
            "competitor_mentions": mentions,
            "top_liked": [{"likes": c.get("likes"), "author": c.get("author"), "text": (c.get("text") or "")[:400]} for c in top]}


# --------------------------------------------------------------------------- #
# Pipeline stages
# --------------------------------------------------------------------------- #
def expand_variants(query: str, mode: str, extra: list[str] | None, limit: int) -> list[tuple[str, str]]:
    year = str(dt.date.today().year)
    seen, out = set(), []
    for t in (extra or []) + VARIANT_TEMPLATES[mode]:
        v = t.format(q=query, year=year).strip()
        if v.lower() not in seen:
            seen.add(v.lower())
            out.append((v, "relevance"))
    out = out[:limit]
    if mode in DATE_SORT_MODES:
        out.append((query, "date"))
    return out


def stage_search(provider, query: str, mode: str, args) -> tuple[list[dict], list[dict]]:
    variants = expand_variants(query, mode, args.variants, args.max_variants)
    search_log: list[dict] = []
    pool: dict[str, dict] = {}
    for variant, sort in variants:
        log(f"search [{sort}] “{variant}” (n={args.per_variant})")
        kwargs = {"published_after": args.since} if (provider.name == "api" and args.since) else {}
        entries = provider.search(variant, args.per_variant, sort=sort, **kwargs)
        search_log.append({"variant": variant, "sort": sort, "entries": [{"id": e["id"], "rank": e["rank"]} for e in entries]})
        for e in entries:
            c = pool.setdefault(e["id"], {**e, "_hits": 0, "_best_rank": 999})
            c["_hits"] += 1
            c["_best_rank"] = min(c["_best_rank"], e["rank"])
    return search_log, list(pool.values())


def prefilter(cands: list[dict], args) -> list[dict]:
    out = []
    for c in cands:
        if c.get("live_status") in ("is_live", "is_upcoming"):
            continue
        d = c.get("duration_s")
        if d is not None and d <= 60 and not args.include_shorts:
            continue
        if d is not None and d > args.max_minutes * 60:
            continue
        out.append(c)
    # When the pool exceeds the enrich budget keep the candidates most central to the query:
    # hit by several variants first, then best search rank, then (last) views — so the cut itself
    # does not reintroduce a view-count bias.
    out.sort(key=lambda c: (-(c.get("_hits") or 1), c.get("_best_rank", 999), -(c.get("views") or 0)))
    return out[:args.pool]


def run_collection(args) -> Path:
    provider = make_provider(args)
    mode = args.mode
    out = Path(args.out) if args.out else DEFAULT_OUT_ROOT / f"{dt.datetime.now():%Y%m%d-%H%M}-{mode}-{slugify(args.query)}"
    out.mkdir(parents=True, exist_ok=True)
    log(f"run folder: {out}")
    notes = []
    search_log, cands = stage_search(provider, args.query, mode, args)
    log(f"candidate pool: {len(cands)} unique videos")
    cands = prefilter(cands, args)
    log(f"after prefilter: {len(cands)} → enriching")
    write_json(out / "search.json", {"query": args.query, "mode": mode, "variants": search_log, "candidates": cands})
    videos = provider.video_details([c["id"] for c in cands], workers=args.workers)
    if args.since:
        before = len(videos)
        videos = [v for v in videos if (v.get("published") or "9999") >= args.since]
        if before != len(videos):
            notes.append(f"{before - len(videos)} video(s) dropped as older than {args.since}.")
    if not args.include_shorts:
        videos = [v for v in videos if not v.get("is_short")]
    log(f"enriched {len(videos)} videos")
    # channel enrichment for the channels that matter most (most candidates / most views)
    channels = []
    if not args.no_channel_enrich and videos:
        agg: dict[str, int] = {}
        for v in videos:
            if v.get("channel_id"):
                agg[v["channel_id"]] = agg.get(v["channel_id"], 0) + 1 + int(math.log10((v.get("views") or 0) + 1))
        order = sorted(agg, key=agg.get, reverse=True)[:args.max_channels]
        log(f"channel enrichment for {len(order)} channels")

        def one(cid):
            time.sleep(random.uniform(0, 0.4))
            return provider.channel_recent(cid, n=20)
        with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 3))) as ex:
            for f in as_completed([ex.submit(one, c) for c in order]):
                try:
                    r = f.result()
                    if r:
                        channels.append(r)
                except BlockedError as e:
                    notes.append(f"Channel enrichment interrupted: {e}")
                    break
                except Exception as e:  # noqa: BLE001
                    log(f"  ! channel: {type(e).__name__}: {str(e)[:100]}")
    run = {"meta": {"query": args.query, "mode": mode, "provider": provider.name, "collected_at": dt.datetime.now().isoformat(timespec="seconds"),
                    "variants": [s["variant"] + (" [date]" if s["sort"] == "date" else "") for s in search_log],
                    "pool_size": len(cands), "since": args.since, "include_shorts": args.include_shorts, "provider_notes": notes,
                    "domains": args.domain, "owned": args.owned or []},
           "search": search_log, "videos": videos, "channels": channels}
    write_json(out / "run.json", run)
    results = do_score(run, out, mode, args)
    if args.transcripts:
        fetch_transcripts(provider, results, out, args.transcripts, args.lang)
        export(results, out)
    if args.comments:
        fetch_comments(provider, results, out, args.comments, args.comments_per_video, args.compare or [])
        export(results, out)
    if args.compare and mode == "brand":
        share_of_voice(provider, args, out)
    log(f"done → {out / 'report.md'}")
    return out


def do_score(run: dict, out: Path, mode: str, args) -> dict:
    paths = [Path(args.trusted)] if getattr(args, "trusted", None) else [DEFAULT_TRUSTED, USER_TRUSTED]
    trusted = TrustedLists(paths, args.domain)
    changed = False
    if getattr(args, "owned", None):
        run["meta"]["owned"] = sorted(set(run["meta"].get("owned") or []) | set(args.owned))
        changed = True
    if getattr(args, "require", None) is not None:
        run["meta"]["require"] = args.require or None   # --require "" clears a stored filter
        changed = True
    if changed:
        write_json(out / "run.json", run)
    results = score_run(run, mode, trusted, args.n, args.max_per_channel)
    # carry over transcript/comment file pointers from a previous scoring of the same run
    prev = read_json(out / "results.json", {}) or {}
    ptr = {v["id"]: v for v in prev.get("videos", [])}
    for v in results["videos"]:
        for k in ("transcript_file", "comments_file"):
            if ptr.get(v["id"], {}).get(k):
                v[k] = ptr[v["id"]][k]
    export(results, out)
    return results


def fetch_transcripts(provider, results: dict, out: Path, top: int, lang: str) -> None:
    tdir = out / "transcripts"
    tdir.mkdir(exist_ok=True)
    raw_videos = {v["id"]: v for v in (read_json(out / "run.json", {}) or {}).get("videos", [])}
    targets = [v for v in results["videos"] if v.get("rank")][:top]
    log(f"transcripts for top {len(targets)} videos (lang {lang})")
    ok = 0
    for v in targets:
        if (tdir / f"{v['id']}.txt").exists():
            v["transcript_file"] = f"transcripts/{v['id']}.txt"; ok += 1
            continue
        try:
            t = provider.transcript(raw_videos.get(v["id"], v), lang)
        except BlockedError as e:
            log(f"  transcripts stopped: {e}")
            break
        except Exception as e:  # noqa: BLE001
            log(f"  ! {v['id']}: {type(e).__name__}: {str(e)[:100]}")
            t = None
        if not t:
            v["transcript_file"] = None
            continue
        header = f"# {v.get('title')}\n# {v.get('url')} · {v.get('channel')} · {v.get('published')} · {t['kind']} captions ({t['lang']}) · ~{t['words']} words\n\n"
        (tdir / f"{v['id']}.txt").write_text(header + t["text"], encoding="utf-8")
        write_json(tdir / f"{v['id']}.json", {k: t[k] for k in ("video_id", "lang", "kind", "segments", "words")})
        v["transcript_file"] = f"transcripts/{v['id']}.txt"
        ok += 1
    log(f"  {ok}/{len(targets)} transcripts saved")


def fetch_comments(provider, results: dict, out: Path, top: int, per_video: int, compare: list[str]) -> None:
    cdir = out / "comments"
    cdir.mkdir(exist_ok=True)
    targets = [v for v in results["videos"] if v.get("rank")][:top]
    log(f"comments for top {len(targets)} videos ({per_video} each)")
    summaries, all_rows = [], []
    for v in targets:
        try:
            cs = provider.comments(v["id"], per_video)
        except BlockedError as e:
            log(f"  comments stopped: {e}")
            break
        except Exception as e:  # noqa: BLE001
            log(f"  ! {v['id']}: {type(e).__name__}: {str(e)[:100]}")
            continue
        write_json(cdir / f"{v['id']}.json", cs)
        v["comments_file"] = f"comments/{v['id']}.json"
        summaries.append(analyse_comments(v, cs, compare))
        for c in cs:
            all_rows.append({"video_id": v["id"], "video_title": v.get("title"), "channel": v.get("channel"), "likes": c.get("likes"),
                             "author": c.get("author"), "uploader": c.get("author_is_uploader"), "when": c.get("time_text"), "text": c.get("text")})
    write_json(out / "comments_summary.json", summaries)
    with (out / "comments.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=["video_id", "video_title", "channel", "likes", "author", "uploader", "when", "text"])
        wr.writeheader(); wr.writerows(all_rows)
    tot = {"positive": 0, "negative": 0, "neutral_or_mixed": 0, "questions": 0}
    for s in summaries:
        for k in tot:
            tot[k] += s["heuristic_sentiment"][k]
    L = ["# Comment pre-analysis (heuristic lexicon pass — read the samples before concluding anything)", "",
         f"{len(all_rows)} comments across {len(summaries)} videos. Lexicon tally: {tot}.", ""]
    for s in summaries:
        hs = s["heuristic_sentiment"]
        L += [f"## {s['title']}", f"{s['url']} · {s['n']} comments · +{hs['positive']} / −{hs['negative']} / ~{hs['neutral_or_mixed']} · {hs['questions']} questions · {s['uploader_replies']} uploader replies",
              f"Keywords: {', '.join(k for k, _ in s['top_keywords'][:15])}", ""]
        if any(s["competitor_mentions"].values()):
            L.append(f"Competitor mentions: {s['competitor_mentions']}")
        for c in s["top_liked"][:5]:
            L.append(f"- ({c['likes']} likes) {c['author']}: {c['text'][:300]}")
        L.append("")
    (out / "comments.md").write_text("\n".join(L), encoding="utf-8")
    log(f"  comments saved for {len(summaries)} videos")


def share_of_voice(provider, args, out: Path) -> None:
    """Brand mode: compact comparison of the brand vs. --compare terms over the last 12 months."""
    rows = []
    since = (dt.date.today() - dt.timedelta(days=365)).isoformat()
    for term in [args.query] + list(args.compare):
        try:
            ents = {}
            for variant in (term, f"{term} review"):
                for e in provider.search(variant, 30):
                    ents.setdefault(e["id"], e)
            ids = [e["id"] for e in sorted(ents.values(), key=lambda e: e.get("views") or 0, reverse=True)[:40]]
            vids = [v for v in provider.video_details(ids, workers=args.workers) if (v.get("published") or "0000") >= since]
            vids = [v for v in vids if term.lower() in ((v.get("title") or "") + " " + (v.get("description") or "")).lower()]
            ers = sorted([(v["likes"] + (v.get("comments_count") or 0)) / v["views"] for v in vids if v.get("views") and v.get("likes") is not None])
            rows.append({"term": term, "videos_12m": len(vids), "total_views_12m": sum(v.get("views") or 0 for v in vids),
                         "median_er_pct": round(100 * ers[len(ers) // 2], 2) if ers else None,
                         "channels": len({v.get("channel_id") for v in vids}),
                         "top_channels": ", ".join(sorted({v.get("channel") or "" for v in vids}, key=lambda c: -sum((x.get("views") or 0) for x in vids if x.get("channel") == c))[:5])})
        except BlockedError as e:
            log(f"  share of voice stopped: {e}")
            break
    with (out / "share_of_voice.csv").open("w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=["term", "videos_12m", "total_views_12m", "median_er_pct", "channels", "top_channels"])
        wr.writeheader(); wr.writerows(rows)
    log(f"  share of voice: {len(rows)} terms → share_of_voice.csv")


# --------------------------------------------------------------------------- #
# doctor
# --------------------------------------------------------------------------- #
def doctor(args) -> None:
    print("yt-research doctor")
    try:
        import yt_dlp
        print(f"  yt-dlp           : {yt_dlp.version.__version__} (update with: pip install -U yt-dlp)")
    except ImportError:
        print("  yt-dlp           : MISSING → pip install -U yt-dlp")
    for name in ("deno", "node"):
        print(f"  {name:<17}: {'found' if shutil.which(name) else 'not found'}" + ("  (a JS runtime helps yt-dlp with YouTube's challenges)" if name == "deno" else ""))
    key = os.environ.get("YOUTUBE_API_KEY")
    print(f"  YOUTUBE_API_KEY  : {'set (API provider will be used with --provider auto)' if key else 'not set (yt-dlp only)'}")
    print(f"  trusted lists    : seed {DEFAULT_TRUSTED} {'OK' if DEFAULT_TRUSTED.exists() else 'MISSING'}; user override {USER_TRUSTED} {'OK' if USER_TRUSTED.exists() else '(none yet)'}")
    for host in ("https://www.youtube.com/", "https://www.googleapis.com/discovery/v1/apis"):
        try:
            with urllib.request.urlopen(urllib.request.Request(host, headers={"User-Agent": "Mozilla/5.0"}), timeout=12) as r:
                print(f"  {host:<48}: reachable (HTTP {r.status})")
        except Exception as e:  # noqa: BLE001
            print(f"  {host:<48}: BLOCKED/unreachable ({str(e)[:70]})")
    if not args.offline:
        try:
            p = YtdlpProvider(args.cookies_from_browser, args.cookies, sleep=0)
            res = p.search("youtube data api", 3)
            if not res:
                print(f"  yt-dlp search    : FAILED — 0 results. Last yt-dlp error: {p.logger.last_error or 'none recorded'}")
            else:
                print(f"  yt-dlp search    : OK ({len(res)} results)")
                d = p.video_details([res[0]["id"]], workers=1)
                print(f"  yt-dlp details   : {'OK — likes ' + str(d[0].get('likes')) + ', subs ' + str(d[0].get('channel_subs')) if d else 'FAILED'}")
        except BlockedError as e:
            print(f"  yt-dlp live test : BLOCKED — {e}")
        except Exception as e:  # noqa: BLE001
            print(f"  yt-dlp live test : ERROR — {type(e).__name__}: {str(e)[:120]}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="yt_research.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--mode", choices=MODES, default="topic")
        sp.add_argument("--n", type=int, default=25, help="size of the ranked top list (10–50)")
        sp.add_argument("--max-per-channel", type=int, default=3)
        sp.add_argument("--domain", nargs="*", default=None, help="trusted-list domains to apply (default: all)")
        sp.add_argument("--trusted", help="path to a trusted-channels JSON (overrides seed + user file)")
        sp.add_argument("--owned", nargs="*", default=None, help="brand mode: the brand's own channel handles/names → flagged official-or-affiliated")
        sp.add_argument("--require", default=None, help="case-insensitive regex that must appear in title/description/tags/channel, e.g. 'sample-token|the client protocol|makerdao' — for ambiguous brand words")

    def net(sp):
        sp.add_argument("--provider", choices=("auto", "ytdlp", "api"), default="auto")
        sp.add_argument("--cookies-from-browser", help="e.g. chrome, firefox, edge, brave (helps with bot checks)")
        sp.add_argument("--cookies", help="Netscape cookies.txt file")
        sp.add_argument("--workers", type=int, default=4)
        sp.add_argument("--sleep", type=float, default=0.5, help="seconds between yt-dlp requests")

    r = sub.add_parser("run", help="collect + score a query")
    r.add_argument("query")
    common(r); net(r)
    r.add_argument("--variants", nargs="*", help="extra query variants (use {q} placeholder or literal text)")
    r.add_argument("--max-variants", type=int, default=6)
    r.add_argument("--per-variant", type=int, default=30, help="results per search variant (≤50)")
    r.add_argument("--pool", type=int, default=90, help="max candidates to enrich with full metadata")
    r.add_argument("--max-channels", type=int, default=30, help="channels to enrich with recent-upload stats")
    r.add_argument("--no-channel-enrich", action="store_true")
    r.add_argument("--include-shorts", action="store_true")
    r.add_argument("--max-minutes", type=int, default=300, help="drop videos longer than this (streams)")
    r.add_argument("--since", help="only keep videos published on/after YYYY-MM-DD")
    r.add_argument("--lang", default="en", help="preferred caption language")
    r.add_argument("--transcripts", type=int, default=0, help="fetch transcripts for the top N")
    r.add_argument("--comments", type=int, default=0, help="fetch comments for the top N videos")
    r.add_argument("--comments-per-video", type=int, default=60)
    r.add_argument("--compare", nargs="*", help="brand mode: competitor terms for share-of-voice")
    r.add_argument("--out", help="run folder (default: ./youtube-research-runs/<timestamp>-<mode>-<slug>)")

    s = sub.add_parser("rescore", help="re-score an existing run folder offline")
    s.add_argument("run_dir")
    common(s)

    t = sub.add_parser("transcripts", help="fetch transcripts for the top N of a run")
    t.add_argument("run_dir"); t.add_argument("--top", type=int, default=8); t.add_argument("--lang", default="en"); net(t)

    c = sub.add_parser("comments", help="fetch comments for the top N of a run")
    c.add_argument("run_dir"); c.add_argument("--top", type=int, default=15); c.add_argument("--per-video", type=int, default=60)
    c.add_argument("--compare", nargs="*", default=[]); net(c)

    d = sub.add_parser("doctor", help="environment & reachability check")
    d.add_argument("--offline", action="store_true", help="skip the live yt-dlp test")
    d.add_argument("--cookies-from-browser"); d.add_argument("--cookies")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.cmd == "run":
            run_collection(args)
        elif args.cmd == "rescore":
            out = Path(args.run_dir)
            run = read_json(out / "run.json")
            if not run:
                raise SystemExit(f"no run.json in {out}")
            do_score(run, out, args.mode, args)
            log(f"re-scored → {out / 'report.md'}")
        elif args.cmd == "transcripts":
            out = Path(args.run_dir)
            results = read_json(out / "results.json")
            if not results:
                raise SystemExit(f"no results.json in {out} — run or rescore first")
            fetch_transcripts(make_provider(args), results, out, args.top, args.lang)
            export(results, out)
        elif args.cmd == "comments":
            out = Path(args.run_dir)
            results = read_json(out / "results.json")
            if not results:
                raise SystemExit(f"no results.json in {out} — run or rescore first")
            fetch_comments(make_provider(args), results, out, args.top, args.per_video, args.compare)
            export(results, out)
        elif args.cmd == "doctor":
            doctor(args)
    except BlockedError as e:
        log(f"BLOCKED: {e}")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
