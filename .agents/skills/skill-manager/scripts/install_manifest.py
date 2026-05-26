#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


def skill_home() -> Path:
    project_home = Path.cwd() / ".agents" / "skills"
    if project_home.is_dir():
        return project_home
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"


def global_skill_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"


def installer_script() -> Path:
    return global_skill_home() / ".system/skill-installer/scripts/install-skill-from-github.py"


def load_manifest(path: Path) -> list[dict]:
    data = json.loads(path.expanduser().read_text(encoding="utf-8"))
    return data.get("skills", [])


def installed(name: str) -> bool:
    root = skill_home()
    return (root / name / "SKILL.md").is_file() or (global_skill_home() / ".system" / name / "SKILL.md").is_file()


def main() -> int:
    manifest = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else skill_home() / "skill-manager/references/desired-skills.json"
    skills = load_manifest(manifest)
    grouped = defaultdict(list)

    for item in skills:
        name = item["name"]
        if item.get("local") or installed(name):
            continue
        repo = item.get("repo")
        path = item.get("path")
        ref = item.get("ref", "main")
        if not repo or not path:
            print(f"Skipping {name}: missing repo/path")
            continue
        grouped[(repo, ref)].append(path)

    if not grouped:
        print("All manifest skills are already installed.")
        return 0

    script = installer_script()
    if not script.is_file():
        print(f"Installer script not found: {script}", file=sys.stderr)
        return 2

    status = 0
    for (repo, ref), paths in grouped.items():
        cmd = ["python3", str(script), "--repo", repo, "--ref", ref, "--path", *paths]
        print("$ " + " ".join(cmd))
        result = subprocess.run(cmd)
        status = status or result.returncode
    return status


if __name__ == "__main__":
    raise SystemExit(main())
