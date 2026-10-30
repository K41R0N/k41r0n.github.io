#!/usr/bin/env bash
# Push gate. Run before every push (use: bash scripts/local/push_gate.sh [root]).
# Scans the working tree AND, when root is a git repo, every commit's diff in history.
# Fails on: a denylist term (case-insensitive whole word), a credential-looking string,
# a missing or empty denylist, or any scan error (an error is never treated as clean).
set -u
ROOT="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
DENY="$ROOT/scripts/local/denylist.txt"
CRED='gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY'
fail=0
if [ ! -f "$DENY" ]; then echo "FAIL: scripts/local/denylist.txt missing."; exit 2; fi
terms=()
while IFS= read -r term || [ -n "$term" ]; do
  term="${term%$'\r'}"
  case "$term" in ''|\#*) continue;; esac
  terms+=("$term")
done < "$DENY"
if [ ${#terms[@]} -eq 0 ]; then echo "FAIL: denylist has no terms."; exit 2; fi

# Exclusions are exact paths only, never basenames elsewhere in the tree.
EX1=./scripts/local/denylist.txt; EX2=./scripts/local/denylist.example.txt; EX3=./scripts/local/test_push_gate.sh

scan_tree() { # grep args in "$@"; prints matches; prints GATE_SCAN_ERROR if any grep errored
  (cd "$ROOT" && find . -type f -not -path './.git/*' ! -path "$EX1" ! -path "$EX2" ! -path "$EX3" -print0 \
    | xargs -0 -r sh -c 'grep -I "$@" ; rc=$?; [ $rc -le 1 ] || echo GATE_SCAN_ERROR' sh "$@")
}
for term in "${terms[@]}"; do
  out=$(scan_tree -i -l -w -F -e "$term")
  if echo "$out" | grep -q GATE_SCAN_ERROR; then echo "FAIL: scan error on working tree"; fail=1
  elif [ -n "$out" ]; then echo "FAIL: denylisted term in: $(echo "$out" | tr '\n' ' ')"; fail=1; fi
done
out=$(scan_tree -l -E -e "$CRED")
if echo "$out" | grep -q GATE_SCAN_ERROR; then echo "FAIL: scan error on working tree"; fail=1
elif [ -n "$out" ]; then echo "FAIL: credential-like string in: $(echo "$out" | tr '\n' ' ')"; fail=1; fi

# History: every added or removed line in every commit, all refs.
if git -C "$ROOT" rev-parse --git-dir >/dev/null 2>&1 && git -C "$ROOT" rev-parse HEAD >/dev/null 2>&1; then
  hist=$(mktemp)
  if ! git -C "$ROOT" log --all -p --no-color -- . ":(exclude)scripts/local/denylist.txt" ":(exclude)scripts/local/denylist.example.txt" ":(exclude)scripts/local/test_push_gate.sh" ":(exclude)methods-library/scripts/local/denylist.txt" ":(exclude)methods-library/scripts/local/denylist.example.txt" ":(exclude)methods-library/scripts/local/test_push_gate.sh" > "$hist" 2>/dev/null; then
    echo "FAIL: could not read git history"; fail=1
  else
    for term in "${terms[@]}"; do
      grep -i -w -F -q -e "$term" "$hist"; rc=$?
      if [ $rc -eq 0 ]; then echo "FAIL: denylisted term found in commit history"; fail=1
      elif [ $rc -ge 2 ]; then echo "FAIL: scan error on history"; fail=1; fi
    done
    grep -E -q -e "$CRED" "$hist"; rc=$?
    if [ $rc -eq 0 ]; then echo "FAIL: credential-like string in commit history"; fail=1
    elif [ $rc -ge 2 ]; then echo "FAIL: scan error on history"; fail=1; fi
  fi
  rm -f "$hist"
fi
[ $fail -eq 0 ] && echo "PASS: push gate clean"
exit $fail
