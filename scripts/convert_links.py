#!/usr/bin/env python3
"""
Convert Obsidian wikilinks to standard Markdown links in-place across markdown files.
"""

import os
import re
import sys
import urllib.parse

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

IGNORE_DIRS = {
    ".git",
    ".obsidian",
    ".gemini",
    ".agents",
    "site",
    "scripts",
    "__pycache__",
    ".venv",
}


def build_file_index(root_dir):
    """
    Build index mapping target identifiers to relative paths from root_dir.
    .md files take absolute precedence over non-markdown files.
    """
    md_index = {}
    other_index = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS and not (d == "docs" and os.path.abspath(dirpath) == ROOT_DIR)
        ]
        for f in filenames:
            if f.startswith("."):
                continue  # skip hidden dotfiles like .obsidian.vimrc
            rel_path = os.path.relpath(os.path.join(dirpath, f), root_dir)
            base_name = f
            stem, ext = os.path.splitext(f)
            is_md = ext.lower() == ".md"
            target_dict = md_index if is_md else other_index

            variants = [
                rel_path,
                os.path.splitext(rel_path)[0],
                base_name,
                stem,
                re.sub(r"\(.*?\)", "", stem).strip(),
                re.sub(r"[^a-zA-Z0-9]", "", stem),
            ]

            for var in variants:
                if not var:
                    continue
                var_lower = var.lower()
                if var_lower not in target_dict:
                    target_dict[var_lower] = rel_path
                target_dict.setdefault(var, rel_path)

    # Merge: md_index overrides other_index completely
    combined = {**other_index, **md_index}
    return combined


def slugify_anchor(anchor_text):
    """
    Convert an anchor text like 'Connect local app' to a markdown header slug.
    """
    slug = anchor_text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug


def resolve_link(target_raw, alias_raw, current_file_rel, index, inline_codes):
    """
    Resolve target and alias into (label, relative_link).
    """
    # Restore any inline codes within target_raw / alias_raw first
    for i, code in enumerate(inline_codes):
        placeholder = f"__INLINE_CODE_{i}__"
        clean_code = code.strip("`")
        if placeholder in target_raw:
            target_raw = target_raw.replace(placeholder, clean_code)
        if alias_raw and placeholder in alias_raw:
            alias_raw = alias_raw.replace(placeholder, clean_code)

    if "#" in target_raw:
        target_name, anchor = target_raw.split("#", 1)
        target_name = target_name.strip()
        anchor = anchor.strip()
    else:
        target_name = target_raw.strip()
        anchor = None

    alias = alias_raw.strip() if alias_raw else None

    # Internal anchor on same page
    if not target_name:
        label = alias if alias else (anchor if anchor else "section")
        link = f"#{slugify_anchor(anchor)}" if anchor else "#"
        return label, link

    clean_target = target_name
    matched_rel_path = None

    lookup_candidates = [
        clean_target,
        clean_target.lower(),
        clean_target.removesuffix(".md").lower(),
        re.sub(r"\(.*?\)", "", clean_target).strip().lower(),
        re.sub(r"[^a-zA-Z0-9]", "", clean_target.lower()),
    ]

    for cand in lookup_candidates:
        if cand in index:
            matched_rel_path = index[cand]
            break

    label = alias if alias else target_name

    if not matched_rel_path:
        base_cand = os.path.basename(clean_target).lower()
        if base_cand in index:
            matched_rel_path = index[base_cand]

    if matched_rel_path:
        curr_dir = os.path.dirname(os.path.join(ROOT_DIR, current_file_rel))
        target_abs = os.path.join(ROOT_DIR, matched_rel_path)
        rel_from_curr = os.path.relpath(target_abs, curr_dir)

        # URL encode path while keeping forward slashes
        parts = rel_from_curr.split(os.sep)
        encoded_parts = [urllib.parse.quote(p) for p in parts]
        encoded_link = "/".join(encoded_parts)

        if anchor:
            encoded_link += f"#{slugify_anchor(anchor)}"
        return label, encoded_link
    else:
        # Dangling/unresolved note link: return text
        if anchor:
            label = f"{label} ({anchor})"
        return label, None


def convert_text(text, current_file_rel, index, stats):
    """
    Convert text while preserving fenced code blocks and inline code.
    """
    code_blocks = []
    def save_fence(m):
        code_blocks.append(m.group(0))
        return f"__FENCED_CODE_BLOCK_{len(code_blocks)-1}__"

    text = re.sub(r"```[a-zA-Z0-9_-]*\n.*?```", save_fence, text, flags=re.DOTALL)

    inline_codes = []
    def save_inline(m):
        inline_codes.append(m.group(0))
        return f"__INLINE_CODE_{len(inline_codes)-1}__"

    text = re.sub(r"`[^`\n]+`", save_inline, text)

    wikilink_pattern = re.compile(r"\[\[(.*?)\]\]")

    def replace_wikilink(m):
        raw_inside = m.group(1).strip()
        stats["total_wikilinks"] += 1

        parts = raw_inside.split("|")
        target_raw = parts[0].strip()
        alias_raw = parts[1].strip() if len(parts) > 1 else None

        label, link = resolve_link(target_raw, alias_raw, current_file_rel, index, inline_codes)

        if link:
            stats["resolved"] += 1
            return f"[{label}]({link})"
        else:
            stats["dangling"].append((current_file_rel, raw_inside))
            return f"**{label}**"

    converted = wikilink_pattern.sub(replace_wikilink, text)

    for i, code in enumerate(inline_codes):
        converted = converted.replace(f"__INLINE_CODE_{i}__", code)

    for i, block in enumerate(code_blocks):
        converted = converted.replace(f"__FENCED_CODE_BLOCK_{i}__", block)

    return converted


def main():
    dry_run = "--dry-run" in sys.argv
    root = ROOT_DIR

    index = build_file_index(root)
    print(f"Indexed {len(index)} file lookup keys across repository.")

    stats = {
        "total_files": 0,
        "modified_files": 0,
        "total_wikilinks": 0,
        "resolved": 0,
        "dangling": [],
    }

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS and not (d == "docs" and os.path.abspath(dirpath) == ROOT_DIR)
        ]
        for f in filenames:
            if not f.endswith(".md"):
                continue
            stats["total_files"] += 1
            filepath = os.path.join(dirpath, f)
            rel_path = os.path.relpath(filepath, root)

            with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
                original = fp.read()

            converted = convert_text(original, rel_path, index, stats)

            if converted != original:
                stats["modified_files"] += 1
                if not dry_run:
                    with open(filepath, "w", encoding="utf-8") as fp:
                        fp.write(converted)
                print(f"{'[DRY RUN] Would update' if dry_run else 'Updated'}: {rel_path}")

    print("\n" + "=" * 50)
    print(f"Files scanned: {stats['total_files']}")
    print(f"Files modified: {stats['modified_files']}")
    print(f"Total wikilinks processed: {stats['total_wikilinks']}")
    print(f"Successfully resolved: {stats['resolved']}")
    print(f"Dangling (kept as bold text): {len(stats['dangling'])}")
    for d in stats["dangling"]:
        print(f"  - In {d[0]}: [[{d[1]}]]")
    print("=" * 50)


if __name__ == "__main__":
    main()
