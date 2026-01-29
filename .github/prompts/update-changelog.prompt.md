---
agent: agent
description: Update the workspace root CHANGELOG.md to accurately summarize repository changes
model: GPT-5 mini (copilot)
name: update-changelog
---
Update the repository root `CHANGELOG.md` so it accurately and concisely summarizes all repository changes since the last dated entry.

Scope
- Only read repository commits, PR metadata, tags, and file diffs as needed.
- Only create or modify the workspace root `CHANGELOG.md`. Do not change any other files.

Format requirements
- Follow "Keep a Changelog" conventions (https://keepachangelog.com/).
- Use a dated release heading in the exact `YYYY-mm-dd` format (for example: `## 2026-01-29`).
- Include one or more of these sections under each release (omit empty sections): Added, Changed, Deprecated, Removed, Fixed, Security.
- Each bullet must be concise (≤1 sentence) and reference at least one source (file path, commit hash, or PR number) in parentheses when available.

Behavior rules
- If `CHANGELOG.md` exists: append one new dated entry that summarizes changes since the most recent dated entry. If there are no changes since the last dated entry, do not add a new entry — return unchanged.
- If `CHANGELOG.md` does not exist: create it at the repo root. Add a brief top section describing the changelog style and include a dated entry covering project history or an initial release summary.

Source and classification
- Gather changes from commits, PR titles/descriptions, tags, and file diffs. Prefer high-level user-facing changes first (features, bug fixes, behavior/API changes), then documentation or tooling updates.
- Map each change to exactly one canonical category: Added, Changed, Deprecated, Removed, Fixed, or Security.
- For ambiguous items, write a conservative summary and include the reference for traceability.

Recommended steps
1. Detect whether `CHANGELOG.md` exists at the repository root.
2. If present, find the most recent dated entry and collect commits/PRs since it; otherwise collect project history for an initial entry.
3. Classify each change into a canonical category and condense related small changes into single bullets where appropriate.
4. Draft a single new dated changelog entry using the `YYYY-mm-dd` date for the heading.
5. Append or create `CHANGELOG.md` and ensure the file follows Keep a Changelog structure (top-level description, release entries).

Output format
- Return a single JSON object (no surrounding commentary) with these keys:
  - "action": one of "created", "updated", or "unchanged".
  - "file_path": "CHANGELOG.md"
  - "updated_contents": string — full contents of the resulting `CHANGELOG.md` (if "unchanged", return original contents).
  - "summary": string — a short (1–3 sentence) human summary of what was added or why no change was needed.
  - "notes" (optional): string — any assumptions or unresolved items (for example, missing PR metadata).

Examples
- Example release entry:
  ## 2026-01-29
  ### Added
  - Add `keybindings-evolve` CLI to merge and propose keybindings (bin/keybindings-evolve) (commit abc1234).
  ### Fixed
  - Fix parsing of keybinding comments in `bin/keybindings-remove-comments.py` (PR #12).

- Example output JSON (illustrative):
  {
    "action":"updated",
    "file_path":"CHANGELOG.md",
    "updated_contents":"...full file text here...",
    "summary":"Appended 2026-01-29 entry summarizing new CLI and parsing fix.",
    "notes":"Inferred categories from commit messages and PR titles."
  }

Notes
- Use the ISO date `YYYY-mm-dd` for the release heading you add.
- If there are no changes since the last dated entry, return `action: "unchanged"` with a brief `summary` explaining why.
- Do not modify files other than the root `CHANGELOG.md`.
- When uncertain about intent, summarize conservatively and include references for traceability.