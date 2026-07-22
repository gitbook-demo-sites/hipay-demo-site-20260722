---
description: "Marketplace vendor, KYC, bank info, and cash-out API surfaces."
icon: people-arrows
---

# Marketplace API

Marketplace implementations need reference documentation plus operational guidance for vendor onboarding.

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/user-account.{_format}" method="post" %}
[Create vendor account](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml" path="/transfer.{_format}" method="post" %}
[Create transfer](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
{% endopenapi %}
