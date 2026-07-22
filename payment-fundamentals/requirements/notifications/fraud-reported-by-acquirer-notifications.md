---
description: "To improve responsiveness to fraudulent transactions, HiPay now automates the transmission of fraud information reported directly by the acquirer. Thi"
icon: file-lines
---

# Fraud Reported By Acquirer

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/requirements/notifications/fraud-reported-by-acquirer-notifications](https://developer.hipay.com/payment-fundamentals/requirements/notifications/fraud-reported-by-acquirer-notifications)
{% endhint %}

To improve responsiveness to fraudulent transactions, HiPay now automates the transmission of fraud information reported directly by the acquirer. This notification allows you to react instantly without any manual file processing.

## 1. Configuration

No specific configuration is required if your system is already configured to receive Webhook notifications ( svnotif.url field). The operation.fraud_reported_by_acquirer event will be sent automatically to this URL.

* Expected response: Your server must respond with an HTTP 200 OK status code.
* Reconciliation: In case of doubt, you can check the transaction status via the GET /v3/transactions/{trx_id} endpoint.

## 2. Notification Format

You will receive a JSON payload in the body of the POST request. The structure includes the full transaction object, enriched with fraud indicators.

Structure:

JSON

{

event_key: operation.fraud_reported_by_acquirer,

data: { ... Full Transaction Object ... },

sent_date: timestamp

}

* event_key (string): operation.fraud_reported_by_acquirer
* data (json): The full transaction object. Fields added for fraud tracking:

* Transaction level: fraud_reported_by_acquirer : boolean ( true if at least one operation is marked as fraudulent)
* Operation level: date_fraud_by_acquirer : YYYY-MM-DD... (the date the fraud was reported).

## 3. Notification Example

Example payload sent when an operation is marked as fraudulent:

JSON

{

id: 155227950169,

order: { },

operations: [

{

type: CAPTURE,

status: COMPLETED,

amount: 49.70,

date_created: 2026-07-05T05:09:26+02:00,

date_updated: 2026-07-08T08:02:45+02:00,

date_fraud_by_acquirer: 2026-07-08T00:00:00+02:00,

id: 820091834,

currency: GBP,

decimals: 2

}

],

fraud_reported_by_acquirer: true

}

### Summary of New Features for Merchants

Feature

Description

Real-Time Notification

operation.fraud_reported_by_acquirer event received as soon as the acquirer updates the status.

Lookup API

The fraud_reported_by_acquirer field is now available in your GET /v3/transactions responses.

Operation Visibility

The date_fraud_by_acquirer field allows you to precisely identify the affected operation.
