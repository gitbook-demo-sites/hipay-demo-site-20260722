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

SPACES = [
    {"key": "HOME", "folder": "home", "title": "Home"},
    {"key": "ONLINE", "folder": "online-payments", "title": "Online Payments"},
    {"key": "COMMERCE", "folder": "commerce-platforms", "title": "Commerce Platforms"},
    {"key": "FUNDAMENTALS", "folder": "payment-fundamentals", "title": "Payment Fundamentals"},
    {"key": "API", "folder": "api-reference", "title": "API Reference"},
]


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


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
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def chunked(items: list[dict], size: int = 20):
    for idx in range(0, len(items), size):
        yield items[idx : idx + size]


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


def markdown_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.M)
    title = match.group(1).strip() if match else fallback
    title = re.sub(r"[*`_]+", "", title)
    title = re.sub(r"\.(md|markdown|mdx)$", "", title, flags=re.I).strip()
    return title[:80]


def parse_summary(space_dir: Path) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    seen_paths = set()
    for line in (space_dir / "SUMMARY.md").read_text(encoding="utf-8").splitlines():
        bullet = re.match(r"^\*\s+\[([^\]]+)\]\(([^)]+)\)", line)
        if not bullet:
            continue
        title, rel = bullet.group(1).strip(), bullet.group(2).strip()
        if rel == "README.md" or not rel.endswith(".md") or rel in seen_paths:
            continue
        if (space_dir / rel).exists():
            entries.append((title, rel))
            seen_paths.add(rel)
    return entries


def card_table(rows: list[tuple[str, str, str, str]]) -> str:
    body = "\n".join(
        f'<tr><td><h4><i class="fa-{icon}" style="color:$primary;"></i></h4></td><td><strong>{title}</strong></td><td>{desc}</td><td><a href="{href}">{title}</a></td></tr>'
        for icon, title, desc, href in rows
    )
    return (
        '<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th>'
        '<th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>\n'
        + body
        + "\n</tbody></table>"
    )


def scaffold_files() -> None:
    write(
        "home/SUMMARY.md",
        """
# Table of contents

* [Home](README.md)
* [Migration story](migration-story.md)
* [Demo checklist](demo-checklist.md)
""",
    )
    write(
        "home/README.md",
        """
---
description: "A GitBook-first developer portal for HiPay merchants, developers, and support teams."
icon: house
cover: "https://ik.imagekit.io/hipay/homepage_hero_a6ce98e81f_0Grsw-VSV.png?tr=w-1600,h-700"
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: true
---

# HiPay Developer Documentation

{% columns %}
{% column width="50%" %}
Build, launch, and operate payment experiences across online checkout, marketplaces, mobile apps, and point of sale.

This demo turns HiPay's WordPress developer portal into a modern GitBook experience: curated navigation, AI-assisted answers, OpenAPI-powered references, and authoring blocks that make implementation steps easier to follow.

<button type="button" class="button primary" data-action="ask" data-icon="gitbook-assistant">Ask HiPay AI</button>

<button type="button" class="button secondary" data-action="ask" data-query="Which HiPay integration path should I choose?" data-icon="route">Choose an integration</button> <button type="button" class="button secondary" data-action="ask" data-query="How do I create and refund a test payment?" data-icon="credit-card">Run a payment</button> <button type="button" class="button secondary" data-action="ask" data-query="How do I verify HiPay signatures?" data-icon="shield-check">Verify signatures</button>
{% endcolumn %}

{% column width="50%" %}
{% hint style="success" icon="gitbook" %}
**A note from GitBook**

This version is intentionally demo-led instead of a raw import. It keeps the HiPay information architecture, but upgrades the pages that matter in a sales conversation with cards, steppers, tabs, code samples, tables, Mermaid diagrams, and OpenAPI blocks.
{% endhint %}

```mermaid
flowchart TD
    Merchant[Merchant or developer] --> Search[Ask HiPay AI]
    Search --> Guided[Guided answer]
    Guided --> Page[Structured GitBook page]
    Page --> API[OpenAPI reference]
    Page --> Feedback[Page feedback]
    Feedback --> Owner[Docs owner fixes source]
```
{% endcolumn %}
{% endcolumns %}

***

## Start with a goal

""" + card_table([
            ("route", "Choose an integration path", "Hosted Page, Hosted Fields, API-only, CMS module, mobile SDK, marketplace, or POS.", "https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/choose-integration-path"),
            ("wand-magic-sparkles", "Use the AI entry point", "Ask implementation questions in natural language and land on the right page or API operation.", "migration-story.md"),
            ("code", "Explore API references", "Use inline OpenAPI blocks for the most important gateway, hosted page, and marketplace operations.", "https://app.gitbook.com/s/iLPCxDjmgR6F8AXe5kC9/"),
            ("store", "Launch commerce channels", "CMS modules, marketplace onboarding, POS, and mobile payments are organized by channel.", "https://app.gitbook.com/s/DXPlTLH37dJoMvok3HAf/"),
        ]) + """

## Picked for you

{% if visitor.claims.unsigned.audience === "developer" %}
{% hint style="info" icon="code" %}
Developer view: start with Hosted Fields, API Gateway, webhook signatures, and transaction operations.
{% endhint %}
{% endif %}

{% if visitor.claims.unsigned.audience === "merchant" %}
{% hint style="info" icon="store" %}
Merchant view: start with integration choice, payment methods, CMS launch, and self-service support flows.
{% endhint %}
{% endif %}

""" + card_table([
            ("credit-card", "Online payments", "Hosted checkout, embedded fields, API-only payment creation, payment means, and maintenance.", "https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/"),
            ("cart-shopping", "Commerce platforms", "CMS modules, marketplace vendors, mobile apps, and point-of-sale journeys.", "https://app.gitbook.com/s/DXPlTLH37dJoMvok3HAf/"),
            ("shield-halved", "Payment fundamentals", "Security, SCA, signatures, transaction lifecycle, statuses, and error handling.", "https://app.gitbook.com/s/77QPwl2jzuBosZDzPHML/"),
            ("terminal", "API reference", "Gateway, Hosted Page, Marketplace, Settlements, Apple Pay, and terminal APIs.", "https://app.gitbook.com/s/iLPCxDjmgR6F8AXe5kC9/"),
        ]) + """

## What changed from the WordPress portal

{% columns %}
{% column width="50%" %}
### Before

* Long pages with important code samples buried in prose.
* API reference pages maintained separately from the spec.
* Navigation that mirrored WordPress categories.
* Support tickets when merchants could not find current answers.
{% endcolumn %}

{% column width="50%" %}
### With GitBook

* AI search and page feedback on every page.
* OpenAPI rendered directly in the docs experience.
* Structured blocks for complex implementation steps.
* A maintainable source workflow for docs owners.
{% endcolumn %}
{% endcolumns %}
""",
    )
    write(
        "home/migration-story.md",
        """
---
description: "How the HiPay WordPress portal maps to a GitBook-first developer experience."
icon: arrows-rotate
---

# Migration story

This demo keeps the useful parts of the current HiPay portal while removing the raw-import feel. The high-traffic journeys are rebuilt as GitBook-native pages and the long tail can be migrated iteratively.

{% stepper %}
{% step %}
## Mirror the existing portal

Start from the current HiPay documentation areas: Online Payments, CMS Modules, Marketplace, Point of Sale, Mobile Payments, Payment Fundamentals, API Explorer, and Agentic Interfaces.
{% endstep %}

{% step %}
## Rebuild the anchor pages

The homepage, integration chooser, Hosted Fields guide, CMS launch guide, signature verification, and API overview get the full GitBook treatment first.
{% endstep %}

{% step %}
## Keep API docs tied to specs

OpenAPI blocks reference the public HiPay OpenAPI sources instead of duplicating endpoint tables by hand.
{% endstep %}

{% step %}
## Use feedback and AI insights to prioritize cleanup

Docs owners can use page feedback and AI questions to decide which imported long-tail pages need editorial cleanup next.
{% endstep %}
{% endstepper %}

## Demo moments

""" + card_table([
            ("magnifying-glass", "Prominent AI search", "Use the homepage buttons to ask common implementation questions.", "README.md"),
            ("list-check", "Stepper conversion", "Hosted Fields and CMS flows are written as ordered GitBook steppers.", "https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/hosted-fields-quickstart"),
            ("table", "Real tables", "Payment means and error handling use structured tables rather than prose placeholders.", "https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/payment-methods"),
            ("code", "Code that renders", "API and SDK examples are in fenced code blocks and tabs.", "https://app.gitbook.com/s/iLPCxDjmgR6F8AXe5kC9/gateway-api"),
        ]) + """
""",
    )
    write(
        "home/demo-checklist.md",
        """
---
description: "A short checklist for reviewing the HiPay demo site."
icon: clipboard-check
---

# Demo checklist

{% hint style="info" %}
Use this page as the internal review checklist before showing the site to HiPay.
{% endhint %}

{% stepper %}
{% step %}
## Open the homepage

Confirm the hero, HiPay branding, AI search buttons, and card navigation feel closer to the Evolve demo site than a raw import.
{% endstep %}

{% step %}
## Test a developer journey

Open **Online Payments -> Hosted Fields quickstart** and check that the numbered implementation flow uses steppers, tabs, hints, and code blocks.
{% endstep %}

{% step %}
## Test a merchant journey

Open **Commerce Platforms -> CMS module launch** and confirm the page reads like a launch guide rather than imported WordPress text.
{% endstep %}

{% step %}
## Test an API journey

Open **API Reference -> Gateway API** and confirm OpenAPI blocks, request examples, and implementation context are visible.
{% endstep %}
{% endstepper %}
""",
    )

    write(
        "online-payments/SUMMARY.md",
        """
# Table of contents

* [Online Payments](README.md)
* [Choose an integration path](choose-integration-path.md)
* [Hosted Page quickstart](hosted-page-quickstart.md)
* [Hosted Fields quickstart](hosted-fields-quickstart.md)
* [Payment methods](payment-methods.md)
* [Webhooks and notifications](webhooks-and-notifications.md)
* [Transaction operations](transaction-operations.md)
""",
    )
    write(
        "online-payments/README.md",
        """
---
description: "Choose and build the right HiPay online payment integration."
icon: credit-card
layout:
  width: wide
  tableOfContents:
    visible: true
  outline:
    visible: true
---

# Online Payments

Accept online payments with Hosted Page, Hosted Fields, API-only flows, SDKs, and payment methods that match each merchant journey.

<button type="button" class="button primary" data-action="ask" data-query="Which HiPay online payment integration should I choose?" data-icon="gitbook-assistant">Ask which integration fits</button>

""" + card_table([
            ("route", "Choose an integration path", "Compare Hosted Page, Hosted Fields, Hosted Payments, API-only, and CMS module routes.", "choose-integration-path.md"),
            ("window-maximize", "Hosted Page quickstart", "Redirect customers to a HiPay-hosted checkout and customize the experience.", "hosted-page-quickstart.md"),
            ("credit-card", "Hosted Fields quickstart", "Embed secure card fields while keeping sensitive data off your servers.", "hosted-fields-quickstart.md"),
            ("bell", "Webhooks and notifications", "Receive server-to-server notifications and keep merchant systems in sync.", "webhooks-and-notifications.md"),
        ]) + """

## Payment flow at a glance

```mermaid
sequenceDiagram
    participant Shopper
    participant Merchant
    participant HiPay
    participant Bank
    Shopper->>Merchant: Starts checkout
    Merchant->>HiPay: Creates payment or hosted page
    HiPay->>Bank: Authorizes payment
    Bank-->>HiPay: Authorization result
    HiPay-->>Merchant: API response
    HiPay-->>Merchant: Server notification
    Merchant-->>Shopper: Confirmation page
```
""",
    )
    write(
        "online-payments/choose-integration-path.md",
        """
---
description: "Compare HiPay integration patterns by control, effort, and maintenance."
icon: route
---

# Choose an integration path

The right integration depends on how much checkout control the merchant needs and how much technical overhead they want to carry.

| Path | Best for | Merchant control | Technical overhead |
| --- | --- | --- | --- |
| Hosted Page | Fast launch with low PCI scope | Medium | Low |
| Hosted Fields | Embedded card form without handling PAN data | High | Medium |
| Hosted Payments | Payment form embedded in an existing journey | Medium | Medium |
| API-only | Fully custom checkout and orchestration | Very high | High |
| CMS module | Shopify, Magento, PrestaShop, Shopware, SFCC, WooCommerce | Medium | Low |

{% hint style="success" %}
For most merchants replacing stale support-heavy docs, start with Hosted Page or a CMS module. Use Hosted Fields when the checkout UX must stay embedded.
{% endhint %}

{% tabs %}
{% tab title="Fast launch" %}
Use **Hosted Page** or a **CMS module**. HiPay hosts the checkout surface or maintains the connector, reducing implementation and maintenance work.
{% endtab %}

{% tab title="Custom checkout" %}
Use **Hosted Fields** or **API-only**. You keep control over the page and can orchestrate advanced payment logic.
{% endtab %}

{% tab title="Marketplace" %}
Use **Marketplace APIs** for vendor onboarding, KYC, bank information, cash out, and split flows.
{% endtab %}
{% endtabs %}

## Selection workflow

{% stepper %}
{% step %}
## Identify the sales channel

Online store, mobile app, marketplace, or point of sale. This determines the first branch in the docs.
{% endstep %}

{% step %}
## Decide who owns checkout UI

If HiPay can host the checkout, choose Hosted Page. If the merchant must own the UI, choose Hosted Fields or API-only.
{% endstep %}

{% step %}
## Match the operational model

If non-technical teams must maintain the integration, prefer CMS modules and documented configuration screens.
{% endstep %}

{% step %}
## Connect to the API reference

Use the generated OpenAPI reference for exact endpoints, required fields, and response schemas.
{% endstep %}
{% endstepper %}
""",
    )
    write(
        "online-payments/hosted-page-quickstart.md",
        """
---
description: "Create and customize a HiPay Hosted Page payment."
icon: window-maximize
---

# Hosted Page quickstart

Hosted Page lets a merchant redirect shoppers to a HiPay-managed checkout while keeping implementation effort low.

{% stepper %}
{% step %}
## Create the hosted payment

Call the Hosted Page API with the order amount, currency, order id, customer information, and redirect URLs.

{% code title="Create a Hosted Page payment" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/hpayment" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \\
  -d "orderid=HP-DEMO-1001" \\
  -d "amount=49.90" \\
  -d "currency=EUR" \\
  -d "description=Demo checkout" \\
  -d "accept_url=https://merchant.example/success" \\
  -d "decline_url=https://merchant.example/declined"
```
{% endcode %}
{% endstep %}

{% step %}
## Redirect the shopper

Use the redirect URL returned by HiPay. Keep the merchant confirmation page focused on order status, not payment assumptions.
{% endstep %}

{% step %}
## Listen for the server notification

Use the notification to update the order in the merchant system. Do not rely only on the shopper redirect.
{% endstep %}

{% step %}
## Capture, refund, or challenge when needed

Use maintenance operations to manage the transaction lifecycle after authorization.
{% endstep %}
{% endstepper %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml" path="/v1/hpayment" method="post" %}
[Hosted Page API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml)
{% endopenapi %}
""",
    )
    write(
        "online-payments/hosted-fields-quickstart.md",
        """
---
description: "Embed secure HiPay card fields in a merchant checkout."
icon: credit-card
---

# Hosted Fields quickstart

Hosted Fields gives merchants an embedded checkout while keeping sensitive card data inside HiPay-hosted components.

{% hint style="warning" %}
Only public credentials belong in browser code. Server-side order creation still uses private credentials.
{% endhint %}

{% stepper %}
{% step %}
## Load the JavaScript SDK

Add the HiPay JavaScript SDK to the checkout page and initialize it with public credentials.

```html
<script src="https://libs.hipay.com/js/sdkjs.js"></script>
<script>
  const hipay = HiPay({
    username: "HIPAY_PUBLIC_LOGIN",
    password: "HIPAY_PUBLIC_PASSWORD",
    environment: "stage",
    lang: "en"
  });
</script>
```
{% endstep %}

{% step %}
## Create the field containers

Use stable container IDs for card holder, card number, expiry date, and CVC.

```html
<label>Card holder</label>
<div id="hipay-card-holder"></div>

<label>Card number</label>
<div id="hipay-card-number"></div>

<label>Expiry date</label>
<div id="hipay-expiry-date"></div>

<label>CVC</label>
<div id="hipay-cvc"></div>
```
{% endstep %}

{% step %}
## Mount the Hosted Fields

Choose automatic mode for lower maintenance or custom mode when the merchant needs full checkout layout control.

{% tabs %}
{% tab title="Automatic mode" %}
```js
const cardInstance = hipay.create("card", {
  template: "auto",
  selector: "hipay-hostedfields-form"
});
```
{% endtab %}

{% tab title="Custom mode" %}
```js
const cardInstance = hipay.create("card", {
  fields: {
    cardHolder: { selector: "hipay-card-holder" },
    cardNumber: { selector: "hipay-card-number" },
    expiryDate: { selector: "hipay-expiry-date" },
    cvc: { selector: "hipay-cvc", helpButton: true }
  }
});
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
## Tokenize the card

Submit the hosted fields to get a token. Send that token to the merchant backend, never raw card data.
{% endstep %}

{% step %}
## Create the order server-side

The backend calls the HiPay Order API with the card token, amount, currency, order id, and customer details.
{% endstep %}
{% endstepper %}

## Field state reference

| State class | Meaning | Typical UI treatment |
| --- | --- | --- |
| `HiPayField-empty` | No value entered yet | Neutral border |
| `HiPayField-focused` | Shopper is editing the field | Brand accent border |
| `HiPayField-valid` | Field passed validation | Success state |
| `HiPayField-invalid` | Field failed validation | Error message and retry |
""",
    )
    write(
        "online-payments/payment-methods.md",
        """
---
description: "Payment method guidance for HiPay merchants."
icon: wallet
---

# Payment methods

Use payment method pages to answer merchant questions before they become support tickets: availability, shopper experience, testing, settlement behavior, and special requirements.

| Method | Region or use case | Integration note |
| --- | --- | --- |
| Cards | Broad international coverage | Works across Hosted Page, Hosted Fields, and API-only flows |
| Apple Pay | Web and mobile checkout | Requires merchant validation and wallet-specific setup |
| PayPal | Alternative wallet | Useful where wallet conversion is strong |
| Bancontact | Belgian shoppers | Include local language checkout guidance |
| iDEAL | Dutch shoppers | Redirect-based experience |
| SEPA Direct Debit | Bank-account payments | Make mandate and timing clear |
| MB Way | Portuguese shoppers | Mobile confirmation flow |

{% hint style="info" %}
In the production migration, each method can keep a dedicated page. This demo surfaces the structured table pattern HiPay can apply to the long tail.
{% endhint %}
""",
    )
    write(
        "online-payments/webhooks-and-notifications.md",
        """
---
description: "Use HiPay notifications to keep merchant systems synchronized."
icon: bell
---

# Webhooks and notifications

Server-to-server notifications are the reliable source for payment status changes. Redirect pages improve shopper experience, but notifications update the merchant system.

```mermaid
sequenceDiagram
    participant HiPay
    participant Merchant
    participant OMS
    HiPay->>Merchant: POST notification
    Merchant->>Merchant: Verify signature
    Merchant->>OMS: Update order status
    Merchant-->>HiPay: 200 OK
```

{% stepper %}
{% step %}
## Expose a notification endpoint

Create an HTTPS endpoint that accepts HiPay notification payloads and logs the raw request for audit and replay.
{% endstep %}

{% step %}
## Verify the signature

Reject notifications where the signature does not match the shared secret or expected account.
{% endstep %}

{% step %}
## Make processing idempotent

Store the transaction reference and status transition so repeated notifications do not duplicate operations.
{% endstep %}

{% step %}
## Return a 2xx response

Return success only after the merchant system has persisted the status update.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Do not mark an order as paid from the shopper redirect alone. Always wait for the HiPay server notification or verify transaction status through the API.
{% endhint %}
""",
    )
    write(
        "online-payments/transaction-operations.md",
        """
---
description: "Create, inspect, capture, and refund HiPay transactions."
icon: arrows-rotate
---

# Transaction operations

Common support questions often map to a small set of transaction operations: create the payment, inspect status, capture, refund, or challenge.

{% tabs %}
{% tab title="Create order" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/order" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \\
  -d "orderid=ORDER-1001" \\
  -d "amount=49.90" \\
  -d "currency=EUR" \\
  -d "cardtoken=$CARD_TOKEN"
```
{% endtab %}

{% tab title="Refund" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/maintenance/transaction/$TRANSACTION_REFERENCE" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \\
  -d "operation=refund" \\
  -d "amount=10.00"
```
{% endtab %}

{% tab title="Get status" %}
```bash
curl "https://stage-secure-gateway.hipay-tpp.com/rest/v1/transaction/$TRANSACTION_REFERENCE" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD"
```
{% endtab %}
{% endtabs %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/order" method="post" %}
[Order API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/maintenance/transaction/{transaction_reference}" method="post" %}
[Maintenance API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}
""",
    )

    write(
        "commerce-platforms/SUMMARY.md",
        """
# Table of contents

* [Commerce Platforms](README.md)
* [CMS module launch](cms-module-launch.md)
* [Marketplace onboarding](marketplace-onboarding.md)
* [Point of Sale](point-of-sale-guide.md)
* [Mobile payments](mobile-payments-guide.md)
""",
    )
    write(
        "commerce-platforms/README.md",
        """
---
description: "Launch HiPay across CMS, marketplace, mobile, and point-of-sale channels."
icon: store
layout:
  width: wide
---

# Commerce Platforms

Commerce teams often need less API theory and more launch guidance. This space organizes HiPay by the channel the merchant is trying to ship.

""" + card_table([
            ("puzzle-piece", "CMS module launch", "Prerequisites, back-office configuration, test payments, and go-live checks.", "cms-module-launch.md"),
            ("people-arrows", "Marketplace onboarding", "Vendor creation, KYC, bank information, and cash-out flows.", "marketplace-onboarding.md"),
            ("cash-register", "Point of Sale", "Online-to-instore, smart terminal, cloud API, local API, and terminal journeys.", "point-of-sale-guide.md"),
            ("mobile-screen", "Mobile payments", "iOS and Android integration paths with SDK configuration guidance.", "mobile-payments-guide.md"),
        ]) + """
""",
    )
    write(
        "commerce-platforms/cms-module-launch.md",
        """
---
description: "A GitBook-native launch guide for HiPay CMS modules."
icon: puzzle-piece
---

# CMS module launch

Use CMS module docs when a merchant wants low technical overhead and clear back-office configuration guidance.

{% stepper %}
{% step %}
## Confirm platform and module version

Identify the merchant platform: Shopify, Magento, PrestaShop, Shopware, Salesforce Commerce Cloud, Sylius, WooCommerce, or WiziShop.
{% endstep %}

{% step %}
## Check prerequisites

Confirm account credentials, allowed countries, payment methods, notification URL, and test environment access.
{% endstep %}

{% step %}
## Configure the back office

Set API credentials, environment, capture mode, payment methods, redirect URLs, and notification settings.
{% endstep %}

{% step %}
## Run a test payment

Create a low-value payment, check the order timeline, refund it, and verify the status changed in the CMS.
{% endstep %}

{% step %}
## Go live

Switch to production credentials, run one controlled production transaction, and monitor notifications.
{% endstep %}
{% endstepper %}

## Module comparison

| Platform | Typical buyer | Best documentation pattern |
| --- | --- | --- |
| Shopify | Merchant ops team | Configuration checklist and testing steps |
| Magento | Technical commerce team | Version matrix, module install, and troubleshooting |
| Salesforce Commerce Cloud | Enterprise commerce team | Cartridge integration and staged rollout |
| PrestaShop | Mid-market merchant | Module setup plus common support answers |
""",
    )
    write(
        "commerce-platforms/marketplace-onboarding.md",
        """
---
description: "Vendor onboarding, KYC, bank info, and cash-out flows for marketplaces."
icon: people-arrows
---

# Marketplace onboarding

Marketplace docs should make vendor onboarding operationally clear: who collects data, who verifies it, and what status each vendor is in.

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> KYCRequired
    KYCRequired --> UnderReview
    UnderReview --> Active
    UnderReview --> Rejected
    Active --> BankInfoUpdated
    BankInfoUpdated --> CashOutReady
```

{% stepper %}
{% step %}
## Create the vendor

Register the vendor account with the marketplace API and store the HiPay vendor identifier in the marketplace back office.
{% endstep %}

{% step %}
## Collect KYC documents

Upload required identification and legal documents. Keep the vendor-facing checklist specific to country and business type.
{% endstep %}

{% step %}
## Add bank information

Collect and validate bank details before enabling cash-out.
{% endstep %}

{% step %}
## Monitor status changes

Use notifications and status checks to show vendors what is missing and when payouts can start.
{% endstep %}
{% endstepper %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/user-account.{_format}" method="post" %}
[Marketplace vendor API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}
""",
    )
    write(
        "commerce-platforms/point-of-sale-guide.md",
        """
---
description: "Online-to-instore and smart terminal implementation guide."
icon: cash-register
---

# Point of Sale

Point-of-sale integrations should be documented around the store journey, not only terminal APIs.

{% tabs %}
{% tab title="Online to instore" %}
Use this path when an online order needs in-store collection or in-store payment completion.
{% endtab %}

{% tab title="Smart terminal" %}
Use this path when the merchant runs payment flows directly on a smart terminal or tablet connector.
{% endtab %}

{% tab title="Unattended terminal" %}
Use this path for kiosk and unattended payment scenarios where user prompts and timeout behavior must be explicit.
{% endtab %}
{% endtabs %}

## Store payment sequence

```mermaid
sequenceDiagram
    participant Store
    participant ECR
    participant Terminal
    participant HiPay
    Store->>ECR: Starts checkout
    ECR->>Terminal: Sends amount
    Terminal->>HiPay: Requests authorization
    HiPay-->>Terminal: Result
    Terminal-->>ECR: Payment status
    ECR-->>Store: Receipt and order update
```
""",
    )
    write(
        "commerce-platforms/mobile-payments-guide.md",
        """
---
description: "Mobile payment integration paths for iOS and Android."
icon: mobile-screen
---

# Mobile payments

Mobile docs should separate SDK setup, fast integration, advanced integration, and wallet-specific requirements.

{% columns %}
{% column width="50%" %}
## iOS

* SDK configuration
* Fast integration
* Advanced integration
* Apple Pay app guidance
{% endcolumn %}

{% column width="50%" %}
## Android

* SDK configuration
* Fast integration
* Advanced integration
* Wallet and redirect behavior
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
For a production migration, keep the detailed iOS and Android pages as long-tail content. Use this page as the channel landing page.
{% endhint %}
""",
    )

    write(
        "payment-fundamentals/SUMMARY.md",
        """
# Table of contents

* [Payment Fundamentals](README.md)
* [Transaction lifecycle](transaction-lifecycle.md)
* [Signature verification](signature-verification.md)
* [Security and SCA](security-and-sca.md)
* [Error handling](error-handling.md)
""",
    )
    write(
        "payment-fundamentals/README.md",
        """
---
description: "Payment concepts and requirements every HiPay integration needs."
icon: shield-halved
layout:
  width: wide
---

# Payment Fundamentals

This space answers the questions that cut across all integration paths: transaction states, redirects, notifications, SCA, signatures, and errors.

""" + card_table([
            ("diagram-project", "Transaction lifecycle", "Authorization, capture, challenge, refund, failure, and dispute states.", "transaction-lifecycle.md"),
            ("signature", "Signature verification", "How merchants should verify HiPay notifications before updating orders.", "signature-verification.md"),
            ("shield-check", "Security and SCA", "PSD2, 3-D Secure, device fingerprinting, and operational security guidance.", "security-and-sca.md"),
            ("triangle-exclamation", "Error handling", "Readable error tables and retry behavior for support teams.", "error-handling.md"),
        ]) + """
""",
    )
    write(
        "payment-fundamentals/transaction-lifecycle.md",
        """
---
description: "Understand the lifecycle of a HiPay transaction."
icon: diagram-project
---

# Transaction lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Authorized
    Created --> Declined
    Authorized --> Captured
    Authorized --> Voided
    Authorized --> ChallengeRequested
    ChallengeRequested --> Authorized
    ChallengeRequested --> Declined
    Captured --> Refunded
    Captured --> Disputed
```

| State | Meaning | Merchant action |
| --- | --- | --- |
| Created | Payment attempt exists | Wait for authorization or notification |
| Authorized | Funds approved | Capture, ship, or void according to business rules |
| Challenge requested | Authentication step required | Let shopper complete the challenge |
| Captured | Funds captured | Fulfill order and reconcile settlement |
| Refunded | Funds returned | Update order and customer communication |
| Declined | Payment failed | Show retry or alternative payment method |
""",
    )
    write(
        "payment-fundamentals/signature-verification.md",
        """
---
description: "Verify HiPay server notifications before updating merchant systems."
icon: signature
---

# Signature verification

Signature verification protects merchants from accepting forged notifications.

{% stepper %}
{% step %}
## Capture the raw payload

Read the exact request body and headers sent by HiPay. Do not normalize or reorder fields before verification.
{% endstep %}

{% step %}
## Recompute the signature

Use the shared secret configured for the account to compute the expected signature.
{% endstep %}

{% step %}
## Compare safely

Use a constant-time comparison function when available.
{% endstep %}

{% step %}
## Process idempotently

Only update the order if the signature is valid and the status transition has not already been applied.
{% endstep %}
{% endstepper %}

{% tabs %}
{% tab title="Node.js" %}
```js
import crypto from "node:crypto";

function verifyHipaySignature(rawBody, receivedSignature, secret) {
  const expected = crypto
    .createHmac("sha256", secret)
    .update(rawBody)
    .digest("hex");

  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(receivedSignature)
  );
}
```
{% endtab %}

{% tab title="PHP" %}
```php
function verifyHipaySignature(string $rawBody, string $received, string $secret): bool {
    $expected = hash_hmac('sha256', $rawBody, $secret);
    return hash_equals($expected, $received);
}
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
The exact signing algorithm and header names should be confirmed against the merchant account configuration during implementation.
{% endhint %}
""",
    )
    write(
        "payment-fundamentals/security-and-sca.md",
        """
---
description: "Security, PSD2, SCA, 3-D Secure, and device fingerprinting guidance."
icon: shield-check
---

# Security and SCA

Security pages should be operational and specific: what the merchant must configure, what HiPay handles, and what the shopper sees.

| Topic | Why it matters | Documentation pattern |
| --- | --- | --- |
| PSD2 and SCA | Strong Customer Authentication may be required for card payments | Explain exemptions, challenges, and fallback behavior |
| 3-D Secure | Authentication affects authorization and conversion | Use diagrams and testing scenarios |
| Device fingerprint | Fraud and risk signals improve decisioning | Provide copy-paste setup steps |
| Redirect pages | Shopper experience and status handling | Pair with notification guidance |

{% hint style="success" %}
This is a strong GitBook use case: requirements can be surfaced by audience, while the API and implementation pages stay connected.
{% endhint %}
""",
    )
    write(
        "payment-fundamentals/error-handling.md",
        """
---
description: "Readable error and retry guidance for HiPay integrations."
icon: triangle-exclamation
---

# Error handling

Clear error guidance reduces support tickets because merchants can tell retryable failures from configuration mistakes.

| Error family | Example cause | Merchant action |
| --- | --- | --- |
| Validation | Missing amount, currency, or order id | Fix request construction before retrying |
| Authentication | Invalid credentials or environment mismatch | Check API login, password, and stage/live mode |
| Payment declined | Issuer or shopper authentication failure | Ask shopper to retry or choose another method |
| Risk or fraud | Risk controls blocked the transaction | Review fraud settings and customer details |
| Notification failure | Merchant endpoint unavailable | Replay after endpoint is healthy |

<details>
<summary>Support macro example</summary>

Ask the merchant for the transaction reference, environment, timestamp, request id if available, and whether the failure happened during authorization, notification, capture, or refund.
</details>
""",
    )

    write(
        "api-reference/SUMMARY.md",
        """
# Table of contents

* [API Reference](README.md)
* [Gateway API](gateway-api.md)
* [Hosted Page API](hosted-page-api.md)
* [Marketplace API](marketplace-api.md)
* [Agentic interfaces](agentic-interfaces.md)
""",
    )
    write(
        "api-reference/README.md",
        """
---
description: "OpenAPI-led API reference pages for HiPay developers."
icon: code
layout:
  width: wide
---

# API Reference

The API reference should be generated from OpenAPI wherever possible. This demo foregrounds the most important specs and shows how GitBook can render API operations alongside implementation context.

""" + card_table([
            ("terminal", "Gateway API", "Create orders, retrieve transaction status, and run maintenance operations.", "gateway-api.md"),
            ("window-maximize", "Hosted Page API", "Create a HiPay-hosted checkout session.", "hosted-page-api.md"),
            ("people-arrows", "Marketplace API", "Create vendors, collect KYC, add bank information, and cash out.", "marketplace-api.md"),
            ("robot", "Agentic interfaces", "How a HiPay MCP server and AI-readable docs could reduce support load.", "agentic-interfaces.md"),
        ]) + """

{% hint style="info" %}
The source OpenAPI specs are hosted in the public `hipay/openapi-hipay` repository. In a production GitBook migration, these specs should drive generated reference pages instead of hand-maintained endpoint text.
{% endhint %}
""",
    )
    write(
        "api-reference/gateway-api.md",
        """
---
description: "Create orders and manage HiPay transactions with the Gateway API."
icon: terminal
---

# Gateway API

Use the Gateway API for direct order creation, transaction lookup, and maintenance operations.

{% tabs %}
{% tab title="Create order" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/order" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \\
  -d "orderid=ORDER-1001" \\
  -d "amount=49.90" \\
  -d "currency=EUR" \\
  -d "description=Demo order"
```
{% endtab %}

{% tab title="Retrieve transaction" %}
```bash
curl "https://stage-secure-gateway.hipay-tpp.com/rest/v1/transaction/$TRANSACTION_REFERENCE" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD"
```
{% endtab %}

{% tab title="Refund" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/maintenance/transaction/$TRANSACTION_REFERENCE" \\
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \\
  -d "operation=refund" \\
  -d "amount=10.00"
```
{% endtab %}
{% endtabs %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/order" method="post" %}
[Order API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/transaction/{transaction_reference}" method="get" %}
[Transaction lookup](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}
""",
    )
    write(
        "api-reference/hosted-page-api.md",
        """
---
description: "Create HiPay hosted checkout sessions."
icon: window-maximize
---

# Hosted Page API

Hosted Page is the fastest way to launch a HiPay checkout while keeping maintenance overhead low.

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml" path="/v1/hpayment" method="post" %}
[Hosted Page API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml)
{% endopenapi %}

{% hint style="success" %}
Pair this reference with the Hosted Page quickstart so developers get both the exact endpoint and the implementation journey.
{% endhint %}
""",
    )
    write(
        "api-reference/marketplace-api.md",
        """
---
description: "Marketplace vendor, KYC, bank info, and cash-out API surfaces."
icon: people-arrows
---

# Marketplace API

Marketplace implementations need reference documentation plus operational guidance for vendor onboarding.

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/user-account.{_format}" method="post" %}
[Create vendor account](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/transfer.{_format}" method="post" %}
[Create transfer](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}
""",
    )
    write(
        "api-reference/agentic-interfaces.md",
        """
---
description: "How GitBook and MCP can make HiPay docs more useful for AI agents."
icon: robot
---

# Agentic interfaces

HiPay can use GitBook to make developer content easier for humans and AI agents to consume.

{% columns %}
{% column width="50%" %}
## AI-readable docs

GitBook page actions expose markdown and MCP-friendly access patterns, so implementation content can be used directly by coding assistants.
{% endcolumn %}

{% column width="50%" %}
## HiPay MCP server

An MCP server can let approved agents retrieve payment docs, check transaction status, or open support workflows without scraping the portal.
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
This is especially relevant because HiPay has broad developer content and multiple technical audiences. AI search and MCP reduce the friction of finding the right page.
{% endhint %}
""",
    )


def import_space(space: dict, created: dict) -> dict:
    space_id = created["spaces"][space["key"]]
    space_dir = ROOT / space["folder"]
    _, cr = api("POST", f"/spaces/{space_id}/change-requests", {"subject": "Repair HiPay demo content quality"})
    cr_id = cr["id"]

    current_pages = content_tree(space_id, cr_id)
    for batch in chunked(current_pages, 20):
        api(
            "POST",
            f"/spaces/{space_id}/change-requests/{cr_id}/content",
            {"changes": [{"operation": "delete_page", "page": page["id"]} for page in batch]},
        )

    entries = parse_summary(space_dir)
    changes = [
        {
            "operation": "insert_page",
            "title": markdown_title((space_dir / "README.md").read_text(encoding="utf-8"), space["title"]),
            "document": {"markdown": (space_dir / "README.md").read_text(encoding="utf-8")},
        }
    ]
    for title, rel in entries:
        markdown = (space_dir / rel).read_text(encoding="utf-8")
        changes.append(
            {
                "operation": "insert_page",
                "title": markdown_title(markdown, title),
                "document": {"markdown": markdown},
            }
        )

    for batch in chunked(changes, 15):
        api("POST", f"/spaces/{space_id}/change-requests/{cr_id}/content", {"changes": batch})

    api("POST", f"/spaces/{space_id}/change-requests/{cr_id}/merge")
    time.sleep(2)
    live_pages = flatten_pages(content_tree(space_id))
    return {
        "space": space_id,
        "change_request": cr_id,
        "inserted_pages": len(changes),
        "live_pages": len(live_pages),
        "top_level_pages": [page.get("title") for page in content_tree(space_id)],
    }


def main() -> None:
    scaffold_files()
    created = json.loads((ROOT / "gitbook-created.json").read_text(encoding="utf-8"))
    results = {}
    for space in SPACES:
        results[space["key"]] = import_space(space, created)
        print(space["key"], results[space["key"]])
    (ROOT / "gitbook-repair-result.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    try:
        api("POST", f"/orgs/{created['org']}/sites/{created['site']}/publish")
    except RuntimeError as exc:
        if "Site is already published" not in str(exc):
            raise


if __name__ == "__main__":
    main()
