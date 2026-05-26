#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path, PurePosixPath


BLOCKED_TRACKED_PATHS = {
    ".obsidian/workspace.json",
    ".obsidian/workspaces.json",
}

BLOCKED_SUFFIXES = {
    ".DS_Store",
    "Thumbs.db",
}

BLOCKED_PATH_PARTS = {
    "__pycache__",
}

BLOCKED_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".pyd",
}


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(cmd))
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if check and result.returncode != 0:
        raise SystemExit(result.returncode)
    return result


def git_output(args: list[str]) -> str:
    result = run(["git", *args], check=True)
    return result.stdout.strip()


def ensure_repo_root() -> None:
    result = run(["git", "rev-parse", "--show-toplevel"], check=True)
    root = Path(result.stdout.strip())
    if root != Path.cwd():
        print(f"Run from repo root: {root}", file=sys.stderr)
        raise SystemExit(2)


def verify_project_skills() -> None:
    script = Path(".agents/skills/skill-manager/scripts/verify_manifest.py")
    if script.is_file():
        run(["python3", str(script)], check=True)
    else:
        print("Skill manifest verifier not found; skipping skill check.")


def collect_status_lines() -> list[str]:
    result = run(["git", "status", "--short"], check=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def path_from_status(line: str) -> str:
    value = line[3:].strip()
    if " -> " in value:
        value = value.split(" -> ", 1)[1]
    return value.strip('"')


def is_blocked_path(path: str) -> bool:
    normalized = path.replace("\\", "/")
    posix_path = PurePosixPath(normalized)
    return (
        normalized in BLOCKED_TRACKED_PATHS
        or any(normalized.endswith(suffix) for suffix in BLOCKED_SUFFIXES)
        or any(part in BLOCKED_PATH_PARTS for part in posix_path.parts)
        or posix_path.suffix in BLOCKED_EXTENSIONS
    )


def ensure_safe_status(lines: list[str]) -> None:
    blocked = []
    for line in lines:
        path = path_from_status(line)
        if is_blocked_path(path):
            blocked.append(path)
    if blocked:
        print("Blocked unsafe local files:", file=sys.stderr)
        for path in blocked:
            print(f"  {path}", file=sys.stderr)
        raise SystemExit(3)


def has_upstream() -> bool:
    result = run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], check=False)
    return result.returncode == 0 and bool(result.stdout.strip())


def push_current_branch() -> None:
    branch = git_output(["branch", "--show-current"])
    if not branch:
        print("Cannot push from detached HEAD.", file=sys.stderr)
        raise SystemExit(4)
    if has_upstream():
        run(["git", "push"], check=True)
    else:
        run(["git", "push", "-u", "origin", branch], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run checks, commit, and push current repo changes.")
    parser.add_argument("message", help="Commit message.")
    parser.add_argument("--no-push", action="store_true", help="Create the commit but skip git push.")
    args = parser.parse_args()

    message = args.message.strip()
    if not message:
        print("Commit message must not be empty.", file=sys.stderr)
        return 2

    ensure_repo_root()
    verify_project_skills()

    status_lines = collect_status_lines()
    if not status_lines:
        print("No changes to commit.")
        if not args.no_push:
            push_current_branch()
            print("Push complete.")
        return 0
    ensure_safe_status(status_lines)

    run(["git", "add", "."], check=True)
    staged = run(["git", "diff", "--cached", "--stat"], check=True)
    if not staged.stdout.strip():
        print("No staged changes after git add.")
        return 0

    run(["git", "commit", "-m", message], check=True)
    commit_hash = git_output(["rev-parse", "--short", "HEAD"])
    print(f"Created commit: {commit_hash}")

    if args.no_push:
        print("Skipped push because --no-push was set.")
    else:
        push_current_branch()
        print("Push complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
