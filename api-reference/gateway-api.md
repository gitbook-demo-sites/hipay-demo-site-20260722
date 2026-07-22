---
description: "Create orders and manage HiPay transactions with the Gateway API."
icon: terminal
---

# Gateway API

Use the Gateway API for direct order creation, transaction lookup, and maintenance operations.

{% tabs %}
{% tab title="Create order" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/order" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \
  -d "orderid=ORDER-1001" \
  -d "amount=49.90" \
  -d "currency=EUR" \
  -d "description=Demo order"
```
{% endtab %}

{% tab title="Retrieve transaction" %}
```bash
curl "https://stage-secure-gateway.hipay-tpp.com/rest/v1/transaction/$TRANSACTION_REFERENCE" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD"
```
{% endtab %}

{% tab title="Refund" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/maintenance/transaction/$TRANSACTION_REFERENCE" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \
  -d "operation=refund" \
  -d "amount=10.00"
```
{% endtab %}
{% endtabs %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/order" method="post" %}
[Order API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/transaction/{transaction_reference}" method="get" %}
[Transaction lookup](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}
