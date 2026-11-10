---
title: Report
description: What the frame of the report contains, what the agent adds, and what is verified afterwards.
order: 2
---

A report has two authors. `scripts/digest.py` turns the engine's JSON into a fixed frame, and the
agent writes below its lines. The frame is not rewritten.

## The frame

- **Every finding once**, under its rule id, with line, column, the source line (for a local file)
  and the evidence of the engine, such as a measured contrast ratio.
- **Counts from the engine summary.** If the summary and the list of findings disagree, the frame
  carries a warning with both numbers instead of a corrected one.
- **Unusable inputs first.** A stylesheet the engine could not load is named before any result.
- **Rules that did not run**, each with the reason the engine gave.
- **Best practice marked as such.** A finding without a WCAG basis is a recommendation, not a
  violation.

Each finding has a key of the form `rule-id@line:column`, for example `images/alt-missing@14:3`.
The key identifies a finding within one report. It is not the engine's cross-run `FindingId`,
which `barrierlab --json` does not print.

## What the agent adds

| Section | Added below the frame |
| --- | --- |
| Failed | Why it matters for a user, and the change to the source as a diff. If the source cannot be found, the report says so. |
| Needs review | "Assessment (agent, not a verdict)" with reasoning and the lines read. The outcome stays `review`. |
| Not checked | The concrete step that would decide each finding, and what the rules that did not run would need. |
| Plan | An order of work by severity, then by how many findings a change removes. |

The agent does not add, drop, merge or re-grade findings, gives no score, and makes no statement
about conformance or law. It names the WCAG criteria; the conclusion is the reader's.

## The check

After the report is written, the same script reads it back:

```sh
python3 scripts/digest.py report.json --check report.md
```

It passes when the key of every finding and the id of every rule that did not run still appear in
the report, and names each one that is missing otherwise.

## Use the script on its own

`digest.py` needs only the JSON of a run and works without the plugin:

```sh
barrierlab --json page.html > report.json
python3 scripts/digest.py report.json --source page.html --target page.html
```

`--source` adds the source line of each finding, `--target` sets the name in the title. Only
report schema 1 is accepted.
