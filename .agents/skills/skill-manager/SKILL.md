---
name: skill-manager
description: Manage Codex skills from a desired-skill manifest. Use when installing batches of skills, checking which expected skills are installed, updating skill inventories, or producing post-install verification reports.
---

# Skill Manager

Use this skill to keep Codex skills reproducible and auditable.

## Workflow

1. Locate or create a manifest JSON with desired skills.
   - Default project manifest: `.agents/skills/skill-manager/references/desired-skills.json`
   - Personal manifests can also be used, for example `~/.codex/skills/skill-manager/references/desired-skills.json`.
   - In this repository, treat the default project manifest as the source of truth because it includes local custom skills.
2. Install missing GitHub-hosted skills with:
   ```bash
   python3 .agents/skills/skill-manager/scripts/install_manifest.py <manifest.json>
   ```
3. Verify installation with:
   ```bash
   python3 .agents/skills/skill-manager/scripts/verify_manifest.py <manifest.json>
   ```
4. Report installed, missing, and failed skills clearly.
5. Tell the user to restart Codex after installing or updating skills.

## Manifest Format

```json
{
  "skills": [
    {
      "name": "obsidian-markdown",
      "repo": "kepano/obsidian-skills",
      "path": "skills/obsidian-markdown",
      "ref": "main"
    }
  ]
}
```

## Rules

- Do not overwrite an existing skill directory without explicit user approval.
- Treat system skills under `~/.codex/skills/.system` as preinstalled.
- For project-scoped skills, verify `.agents/skills/<name>/SKILL.md` first.
- Prefer the built-in `skill-installer` scripts for GitHub installs.
- Use `skills list --json` as an optional secondary signal, but verify the filesystem because Codex loads skills from directories containing `SKILL.md`.
- Keep project automation under `.agents/skills/skill-manager` when the user wants project-level reproducibility.
