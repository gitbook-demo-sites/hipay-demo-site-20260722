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
