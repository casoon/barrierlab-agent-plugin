# Changelog

All notable changes to barrierlab-agent-plugin are listed here. The plugin follows
[Semantic Versioning](https://semver.org/): while it is 0.x, a minor version may change commands
or the report layout.

## [Unreleased]

### Added

- **Commands:** `/barrierlab:page <url|file>` audits one page with `barrierlab --json` and reports
  it in four sections (failed, needs review, not checked, plan); report and JSON are stored under
  `.barrierlab/runs/<timestamp>/`.
- **Commands:** `/barrierlab:doctor` checks, without changing anything, that the engine and
  `python3` are present and that findings carry a source position.
- **Report:** `scripts/digest.py` builds the report frame from the engine's JSON: every finding
  once with position, source line and evidence, counts from the engine summary, unusable inputs
  first, rules that did not run with their reason. `--check` verifies that a finished report still
  names all of them.
- **Docs:** project site with installation, commands, report and limits at
  [casoon.github.io/barrierlab-agent-plugin](https://casoon.github.io/barrierlab-agent-plugin/); `examples/` holds the report frames it shows.

### Changed

- **Pages:** the project site uses the current shared theme (0.12.12).

