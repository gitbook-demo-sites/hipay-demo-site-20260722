---
description: "The redirect pages are pages to which HiPay Enterprise redirects your customers' browser after the transaction is processed if it was made outside of "
icon: file-lines
---

# Redirect Pages

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/requirements/redirect-pages](https://developer.hipay.com/payment-fundamentals/requirements/redirect-pages)
{% endhint %}

The redirect pages are pages to which HiPay Enterprise redirects your customers' browser after the transaction is processed if it was made outside of your website (hosted payment page, local payments, 3-D Secure authentication, etc.).

Typically, this is a secure page on your site. The main purpose is to redirect your customers back to your website once they have completed a payment.

## Redirect pages setup

You can configure redirect pages in the Integration -> Redirect Pages section of your HiPay Enterprise back office.

You can overwrite the default redirect pages by sending custom URLs along with the order details in your requests to the payment gateway. Please refer to the HiPay Enterprise Gateway API documentation .

## Default redirect pages

Field name

Description

Accept page

Page where to redirect your customer if the transaction was successful.

Decline page

Page where to redirect your customer if the transaction was refused.

Pending page

Page where to redirect your customer if the transaction is pending.

Cancel page

Page where to redirect your customer if the transaction was cancelled.

Exception page

Page where to redirect the customer's browser after a system failure or when the payment gateway is temporarily unavailable. If the page is not defined, the default page for exceptions is displayed by the payment gateway.

## Feedback parameters

Select this option in your HiPay Enterprise back office if you want HiPay Enterprise to send back transaction parameters to your redirect pages for further processing within your own website.

To activate this option, you MUST specify at least an Accept page URL. Sent parameters are included in your redirect pages on HTTP GET.

## Sent fields

The following table lists and describes the fields sent to your redirect pages.

Field name

Description

orderid

Unique identifier of the order as provided by the merchant

cid

Unique identifier of the customer as provided by the merchant

state

Transaction state. The value must be from the following list: completed, pending, declined or error.

status

Transaction status. A list of possible transaction statuses can be found in the Transaction statuses article.

test

1 if the transaction is a test transaction; otherwise 0.

reference

Unique identifier of the transaction

approval

Authorization code (up to 35 characters) generated for each approved or pending transaction by the acquiring provider

authorized

Time when the transaction was authorized

ip

IP address of the customer making the purchase

country

Country code associated to the customer's IP address

lang

Language code of the customer

email

Email address of the customer

cdata1cdata2 ... cdata10

Custom data

score

Total score assigned to the transaction (main risk indicator)

fraud

Overall result of risk assessment returned by the payment gateway. The value must be from the following list: pending (rules have not been checked), accepted (the transaction has been accepted), blocked (the transaction has been rejected due to reviewing system rules), challenged (the transaction has been flagged for review)

review

Decision made when the overall risk result returns challenged. An empty value means no review is required. The value must be from the following list: pending (a decision to release or cancel the transaction is pending), allowed (the transaction has been released for processing), denied (the transaction has been cancelled).

avscheck

Result of the Address Verification Service (AVS). Possible AVS result codes can be found in the Address Verification Service article.

cvccheck

Result of the CVC (Card Verification Code) check. Possible CVC result codes can be found in the Card Verification Code article.

pp

Payment product used to complete the transaction. Informs about the payment_method section type. Possible payment products can be found in the Payment means article.

eci3ds

3-D Secure (3DS) electronic commerce indicator

veres

3-D Secure (3DS) enrollment status

pares

3-D Secure (3DS) authentication status. This field is only included if payment authentication was attempted and a value was received.

cardtoken

Card token

cardbrand

Card brand (e.g.: VISA, MASTERCARD, AMERICAN EXPRESS, MAESTRO)

cardpan

Card number (up to 19 characters). Note that, due to the PCI DSS security standards, our system has to mask credit card numbers in any output (e.g.: **4769).

cardexpiry

Card expiry year and month (YYYYMM)

cardcountry

Bank country code where the card was issued. This two-letter country code complies with ISO 3166-1 (alpha 2).
