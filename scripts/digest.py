#!/usr/bin/env python3
"""Turns a `barrierlab --json` report into the four-section skeleton.

The engine decides; this script only arranges. Every finding and every rule
that did not run appears exactly once, counts are the engine's `summary`, and
nothing is scored. The agent fills in explanations below the skeleton, it does
not rewrite it.

Usage: digest.py <report.json> [--source <page.html>] [--target <name>]
       digest.py <report.json> --check <report.md>
"""

import argparse
import json
import sys

OUTCOMES = ("fail", "review", "untested")


def source_line(lines, position):
    if lines is None or position is None:
        return None
    index = position["line"] - 1
    if 0 <= index < len(lines):
        return lines[index].strip()
    return None


def key(finding):
    """Display key of a finding within one report. Not the engine's FindingId."""
    position = finding["location"].get("position")
    if position is None:
        return f"{finding['rule_id']}@node{finding['location'].get('node', '?')}"
    return f"{finding['rule_id']}@{position['line']}:{position['column']}"


def group_by_rule(findings):
    groups = {}
    for finding in findings:
        groups.setdefault(finding["rule_id"], []).append(finding)
    return groups


def render_group(rule_id, findings, lines):
    first = findings[0]
    head = [f"`{rule_id}`"]
    if first.get("wcag"):
        head.append("WCAG " + ", ".join(first["wcag"]))
    if first.get("basis") == "best_practice":
        head.append("recommendation (best practice), not a violation")
    head.append(f"severity {first['severity']}")
    out = ["### " + " · ".join(head), ""]
    for finding in findings:
        position = finding["location"].get("position")
        where = f"line {position['line']}, column {position['column']}" if position else "no source position"
        out.append(f"- `{key(finding)}` ({where}): {finding['message']}")
        quoted = source_line(lines, position)
        if quoted:
            out.append(f"  - source: `{quoted}`")
        for item in finding.get("evidence", []):
            out.append(f"  - evidence ({item['source']}): {item['field']} = {item['value']}")
    out.append("")
    return out


def digest(report, lines=None, target="page"):
    summary = report["summary"]
    by_outcome = {outcome: [] for outcome in OUTCOMES}
    other = []
    for finding in report["findings"]:
        by_outcome.get(finding["outcome"], other).append(finding)
    not_run = [run for run in report["rule_runs"] if "not_run" in run]

    out = [f"# Accessibility report: {target}", ""]
    out.append(
        "Engine summary: "
        f"{summary['fail']} failed · {summary['review']} need review · "
        f"{summary['untested']} not checked · {summary['rules_not_run']} rules did not run · "
        f"{len(report['rule_runs'])} rules in the run"
    )
    out.append("")

    for outcome in OUTCOMES:
        if len(by_outcome[outcome]) != summary[outcome]:
            out.append(
                f"> Warning: the report lists {len(by_outcome[outcome])} `{outcome}` findings, "
                f"its summary says {summary[outcome]}. Report this; do not correct either number."
            )
            out.append("")
    if len(not_run) != summary["rules_not_run"]:
        out.append(
            f"> Warning: {len(not_run)} rule runs carry `not_run`, the summary says "
            f"{summary['rules_not_run']}. Report this; do not correct either number."
        )
        out.append("")

    inputs = report.get("inputs", [])
    if inputs:
        out += ["## Inputs the engine could not use", ""]
        for note in inputs:
            out.append(f"- {note['kind']}: `{note['subject']}` ({note['detail']})")
        out.append("")

    sections = (
        ("fail", "1. Failed"),
        ("review", "2. Needs review"),
        ("untested", "3. Not checked"),
    )
    for outcome, title in sections:
        out += [f"## {title}", ""]
        findings = by_outcome[outcome]
        if not findings and not (outcome == "untested" and not_run):
            out += ["None.", ""]
        for rule_id, group in group_by_rule(findings).items():
            out += render_group(rule_id, group, lines)
        if outcome == "untested" and not_run:
            out += ["### Rules that did not run", ""]
            for run in not_run:
                wcag = " · WCAG " + ", ".join(run["wcag"]) if run.get("wcag") else ""
                out.append(f"- `{run['rule_id']}`{wcag}: {run['not_run']} ({run.get('reason', 'no reason given')})")
            out.append("")

    if other:
        out += ["## Other outcomes", ""]
        for rule_id, group in group_by_rule(other).items():
            out += render_group(rule_id, group, lines)

    out += ["## 4. Plan", "", "(written by the agent, see the command)", ""]
    return "\n".join(out)


def missing(report, text):
    """What a finished report lost: finding keys and rules that did not run."""
    lost = [key(finding) for finding in report["findings"] if f"`{key(finding)}`" not in text]
    lost += [run["rule_id"] for run in report["rule_runs"] if "not_run" in run and f"`{run['rule_id']}`" not in text]
    return lost


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("report")
    parser.add_argument("--source", help="the audited HTML file, to quote the line of each finding")
    parser.add_argument("--target", help="name shown in the title; defaults to --source or the report path")
    parser.add_argument("--check", metavar="REPORT_MD", help="verify that a finished report still names every finding")
    args = parser.parse_args(argv)

    with open(args.report, encoding="utf-8") as handle:
        report = json.load(handle)
    if report.get("schema") != 1:
        sys.exit(f"digest.py: report schema {report.get('schema')!r} is not supported (expected 1)")

    if args.check:
        with open(args.check, encoding="utf-8") as handle:
            lost = missing(report, handle.read())
        if lost:
            sys.exit("digest.py: missing from the report: " + ", ".join(lost))
        print(f"ok: all {len(report['findings'])} findings and every rule that did not run are named")
        return

    lines = None
    if args.source:
        with open(args.source, encoding="utf-8", errors="replace") as handle:
            lines = handle.read().split("\n")

    print(digest(report, lines, args.target or args.source or args.report))


if __name__ == "__main__":
    main(sys.argv[1:])
