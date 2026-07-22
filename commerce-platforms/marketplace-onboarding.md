---
description: "Vendor onboarding, KYC, bank info, and cash-out flows for marketplaces."
icon: people-arrows
---

# Marketplace onboarding

Marketplace docs should make vendor onboarding operationally clear: who collects data, who verifies it, and what status each vendor is in.

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> KYCRequired
    KYCRequired --> UnderReview
    UnderReview --> Active
    UnderReview --> Rejected
    Active --> BankInfoUpdated
    BankInfoUpdated --> CashOutReady
```

{% stepper %}
{% step %}
## Create the vendor

Register the vendor account with the marketplace API and store the HiPay vendor identifier in the marketplace back office.
{% endstep %}

{% step %}
## Collect KYC documents

Upload required identification and legal documents. Keep the vendor-facing checklist specific to country and business type.
{% endstep %}

{% step %}
## Add bank information

Collect and validate bank details before enabling cash-out.
{% endstep %}

{% step %}
## Monitor status changes

Use notifications and status checks to show vendors what is missing and when payouts can start.
{% endstep %}
{% endstepper %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/user-account.{_format}" method="post" %}
[Marketplace vendor API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}
