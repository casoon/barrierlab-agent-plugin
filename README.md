# barrierlab-agent-plugin

A plugin for Claude Code that audits a page with the
[barrierlab](https://github.com/casoon/barrierlab) rule set and works with the result: it explains
findings, proposes fixes for the project's source and keeps everything that was not checked
visible.

The engine decides, the agent works with the decision. Outcomes, rule ids and counts come from
[`barrierlab-cli`](https://github.com/casoon/barrierlab-cli); the agent never adds, drops or
re-grades a finding. There is no score and no statement about conformance or law.

**Documentation: <https://casoon.github.io/barrierlab-agent-plugin/>**

## Install

```sh
cargo install --git https://github.com/casoon/barrierlab-cli
```

Then, inside Claude Code:

```text
/plugin marketplace add casoon/barrierlab-agent-plugin
/plugin install barrierlab@barrierlab
```

## Commands

| Command | Does |
|---|---|
| `/barrierlab:doctor` | Checks the setup. Changes nothing. |
| `/barrierlab:page <url\|file>` | Audits one page and reports in four sections: failed, needs review, not checked, plan. |

Details: [commands](https://casoon.github.io/barrierlab-agent-plugin/docs/reference/commands/),
[report](https://casoon.github.io/barrierlab-agent-plugin/docs/reference/report/),
[limits](https://casoon.github.io/barrierlab-agent-plugin/docs/reference/limits/),
[development](https://casoon.github.io/barrierlab-agent-plugin/docs/reference/development/).

## License

MIT
