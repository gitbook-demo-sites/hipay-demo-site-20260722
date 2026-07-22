---
description: "Alma is an e-commerce payment system used in France, based on deffered payment. This payment method is one of the most popular method for Buy Now Pay "
icon: file-lines
---

# Alma

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/alma](https://developer.hipay.com/online-payments/payment-means/alma)
{% endhint %}

Alma is an e-commerce payment system used in France, based on deffered payment. This payment method is one of the most popular method for Buy Now Pay later payments in France. It allows customers to pay in 3 or 4 installments, when the merchant is paid immediately..

## Presentation

Brand Payment flow API Product Code Country Currency 3DS Refund / Partial refund Recurring Alma Redirect alma-3x
alma-4x
Only in France
EUR /

For any questions regarding minimum and maximum amounts, please contact support or your account manager. By default, the thresholds are 50 to 2000 euros.

## Integration

Hosted Payments
Hosted Fields
Hosted Page
Order API

Hosted Payments
User Experience

* Choice of Alma as payment method (Hosted Payments on the merchant's website)
* Redirection and Payment (Alma's website)
* Confirmation page display (merchant's website)

Integration

With this integration you are in charge of redirecting the customer to Alma's website, once the customers clicks on the payment button. The hosted payments will take care of displaying the Alma payment method.

To display the Hosted Payments you will need to integrate the Javascript SDK and the ORDER API .

* In order to filter Alma payment methods according to amount, you could specify the request's amount during the initialization of the Hosted Payment. Please refer to the JS Doc Reference . Here you have the mandatory parameters of the ORDER API : payment_product : alma-3x or alma-4x orderid : unique order id. Ex: ORDER_1583157210 description : order short description. Ex. Summer Sales amount : Total order amount. Ex: 99.99 currency : Order ISO 4217 three-character currency code. Ex: EUR
* Endpoints Stage: https://stage-secure-gateway.hipay-tpp.com/rest/v1/order Production: https://secure-gateway.hipay-tpp.com/rest/v1/order Make sure you have configured your HiPay account and the redirection urls before using the Order API. Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API.
Hosted Fields
User Experience

* Choice of Alma as payment method (merchant's website)
* Redirection and Payment (Alma's website)
* Confirmation page display (merchant's website) Integration

With this integration you are in charge of displaying the choice of Alma and redirecting the customer to Alma's website, once the customers clicks on the payment button. The hosted fields will take care of displaying the list of the issuer banks.

To display the Hosted Fields you will need to integrate the Javascript SDK and the ORDER API to redirect the customer to the issuing bank's website.

In order to check the eligibility of Alma payment methods according to amount, you could specify the request's amount during the initialization of the Hosted Field. Please refer to the JS Doc Reference .

Here you have the mandatory parameters of the ORDER API :

payment_product : alma-3x or alma-4x

orderid : unique order id. Ex: ORDER_1583157210

description : order short description. Ex. Summer Sales

amount : Total order amount. Ex: 99.99

currency : Order ISO 4217 three-character currency code. Ex: EUR

Endpoints

Stage: https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production: https://secure-gateway.hipay-tpp.com/rest/v1/order

Make sure you have configured your HiPay account and the redirection urls before using the Order API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API.

Hosted Page
User Experience

* Choice of Alma as payment method (merchant's website or Hosted Page)
* Redirection and Payment (Alma's website)
* Confirmation page display (merchant's website) Integration

With this integration HiPay will be in charge of displaying the payment method.

Note that Alma payment methods will be displayed only if they are eligible according to the requested amount.

In order to do so, you need to request a Hosted Page . Here you have the mandatory parameters of the HPAYMENT API :

payment_product_list : alma-3x or alma-4x

orderid : unique order id. Ex: ORDER_1583157210

description : order short description. Ex. Summer Sales

amount : Total order amount. Ex: 99.99

currency : Order ISO 4217 three-character currency code. Ex: EUR

Endpoints

Stage: https://stage-api.hipay.com/v1/hpayment

Production: https://api.hipay.com/v1/hpayment

Make sure you have configured your HiPay account and the redirection url before using the Order API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API.

Order API
User Experience

* Choice of Alma as payment method (merchant's website)

* Redirection and Payment (Alma's website)

* Confirmation page display (merchant's website)

Integration

With this integration you are in charge of displaying the payment method.

You may use the Order API in order to redirect the customer to Alma's website.

Here you have the mandatory parameters of the ORDER API :

payment_product : alma-3x or alma-4x

orderid : unique order id. Ex: ORDER_1583157210

description : order short description. Ex. Summer Sales

amount : Total order amount. Ex: 99.99

currency : Order ISO 4217 three-character currency code. Ex: EUR

Endpoints

Stage: https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production: https://secure-gateway.hipay-tpp.com/rest/v1/order

Make sure you have configured your HiPay account and the redirection urls before using the Order API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API.
