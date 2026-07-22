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

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h4><i class="fa-magnifying-glass" style="color:$primary;"></i></h4></td><td><strong>Prominent AI search</strong></td><td>Use the homepage buttons to ask common implementation questions.</td><td><a href="README.md">Prominent AI search</a></td></tr>
<tr><td><h4><i class="fa-list-check" style="color:$primary;"></i></h4></td><td><strong>Stepper conversion</strong></td><td>Hosted Fields and CMS flows are written as ordered GitBook steppers.</td><td><a href="https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/hosted-fields-quickstart">Stepper conversion</a></td></tr>
<tr><td><h4><i class="fa-table" style="color:$primary;"></i></h4></td><td><strong>Real tables</strong></td><td>Payment means and error handling use structured tables rather than prose placeholders.</td><td><a href="https://app.gitbook.com/s/NgbUMQ3SLCpm1fOa0LBR/payment-methods">Real tables</a></td></tr>
<tr><td><h4><i class="fa-code" style="color:$primary;"></i></h4></td><td><strong>Code that renders</strong></td><td>API and SDK examples are in fenced code blocks and tabs.</td><td><a href="https://app.gitbook.com/s/iLPCxDjmgR6F8AXe5kC9/gateway-api">Code that renders</a></td></tr>
</tbody></table>
