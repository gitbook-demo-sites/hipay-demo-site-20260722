---
description: "Based on the screening results of HiPay's Fraud Protection Service, when a transaction is suspected of being fraudulent, it is in challenged status. W"
icon: file-lines
---

# Challenge

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/maintenance/challenge](https://developer.hipay.com/online-payments/maintenance/challenge)
{% endhint %}

Based on the screening results of HiPay's Fraud Protection Service, when a transaction is suspected of being fraudulent, it is in challenged status.

When a transaction is in the challenge status; you may perform decide whether you accept the transaction or not. There are two ways to accept or deny a payment: either from your HiPay Enterprise back office, or using HiPay Maintenance API .

## HiPay Backoffice

In order to manage a challenged transaction you should go to the Transaction Preview .

Here, you will find a fraud review alert. You can either mark the transaction as accepted (and capture it) or mark it as denied.

## API Request

In order to manage a challenged transaction through an API you will need to use the maintenance API .

Accepting a challenge : In order to accept a transaction that has been challenged you will need to send the operation parameter with the value acceptChallenge.

Denying a challenge : In order to deny a a transaction that has been challenged you will need to send the operation parameter with the value denyChallenge.
