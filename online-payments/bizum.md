---
description: "This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Bizum. Bizum Pa"
icon: file-lines
---

# Bizum

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/bizum](https://developer.hipay.com/online-payments/bizum)
{% endhint %}

This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Bizum.

Bizum Payment Method - HiPay

Bizum is a leading payment solution in Spain, offering secure redirection payments via the customer's banking app. Users require an active bank account linked to Bizum and must validate transactions within their mobile banking application.

## PRESENTATION

Brand Bizum
Payment Flow Push notification in banking app
Integration Hosted Payments / Hosted Page / Order API
Product Code bizum
Country Spain
Currency EUR
Minimum amount 0.50
Maximum amount Defined by the customer's bank
3DS No
Authentication Via push notification in banking app
Refund / Dispute / Chargeback

* Refund possible up to 13 months

* Dispute: 15-day response

* Chargeback fees applied per HiPay policy

## ESSENTIAL INFORMATION

### USER EXPERIENCE

The customer must have an active Bizum account enabled in their banking app. Steps:

* Customer selects Bizum on the merchant site.

* HiPay prepares the transaction.

* Customer receives a push notification via their banking app.

* Customer authenticates and validates the payment (max duration: 5 min).

* Bank sends the status to HiPay.

* HiPay notifies the merchant and confirms transaction to the customer.

### SECURITY AND COMPATIBILITY

Transactions are authenticated via the customer's banking app, complying with security standards without storing sensitive data. Compatible across browsers and mobile devices.

### CONFIGURATION AND COMPLIANCE

Ensure HiPay account is correctly configured. Only EUR transactions are supported. Use Redirect Pages Requirements .

## INTEGRATION

### ENDPOINTS

Environment URL

Stage https://stage-secure-gateway.hipay-tpp.com/rest/v1/order
Production https://secure-gateway.hipay-tpp.com/rest/v1/order

### MANDATORY PARAMETERS

Parameter Description / Example

payment_product bizum
orderid Unique identifier (e.g., ORDER_1583157211)
description Brief description (e.g., Summer Sale)
amount Total amount (e.g., 99.99)
currency ISO 4217 code (e.g., PLN or EUR)
firstname Customer's first name
lastname Customer's last name
phone Customer phone number with country code prefix
country Customer's country (e.g., IT)

### BIZUM SAMPLE REQUEST

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization:*****'\
--data-urlencode 'payment_product=bizum' \
--data-urlencode 'orderid=1769530975' \
--data-urlencode 'amount=1.50' \
--data-urlencode 'currency=EUR' \
--data-urlencode 'description=description Bizum' \
--data-urlencode 'firstname=John' \
--data-urlencode 'lastname=Doe' \
--data-urlencode 'country=ES' \
--data-urlencode 'phone=+34700000000'
```

### TRANSACTION STATUSES

Status Description

pending Transaction in progress, customer redirected
accepted Payment confirmed by the bank
refused Transaction refused by the bank
cancelled Customer cancelled the transaction
error Technical error

### Hosted Integration

#### Hosted fields

With this integration you are in charge of displaying the choice of Bizum.

To display the Hosted Fields you will need to integrate the Javascript SDK and the ORDER API to redirect the customer to the issuing bank's website.

Here you have the mandatory parameters of the ORDER API.

#### Hosted payments

With this integration, you are in charge of creating the carousel yourself. HiPay then displays the payment methods

To display the Hosted Payments you will need to integrate the Javascript SDK and the ORDER API.

Here you have the mandatory parameters of the ORDER API.

#### Hosted page

With this integration HiPay will be in charge of displaying the payment method.

In order to do so, you need to request a Hosted Page. Here you have the mandatory parameters of the HPAYMENT API

#### Recommendation

Make sure you have configured your HiPay account and the redirection urls before using the Order API. We strongly recommend that you provide a pending URL so that the page displayed after payment is not a success URL. You can then listen for the order response in order to display the page corresponding to the result.

Important ! To have better insights of your payments you can leverage HiPay's platform data management. To do so, we strongly recommend to send as much data as possible, as the basket and the customer information. Here you have all the parameters of the API.

### Sandbox Environment

To ensure your Bizum integration is set up correctly, we provide a sandbox environment. This environment allows you to simulate transactions and validate different scenarios before going live.

#### Test Phone Number

For all your test transactions in the sandbox environment, please use the following phone number:

Parameter
Value

phone
+34700000000

#### Payment Scenarios

The transaction outcome (success or failure) is determined by the amount you specify in the amount field. Here are the scenarios you can test:

Amount (EUR)
Transaction Outcome
Scenario Description

0.50 - 4.99
Success
The transaction is successfully approved.

5.00 - 9.99
Authentication Failure
The transaction is declined because authentication could not be completed.

10.00 - 14.99
Feature Not Available
The transaction fails because the requested feature is not yet implemented.

15.00 - 50.00
Inactive User
The transaction is declined because the phone number is not associated with an active Bizum user.

### Best practices for Bizum integration

* Verify that the phone number is in international format

* Set a client-side timeout corresponding to the maximum validation duration (5 min)

* Use server-to-server notifications to track status changes in real time

* Test in the Stage environment before production

* Handle refunds within the allowed window

* Monitor disputes and respond within 15 calendar days with appropriate supporting documents

* Track chargebacks and account for associated fees

* Ensure the customer has an active Bizum account and their banking app installed

* Check error codes and technical messages (general): HiPay Error Messages
