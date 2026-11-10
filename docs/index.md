---
title: Overview
description: What the plugin does with an accessibility audit, where it stops, and how this documentation is organised.
order: 0
---

barrierlab-agent-plugin adds two commands to Claude Code. `/barrierlab:page` audits one page with
the [barrierlab](https://github.com/casoon/barrierlab) rule set and writes a report the agent then
works with: it explains each finding, proposes fixes for the source of the project and keeps
everything that was not checked visible.

## The engine decides

Outcomes, rule ids and counts come from
[`barrierlab-cli`](https://github.com/casoon/barrierlab-cli). The agent never adds, drops or
re-grades a finding. A script builds the frame of the report from the engine's JSON, and a second
pass of the same script verifies that the finished report still names every finding.

## Where it stops

- One page per run, analysed statically. What needs a browser is reported as not checked.
- No score, and no statement about conformance or law.
- Fixes are proposed as diffs, not applied.

The full list is on [Limits](reference/limits/).

## How the docs are organised

- **Getting started**: [install](getting-started/installation/) the engine and the plugin, then
  run a [first audit](getting-started/first-audit/).
- **Reference**: the [commands](reference/commands/), the [report](reference/report/) and its
  guarantees, the [limits](reference/limits/), and how to [work on the plugin](reference/development/).
