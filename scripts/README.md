# Documentation Tooling Scripts

This directory contains automation scripts for maintaining and publishing the documentation.

## Scripts

### 1. `build_docs.py`
Stages source markdown files and static assets into `docs/` and triggers Zensical builds.

```bash
# Start local live preview server (http://127.0.0.1:8000)
uv run python scripts/build_docs.py --serve

# Clean previous output and build static HTML into site/
uv run python scripts/build_docs.py --clean

# Build with strict link and anchor validation (fails on warnings)
uv run python scripts/build_docs.py --clean --strict
```

### 2. `convert_links.py`
In-place link migration tool that converts Obsidian-style wikilinks (`[[Note]]`, `[[Note|Alias]]`, `[[Note#Section]]`) into standard relative Markdown links.

```bash
# Dry run to preview conversions without modifying files
uv run python scripts/convert_links.py --dry-run

# Convert wikilinks in-place across all markdown files
uv run python scripts/convert_links.py
```
