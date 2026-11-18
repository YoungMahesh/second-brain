#!/usr/bin/env python3
"""
Prepares the documentation directory and builds/serves the HTML documentation using Zensical.
"""

import argparse
import os
import shutil
import subprocess
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
SITE_DIR = os.path.join(ROOT_DIR, "site")

SOURCE_DIRS = [
    "00_Inbox",
    "10_Foundations",
    "20_Tooling",
    "30_Domains",
    "40_Resources",
]

EXCLUDE_PATTERNS = {
    ".obsidian",
    ".git",
    "__pycache__",
    ".canvas",
}


def clean_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)


def stage_documentation():
    """
    Stage source directories and root README.md into docs/.
    """
    os.makedirs(DOCS_DIR, exist_ok=True)

    # 1. Copy source directories
    for src in SOURCE_DIRS:
        src_path = os.path.join(ROOT_DIR, src)
        dest_path = os.path.join(DOCS_DIR, src)
        if not os.path.exists(src_path):
            continue

        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)

        def ignore_patterns(folder, items):
            ignored = []
            for item in items:
                if item in EXCLUDE_PATTERNS or item.endswith(".canvas"):
                    ignored.append(item)
            return ignored

        shutil.copytree(src_path, dest_path, ignore=ignore_patterns)

    # 2. Copy root README.md as docs/index.md
    readme_path = os.path.join(ROOT_DIR, "README.md")
    index_dest = os.path.join(DOCS_DIR, "index.md")
    if os.path.exists(readme_path):
        shutil.copy2(readme_path, index_dest)

    print(f"Documentation successfully staged into '{DOCS_DIR}'.")


def run_zensical(command, extra_args=None):
    """
    Execute zensical CLI via uv run.
    """
    cmd = ["uv", "run", "--with", "zensical", "zensical", command]
    if extra_args:
        cmd.extend(extra_args)

    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=ROOT_DIR)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Build or serve documentation using Zensical.")
    parser.add_argument("--serve", action="store_true", help="Start local development server with auto-reload")
    parser.add_argument("--clean", action="store_true", help="Clean docs/ and site/ before building")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode (fail on warnings)")

    args = parser.parse_args()

    if args.clean:
        print("Cleaning previous build directories...")
        clean_dir(DOCS_DIR)
        clean_dir(SITE_DIR)

    stage_documentation()

    if args.serve:
        sys.exit(run_zensical("serve"))
    else:
        extra = []
        if args.strict:
            extra.append("-s")
        sys.exit(run_zensical("build", extra))


if __name__ == "__main__":
    main()
