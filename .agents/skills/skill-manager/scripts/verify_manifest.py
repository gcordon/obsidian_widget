#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def skill_home() -> Path:
    project_home = Path.cwd() / ".agents" / "skills"
    if project_home.is_dir():
        return project_home
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"


def global_skill_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills"


def load_manifest(path: Path) -> list[dict]:
    data = json.loads(path.expanduser().read_text(encoding="utf-8"))
    return data.get("skills", [])


def cli_installed_names() -> set[str]:
    if shutil.which("skills"):
        cmd = ["skills", "list", "--json", "-g"]
    elif shutil.which("npx"):
        cmd = ["npx", "skills", "list", "--json", "-g"]
    else:
        return set()

    try:
        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return set()
    if result.returncode != 0 or not result.stdout.strip():
        return set()
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return set()
    names = set()
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "name" in item:
                names.add(str(item["name"]))
            elif isinstance(item, str):
                names.add(item)
    return names


def main() -> int:
    manifest = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else skill_home() / "skill-manager/references/desired-skills.json"
    skills = load_manifest(manifest)
    root = skill_home()
    cli_names = cli_installed_names()

    installed = []
    missing = []
    for item in skills:
        name = item["name"]
        skill_file = root / name / "SKILL.md"
        system_file = global_skill_home() / ".system" / name / "SKILL.md"
        ok = skill_file.is_file() or system_file.is_file() or name in cli_names
        (installed if ok else missing).append(name)

    print(f"Manifest: {manifest}")
    print(f"Skill home: {root}")
    print(f"Installed: {len(installed)}")
    for name in installed:
        print(f"  OK {name}")
    print(f"Missing: {len(missing)}")
    for name in missing:
        print(f"  MISSING {name}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
