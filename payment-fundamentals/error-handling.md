---
description: "Readable error and retry guidance for HiPay integrations."
icon: triangle-exclamation
---

# Error handling

Clear error guidance reduces support tickets because merchants can tell retryable failures from configuration mistakes.

| Error family | Example cause | Merchant action |
| --- | --- | --- |
| Validation | Missing amount, currency, or order id | Fix request construction before retrying |
| Authentication | Invalid credentials or environment mismatch | Check API login, password, and stage/live mode |
| Payment declined | Issuer or shopper authentication failure | Ask shopper to retry or choose another method |
| Risk or fraud | Risk controls blocked the transaction | Review fraud settings and customer details |
| Notification failure | Merchant endpoint unavailable | Replay after endpoint is healthy |

<details>
<summary>Support macro example</summary>

Ask the merchant for the transaction reference, environment, timestamp, request id if available, and whether the failure happened during authorization, notification, capture, or refund.
</details>
