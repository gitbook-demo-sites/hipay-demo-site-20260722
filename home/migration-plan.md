---
description: "How the WordPress developer portal maps into a GitBook-first operating model."
icon: arrows-rotate
---

# Migration Plan

{% stepper %}
{% step %}
## Import and preserve the current IA

The demo imports the current sitemap into spaces that mirror reader jobs: online payments, commerce platforms, fundamentals, and API reference.
{% endstep %}

{% step %}
## Promote API Explorer pages to OpenAPI

Where the current portal embeds Swagger from GitHub, the demo registers the public OpenAPI specs and renders them with GitBook's OpenAPI block.
{% endstep %}

{% step %}
## Add audience paths

GitBook can later gate additive implementation notes by visitor claims such as `persona=developer`, `persona=merchant`, or `persona=partner`.
{% endstep %}

{% step %}
## Replace ticket triggers with feedback loops

Page feedback, AI search insights, and review workflows give the docs team a way to identify stale or missing answers before support tickets pile up.
{% endstep %}
{% endstepper %}
