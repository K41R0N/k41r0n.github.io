"""Checks that an advice draft fits the person asking.
Format: 'asker: beginner|informed|expert', '## Answer', '## Next step' (one item), '## Confidence' ('- sure:', '- checked:', '- not known:').
A clean result means only that these patterns are absent. It never judges whether the advice is right or sounds like him."""
import re
BUZZ = ["leverage", "synergy", "holistic", "robust", "seamless", "streamline", "delve", "game-changer", "cutting-edge", "empower", "unlock"]
JARGON = ["funnel", "kpi", "icp", "gtm", "engagement rate", "positioning", "conversion", "algorithm", "prompt engineering", "llm", "harness", "workflow", "stakeholder"]

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def check(text):
    out = []
    sec = _sections(text)
    m = re.search(r"^asker:\s*(\w+)", text, re.M)
    level = m.group(1).lower() if m else ""
    if level not in ("beginner", "informed", "expert"):
        out.append(("FAIL", "AF1-asker-level-missing", "asker: beginner, informed or expert"))
    ans = sec.get("Answer", "")
    low = ans.lower()
    for w in BUZZ:
        if re.search(rf"\b{re.escape(w)}", low):
            out.append(("FAIL", "AF2-buzzword", w)); break
    if level in ("beginner", "informed"):
        for w in JARGON:
            for mm in re.finditer(rf"\b{re.escape(w)}\b", low):
                tail = low[mm.end():mm.end() + 40]
                if not re.match(r"\s*(\(|means|is when|is the)", tail):
                    out.append(("FAIL", "AF3-jargon-without-plain-words", w)); break
            else:
                continue
            break
    limit = 20 if level == "beginner" else 28
    for s in re.split(r"(?<=[.!?])\s+", ans.strip()):
        if len(s.split()) > limit:
            out.append(("FAIL", "AF4-sentence-too-long", s[:40])); break
    nxt = [l for l in sec.get("Next step", "").splitlines() if l.strip().startswith("- ")]
    if len(nxt) != 1:
        out.append(("FAIL", "AF5-not-one-next-step", f"{len(nxt)} next steps"))
    conf = sec.get("Confidence", "")
    for k in ("sure", "checked", "not known"):
        if not re.search(rf"^- {k}:\s*\S", conf, re.M):
            out.append(("FAIL", "AF6-confidence-line-missing", k))
    return out
