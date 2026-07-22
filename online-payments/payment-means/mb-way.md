---
description: "MB Way is a Portuguese application developed by SIBS and available for Android, iOS, Windows, Windows Phone and Tizen devices. Currently, the MB Way a"
icon: file-lines
---

# MB Way

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/mb-way](https://developer.hipay.com/online-payments/payment-means/mb-way)
{% endhint %}

MB Way is a Portuguese application developed by SIBS and available for Android, iOS, Windows, Windows Phone and Tizen devices.

Currently, the MB Way application allows you to make instant money transfers between mobile phone numbers associated with MB Way, generate MB Net virtual cards for online purchases, pay for purchases in physical stores through mobile phone number, QR code and contactless, and use an ATM without having to use a bank card.

## User Experience

The user experience of MB Way will depend on the integration type that the merchant has chosen: Hosted Payment Page or API.

HOSTED PAGE

Once the user has chosen to pay with MB Way, you can use HPAYMENT API to create a Hosted Payment Page where the customer will introduce its phone number.

Once the user confirms the phone number, MB Way will send a message to that phone number to confirm the payment on the MB Way mobile APP.

You can personalize the styling of the Hosted Payment Page. More information here.

API INTEGRATION

With this integration, once the user chooses to pay with MB Way, the merchant will be in charge of displaying the phone field.

Once the user confirms the phone number, the merchant will need to make an ORDER API call. Once done, MB Way will send a message to that phone number to confirm the payment on the MB Way mobile APP.

## Hosted Page Integration

To create a MB Way transaction on the HiPay Enterprise Payment Gateway, you must send, at least, these mandatory parameters in your HPAYMENT API call .

payment_product_list mbway

currency The only accepted currency is the euro. Ex. EUR

description Description of your order. Ex: Summer sales

orderid Unique order ID. Ex: Order_1232

amount Total order amount. Ex: 9.99

Endpoints

Stage: https://stage-secure-gateway.hipay-tpp.com/rest /v1/hpayment

Production: https://secure-gateway.hipay-tpp.com/rest/ v1/hpayment

Make sure you have configured your HiPay account and the redirection urls before using the Hpayment API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API .

### Hpayment Reponse

XML

XML

```

https://secure-gateway.hipay-tpp.com/0000-133-7621/payment/web/pay/f377ba63-d2de-46a0-9b5f-2db2e02c1afb
true
00001337621

```

## API Integration

To create a MB Way transaction on the HiPay Enterprise Payment Gateway, you must send, at least, these mandatory parameters in your ORDER API call .

payment_product mbway

currency The only accepted currency is the euro. Ex. EUR

description Description of your order. Ex: Summer sales

orderid Unique order ID. Ex: Order_1232

amount Total order amount. Ex: 9.99

phone Customer's phone number. Ex: 07 00 00 00 00

Endpoints

Stage: https://stage-secure-gateway.hipay-tpp.com/rest /v1/order

Production: https://secure-gateway.hipay-tpp.com/rest/ v1/order

Make sure you have configured your HiPay account and the redirection urls before using the Order API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API .

### Order Reponse

XML

XML

```

pending

true
00001337621
1

800043480714
2020-06-09T15:18:59+0000
2020-06-09T15:19:02+0000

142
Authorization Requested
0.00
0.00
0.00
0.00
2
EUR
0.0.0.0

7
mbway

0
ACCEPTED

```

## Refunds

Refunds are possible using MB Way. In order to integrate this functionality, please read the refund documentation.
