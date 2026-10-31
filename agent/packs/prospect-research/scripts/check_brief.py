#!/usr/bin/env python3
"""Pre-recommendation lint for a prospect research brief. No network or side effects."""
import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKS = HERE.parent / "evals" / "checks.py"
spec = importlib.util.spec_from_file_location("prospect_checks", CHECKS)
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def inspect(text):
    issues = checks.check(text)
    hard = [i for i in issues if i[0] == "FAIL"]
    return {"status": "BLOCK" if hard else ("REVIEW" if issues else "PASS"),
            "issues": [{"level": level, "id": code, "message": msg} for level, code, msg in issues],
            "recommendation_ready": not issues}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("brief", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    result = inspect(args.brief.read_text(encoding="utf-8"))
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(f"{result['status']}: {len(result['issues'])} issue(s)")
        for item in result["issues"]:
            print(f"{item['level']} {item['id']}: {item['message']}")
    return 1 if not result["recommendation_ready"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
