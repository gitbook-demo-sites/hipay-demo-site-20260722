---
description: "In order to inform you of events related to KYC/KYB document validation, the HiPay platform can send your application a server-to-server notification."
icon: file-lines
---

# KYC - Notifications

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/kyc-notifications](https://developer.hipay.com/marketplace/api-integration/kyc-notifications)
{% endhint %}

In order to inform you of events related to KYC/KYB document validation, the HiPay platform can send your application a server-to-server notification.

To set your notification URL, please submit a request to our Support team (specifying HiPay Marketplace).

## Response fields

Field name Description md5content SHA1 encoding of the field operation Name of the notification (document_validation) status - ok: the document is validated

- nok: the document is not validated

message Description of the status date Date of the notification (YYYY-MM-DD) time Time of the notification (HH:MM:SS Time zone) document_type Type of KYC/KYB document

(please see here for a detailed description)

document_type_label Description of the document (please see here for a detailed description) account_id HiPay account ID for which the KYC/KYB was uploaded

## Callback messages

Please find hereafter the various reasons for refusal provided by notification.

Invalid date Unreadable Missing data Inconsistency: {personalized-msg} Not verified: missing document Invalid document type Falsified Front missing Supplier outside the scope Bank outside the scope Inconsistent Other Invalid Address Expired

## Response example

Example of a KYC/KYB document notification in XML format

XML

XML

```

d9e43bb0a9b92aba4fb22eed4164a1f0

document_validation
nok
Not a proof of address
2018-06-29
16:39:42 Europe/Paris+0200
2
Proof of address
543210

```
