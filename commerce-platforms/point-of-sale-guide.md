---
description: "Online-to-instore and smart terminal implementation guide."
icon: cash-register
---

# Point of Sale

Point-of-sale integrations should be documented around the store journey, not only terminal APIs.

{% tabs %}
{% tab title="Online to instore" %}
Use this path when an online order needs in-store collection or in-store payment completion.
{% endtab %}

{% tab title="Smart terminal" %}
Use this path when the merchant runs payment flows directly on a smart terminal or tablet connector.
{% endtab %}

{% tab title="Unattended terminal" %}
Use this path for kiosk and unattended payment scenarios where user prompts and timeout behavior must be explicit.
{% endtab %}
{% endtabs %}

## Store payment sequence

```mermaid
sequenceDiagram
    participant Store
    participant ECR
    participant Terminal
    participant HiPay
    Store->>ECR: Starts checkout
    ECR->>Terminal: Sends amount
    Terminal->>HiPay: Requests authorization
    HiPay-->>Terminal: Result
    Terminal-->>ECR: Payment status
    ECR-->>Store: Receipt and order update
```
