---
description: "This integration allows you to leverage Hipay's platform to manage the transaction lifecycle and its data while using another PSP to perform the POS p"
icon: file-lines
---

# POS Passive Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/smart-terminal/pos-passive-integration](https://developer.hipay.com/point-of-sale/smart-terminal/pos-passive-integration)
{% endhint %}

This integration allows you to leverage Hipay's platform to manage the transaction lifecycle and its data while using another PSP to perform the POS payment.

## Payment

Here is the 5-step process to pay using a POS terminal in passive mode:

* To display the transaction on your POS terminal your ECR system will request a payment to your non-HiPay PSP.

* This PSP, will display the amount to pay in your POS terminal.

* Once the card is inserted, the PSP will get the customer's card details.

* Using these card details, the PSP will be able to authorize the customer using an external AAS Acquirer.

* The authorization response will be sent to your ECR.

## Transaction Log

Once the payment has been confirmed, your system will request HiPay to create a passive transaction. This process is divided in two steps:

### Tokenization

A secure token can be generated from the customer's card details using HiPay's Tokenization API .

Please, follow the tokenization API documentation in order to integrate this feature.

This first step is optional and can be implemented if you have the card information.

### Order

You can use the Order API in order to create the transaction after you have created an HiPay's token or you can create an order without the token (in the last case, the token will be added during the reconciliation). In order to do so, you need to integrate the Order API in the following way:

Endpoint URL

Stage https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production https://secure-gateway.hipay-tpp.com/rest/v1/order

Authentication

Basic Auth of your Hips private account credentials (username, pwd)

Order API call

Parameter
Type
Presence
Description
Example

orderid
STRING
Mandatory
Unique order ID
ORDER_234

eci
INTEGER
Mandatory
The Electronic Commerce Indicator (ECI) indicates the security level at which the payment information is processed between the cardholder and merchant. Value is :

10 = proxi
10

description
STRING
Mandatory
Short description of the order.
Transaction

currency
STRING
Mandatory
ISO 4217 three-character currency code.
EUR

amount
INTEGER
Mandatory
Total order amount, calculated as the sum of purchased items, plus shipping fees, plus tax fees.
8.99

payment_product
STRING
Mandatory
The payment method used to proceed checkout. Value is:

tpe = without card token
tpe

initialize_payment_terminal
BOOLEAN
Mandatory
Whether a transaction is in passive mode. Value is :

0 = Passive mode
0

payment_product_parameters
JSON
Mandatory
hash : hash algorithm based on sha1(orderid + amount + currency + hashkey)
db75353234324dfdfdsd5635d

Mandatory
code : transaction status. Values are:

200000 = Authorized

200100 = Captured

200350 = Credit
200100

Mandatory
mid : merchant contract
6

Mandatory
acquirer_registrationid : merchant contract
6

Conditional
acquirer_reference : bank field 37, that represents a unique id for the authorized transactions.
Data used for the reconciliation. Max length value = 11 digits.
12345678901

Conditional
authorization_code : if an authorization code is delivered by issuer for this transaction
100969

Optional
cardToken : token of the tokenization API.
ef3b4d50325268e59d216c0b053a4f5c7eb559f9abeca0ef178ea1941b2d156a

operation
STRING
Optional
Transaction type:

Sale indicates that the transaction is automatically submitted for capture.

Authorization indicates that this transaction is sent for authorization only.

Credit indicates that this is a credit transaction.

Default value : Authorization
authorization

custom_data
JSON
Optional
custom data to be linked with the transaction
{internal_reference:ORD_987465,customer_first_order:true,other_sample_parameter:Other sample value}

firstname
STRING
Optional
Cardholder's name
John

lastname
STRING
Optional
Cardholder's lastname
Doe

email
STRING
Optional
Cardholder's email
[email protected]

cid
STRING
Optional
Customer ID
12345

basket
JSON
Optional
Shopping cart details.

More information

This cart content must be compliant with the transaction fields (total amount must be equal to the products in the basket, ...)
[{european_article_numbering:4711892728946,product_reference:NF-a1690,name:My first product,type:good,quantity:1,unit_price:8.99,discount:0,tax_rate:8.20,total_amount:8.99}]

If you want to have a better understanding of the Order API, please read the following documentation .

#### Capture & Cancel

At the end of the day, once the daily collection is done, you can update the status of the transactions created at HiPay to Captured or Cancelled. In order to do this, you need to integrate the Maintenance API.

Please read the following documentation in order to integrate it.

#### Acquirer reconciliation journal

The Acquirer reconciliation journal refers to the acquirer's reconciliation file or API. This document contains the transactions that have been authorized by a given acquirer, and that have been successfully settled.

This journal is essential to reflect, as until this moment HiPay doesn't know for sure the transactions that have been successfully settled. Once HiPay receives this information, it updates the transaction status.

## Refund a Transaction

To make a total or partial refund of a transaction, you can use either our API or the HiPay Enterprise back office. Here you have the documentation to refund a transaction using the API.

Please note:

* refunds can't be made if an operation chargeback was already asked from the customer for this transaction.

* refunds must be made within 11 months after capture for card transactions. Conditions may differ depending on payment methods.
