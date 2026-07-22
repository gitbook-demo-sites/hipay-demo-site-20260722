---
description: "Embed secure HiPay card fields in a merchant checkout."
icon: credit-card
---

# Hosted Fields quickstart

Hosted Fields gives merchants an embedded checkout while keeping sensitive card data inside HiPay-hosted components.

{% hint style="warning" %}
Only public credentials belong in browser code. Server-side order creation still uses private credentials.
{% endhint %}

{% stepper %}
{% step %}
## Load the JavaScript SDK

Add the HiPay JavaScript SDK to the checkout page and initialize it with public credentials.

```html
<script src="https://libs.hipay.com/js/sdkjs.js"></script>
<script>
  const hipay = HiPay({
    username: "HIPAY_PUBLIC_LOGIN",
    password: "HIPAY_PUBLIC_PASSWORD",
    environment: "stage",
    lang: "en"
  });
</script>
```
{% endstep %}

{% step %}
## Create the field containers

Use stable container IDs for card holder, card number, expiry date, and CVC.

```html
<label>Card holder</label>
<div id="hipay-card-holder"></div>

<label>Card number</label>
<div id="hipay-card-number"></div>

<label>Expiry date</label>
<div id="hipay-expiry-date"></div>

<label>CVC</label>
<div id="hipay-cvc"></div>
```
{% endstep %}

{% step %}
## Mount the Hosted Fields

Choose automatic mode for lower maintenance or custom mode when the merchant needs full checkout layout control.

{% tabs %}
{% tab title="Automatic mode" %}
```js
const cardInstance = hipay.create("card", {
  template: "auto",
  selector: "hipay-hostedfields-form"
});
```
{% endtab %}

{% tab title="Custom mode" %}
```js
const cardInstance = hipay.create("card", {
  fields: {
    cardHolder: { selector: "hipay-card-holder" },
    cardNumber: { selector: "hipay-card-number" },
    expiryDate: { selector: "hipay-expiry-date" },
    cvc: { selector: "hipay-cvc", helpButton: true }
  }
});
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
## Tokenize the card

Submit the hosted fields to get a token. Send that token to the merchant backend, never raw card data.
{% endstep %}

{% step %}
## Create the order server-side

The backend calls the HiPay Order API with the card token, amount, currency, order id, and customer details.
{% endstep %}
{% endstepper %}

## Field state reference

| State class | Meaning | Typical UI treatment |
| --- | --- | --- |
| `HiPayField-empty` | No value entered yet | Neutral border |
| `HiPayField-focused` | Shopper is editing the field | Brand accent border |
| `HiPayField-valid` | Field passed validation | Success state |
| `HiPayField-invalid` | Field failed validation | Error message and retry |
