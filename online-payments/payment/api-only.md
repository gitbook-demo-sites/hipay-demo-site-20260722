---
description: "With this option you will be in charge of handling the checkout page, the payment methods and form, as you will only integrate the HiPay Entreprise pl"
icon: file-lines
---

# Payment - API Order

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/api-only](https://developer.hipay.com/online-payments/payment/api-only)
{% endhint %}

With this option you will be in charge of handling the checkout page, the payment methods and form, as you will only integrate the HiPay Entreprise platform to process the transaction for you.

In this case, the payment page is hosted on your website, allowing you to have a unified, fully customized workflow.

## Integration

In order to request a new order, you will need to integrate the GATEWAY API, in particular, the POST Order API Service . If you will, you can use the PHP SDK to simplify the API integration.

Here you have an example of a basic request for a Visa payment (required fields only):
orderid : unique order id. Ex: ORDER_1583157210

description : order short description. Ex. Sales

amount : Total order amount. Ex: 9.99

currency : Order ISO 4217 three-character currency code. Ex: EUR

payment_product : The payment method used to proceed checkout. Ex: visa

cardtoken : This is a token HiPay for a credit or debit card. Ex: ef3b4d50325268e59d216c0b053a4f5c7eb559f9abeca0ef178ea1941b2d156a

Please note that:

* If you want to execute transactions with credit or debit card payment products, you will need to tokenize card numbers beforehand by using either the JS SDK or the HiPay Entreprise Tokenization API .

* Depending on the payment product, parameters specific to the payment method are required.

## Timeout

We recommend you to use a client request timeout of 60 seconds.

Indeed, some API requests may take longer than expected because they rely on different actors.

If your client request timeout is too short and the response takes longer, the transaction will be paid and created at HiPay but your end user will have an error.

Our PHP SDK allows you to easily change this value.
