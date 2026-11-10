---
title: Limits
description: What the plugin does not do, and what a report cannot tell you.
order: 3
---

- **One page per run.** No site crawl, no baseline and no comparison between runs yet.
- **Static analysis only.** What needs a browser (scripted content, focus, layout) is reported as
  not checked or not run, never as passed.
- **Keys are local to a report.** Findings are keyed by rule id and position. This is not the
  engine's cross-run `FindingId`, which `barrierlab --json` does not print.
- **Fixes are proposed, not applied.** The report shows diffs.
- **No HTML conformance findings.** Results of `html-conform` are not part of the report.
- **No score and no verdict.** The report counts what the engine counted and names WCAG criteria.
  It does not say whether a page conforms or meets a law.
- **Claude Code only.** The commands use the plugin format of Claude Code.

Planned phases are tracked in
[casoon/barrierlab#127](https://github.com/casoon/barrierlab/issues/127).
