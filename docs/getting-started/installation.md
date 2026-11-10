---
title: Installation
description: Install the engine, add the plugin to Claude Code and check that both work.
order: 1
---

The plugin needs two things on the machine: the `barrierlab` binary, which does the audit, and
`python3` (3.9 or newer, standard library only), which builds the frame of the report.

## The engine

`barrierlab-cli` is installed from its repository and needs Rust 1.88 or newer:

```sh
cargo install --git https://github.com/casoon/barrierlab-cli
```

## The plugin

Inside Claude Code, add the marketplace and install the plugin from it:

```text
/plugin marketplace add casoon/barrierlab-agent-plugin
/plugin install barrierlab@barrierlab
```

## Check the setup

```text
/barrierlab:doctor
```

The command changes nothing. It reports one line per check and, for anything missing, the command
that fixes it. What it checks is listed under [Commands](../../reference/commands/#barrierlabdoctor).
