# barrierlab-agent-plugin

A plugin for Claude Code that audits a page with the
[barrierlab](https://github.com/casoon/barrierlab) rule set and works with the result: it explains
findings, proposes fixes for the project's source and keeps everything that was not checked
visible.

The engine decides, the agent works with the decision. Outcomes, rule ids and counts come from
[`barrierlab-cli`](https://github.com/casoon/barrierlab-cli); the agent never adds, drops or
re-grades a finding.

## Commands

| Command | Does |
|---|---|
| `/barrierlab:doctor` | Checks that `barrierlab` and `python3` are present and that findings carry a source position. Changes nothing. |
| `/barrierlab:page <url\|file>` | Runs the engine on one page and reports in four sections: failed, needs review, not checked, plan. Stores `report.json` and `report.md` under `.barrierlab/runs/<timestamp>/`. |

`/barrierlab:page` passes `--base-url`, `--width` and `--dark` on to `barrierlab`.

## Install

1. The engine (needs Rust 1.88 or newer):

   ```sh
   cargo install --git https://github.com/casoon/barrierlab-cli
   ```

2. The plugin, inside Claude Code:

   ```text
   /plugin marketplace add casoon/barrierlab-agent-plugin
   /plugin install barrierlab@barrierlab
   ```

3. `/barrierlab:doctor`

`python3` (3.9 or newer, standard library only) is needed for the report skeleton.

## What the report contains

`scripts/digest.py` turns the engine's JSON into a fixed frame, and the agent writes below it:

- every finding once, under its rule id, with line, column, the source line and the engine's
  evidence;
- counts taken from the engine's summary; if the summary and the list disagree, a warning instead
  of a corrected number;
- stylesheets the engine could not load, before any result;
- rules that did not run, with the engine's reason;
- best-practice findings marked as recommendations.

After the agent has written the report, `digest.py --check` verifies that every finding and every
rule that did not run is still named in it.

There is no score and no statement about conformance or law.

## Limits

- One page per run. No site crawl, no baseline or comparison between runs yet.
- Static analysis only: what needs a browser (scripted content, focus, layout) is reported as not
  checked or not run.
- Findings are keyed by rule id and position within one report. This key is not the engine's
  cross-run `FindingId`, which `barrierlab --json` does not print.
- Fixes are proposed as diffs, not applied.
- HTML conformance findings (`html-conform`) are not part of the report.

## Development

```sh
python3 -m unittest discover -s tests
```

The tests run the digest over real `barrierlab --json` output in `tests/fixtures/`
(`barrierlab-cli` 0.1.0 with `a11y-static` 0.2.1).

Concept and phases: [casoon/barrierlab#127](https://github.com/casoon/barrierlab/issues/127).

## License

MIT
