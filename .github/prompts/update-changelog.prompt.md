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

agent: agent
- Gather changes from git logs and commit descriptions, group them by date, and put them under the appropriate dated heading. Include all changes on or after the parsed date (inclusive).
- Always read the current `CHANGELOG.md` file fresh from disk at the start of the task; do not rely on cached or previously-parsed contents.
- If `CHANGELOG.md` exists: detect the most recent dated release heading in the file by matching a markdown header of the form `## YYYY-mm-dd` and parse that date as the origin. Collect repository changes (commits, PRs, tags, diffs) **inclusive** of that date (i.e., include changes authored on that date). Append one new dated entry that summarizes changes since that parsed date. If there are no changes on or after that date, return `action: "unchanged"` and do not modify the file.
- If `CHANGELOG.md` exists but contains no `## YYYY-mm-dd` headings: treat this as the initial-import case. Use `git` to list all commits from repository inception, group commits by commit date (ISO `YYYY-mm-dd`), and generate a comprehensive changelog covering repository history. For each commit date present, create a `## YYYY-mm-dd` heading and summarize that day's notable changes (condense related commits into single bullets where appropriate), classifying bullets into the standard sections (Added, Changed, Deprecated, Removed, Fixed, Security) and referencing commits or files for traceability.
- If `CHANGELOG.md` does not exist: create it at the repo root. Add a brief top section describing the changelog style and include a dated entry covering project history or an initial release summary.

Source and classification
- For ambiguous items, write a conservative summary and include the reference for traceability.

4. Classify each change into a canonical category and condense related small changes into single bullets where appropriate.
5. Draft a single new dated changelog entry using the `YYYY-mm-dd` date for the heading (use today's date for the new entry) and append it to `CHANGELOG.md`.
Output format
- Return a single JSON object (no surrounding commentary) with these keys:
  - "summary": string — a short (1–3 sentence) human summary of what was added or why no change was needed.
  - "notes" (optional): string — any assumptions or unresolved items (for example, missing PR metadata).
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
- Treat the parsed last-date header as inclusive: collect changes authored on that date as part of the "since" set.
- If the parsed last-date equals today's date, still collect and evaluate changes for that date and append a new entry if new commits/PRs are found.
- If there are no changes on or after the parsed date, return `action: "unchanged"` with a brief `summary` explaining why.
- Do not modify files other than the root `CHANGELOG.md`.
- When uncertain about intent, summarize conservatively and include references for traceability.