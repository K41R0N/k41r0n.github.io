#!/usr/bin/env bash
# Self-test for push_gate.sh. Prints one line per case; exits non-zero if any case is wrong.
set -u
GATE="$(cd "$(dirname "$0")" && pwd)/push_gate.sh"
ok=0
new() { T=$(mktemp -d); mkdir -p "$T/scripts/local"; printf '%b' "$1" > "$T/scripts/local/denylist.txt"; echo "hello method" > "$T/a.md"; }
expect() { # name want(0 pass|1 fail)
  bash "$GATE" "$T" >/dev/null 2>&1; rc=$?
  if { [ "$2" = 0 ] && [ $rc -eq 0 ]; } || { [ "$2" = 1 ] && [ $rc -ne 0 ]; }; then echo "PASS $1"; else echo "FAIL $1 (rc=$rc)"; ok=1; fi; }
new 'secretterm\n'; expect "clean tree" 0
echo "mentions SecretTerm" > "$T/b.md"; expect "planted term" 1; rm -rf "$T"
new 'secretterm'; echo "SecretTerm" > "$T/b.md"; expect "last term without newline" 1; rm -rf "$T"
new 'secretterm\r\n'; echo "secretterm" > "$T/b.md"; expect "CRLF denylist" 1; rm -rf "$T"
new 'secretterm\n'; echo "secretterm" > "$T/my file
x.md"; expect "filename with space and newline" 1; rm -rf "$T"
new 'secretterm\n'; mkdir "$T/sub"; echo "secretterm" > "$T/sub/denylist.txt"; expect "denylist.txt basename elsewhere is scanned" 1; rm -rf "$T"
new 'secretterm\n'; echo "tok ghp_$(printf 'a%.0s' $(seq 1 36))" > "$T/c.md"; expect "credential" 1; rm -rf "$T"
new 'secretterm\n'; rm "$T/scripts/local/denylist.txt"; expect "missing denylist" 1; rm -rf "$T"
new '# only a comment\n'; expect "empty denylist" 1; rm -rf "$T"
new 'secretterm\n'; echo "x" > "$T/e.md"; chmod 000 "$T/e.md"; [ "$(id -u)" != 0 ] && expect "unreadable file is an error, not clean" 1; chmod 644 "$T/e.md"; rm -rf "$T"
# history: leak committed then removed from the working tree
new 'secretterm\n'; ( cd "$T" && git init -q && git config user.email t@t && git config user.name t && echo "secretterm" > leak.md && git add -A -f . && git commit -q -m leak && git rm -q leak.md && git commit -q -m fix ) ; expect "leak only in history" 1; rm -rf "$T"
new 'secretterm\n'; ( cd "$T" && git init -q && git config user.email t@t && git config user.name t && git add -A -f . && git commit -q -m ok ); expect "clean history" 0; rm -rf "$T"
exit $ok
