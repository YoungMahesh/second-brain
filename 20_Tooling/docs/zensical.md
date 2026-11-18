#tool/docs #note-publish

- [Zensical](https://zensical.org/) - Static site generator built with Rust and Python.

## Commands

### Local Preview
Starts a local web server at `http://127.0.0.1:8000` with live reload on file changes:
```bash
uv run python scripts/build_docs.py --serve
```

### Production Build
Stages content from taxonomy folders into `docs/` and compiles static HTML into `site/`:
```bash
uv run python scripts/build_docs.py --clean
```

### Strict Mode (CI Validation)
Fails the build if any broken links or missing anchors are detected:
```bash
uv run python scripts/build_docs.py --clean --strict
```

### Link Conversion Utility
Verifies or converts any newly added Obsidian-style links in-place to standard Markdown links:
```bash
uv run python scripts/convert_links.py
```

## Configuration & Deployment
- Configuration: `zensical.toml`
- Deployment workflow: `.github/workflows/deploy.yml` (automated GitHub Pages publishing on push to `main`)
