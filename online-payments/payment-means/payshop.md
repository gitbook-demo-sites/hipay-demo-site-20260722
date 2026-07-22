---
description: "Payment services company, specialized in electronic payments of domestic accounts, without the need of bank cards. Have in mind that partial captures "
icon: file-lines
---

# Payshop

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/payshop](https://developer.hipay.com/online-payments/payment-means/payshop)
{% endhint %}

Payment services company, specialized in electronic payments of domestic accounts, without the need of bank cards. Have in mind that partial captures are not possible and refunds are made by IBAN bank transfers only.

## User Experience

The user experience consists in a physical one-time payment functionality using a single numerical reference. The payment deadline is set by merchants.

Once you do the Order API call, you will redirect the customer to the forward_url of the API response. In this page the customer will be able to see the reference number of the transaction, that it will use for making the payment.

Once the customer has the reference number, he needs to pay at any of the Payshop Payment Points.

## Request parameters

To create a Payshop transaction on the HiPay Enterprise Payment Gateway, you must send, at least, these mandatory parameters in your ORDER API call .

payment_product payshop

currency The only supported currency is the euro. Ex. EUR

description Description of your order. Ex: Summer sales

orderid Unique order ID. Ex: Order_1232

amount Total order amount. Ex: 9.99

email Customer's email address. Ex: [email protected]

Endpoints

Stage: https://stage-secure-gateway.hipay-tpp.com/rest /v1/order

Production: https://secure-gateway.hipay-tpp.com/rest/ v1/order

Make sure you have configured your HiPay account and the redirection urls before using the Order API.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API .

## API Response

The ORDER API call will create a transaction and return a forward URL and the below information related to the transaction.

This forward URL is dedicated to display a Payshop payment page.

After payment validation, HiPay will send a server-to-server notification to inform the merchant the status of the transaction.

JSON

JSON

```
{
"state": "forwarding",
"reason": "",
"forwardUrl": "https://secure-gateway.hipay-tpp.com/gateway/forward/40e5d0e8938785df12531dd0285cc1ba",
"test": "true",
"mid": "00001329212",
"attemptId": "1",
"authorizationCode": "",
"transactionReference": "800045274278",
"referenceToPay": {
"reference": "1124900069615",
"amount": "10.00",
"expirationDate": "2020-07-19"
},
"dateCreated": "2020-06-19T09:24:36+0000",
"dateUpdated": "2020-06-19T09:24:37+0000",
"dateAuthorized": "",
"status": "142",
"message": "Authorization Requested",
"authorizedAmount": "0.00",
"capturedAmount": "0.00",
"refundedAmount": "0.00",
"creditedAmount": "0.00",
"decimals": "2",
"currency": "EUR",
"ipAddress": "0.0.0.0",
"ipCountry": "",
"deviceId": "",
"cdata1": "",
"cdata2": "",
"cdata3": "",
"cdata4": "",
"cdata5": "",
"cdata6": "",
"cdata7": "",
"cdata8": "",
"cdata9": "",
"cdata10": "",
"avsResult": "",
"cvcResult": "",
"eci": "7",
"paymentProduct": "payshop",
"paymentMethod": "",
"threeDSecure": "",
"fraudScreening": {
"scoring": "0",
"result": "ACCEPTED",
"review": ""
},
"order": {
"id": "ORDERTEST_1592558676_117",
"dateCreated": "2020-06-19T09:24:36+0000",
"attempts": "1",
"amount": "10.00",
"shipping": "0.00",
"tax": "0.00",
"decimals": "2",
"currency": "EUR",
"customerId": "",
"language": "en_US",
"email": "[email protected]"
},
"debitAgreement": {
"id": "",
"status": ""
}
}
```
