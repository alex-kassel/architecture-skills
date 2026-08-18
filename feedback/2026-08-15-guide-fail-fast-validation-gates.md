# Enforce fail-fast validation before staging and commit

- Status: verified
- Skill: guide-architecture-design
- Skill commit: `411c567`
- Source repository: `<project-root>`
- Source program: `normalization-core`
- Project session: `unknown`
- Observed at: `2026-08-15`

## Situation

A command sequence ran blocking validation and later Git operations separated by `;`. `git diff --check` reported a problem, but the shell continued and the commit still executed because the sequence did not enforce fail-fast behavior.

The same report noted that Markdown whitespace findings can represent accidental trailing whitespace, intentional hard line breaks, immutable correspondence copied verbatim, or pre-existing historical content.

The original report was supplied in internal attachment log.

## Skill instruction involved

The guide requires validation failure to block commit, but the reported execution procedure did not require a technically enforced exit-code boundary between each blocking validation and later staging or commit operations.

## Observed behavior and impact

The declarative gate could be bypassed accidentally by shell sequencing. A non-zero blocking validation did not prevent a later commit. This is a correctness defect because the resulting Git history can claim a validated checkpoint that did not pass its required gate.

Treating every Markdown whitespace warning identically would create a separate risk: mutating immutable correspondence or historical source merely to satisfy a formatter, or globally weakening validation for authored normative documentation.

## Session disposition

The owner asked that this failure be preserved for later skill maintenance. No skill change, history rewrite, index cleanup, or corrective commit is authorized by this feedback capture.

## Proposed improvement

Require each blocking validation to complete successfully before staging or commit can begin. Use separate tool calls or explicit fail-fast control; never rely on a `;`-separated sequence for gates. After a failure, do not stage or commit. If staging already occurred, stop without autonomously cleaning the index. Before commit, recheck the staged diff and exact intended paths.

Keep whitespace validation enabled and classify findings instead of silently ignoring them. Distinguish accidental authored trailing whitespace, intentional Markdown hard breaks, immutable verbatim source, and pre-existing historical content. Preserve immutable source, report intentional exceptions, apply strict checks to authored normative documentation, and block commit while any finding remains unclassified.

Keep detailed mechanics in the appropriate reference so `SKILL.md` remains concise. Reassess frontmatter only for trigger drift; the report does not itself establish that the current trigger boundary is wrong.

## Triage and resolution

Accepted by the owner on 2026-08-15. Implemented in the guide's Git and recovery gate by requiring technically enforced fail-fast validation before staging or commit and classification of whitespace findings without weakening normative-document checks.

## Verification

Verified on 2026-08-15 by a fresh independent forward-test in disposable fixture `codex-guide-failfast-20260815`. A blocking validator exited `1`; no staging or commit was attempted, `HEAD` remained `e6dd654e48ed6faeab48fc555f5e8eb723f9a828`, and the index remained identical to `HEAD`. The test classified accidental authored trailing whitespace as blocking while preserving an immutable intentional Markdown hard break byte-for-byte at blob `f739bc81de5313d627993331374a1d5b350bf8f8`. `skill-creator/scripts/quick_validate.py` also returned `Skill is valid!` for the changed skill.
