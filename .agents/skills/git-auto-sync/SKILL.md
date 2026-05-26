---
name: git-auto-sync
description: Automatically run project checks, create a Git commit, and push the current branch. Use when the user asks to auto-check, commit, and push changes in this repository.
---

# Git Auto Sync

Use this skill for a safe one-command local workflow: check, stage, commit, and push.

## Workflow

1. Inspect current changes with `git status --short --branch`.
2. Run the bundled script with an explicit commit message:
   ```bash
   python3 .agents/skills/git-auto-sync/scripts/git_auto_sync.py "Commit message"
   ```
3. Report:
   - Checks run
   - Files staged
   - Commit hash
   - Push target

## Script Behavior

The script:

- Verifies the project skill manifest with `skill-manager`.
- Blocks ignored/local Obsidian workspace files from being committed.
- Blocks common generated/local files, including `.DS_Store`, `Thumbs.db`, `__pycache__`, and Python bytecode.
- Shows `git status --short`.
- Runs `git add .`.
- Commits with the provided message.
- Pushes to the current branch upstream, or sets upstream to `origin/<current-branch>` if needed.
- If there are no file changes but the branch has unpushed commits, pushes them unless `--no-push` is set.

## Rules

- Always require a non-empty commit message.
- Do not bypass failed checks.
- Do not use `git reset`, force push, or destructive commands.
- If push fails due to authentication or remote rejection, report the error and stop.
- If there are no changes, report that no commit was created.
