# Existing-host review adapter candidate

Status: implemented and offline contract-tested, disabled. Not a verified running host.

Owner source: the current private on-host CLI operations record, updated Nov15. Exact repository/file locator is retained in the private recovery record, not in this shareable change set. It records an installed Claude Code client using the existing operator subscription. This is evidence of a candidate route, not current auth, capacity or account permission.

Official current contracts read Nov16:
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/headless

`writing_claude_adapter.py` accepts only review packets. It requires an absolute installed binary, SHA256, exact version and explicitly selected model. It probes version/help before each model run, fails on missing required flags, starts in a temporary empty directory with restricted mode, no built-in/MCP tools, no session persistence, no resume flags and no inherited API-key/provider overrides. It supplies a replacement system prompt and the whole source-grounded prepared packet. JSON envelope errors, missing structured output, wrong stage or artifact changes block. The main validator then checks the actual receipt, not the process exit alone.

No binary path, hash, model or account is guessed into production settings. Production `executors` remains empty. The host's normal client handles its own subscription login; the adapter does not read credentials. A subscription is not a promise of free or unlimited usage. No API spending, installation or account change is authorized here.

## Host checks still needed

An operator on the existing G14 route must verify current executable/version/help, normal subscription authentication, model choice, exact binary hash and any managed policy hooks. The CLI documents that restricted mode still loads managed settings; therefore this is not an operating-system sandbox or proof that all host-managed hooks are absent. Verify no unexpected tool calls, source reads or remote session resumption in an isolated synthetic conformance run. Do not bypass host safeguards. No such live run was possible from the available execution surface, and the tests mock the client process instead.

The entrypoint strips most environment values. The adapter restores only the OS account home plus a fixed PATH/LANG for the installed client's ordinary auth. It never restores an API key or OAuth-token override. Any unresolved auth, capability or policy conflict stops, not falls back to a different paid service.

Even after those checks, configuring this review candidate does not lift the separate new-author-writing hold. No author prose was generated during implementation.

The dispatcher additionally requires a pinned installed bubblewrap binary and masks the private run directory from workers, including absolute-path attempts. This was tested locally with synthetic workers, not on G14. Its root filesystem is read-only but otherwise visible; credential/data sandbox claims remain out of scope. G14 bubblewrap availability must be verified, not installed without authority.
