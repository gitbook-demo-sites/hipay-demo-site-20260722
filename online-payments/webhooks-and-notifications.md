---
description: "Use HiPay notifications to keep merchant systems synchronized."
icon: bell
---

# Webhooks and notifications

Server-to-server notifications are the reliable source for payment status changes. Redirect pages improve shopper experience, but notifications update the merchant system.

```mermaid
sequenceDiagram
    participant HiPay
    participant Merchant
    participant OMS
    HiPay->>Merchant: POST notification
    Merchant->>Merchant: Verify signature
    Merchant->>OMS: Update order status
    Merchant-->>HiPay: 200 OK
```

{% stepper %}
{% step %}
## Expose a notification endpoint

Create an HTTPS endpoint that accepts HiPay notification payloads and logs the raw request for audit and replay.
{% endstep %}

{% step %}
## Verify the signature

Reject notifications where the signature does not match the shared secret or expected account.
{% endstep %}

{% step %}
## Make processing idempotent

Store the transaction reference and status transition so repeated notifications do not duplicate operations.
{% endstep %}

{% step %}
## Return a 2xx response

Return success only after the merchant system has persisted the status update.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Do not mark an order as paid from the shopper redirect alone. Always wait for the HiPay server notification or verify transaction status through the API.
{% endhint %}
