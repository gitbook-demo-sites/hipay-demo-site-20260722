---
description: "The registered OpenAPI specs used by this demo."
icon: code
---

# OpenAPI Overview

The current HiPay API Explorer embeds public OpenAPI files from GitHub. This demo registers those specs with GitBook and uses `builtin:openapi` entries in the table of contents so endpoint pages are generated from the spec instead of hand-maintained in prose.

{% hint style="success" %}
This directly addresses HiPay's requirement for OpenAPI/API docs rendering and reduces drift between API behavior and documentation.
{% endhint %}

## Registered specs

* [API Gateway v3](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/api-gateway.yml)
* [Online Payments API Gateway v1](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
* [Hosted Page v2](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml)
* [Apple Pay Web API](https://raw.githubusercontent.com/hipay/openapi-hipay/refs/heads/master/enterprise/applepay-web.yaml)
* [Settlements API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/settlement.yaml)
* [Marketplace API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/marketplace/marketplace.yaml)
* [Terminal API](https://raw.githubusercontent.com/hipay/openapi-hipay/refs/heads/master/omnichannel/openapi%20-%20Terminal%20API.yaml)
* [Cloud API for Nepting](https://raw.githubusercontent.com/hipay/openapi-hipay/master/omnichannel/openapi%20-%20Nepting.yaml)
* [Cloud API for Standalone Payment Terminals](https://raw.githubusercontent.com/hipay/openapi-hipay/master/omnichannel/openapi%20-%20ConcertV3.yaml)
