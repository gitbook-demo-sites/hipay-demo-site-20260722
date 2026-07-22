---
description: "The vendor bank information is key. Indeed, even if an account is identified, no withdrawal will be possible until the bank information has been valid"
icon: file-lines
---

# Marketplace - Bank Information

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/bank-information](https://developer.hipay.com/marketplace/api-integration/bank-information)
{% endhint %}

The vendor bank information is key. Indeed, even if an account is identified, no withdrawal will be possible until the bank information has been validated.

You can submit the bank account information any time between account creation and withdrawal requests.

The bank information is composed of:

* A RIB document
* Manual bank details (e. g. bank name, account number, BIC, IBAN, etc.).

## Information submission

In order to provide the bank information for a vendor; you must use the bank-Info API . It can be called:

* Only with the bank identity document
* With the bank identity document and bank info together
* Only with the bank information, only if the bank info document has been uploaded previously In other words, the bank information document is required if it has not been already been provided.

## Related APIs

Other bank information related APIs are also available to the agent:

* BankInfosCheck provides banking information registered on a HiPay account
* BankInfosFields provides the necessary information for a HiPay bank account based on the country of origin;
* BankInfosStatus provides the status of banking information (validated, rejected, pending).
