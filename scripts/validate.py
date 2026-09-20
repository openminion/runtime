from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE",
    "README.md",
    "RELEASING.md",
    "SECURITY.md",
}
FORBIDDEN_SUFFIXES = (
    ".AppImage",
    ".deb",
    ".dmg",
    ".exe",
    ".msi",
    ".rpm",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".zip",
)


def tracked_files() -> list[str]:
    output = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return [line for line in output.splitlines() if line]


def main() -> None:
    tracked = tracked_files()
    missing = sorted(REQUIRED.difference(tracked))
    binaries = sorted(path for path in tracked if path.endswith(FORBIDDEN_SUFFIXES))
    if missing:
        raise SystemExit(f"missing public repository files: {', '.join(missing)}")
    if binaries:
        raise SystemExit(
            "release assets must use GitHub Releases: " + ", ".join(binaries)
        )
    print(f"validated {len(tracked)} tracked repository files")


if __name__ == "__main__":
    main()
