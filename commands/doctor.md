---
description: Check that everything the barrierlab plugin needs is present. Changes nothing.
allowed-tools: Bash(command -v:*), Bash(barrierlab:*), Bash(python3:*)
---

Check readiness without changing anything. Do not install, update or write files.

Run each check and report one line per check as `ok`, `missing` or `failed`, with the fix:

1. **`barrierlab` on PATH**: `command -v barrierlab`.
   Missing: `cargo install --git https://github.com/casoon/barrierlab-cli` (needs Rust 1.88 or newer).
2. **Findings carry a source position**: run
   `barrierlab --json "${CLAUDE_PLUGIN_ROOT}/examples/page.html"` (exit code 1 is expected, the
   example has failures; exit code 2 is a failure of this check) and look at
   `findings[0].location.position`.
   Absent: the binary was built against an older rule set; reinstall with
   `cargo install --force --git https://github.com/casoon/barrierlab-cli`.
3. **`python3` available**: `python3 --version` (3.9 or newer; the digest uses only the standard library).
4. **Digest runs**: run
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/digest.py" "${CLAUDE_PLUGIN_ROOT}/tests/fixtures/page.json"`
   and confirm the output starts with `# Accessibility report`.

End with one line: ready, or what to do first. Do not run the fixes yourself; show them.
