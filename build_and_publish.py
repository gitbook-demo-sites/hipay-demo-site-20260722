from __future__ import annotations

import html
import json
import os
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
BASE = "https://api.gitbook.com/v1"
ORG_ID = "qzcO5fqUkPmCrFmRQDUW"
ORG_TITLE = "HiPay"
REPO_OWNER = "gitbook-demo-sites"
REPO = "hipay-demo-site-20260722"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO}.git"
SITE_TITLE = "HiPay Developer Documentation Hub"
SITE_BASENAME = "hipay-developer-documentation-hub"
LOGO_LIGHT = "https://raw.githubusercontent.com/gitbook-demo-sites/hipay-demo-site-20260722/main/home/.gitbook/assets/hipay-logo-purple.svg"
LOGO_DARK = "https://developer.hipay.com/wp-content/uploads/hipay_logo.svg"

OPENAPI_SPECS = [
    ("hipay-api-gateway-v3", "API Gateway v3", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/api-gateway.yml"),
    ("hipay-online-payments-v1", "Online Payments API Gateway v1", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml"),
    ("hipay-hosted-page-v2", "Hosted Page v2", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml"),
    ("hipay-apple-pay-web", "Apple Pay Web API", "https://raw.githubusercontent.com/hipay/openapi-hipay/refs/heads/master/enterprise/applepay-web.yaml"),
    ("hipay-settlements", "Settlements API", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/settlement.yaml"),
    ("hipay-marketplace", "Marketplace API", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml"),
    ("hipay-terminal-api", "Terminal API", "https://raw.githubusercontent.com/hipay/openapi-hipay/refs/heads/master/omnichannel/openapi%20-%20Terminal%20API.yaml"),
    ("hipay-nepting-cloud-api", "Cloud API for Nepting", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/omnichannel/openapi%20-%20Nepting.yaml"),
    ("hipay-standalone-terminal-cloud-api", "Cloud API for Standalone Payment Terminals", "https://raw.githubusercontent.com/hipay/openapi-hipay/master/omnichannel/openapi%20-%20ConcertV3.yaml"),
]

SPACES = [
    {
        "key": "HOME",
        "sentinel": "XSPACE_HOME",
        "folder": "home",
        "title": "Home",
        "emoji": "1f3e0",
        "icon": "house",
        "path": "home",
        "description": "A branded front door for the migrated HiPay developer experience.",
    },
    {
        "key": "ONLINE",
        "sentinel": "XSPACE_ONLINE",
        "folder": "online-payments",
        "title": "Online Payments",
        "emoji": "1f4b3",
        "icon": "credit-card",
        "path": "online-payments",
        "description": "Hosted Page, Hosted Fields, API-only, SDKs, payment means, and maintenance.",
    },
    {
        "key": "COMMERCE",
        "sentinel": "XSPACE_COMMERCE",
        "folder": "commerce-platforms",
        "title": "Commerce Platforms",
        "emoji": "1f6d2",
        "icon": "store",
        "path": "commerce-platforms",
        "description": "CMS modules, marketplace, mobile payments, point of sale, and omnichannel flows.",
    },
    {
        "key": "FUNDAMENTALS",
        "sentinel": "XSPACE_FUNDAMENTALS",
        "folder": "payment-fundamentals",
        "title": "Payment Fundamentals",
        "emoji": "1f6e1",
        "icon": "shield-halved",
        "path": "payment-fundamentals",
        "description": "Security, redirect pages, notifications, signatures, lifecycle, statuses, and error handling.",
    },
    {
        "key": "API",
        "sentinel": "XSPACE_API",
        "folder": "api-reference",
        "title": "API Reference",
        "emoji": "1f4bb",
        "icon": "code",
        "path": "api-reference",
        "description": "OpenAPI-rendered API references plus HiPay's agentic interface content.",
    },
]


def ascii_text(value: str) -> str:
    value = html.unescape(value or "")
    value = value.replace("\u2013", "-").replace("\u2014", "-").replace("\u2019", "'")
    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")


def slugify(value: str) -> str:
    value = ascii_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "page"


def clean_text(value: str) -> str:
    value = ascii_text(re.sub(r"\s+", " ", value)).strip()
    return value


def write(path: str, content: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    content = content.replace("{{%", "{%").replace("%}}", "%}")
    full.write_text(content.strip() + "\n", encoding="utf-8")


def api(method: str, path: str, body=None, expected=(200, 201, 204)):
    token = os.environ["GITBOOK_TOKEN"]
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "ignore")


def page_urls() -> list[str]:
    urls: list[str] = []
    for sitemap in ["https://developer.hipay.com/post-sitemap.xml", "https://developer.hipay.com/page-sitemap.xml"]:
        text = fetch(sitemap)
        urls.extend(re.findall(r"<loc>(.*?)</loc>", text))
    filtered = []
    for url in urls:
        path = urlparse(url).path.strip("/")
        if not path or path == "privacy-policy":
            continue
        filtered.append(url)
    return sorted(dict.fromkeys(filtered))


def space_for_url(url: str) -> str | None:
    path = urlparse(url).path.strip("/")
    if path.startswith("online-payments/"):
        return "online-payments"
    if path.startswith(("cms-modules/", "marketplace/", "mobile-payments/", "point-of-sale/", "uncategorized/")):
        return "commerce-platforms"
    if path.startswith("payment-fundamentals/"):
        return "payment-fundamentals"
    if path.startswith(("api-explorer/", "agentic-interfaces/")):
        return "api-reference"
    return None


def relative_page_path(url: str, folder: str) -> str:
    path = urlparse(url).path.strip("/")
    prefixes = {
        "online-payments": "online-payments/",
        "commerce-platforms": "",
        "payment-fundamentals": "payment-fundamentals/",
        "api-reference": "",
    }
    prefix = prefixes.get(folder, "")
    if prefix and path.startswith(prefix):
        path = path[len(prefix):]
    parts = [slugify(part) for part in path.split("/") if part]
    if not parts:
        parts = ["overview"]
    return "/".join(parts) + ".md"


def extract_markdown(url: str) -> tuple[str, str]:
    raw = fetch(url)
    title_match = re.search(r'<h1[^>]*class="entry-title"[^>]*>(.*?)</h1>', raw, re.I | re.S)
    if not title_match:
        title_match = re.search(r"<title>(.*?)</title>", raw, re.I | re.S)
    title = clean_text(re.sub("<[^>]+>", " ", title_match.group(1))) if title_match else urlparse(url).path.rsplit("/", 1)[-1]
    title = title.replace(" - Developer | HiPay", "").replace("Homepage - Developer | HiPay", "Homepage")

    start = raw.find('<div class="entry-content">')
    end = raw.find("</article>", start if start != -1 else 0)
    content = raw[start:end] if start != -1 and end != -1 else raw
    content = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", content, flags=re.I)
    content = re.sub(r'<span class="ez-toc-section[^>]*>.*?</span>', "", content, flags=re.I | re.S)
    content = re.sub(r'<span class="ez-toc-section-end[^>]*>.*?</span>', "", content, flags=re.I | re.S)

    def code_block(match: re.Match) -> str:
        text = re.sub("<[^>]+>", "", match.group(1))
        return "\n\n```\n" + ascii_text(html.unescape(text)).strip() + "\n```\n\n"

    content = re.sub(r"<pre[^>]*>([\s\S]*?)</pre>", code_block, content, flags=re.I)
    content = re.sub(r"<h2[^>]*>(.*?)</h2>", lambda m: "\n\n## " + clean_text(re.sub("<[^>]+>", " ", m.group(1))) + "\n\n", content, flags=re.I | re.S)
    content = re.sub(r"<h3[^>]*>(.*?)</h3>", lambda m: "\n\n### " + clean_text(re.sub("<[^>]+>", " ", m.group(1))) + "\n\n", content, flags=re.I | re.S)
    content = re.sub(r"<h4[^>]*>(.*?)</h4>", lambda m: "\n\n#### " + clean_text(re.sub("<[^>]+>", " ", m.group(1))) + "\n\n", content, flags=re.I | re.S)
    content = re.sub(r"<li[^>]*>(.*?)</li>", lambda m: "\n* " + clean_text(re.sub("<[^>]+>", " ", m.group(1))), content, flags=re.I | re.S)
    content = re.sub(r"</p\s*>", "\n\n", content, flags=re.I)
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.I)
    content = re.sub(r"<[^>]+>", " ", content)
    content = ascii_text(html.unescape(content))
    lines = []
    for line in content.splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()
        if not line:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if line.lower() in {"menu and widgets", "developers", "developer | hipay"}:
            continue
        lines.append(line)
    body = "\n".join(lines).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = body[:22000].rstrip()
    if len(body) < 80:
        body = "This imported page should be reviewed against the original WordPress article during a production migration."
    return title, body


def card(icon: str, title: str, desc: str, href: str) -> str:
    return f'<tr><td><i class="fa-{icon}"></i></td><td><strong>{title}</strong></td><td>{desc}</td><td><a href="{href}">{title}</a></td></tr>'


def gitbook_yaml(space: str) -> None:
    write(f"{space}/.gitbook.yaml", "root: ./\nstructure:\n  readme: README.md\n  summary: SUMMARY.md")


def source_page(title: str, url: str, body: str) -> str:
    desc = clean_text(re.sub(r"[#*`]", "", body))[:150]
    return f"""---
description: "{desc.replace('"', "'")}"
icon: file-lines
---

# {title}

{{% hint style="info" %}}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [{url}]({url})
{{% endhint %}}

{body}
"""


def scaffold_static_pages() -> None:
    write("README.md", "# HiPay demo site\n\nFirst-draft GitBook demo content for HiPay. Each top-level folder is a separate GitBook space.")
    write(".gitignore", ".DS_Store\nThumbs.db\n*.swp\n*.swo\n.idea/\n.vscode/")
    for item in SPACES:
        gitbook_yaml(item["folder"])

    cover = "https://ik.imagekit.io/hipay/homepage_hero_a6ce98e81f_0Grsw-VSV.png?tr=w-1600,h-700"
    write(
        "home/README.md",
        f"""---
description: "A modern SaaS developer portal demo for HiPay with AI-assisted self-service."
icon: house
cover: "{cover}"
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: false
---

# HiPay Developer Documentation Hub

Augmented payment documentation for merchants, developers, and commerce teams.

{{% columns %}}
{{% column width="58%" %}}
Move from a maintenance-heavy WordPress portal to a branded GitBook experience where merchants can self-serve, developers can trust generated API references, and editors can keep fast-changing payment guidance current without engineering overhead.

{{% hint style="success" %}}
Demo focus: reduce support tickets from stale documentation by putting AI search, OpenAPI rendering, page feedback, and structured authoring workflows in the same portal.
{{% endhint %}}
{{% endcolumn %}}

{{% column width="42%" %}}
```mermaid
flowchart TD
    Visitor[Merchant or developer] --> AI[Ask HiPay AI]
    AI --> Answer[Grounded answer]
    Answer --> Docs[Relevant docs page]
    Docs --> API[OpenAPI operation]
    Docs --> Feedback[Page feedback]
    Feedback --> Editor[Docs owner review]
```
{{% endcolumn %}}
{{% endcolumns %}}

## Ask HiPay AI

{{% hint style="info" %}}
**What do you want to build?** Try questions like `Which integration path should I choose?`, `How do I verify webhook signatures?`, or `Where is the Hosted Page API reference?`
{{% endhint %}}

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-sparkles"></i></td><td><strong>AI search for implementation answers</strong></td><td>A prominent assistant-style entry point helps merchants find integration, payment method, and troubleshooting answers without opening a support ticket.</td><td><a href="migration-plan.md">AI search demo</a></td></tr>
</tbody></table>

## Choose your path

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
{card("credit-card", "Integrate online payments", "Hosted Page, Hosted Fields, API-only, SDKs, payment methods, and maintenance.", "https://app.gitbook.com/s/XSPACE_ONLINE/")}
{card("store", "Launch commerce channels", "CMS modules, marketplace onboarding, mobile payments, POS, and online-to-instore flows.", "https://app.gitbook.com/s/XSPACE_COMMERCE/")}
{card("shield-halved", "Understand requirements", "Security, notifications, signature verification, transaction lifecycle, statuses, and errors.", "https://app.gitbook.com/s/XSPACE_FUNDAMENTALS/")}
{card("code", "Use the API reference", "Generated OpenAPI pages for gateway, hosted page, marketplace, settlements, and terminal APIs.", "https://app.gitbook.com/s/XSPACE_API/")}
</tbody></table>

## Audience segmentation demo

{{% tabs %}}
{{% tab title="Developers" %}}
Start with integration paths, SDK examples, OpenAPI operations, test cards, webhooks, and payment lifecycle details.
{{% endtab %}}

{{% tab title="Merchants" %}}
Use payment method, marketplace, POS, and support-ready pages to answer launch and operations questions without opening a ticket.
{{% endtab %}}

{{% tab title="Editors" %}}
Use GitBook change requests, Git Sync, page feedback, AI insights, and reusable content to keep high-change payment docs current.
{{% endtab %}}
{{% endtabs %}}
""",
    )
    write(
        "home/migration-plan.md",
        """---
description: "How the WordPress developer portal maps into a GitBook-first operating model."
icon: arrows-rotate
---

# Migration Plan

{{% stepper %}}
{{% step %}}
## Import and preserve the current IA

The demo imports the current sitemap into spaces that mirror reader jobs: online payments, commerce platforms, fundamentals, and API reference.
{{% endstep %}}

{{% step %}}
## Promote API Explorer pages to OpenAPI

Where the current portal embeds Swagger from GitHub, the demo registers the public OpenAPI specs and renders them with GitBook's OpenAPI block.
{{% endstep %}}

{{% step %}}
## Add audience paths

GitBook can later gate additive implementation notes by visitor claims such as `persona=developer`, `persona=merchant`, or `persona=partner`.
{{% endstep %}}

{{% step %}}
## Replace ticket triggers with feedback loops

Page feedback, AI search insights, and review workflows give the docs team a way to identify stale or missing answers before support tickets pile up.
{{% endstep %}}
{{% endstepper %}}
""",
    )
    write(
        "home/SUMMARY.md",
        "# Table of contents\n\n* [Home](README.md)\n* [Migration plan](migration-plan.md)",
    )

    landing_pages = {
        "online-payments/README.md": ("Online Payments", "Accept online payments with HiPay across hosted, embedded, API-only, SDK, payment-method, and maintenance flows.", "credit-card"),
        "commerce-platforms/README.md": ("Commerce Platforms", "Implement HiPay through CMS modules, marketplace connectors, mobile SDKs, POS, and online-to-instore commerce flows.", "store"),
        "payment-fundamentals/README.md": ("Payment Fundamentals", "Keep requirements, notifications, signatures, lifecycle, statuses, and errors in one maintained foundation.", "shield-halved"),
        "api-reference/README.md": ("API Reference", "Render canonical HiPay OpenAPI specs in GitBook and keep prose context beside generated endpoint pages.", "code"),
    }
    for path, (title, desc, icon) in landing_pages.items():
        write(
            path,
            f"""---
description: "{desc}"
icon: {icon}
---

# {title}

{desc}

{{% hint style="info" %}}
This space combines a curated landing page with imported WordPress pages from the current HiPay developer portal. The production migration should reconnect redirects, source ownership, and canonical OpenAPI generation.
{{% endhint %}}
""",
        )

    write(
        "api-reference/openapi-overview.md",
        """---
description: "The registered OpenAPI specs used by this demo."
icon: code
---

# OpenAPI Overview

The current HiPay API Explorer embeds public OpenAPI files from GitHub. This demo registers those specs with GitBook and uses `builtin:openapi` entries in the table of contents so endpoint pages are generated from the spec instead of hand-maintained in prose.

{{% hint style="success" %}}
This directly addresses HiPay's requirement for OpenAPI/API docs rendering and reduces drift between API behavior and documentation.
{{% endhint %}}

## Registered specs

""" + "\n".join([f"* [{label}]({url})" for _, label, url in OPENAPI_SPECS]),
    )


def scaffold_imported_pages() -> dict[str, list[tuple[str, str, str]]]:
    pages_by_space: dict[str, list[tuple[str, str, str]]] = {item["folder"]: [] for item in SPACES}
    for url in page_urls():
        folder = space_for_url(url)
        if not folder:
            continue
        rel = relative_page_path(url, folder)
        try:
            title, body = extract_markdown(url)
        except Exception as exc:
            title = urlparse(url).path.rsplit("/", 1)[-1].replace("-", " ").title()
            body = f"This page failed to import during the first draft scrape and should be retried. Error: `{ascii_text(str(exc))}`"
        write(f"{folder}/{rel}", source_page(title, url, body))
        pages_by_space[folder].append((rel, title, url))
    return pages_by_space


def group_name(folder: str, rel: str) -> str:
    first_part = rel.split("/", 1)[0]
    if first_part.endswith(".md"):
        first_part = first_part[:-3]
    first = first_part.replace("-", " ").title()
    special = {
        "Payment": "Payment",
        "Payment Means": "Payment means",
        "Features": "Features",
        "Maintenance": "Maintenance",
        "Sdk Reference": "SDK Reference",
        "Cms Modules": "CMS Modules",
        "Api Integration": "API Integration",
        "Mirakl": "Mirakl",
        "Izberg": "Izberg",
        "Ios": "iOS",
        "Android": "Android",
        "Smart Terminal": "Smart Terminal",
        "Online To Instore": "Online to inStore",
        "Requirements": "Requirements",
        "Essentials": "Essentials",
        "Api Explorer": "API Explorer",
        "Agentic Interfaces": "Agentic Interfaces",
    }
    return special.get(first, first)


def scaffold_summaries(pages_by_space: dict[str, list[tuple[str, str, str]]]) -> None:
    for item in SPACES:
        folder = item["folder"]
        if folder == "home":
            continue
        lines = ["# Table of contents", "", f"* [{item['title']}](README.md)"]
        if folder == "api-reference":
            lines += ["* [OpenAPI Overview](openapi-overview.md)", "", "## Generated OpenAPI"]
            for slug, label, _ in OPENAPI_SPECS:
                lines += [
                    f"* [{label}](openapi-overview.md)",
                    "* ```yaml",
                    "  type: builtin:openapi",
                    "  props:",
                    "    models: true",
                    "    downloadLink: true",
                    "  dependencies:",
                    "    spec:",
                    "      ref:",
                    "        kind: openapi",
                    f"        spec: {slug}",
                    "  ```",
                ]
        grouped: dict[str, list[tuple[str, str, str]]] = {}
        for rel, title, url in pages_by_space.get(folder, []):
            grouped.setdefault(group_name(folder, rel), []).append((rel, title, url))
        for group in sorted(grouped):
            lines += ["", f"## {group}"]
            for rel, title, _ in sorted(grouped[group], key=lambda x: x[1].lower()):
                lines.append(f"* [{title}]({rel})")
        write(f"{folder}/SUMMARY.md", "\n".join(lines))


def scaffold() -> None:
    scaffold_static_pages()
    pages_by_space = scaffold_imported_pages()
    scaffold_summaries(pages_by_space)
    (ROOT / "source-inventory.json").write_text(json.dumps(pages_by_space, indent=2) + "\n", encoding="utf-8")


def ensure_git_repo() -> None:
    if not (ROOT / ".git").exists():
        subprocess.run(["git", "init"], cwd=ROOT, check=True)
        subprocess.run(["git", "branch", "-M", "main"], cwd=ROOT, check=True)
    subprocess.run(["git", "add", "."], cwd=ROOT, check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode != 0:
        subprocess.run(["git", "commit", "-m", "Initial HiPay demo scaffold"], cwd=ROOT, check=True)
    view = subprocess.run(["gh", "repo", "view", f"{REPO_OWNER}/{REPO}"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if view.returncode != 0:
        subprocess.run(["gh", "repo", "create", f"{REPO_OWNER}/{REPO}", "--public", "--source", str(ROOT), "--remote", "origin", "--push"], cwd=ROOT, check=True)
    else:
        remotes = subprocess.run(["git", "remote"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.split()
        if "origin" not in remotes:
            subprocess.run(["git", "remote", "add", "origin", REPO_URL], cwd=ROOT, check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=ROOT, check=True)


def git_commit_push(message: str) -> None:
    subprocess.run(["git", "add", "."], cwd=ROOT, check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode == 0:
        return
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
    subprocess.run(["git", "push"], cwd=ROOT, check=True)


def ensure_openapi_specs() -> dict[str, dict]:
    results = {}
    for slug, label, url in OPENAPI_SPECS:
        payload = {"slug": slug, "source": {"url": url}}
        try:
            _, spec = api("POST", f"/orgs/{ORG_ID}/openapi", payload)
            results[slug] = {"created": True, "label": label, "spec": spec}
        except RuntimeError as exc:
            if "400" not in str(exc) and "409" not in str(exc):
                raise
            _, specs = api("GET", f"/orgs/{ORG_ID}/openapi")
            items = specs.get("items") or specs.get("results") or []
            match = next((item for item in items if item.get("slug") == slug), None)
            results[slug] = {"created": False, "label": label, "spec": match, "note": "slug already existed"}
    return results


def replace_sentinels(space_ids: dict[str, str]) -> None:
    replacements = {item["sentinel"]: space_ids[item["key"]] for item in SPACES}
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")


def create_site(openapi_results: dict[str, dict]) -> dict:
    _, site = api("POST", f"/orgs/{ORG_ID}/sites", {"type": "ultimate", "title": SITE_TITLE, "visibility": "share-link"})
    site_id = site["id"]
    api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}", {"title": SITE_TITLE, "visibility": "share-link", "basename": SITE_BASENAME})
    created = {"org": ORG_ID, "org_title": ORG_TITLE, "site": site_id, "site_object": site, "spaces": {}, "sections": {}, "site_spaces": {}, "openapi": openapi_results}
    for item in SPACES:
        _, space = api("POST", f"/orgs/{ORG_ID}/spaces", {"title": item["title"], "emoji": item["emoji"], "empty": True, "editMode": "live"})
        space_id = space["id"]
        created["spaces"][item["key"]] = space_id
        _, section = api("POST", f"/orgs/{ORG_ID}/sites/{site_id}/sections", {"spaceId": space_id, "title": item["title"], "icon": item["icon"], "draft": False})
        section_id = section["id"]
        site_space_id = section["siteSpaces"][0]["id"]
        created["sections"][item["key"]] = section_id
        created["site_spaces"][item["key"]] = site_space_id
        api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}/sections/{section_id}", {"path": item["path"], "description": item["description"], "draft": False, "defaultSiteSpace": site_space_id})
    api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}", {"defaultSiteSection": created["sections"]["HOME"], "defaultSiteSpace": created["site_spaces"]["HOME"]})
    replace_sentinels(created["spaces"])
    (ROOT / "gitbook-created.json").write_text(json.dumps(created, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Resolve HiPay GitBook space links")
    return created


def import_spaces(created: dict) -> dict:
    results = {}
    for item in SPACES:
        status, _ = api(
            "POST",
            f"/spaces/{created['spaces'][item['key']]}/git/import",
            {
                "url": REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": f"https://github.com/{REPO_OWNER}/{REPO}/tree/main",
                "repoCommitURL": f"https://github.com/{REPO_OWNER}/{REPO}/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        results[item["key"]] = {"status": status, "space": created["spaces"][item["key"]], "folder": item["folder"]}
    (ROOT / "gitbook-import-results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Add HiPay GitBook import artifacts")
    return results


def customize_and_publish(created: dict) -> dict:
    site_id = created["site"]
    customization = {
        "title": SITE_TITLE,
        "localizedTitle": {},
        "internationalization": {"locale": "en"},
        "styling": {
            "theme": "clean",
            "primaryColor": {"light": "#2C0A64", "dark": "#7C5CFF"},
            "infoColor": {"light": "#2663FF", "dark": "#7C9DFF"},
            "successColor": {"light": "#00A86B", "dark": "#19D38A"},
            "warningColor": {"light": "#F59E0B", "dark": "#FBBF24"},
            "dangerColor": {"light": "#D92D20", "dark": "#F97066"},
            "tint": {"color": {"light": "#F7F5FF", "dark": "#140A2E"}},
            "corners": "straight",
            "depth": "flat",
            "links": "accent",
            "font": "Inter",
            "monospaceFont": "IBMPlexMono",
            "icons": "regular",
            "background": "plain",
            "sidebar": {"background": "filled", "list": "line"},
            "codeTheme": {
                "default": {"light": "default-light", "dark": "default-dark"},
                "openapi": {"light": "default-light", "dark": "default-dark"},
            },
            "search": "prominent",
        },
        "favicon": {"icon": {"light": "https://hipay.com/favicon.svg", "dark": "https://hipay.com/favicon.svg"}},
        "header": {
            "preset": "default",
            "logo": {"light": LOGO_LIGHT, "dark": LOGO_DARK},
            "links": [
                {"title": "HiPay", "to": {"kind": "url", "url": "https://hipay.com/en/"}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Current docs", "to": {"kind": "url", "url": "https://developer.hipay.com/"}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "API reference", "to": {"kind": "space", "space": created["spaces"]["API"]}, "style": "button-secondary", "links": [], "localizedTitle": {}},
            ],
        },
        "footer": {
            "logo": {"light": LOGO_LIGHT, "dark": LOGO_DARK},
            "groups": [
                {
                    "title": "Demo sections",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Online payments", "to": {"kind": "space", "space": created["spaces"]["ONLINE"]}, "localizedTitle": {}},
                        {"title": "Commerce platforms", "to": {"kind": "space", "space": created["spaces"]["COMMERCE"]}, "localizedTitle": {}},
                        {"title": "API reference", "to": {"kind": "space", "space": created["spaces"]["API"]}, "localizedTitle": {}},
                    ],
                },
                {
                    "title": "Sources",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Source repo", "to": {"kind": "url", "url": f"https://github.com/{REPO_OWNER}/{REPO}"}, "localizedTitle": {}},
                        {"title": "HiPay website", "to": {"kind": "url", "url": "https://hipay.com/en/"}, "localizedTitle": {}},
                        {"title": "Current developer portal", "to": {"kind": "url", "url": "https://developer.hipay.com/"}, "localizedTitle": {}},
                    ],
                },
            ],
            "copyright": "HiPay Developer Documentation Hub demo - built for review in GitBook.",
        },
        "themes": {"default": "light", "toggeable": True},
        "pdf": {"enabled": True},
        "feedback": {"enabled": True},
        "ai": {
            "mode": "assistant",
            "suggestions": [
                "Which integration path should a merchant choose?",
                "How do I verify webhook signatures?",
                "Where are the OpenAPI docs for API Gateway v3?",
                "Which CMS modules does HiPay support?",
                "How do refunds and captures work?",
            ],
        },
        "advancedCustomization": {"enabled": True},
        "trademark": {"enabled": True},
        "externalLinks": {"target": "self"},
        "pagination": {"enabled": True},
        "pageActions": {"externalAI": True, "markdown": True, "mcp": True, "items": ["assistant", "markdown", "external-ai", "mcp", "pdf"]},
        "git": {"showEditLink": False},
        "privacyPolicy": {"url": "https://hipay.com/en/privacy-and-terms/"},
        "socialPreview": {"url": "https://ik.imagekit.io/hipay/homepage_hero_a6ce98e81f_0Grsw-VSV.png?tr=w-1200,h-630"},
        "socialAccounts": [],
        "insights": {"trackingCookie": True},
    }
    _, customized = api("PUT", f"/orgs/{ORG_ID}/sites/{site_id}/customization", customization)
    (ROOT / "gitbook-customization-result.json").write_text(json.dumps(customized, indent=2) + "\n", encoding="utf-8")
    publish_status, publish = api("POST", f"/orgs/{ORG_ID}/sites/{site_id}/publish")
    share_status, share = api("POST", f"/orgs/{ORG_ID}/sites/{site_id}/share-links", {"name": "HiPay demo review"})
    final = {
        "publish_status": publish_status,
        "publish": publish,
        "share_status": share_status,
        "share": share,
        "published_url": share["urls"]["published"],
        "app_url": publish["urls"]["app"],
        "preview_url": publish["urls"]["preview"],
    }
    (ROOT / "gitbook-publish-share.json").write_text(json.dumps(final, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Add HiPay GitBook publish artifacts")
    return final


def main() -> None:
    scaffold()
    ensure_git_repo()
    openapi_results = ensure_openapi_specs()
    created = create_site(openapi_results)
    import_spaces(created)
    time.sleep(35)
    final = customize_and_publish(created)
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
