---
description: "Fund allocation The transfer API is then used to allocate funds from the technical account to the merchants' accounts. The transfer API allows a trans"
icon: file-lines
---

# Marketplace - Cash Out

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/cash-out](https://developer.hipay.com/marketplace/api-integration/cash-out)
{% endhint %}

## Fund allocation

The transfer API is then used to allocate funds from the technical account to the merchants' accounts.

The transfer API allows a transfer request to be made on the agent's behalf or on the behalf of a third party. The technical account is therefore a monitoring tool that provides a clear view of fund allocation (fund remittance, refunds, chargebacks).

HiPay suggests performing fund allocation and withdrawal all at once. All the funds are held in escrow before being deposited on the technical account.

## Withdrawal requests

Once funds are allocated, you can ask for a withdrawal request using the withdraw API . There are two withdrawal possibilities:

* Whenever a withdrawal request is made - for example, every ten days, depending on the agent.
* Whenever a transaction is made - please note that this option is not recommended by HiPay;

## Check-related APIs

There are also check-related APIs for enhanced safety.

To secure the system and track fund movements, the agent may use the following APIs that are optional, but strongly suggested, for:

* Status checking, using the bankInfosStatus API
* Account balances, using the getBalance API Transaction history, using the getTransactions API .
