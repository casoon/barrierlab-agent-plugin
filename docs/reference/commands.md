---
title: Commands
description: The two commands of the plugin, their arguments and what they write.
order: 1
---

## /barrierlab:page

```text
/barrierlab:page <url|file> [--base-url <url>] [--width <px>] [--dark]
```

Audits one page and reports it in four sections. The arguments are passed to `barrierlab --json`
as given.

| Argument | Meaning |
| --- | --- |
| `<url\|file>` | The page: a URL or a local HTML file. |
| `--base-url <url>` | Where linked stylesheets of a local file are resolved. |
| `--width <px>` | Viewport width the media queries are evaluated for. |
| `--dark` | Evaluate the dark colour scheme. |

Steps of a run:

1. The engine runs and its JSON is stored as `.barrierlab/runs/<UTC timestamp>/report.json`.
   Exit code 0 or 1 is a completed run. Exit code 2 means the page could not be read: the error is
   shown and no report is written.
2. `scripts/digest.py` builds the [frame of the report](../report/).
3. The agent writes below the frame and stores the result as `report.md` next to `report.json`.
4. `digest.py --check` verifies the finished report; anything it names as missing is put back.

The command writes only inside `.barrierlab/runs/`. It proposes changes to the source as diffs and
does not apply them.

## /barrierlab:doctor

```text
/barrierlab:doctor
```

Checks the setup and changes nothing. One line per check, `ok`, `missing` or `failed`, with the
fix:

1. `barrierlab` is on `PATH`.
2. Findings carry a source position. A binary built against an older rule set prints none;
   reinstall it with `cargo install --force --git https://github.com/casoon/barrierlab-cli`.
3. `python3` is available, 3.9 or newer.
4. The digest runs on the fixture that ships with the plugin.
