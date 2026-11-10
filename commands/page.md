---
description: Audit one page (URL or HTML file) with the barrierlab rule set and report it in four sections.
argument-hint: <url|file> [--base-url <url>] [--width <px>] [--dark]
allowed-tools: Bash(barrierlab:*), Bash(python3:*), Bash(mkdir:*), Bash(date:*), Read, Write, Grep, Glob
---

Audit `$ARGUMENTS` and report it. The engine decides; you explain and plan.

## Rules you do not break

- Never add, drop, merge or re-grade a finding. Every finding the engine reports stays in the
  report with its rule id and its key, in the section the engine's outcome puts it in.
- "Not checked" and "did not run" are never a pass. They stay visible with their reason.
- No scores, grades or percentages. Counts are the ones in the engine summary line.
- No verdict on conformance or law ("compliant", BFSG, EAA). Name the WCAG criteria; the
  conclusion is the reader's.
- Your assessment of a `review` finding is labelled as an assessment, with your reasoning and what
  you looked at. It does not change the outcome.
- Propose fixes as diffs for the project's source. Do not apply them in this command.
- Explain from the finding's message and the WCAG criterion, not from how other tools behave.

## Steps

1. **Run the engine.** Create `.barrierlab/runs/<UTC timestamp, e.g. 20260131T120000Z>/` in the
   current project and run
   `barrierlab --json $ARGUMENTS > .barrierlab/runs/<timestamp>/report.json`
   (the arguments as given, options included).
   Exit code 0 or 1 is a completed run. Exit code 2 means the page could not be read: show the
   error, write no report, stop. If the tool is not found, tell the user to run
   `/barrierlab:doctor` and stop.
   For a local file with linked stylesheets and no `--base-url`, run it anyway; the missing sheets
   show up under inputs.
2. **Build the skeleton.**
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/digest.py" <report.json> [--source <file>] --target <url or file>`
   (`--source` only for a local file; `--target` is the URL or file the user named). Its output is
   the frame of your report: keep every heading, every finding line and every count as printed,
   and add your text below the lines it belongs to. Only the placeholder under "4. Plan" is
   replaced. If it prints a warning, pass it on unchanged.
3. **Inputs first.** If the skeleton has "Inputs the engine could not use", say before anything
   else what that means for the result (an unavailable stylesheet leaves contrast unchecked) and
   how to supply it (`--base-url`). Without that section, skip this step.
4. **Fill in, under the skeleton's lines:**
   - *Failed*: per rule, one or two sentences on why it matters for a user, and the fix direction.
     For a local file inside the project, find the source that produces the element (the file
     itself, or the template or component behind a build output) and show the change as a diff.
     If you cannot find the source, say so instead of guessing a path.
   - *Needs review*: per finding, "Assessment (agent, not a verdict):" with reasoning and the
     lines of the source you read for it. If the source does not settle it, say so and name what
     a person has to look at; do not assess without evidence.
   - *Not checked*, findings: per rule, the concrete step that would decide it, and what counts
     as met.
   - *Not checked*, "Rules that did not run": leave the engine's reasons as printed and add one
     note under the list on what would be needed (for most: a run in a browser).
   - *Plan*: ordered by severity, then by how many findings a change removes. Effort only as a
     stated estimate in words.
5. **Store, check, show.** Write the finished report to `.barrierlab/runs/<timestamp>/report.md`,
   then run
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/digest.py" <report.json> --check <report.md>`.
   If it names anything as missing, put it back and check again. Show the report. After it, in
   your reply and not in `report.md`, give the two paths and one line on how to confirm a fix:
   change the source, run `/barrierlab:page` again, and compare the engine summary.
