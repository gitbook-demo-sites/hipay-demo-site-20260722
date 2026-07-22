---
description: "Create and customize a HiPay Hosted Page payment."
icon: window-maximize
---

# Hosted Page quickstart

Hosted Page lets a merchant redirect shoppers to a HiPay-managed checkout while keeping implementation effort low.

{% stepper %}
{% step %}
## Create the hosted payment

Call the Hosted Page API with the order amount, currency, order id, customer information, and redirect URLs.

{% code title="Create a Hosted Page payment" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/hpayment" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \
  -d "orderid=HP-DEMO-1001" \
  -d "amount=49.90" \
  -d "currency=EUR" \
  -d "description=Demo checkout" \
  -d "accept_url=https://merchant.example/success" \
  -d "decline_url=https://merchant.example/declined"
```
{% endcode %}
{% endstep %}

{% step %}
## Redirect the shopper

Use the redirect URL returned by HiPay. Keep the merchant confirmation page focused on order status, not payment assumptions.
{% endstep %}

{% step %}
## Listen for the server notification

Use the notification to update the order in the merchant system. Do not rely only on the shopper redirect.
{% endstep %}

{% step %}
## Capture, refund, or challenge when needed

Use maintenance operations to manage the transaction lifecycle after authorization.
{% endstep %}
{% endstepper %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml" path="/v1/hpayment" method="post" %}
[Hosted Page API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/hpayment.yaml)
{% endopenapi %}
