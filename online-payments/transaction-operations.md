---
description: "Create, inspect, capture, and refund HiPay transactions."
icon: arrows-rotate
---

# Transaction operations

Common support questions often map to a small set of transaction operations: create the payment, inspect status, capture, refund, or challenge.

{% tabs %}
{% tab title="Create order" %}
```bash
curl -X POST "https://stage-secure-gateway.hipay-tpp.com/rest/v1/order" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD" \
  -d "orderid=ORDER-1001" \
  -d "amount=49.90" \
  -d "currency=EUR" \
  -d "cardtoken=$CARD_TOKEN"
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

{% tab title="Get status" %}
```bash
curl "https://stage-secure-gateway.hipay-tpp.com/rest/v1/transaction/$TRANSACTION_REFERENCE" \
  -u "$HIPAY_API_LOGIN:$HIPAY_API_PASSWORD"
```
{% endtab %}
{% endtabs %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/order" method="post" %}
[Order API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}

{% openapi src="https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml" path="/v1/maintenance/transaction/{transaction_reference}" method="post" %}
[Maintenance API](https://raw.githubusercontent.com/hipay/openapi-hipay/master/enterprise/gateway.yaml)
{% endopenapi %}
