---
description: "This document is designed to provide you details on how to integrate your business to the HiPay Professional payment gateway. This document provides s"
icon: file-lines
---

# Professional Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/professional-integration](https://developer.hipay.com/online-payments/payment/professional-integration)
{% endhint %}

This document is designed to provide you details on how to integrate your business to the HiPay Professional payment gateway. This document provides step-by-step instructions on how to simply and quickly get up and running with our services as well as detailed reference material.
Security Considerations

HiPay Professional SOAP API service is protected to:

* ensure that only authorized Merchants use it,

* prevent payment information from being compromised

## Integration Guidelines

This chapter outlines the basic integration requirements that you app must meet.

### Submitting a Request

#### Endpoints

There are two endpoints (base URLs) that you can make your API calls to.

Environment
Endpoint

Stage
https://test-ws.hipay.com/

Production
https://ws.hipay.com/

#### Authentication

Overview
Authentication

All requests to HiPay SOAP REST API require the Merchant to authenticate himself at each request.
Your API credentials can be found in the Merchant Interface under Sell with Hipay -> Hipay integration -> Merchant Tool Kit / API -> Webservice Access.

#### Character Encoding

All parameters accept UTF-8 encoded text via the API. All other encodings must be converted to UTF-8 before sending them to the HiPay API in order to guarantee that the data is not corrupted.

### Response Handling

Whether a request succeeded or not, it is indicated by the HTTP status code. A 2xx status code indicates a success, whereas a 5xx status code indicates a failure.

#### Status Codes

The HiPay API attempts to return appropriate HTTP status codes for every request. These are the HTTP status codes you may receive and their meaning.

HTTP Status
Description

200 OK
The request was understood and is processing.

404 Not Found
The resource requested does not exist.

500 Server Error
The request has an error, mandatory parameters are missing or you are trying to send unknown parameters to the resource.

503 Service Unavailable
HiPay API is temporarily unable to process the request. Try again later.

#### Format

The HiPay API will respond to your request in SOAP XML format. By default, HiPay SOAP API returns XML in a SOAP Envelope. For example, here is the default XML representation of a generate result.

XML

XML

```

https://payment.hipay.com/index/pay/payid/716...7106fc
0
N/A

```

### Error Handling

HiPay API returns one level of error information: a response body with additional details that can help you determine how to handle the exception.

Exception properties An exception has up to three properties.

Property Description code 0 = OK / >0 = Error. description A descriptive message regarding the exception. i.g. if you receive an exception with status code 400 (Bad Request), the and properties are useful for debugging what went wrong.

XML

XML

```

1
Bad password for login '4f8x3x80fd4x476f1e227c68xefdx0x5'

```

## SOAP API Resources

The following table lists the REST API resources used.

Resource
Description

POST /soap/payment-v2/generate
Allows you to request an order and initialize a hosted payment page.

POST /soap/transaction-v2/confirm
A request instructing the payment gateway to capture a previously- authorized transaction, i.e. transfer the funds from the customer's bank account to the merchant's bank account. This transaction is always preceded by an authorization.

POST /soap/transaction-v2/cancel
A request instructing the payment gateway to cancel a previously- authorized transaction. Only authorized transactions can be canceled, captured transactions must be refunded.

POST /soap/refund-v2/card
A request instructing the payment gateway to fully refund a credit card previously captured transaction.

### Request a New Order

At the time of payment, cardholders are redirected to a secured payment page hosted by HiPay. This page can be personalized with merchants' CSS style sheet to fit his website look and feel. To post your CSS please go to HiPay Professional integration -> Creating a button -> Edit (on your website details)

Order Parameters

FieldName
Format
Length
Req
Description

wsLogin
AN
32
M
Your API Webservice Login.

wsPassword
AN
32
M
Your API Webservice Password.

websiteId
N
11
M
ID of the website created on merchants' account.

categoryId
N
11
M
The order or product categories are attached to, and depend upon, the merchant site's category. Depending on the category that is associated with the site, the categories that are available to the order and products will NOT be the same. You can obtain the list of order and product category ID's for the merchant site at this URL:
Production platform: https://payment.hipay.com/order/list-categories/id/[production websiteID]
Stage platform:
https://test-payment.hipay.com/order/list-categories/id/[stage websiteID]

currency
A
3
M
The currency specified in your HiPay Professional account. This three-character currency code complies with ISO 4217.

amount
R
-
M
The total order amount. It should be calculated as a sum of the items purchased, plus the shipping fee (if present), plus the tax fee (if present).

rating
AN
3
M
Age category of your order.
Accepted values :
+12 : For ages 13 and over
+16 : For ages 16 and over
+18 : For ages 18 and over
ALL : For all ages

locale
AN
5
M
Locale code of your customer (Default to en_GB - English - Great Britain).It may be used for sending confirmation emails to your customer or for displaying payment pages.
Examples:
en_GB
fr_FR
es_ES
it_IT

customerIpAddress
AN
15
M
The IP address of your customer making a purchase.

executionDate
AN
32
M
Date and time of execution of the payment in MySQL DATETIME format (Y-m-dTH:i:s). e.g.: 2014-12-25T10:57:55

manualCapture
N
1
M
Indicates how you want to process the payment.
0: indicates transaction is sent for authorization, and if approved, is automatically submitted for capture.
1: indicates this transaction is sent for authorization only. The transaction will not be sent for settlement until the transaction is submitted for capture manually by the Merchant.

description
AN
255
M
The order short description.

customerEmail
AN
32
-
The customer's e-mail address.

urlCallback
AN
255
M
The URL will be used by our server to send you information in order to update your database. Please refer to Server-to-Server notification chapter.

urlAccept
AN
255
-
The URL to return your customer to once the payment process is completed successfully.

urlDecline
AN
255
-
The URL to return your customer to after the acquirer declines the payment.

urlCancel
AN
255
-
The URL to return your customer to when he or her decides to abort the payment.

urlLogo
AN
255
-
This URL is where the logo you want to appear on your payment page is located.
Important: HTTPS protocol is required.

merchantReference
AN
255
-
Merchants' order refernce.

merchantComment
AN
255
-
Merchants' comment concerning the order.

emailCallback
AN
255
-
Email used by HiPay Professional to post operation notifications.

freedata
AN
-
-
Custom data. You may use these parameters to submit values you wish to receive back in the API response messages or in the notifications, e.g. you can use these parameters to get back session data, order content or user info.

You must format it like this:

XML

XML

```

keyOne
ValueOne

keyTwo
ValueTwo

```

Response Fields The following table lists and describes the response fields.

Field Name Description redirectUrl Payment page URL. Merchant must redirect the customer's browser to this URL. code Status code of the answer. description Reason description (if error).

### Refund an order

To perform a refund on an existing transaction, make an HTTP POST request to the following resource.

Operation Type Resource Description refund /soap/refund-v2/card A request instructing the payment gateway to fully refund a previously credit card captured transaction. Request Parameters

Parameter Format Length Req Description wsLogin AN 32 M Your API Webservice Login. wsPassword AN 32 M Your API Webservice Password. websiteId N 32 M Id of merchants' website were transaction was made. transactionPublicId AN 32 M The unique identifier of the transaction sent to the merchant on the urlCallback (Notification) called transid. Response Fields

The following table lists and describes the response fields.

Field Name Description transactionPublicId The unique identifier of the transaction. code Status code of the answer. description Description of the answer. amount Refunded amount. currency Currency of refunded transaction.

### Maintenance Operations

To perform maintenance on an existing transaction, make an HTTP POST request to the following resources.

Operation Type Resource Description confirm /soap/transaction-v2/confirm A request instructing the payment gateway to capture a previously-authorized transaction, i.e. transfer the funds from the customer's bank account to the merchant's bank account. This transaction is always preceded by an authorization. cancel /soap/transaction-v2/cancel A request instructing the payment gateway to cancel a previously-authorized transaction. Only authorized transactions can be canceled, captured transactions must be refunded. Request Parameters

Parameter Format Length Req Description wsLogin AN 32 M Your API Webservice Login. wsPassword AN 32 M Your API Webservice Password. transactionPublicId AN 32 M The unique identifier of the transaction sent to the merchant on the urlCallback (Notification) called transid. Response Fields

The following table lists and describes the response fields.

Field Name Description transactionPublicId The unique identifier of the transaction. code Status code of the answer. description Description of the answer. Examples

Request

XML

XML

```

107
51X6F4C37X253
4f8x3e8xfd4ex76f1ex27c6xfefdb3e5 2x0c409xc4254x819bfx246d6x02d1x2

```

Response

XML

XML

```

0
Refund to credit card request for transaction 51X6F4C37X253 has been sent !
EUR
4
51X6F4C37X253

```

## Server-to-Server Notifications

In order to notify events related to your payment system, such as a new transaction or a 3-D Secure transaction, our platform can send to your application a Server-to-Server notification.

### Setup

To set your Notification URL you must set it on urlCallback parameter at the moment of generate a new order (please refer to Chapter 3.1 Request a New Order). After a successful purchase, HiPay calls twice your Notification URL in background with comprehensive information about the payment passed through an HTTP POST parameter in an XML array POST['xml'] the first time for the authorization notification and the second one for the capture notification.

Possible actions

Operation Type Description authorization Authorization from the customer's bank to make the capture. capture Notification of the real capture to debit the customer's account. cancellation Previously-authorized transaction was cancelled. refund Previously-captured transaction was refunded. reject Charge Back. The cardholder reversed a capture processed by their bank or credit card company. For instance, the cardholder contacts his credit card company and denies having made the transaction. The credit card company then revokes the already captured payment. Please note the legal difference between shopper who ordered the goods and cardholder who owns the credit card and ends up paying for the order.
In general charge backs only occur incidentally. When they do, contacting the shopper can often solve the situation. Occasionally it is an indication of credit card fraud. Possible status

Operation Type Description ok Operation succeeded. nok Operation not succeeded. cancel Cancelation of the operation. waiting Operation waiting for an action. Response Fields :

The following table lists and describes the response fields received on the notification call.

Field Name Description operation Operation Type. Please report to Types of possible actions table. status Operation Status. Please report to Types of possible status table. date Date of the transaction (YYYY-mm-dd). time Time of the transaction (e.g., 11:00:58 UTC+0000). origAmount The total order amount (e.g., 150.00). It should be calculated as a sum of the items purchased, plus the shipping fee (if present), plus the tax fee (if present). origCurrency Base currency for this order. This three-character currency code complies with ISO 4217. idForMerchant The transaction ID used by the merchant. emailClient Email address of the customer. merchantDatas Custom merchant data provided at the moment of generate a new order (please refer to Chapter 3.1 Request a New Order). transid The unique identifier of the transaction. is3ds Indicates if the used card is 3-D Secure enrolled. paymentMethod Payment method used by the customer. customerCountry Country code of the customer. This two-letter code complies with ISO-3166. returnCode - returnDescriptionShort - returnDescriptionLong -

XML

XML

```

1.0
05049866c4538df62c780fdb08b95ee0

authorization
nok
2014-02-11
11:00:58 UTC+0000
1.00
EUR
ORDER123456
[email protected]

aValueOne
aValueTwo

52F9FFA68486E
Yes
VISA
FR

;
```

## Signature verification

It is strongly recommended to use a signature mechanism to verify the contents of a request or redirection made to your servers.

This prevents customers from tampering with the data in the data exchanges between your servers and our payment system. A unique signature is sent each time that HiPay contact a merchant URL.

### Verification

For the URL notification, the signature is sent on the md5content parameter, to verify it, you just need so concatenate your wsPassword with the result part of the XML posted to you.

Algorithm : Md5 Signature = md5('...' + wsPassword)
