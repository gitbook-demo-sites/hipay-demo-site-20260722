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
