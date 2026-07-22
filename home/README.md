---
description: "A modern SaaS developer portal demo for HiPay."
icon: house
cover: "https://ik.imagekit.io/hipay/homepage_hero_a6ce98e81f_0Grsw-VSV.png?tr=w-1600,h-700"
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

Augmented payment documentation for online, in-store, marketplace, and agentic commerce teams.

{% columns %}
{% column width="56%" %}
This first draft moves HiPay's self-hosted WordPress developer portal into a GitBook-style SaaS documentation hub. It keeps the current content architecture, adds clearer audience paths, and shows how OpenAPI, AI search, page feedback, and editorial review can reduce support tickets from stale or hard-to-find docs.

{% hint style="success" %}
Demo focus: replace maintenance-heavy WordPress docs with a branded, searchable, API-aware GitBook experience that merchants and implementation teams can self-serve.
{% endhint %}
{% endcolumn %}

{% column width="44%" %}
```mermaid
flowchart TD
    Merchant[Merchant team] --> Path{{Choose a path}}
    Path --> Online[Online payments]
    Path --> Store[Unified commerce]
    Path --> Market[Marketplace]
    Online --> API[OpenAPI reference]
    Store --> API
    Market --> API
    API --> SelfServe[Self-service answers]
```
{% endcolumn %}
{% endcolumns %}

## Choose your path

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-credit-card"></i></td><td><strong>Integrate online payments</strong></td><td>Hosted Page, Hosted Fields, API-only, SDKs, payment methods, and maintenance.</td><td><a href="https://app.gitbook.com/s/XSPACE_ONLINE/">Integrate online payments</a></td></tr>
<tr><td><i class="fa-store"></i></td><td><strong>Launch commerce channels</strong></td><td>CMS modules, marketplace onboarding, mobile payments, POS, and online-to-instore flows.</td><td><a href="https://app.gitbook.com/s/XSPACE_COMMERCE/">Launch commerce channels</a></td></tr>
<tr><td><i class="fa-shield-halved"></i></td><td><strong>Understand requirements</strong></td><td>Security, notifications, signature verification, transaction lifecycle, statuses, and errors.</td><td><a href="https://app.gitbook.com/s/XSPACE_FUNDAMENTALS/">Understand requirements</a></td></tr>
<tr><td><i class="fa-code"></i></td><td><strong>Use the API reference</strong></td><td>Generated OpenAPI pages for gateway, hosted page, marketplace, settlements, and terminal APIs.</td><td><a href="https://app.gitbook.com/s/XSPACE_API/">Use the API reference</a></td></tr>
</tbody></table>

## Audience segmentation demo

{% tabs %}
{% tab title="Developers" %}
Start with integration paths, SDK examples, OpenAPI operations, test cards, webhooks, and payment lifecycle details.
{% endtab %}

{% tab title="Merchants" %}
Use payment method, marketplace, POS, and support-ready pages to answer launch and operations questions without opening a ticket.
{% endtab %}

{% tab title="Editors" %}
Use GitBook change requests, Git Sync, page feedback, AI insights, and reusable content to keep high-change payment docs current.
{% endtab %}
{% endtabs %}
