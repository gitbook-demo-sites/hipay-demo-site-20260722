---
description: "OpenAPI-led API reference pages for HiPay developers."
icon: code
layout:
  width: wide
---

# API Reference

The API reference should be generated from OpenAPI wherever possible. This demo foregrounds the most important specs and shows how GitBook can render API operations alongside implementation context.

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h4><i class="fa-terminal" style="color:$primary;"></i></h4></td><td><strong>Gateway API</strong></td><td>Create orders, retrieve transaction status, and run maintenance operations.</td><td><a href="gateway-api.md">Gateway API</a></td></tr>
<tr><td><h4><i class="fa-window-maximize" style="color:$primary;"></i></h4></td><td><strong>Hosted Page API</strong></td><td>Create a HiPay-hosted checkout session.</td><td><a href="hosted-page-api.md">Hosted Page API</a></td></tr>
<tr><td><h4><i class="fa-people-arrows" style="color:$primary;"></i></h4></td><td><strong>Marketplace API</strong></td><td>Create vendors, collect KYC, add bank information, and cash out.</td><td><a href="marketplace-api.md">Marketplace API</a></td></tr>
<tr><td><h4><i class="fa-robot" style="color:$primary;"></i></h4></td><td><strong>Agentic interfaces</strong></td><td>How a HiPay MCP server and AI-readable docs could reduce support load.</td><td><a href="agentic-interfaces.md">Agentic interfaces</a></td></tr>
</tbody></table>

{% hint style="info" %}
The source OpenAPI specs are hosted in the public `hipay/openapi-hipay` repository. In a production GitBook migration, these specs should drive generated reference pages instead of hand-maintained endpoint text.
{% endhint %}
