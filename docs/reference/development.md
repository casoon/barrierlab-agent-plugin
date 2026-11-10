---
title: Development
description: Layout of the repository and how the digest is tested.
order: 4
---

## Layout

| Path | Purpose |
| --- | --- |
| `.claude-plugin/` | Plugin manifest and marketplace entry. |
| `commands/` | The two commands, as Markdown prompts. |
| `scripts/digest.py` | Builds and checks the frame of the report. Standard library only. |
| `examples/` | Pages and the frames built from them; shown in the showcase. |
| `tests/` | Tests of the digest and the engine output they run on. |

## Tests

```sh
python3 -m unittest discover -s tests
```

The tests run the digest over real `barrierlab --json` output in `tests/fixtures/`
(`barrierlab-cli` 0.1.0 with `a11y-static` 0.2.1). They hold the properties the report depends on:
every finding appears once, keys are unique, counts are the engine's, a disagreeing summary is
reported and not corrected, and `examples/*.report.md` is exactly what the digest prints.

## Validate the plugin

```sh
claude plugin validate .
```
