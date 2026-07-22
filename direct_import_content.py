from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = "https://api.gitbook.com/v1"


def api(method: str, path: str, body=None, expected=(200, 201, 204)):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['GITBOOK_TOKEN']}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def chunked(items: list[dict], size: int = 25):
    for idx in range(0, len(items), size):
        yield items[idx : idx + size]


def markdown_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.M)
    if match:
        return re.sub(r"[*`_]+", "", match.group(1)).strip()[:80]
    return fallback


def parse_summary(space_dir: Path) -> list[tuple[str, str, str]]:
    current_group = "Pages"
    entries: list[tuple[str, str, str]] = []
    seen_paths = set()
    for line in (space_dir / "SUMMARY.md").read_text(encoding="utf-8").splitlines():
        group = re.match(r"^##\s+(.+)$", line)
        if group:
            current_group = group.group(1).strip()
            continue
        bullet = re.match(r"^\*\s+\[([^\]]+)\]\(([^)]+)\)", line)
        if not bullet:
            continue
        title, rel = bullet.group(1).strip(), bullet.group(2).strip()
        if not rel.endswith(".md") or rel == "README.md":
            continue
        if rel in seen_paths:
            continue
        seen_paths.add(rel)
        if (space_dir / rel).exists():
            entries.append((current_group, title, rel))
    return entries


def content_tree(space_id: str, cr_id: str | None = None):
    if cr_id:
        _, data = api("GET", f"/spaces/{space_id}/change-requests/{cr_id}/content")
    else:
        _, data = api("GET", f"/spaces/{space_id}/content")
    return data.get("pages") or []


def flatten_pages(pages: list[dict]) -> list[dict]:
    out = []
    for page in pages:
        out.append(page)
        out.extend(flatten_pages(page.get("pages") or []))
    return out


def create_group_markdown(space_title: str, group: str) -> str:
    return f"""---
description: "{group} pages imported from the HiPay developer portal."
icon: folder
---

# {group}

This group collects the {group.lower()} pages imported into the {space_title} space for the first-draft GitBook demo.
"""


def import_space(space: dict, created: dict) -> dict:
    folder = space["folder"]
    space_id = created["spaces"][space["key"]]
    space_dir = ROOT / folder
    _, cr = api("POST", f"/spaces/{space_id}/change-requests", {"subject": "Import HiPay demo content"})
    cr_id = cr["id"]

    readme = (space_dir / "README.md").read_text(encoding="utf-8")
    entries = parse_summary(space_dir)
    groups = []
    for group, _, _ in entries:
        if group not in groups:
            groups.append(group)

    root_changes = [
        {
            "operation": "insert_page",
            "title": markdown_title(readme, space["title"]),
            "document": {"markdown": readme},
        }
    ]
    for group in groups:
        root_changes.append(
            {
                "operation": "insert_page",
                "title": group,
                "document": {"markdown": create_group_markdown(space["title"], group)},
            }
        )
    for batch in chunked(root_changes):
        api("POST", f"/spaces/{space_id}/change-requests/{cr_id}/content", {"changes": batch})

    pages = flatten_pages(content_tree(space_id, cr_id))
    group_ids = {page.get("title"): page.get("id") for page in pages if page.get("title") in groups}
    child_changes = []
    for group, title, rel in entries:
        markdown = (space_dir / rel).read_text(encoding="utf-8")
        child_changes.append(
            {
                "operation": "insert_page",
                "title": markdown_title(markdown, title),
                "into": group_ids[group],
                "document": {"markdown": markdown},
            }
        )
    batches = 0
    for batch in chunked(child_changes):
        api("POST", f"/spaces/{space_id}/change-requests/{cr_id}/content", {"changes": batch})
        batches += 1

    api("POST", f"/spaces/{space_id}/change-requests/{cr_id}/merge")
    time.sleep(2)
    live_pages = flatten_pages(content_tree(space_id))
    return {
        "space": space_id,
        "change_request": cr_id,
        "groups": len(groups),
        "children": len(child_changes),
        "batches": batches,
        "live_pages": len(live_pages),
    }


def main() -> None:
    created = json.loads((ROOT / "gitbook-created.json").read_text(encoding="utf-8"))
    spaces = [
        {"key": "HOME", "folder": "home", "title": "Home"},
        {"key": "ONLINE", "folder": "online-payments", "title": "Online Payments"},
        {"key": "COMMERCE", "folder": "commerce-platforms", "title": "Commerce Platforms"},
        {"key": "FUNDAMENTALS", "folder": "payment-fundamentals", "title": "Payment Fundamentals"},
        {"key": "API", "folder": "api-reference", "title": "API Reference"},
    ]
    results = {}
    for space in spaces:
        results[space["key"]] = import_space(space, created)
        print(space["key"], results[space["key"]])
    (ROOT / "gitbook-direct-import-results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    api("POST", f"/orgs/{created['org']}/sites/{created['site']}/publish")


if __name__ == "__main__":
    main()
