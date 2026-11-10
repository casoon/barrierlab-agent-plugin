---
title: First audit
description: Run /barrierlab:page on a file or URL and read the four sections of the report.
order: 2
---

## Run it

Name a local HTML file or a URL:

```text
/barrierlab:page dist/contact/index.html
```

A local file that links stylesheets needs to know where they live, otherwise contrast stays
unchecked and the report says so first:

```text
/barrierlab:page dist/contact/index.html --base-url https://example.com/contact/
```

## What you get

The run creates `.barrierlab/runs/<UTC timestamp>/` in the project with two files: `report.json`,
the engine's output as it was printed, and `report.md`, the report the agent wrote on top of it.
Add `.barrierlab/` to `.gitignore` unless you want to keep the runs.

The report has four sections, always in this order:

1. **Failed**: what the engine found to be a violation, with the reason it matters and a proposed
   change to the source as a diff.
2. **Needs review**: what a person has to decide. The agent adds an assessment, labelled as one,
   with the lines it read.
3. **Not checked**: what the engine could not decide statically, the step that would decide it,
   and the rules that did not run with the engine's reason.
4. **Plan**: the proposed order of work, by severity and by how many findings a change removes.

Two frames built from real engine output are in the [showcase](../../../showcase/).

## Confirm a fix

Apply the change, run `/barrierlab:page` again and compare the engine summary line at the top of
both reports. The plugin does not compare runs for you yet.
