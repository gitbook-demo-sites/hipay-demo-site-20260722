---
description: "Account Creation In order to create a vendor account The agent checks the email availability with the user-account/is-available API . The agent create"
icon: file-lines
---

# Marketplace - Vendors

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/vendors](https://developer.hipay.com/marketplace/api-integration/vendors)
{% endhint %}

## Account Creation

In order to create a vendor account

* The agent checks the email availability with the user-account/is-available API .
* The agent creates a HiPay account for merchants using the user-account API .
* The agent sends the identification documents (KYC/KYB) using the identification API .
* HiPay validates the identification documents (KYC/KYB) within three days and sends the agent a notification confirming that the merchant is fully operational.

## Account update

Please note that submitted information cannot be modified through APIs, only by e-mail at [email protected] .
