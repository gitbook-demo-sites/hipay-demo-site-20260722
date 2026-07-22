---
description: "This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Bancomat Pay. B"
icon: file-lines
---

# Bancomat Pay

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/bancomat-pay](https://developer.hipay.com/online-payments/bancomat-pay)
{% endhint %}

This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Bancomat Pay.

Bancomat Pay Payment Method - HiPay

Bancomat Pay is a leading payment solution in Italy, offering secure redirection payments via the Bancomat Pay app. Users require an active account and the mobile application for transaction authentication.

## PRESENTATION

Brand Bancomat Pay
Payment Flow Push notification (Direct) / Redirection (Redirect)
Integration Hosted Payments / Hosted Page / Order API
Product Code bancomatpay
Available country codes IT
Currency EUR
Minimum amount 0.01
Maximum amount Defined by the customer's bank
3DS No
Authentication Via push notification in BPay app
Refund

* Refund possible up to 13 months
Dispute / Chargeback

* Dispute: 15-day response

* Chargeback fees applied per HiPay policy

## ESSENTIAL INFORMATION

### POPULARITY AND AVAILABILITY

Bancomat Pay is a widely used mobile payment solution in Italy, heavily adopted for its speed, security, and direct integration with major Italian banks. It effectively meets the needs of online, mobile, and in-store transactions.

### PAYMENT PROCESS

The payment is made via an automatic redirection. Once the customer selects Bancomat Pay, they are securely redirected to the Bancomat Pay app or their bank's portal to authenticate and validate the transaction directly on their device.

### SECURITY AND COMPATIBILITY

Transactions are authenticated via the app, complying with security standards without storing sensitive data. Compatible across browsers and mobile devices.

### CONFIGURATION AND COMPLIANCE

Ensure HiPay account is correctly configured. Only EUR transactions are supported. Use Redirect Pages Requirements .

### USE CASES

Ideal for instant and secure payments, Bancomat Pay is perfectly suited for merchant sites targeting an Italian customer base. The direct/redirect solution is especially useful for providing a frictionless checkout and boosting conversion rates, particularly on mobile devices.

## INTEGRATION

### INTEGRATION METHODS

Method
Description

Hosted Payments
Managed via HiPay's Hosted Payments solution.

Hosted Fields
Allows for a customized checkout experience.

Hosted Page
Uses a pre-designed payment page.

Order API
Enables direct creation and management of transactions.

### DIRECT VS REDIRECT FLOWS

Bancomat Pay supports two distinct authentication paths depending on the parameters sent in your request:

* Direct Flow: Triggered when the phone parameter is provided. The customer receives a push notification on their device.

* Redirect Flow: Triggered when the phone parameter is omitted. The API response will include a forward_url field. You must redirect the customer to this URL to complete the payment

### USER EXPERIENCE

The customer must have an active Bancomat Pay account and the mobile application installed.

* Customer selects Bancomat Pay on the merchant site.

* HiPay prepares the transaction.

* Direct Flow: Customer receives a push notification directly on their Bancomat Pay app. Redirect Flow: Customer is redirected to a Bancomat Pay page to scan a QR code or open the app.

* Customer authenticates and validates the payment (max duration: 5 min).

* Bank sends the status to HiPay.

* HiPay notifies the merchant and confirms transaction to the customer.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter Description / Example

payment_product bancomatpay
orderid Unique identifier (e.g., ORDER_1583157211)
description Brief description (e.g., Summer Sale)
amount Total amount (e.g., 99.99)
currency ISO 4217 code (e.g., PLN or EUR)
firstname Customer's first name
lastname Customer's last name
country Customer's country (IT)

#### SPECIFIC INPUT PARAMETERS (OPTIONAL BUT RECOMMENDED)

Parameter
Description

phone
Customer phone number with country code prefix

Required for direct flow

email
Customer's email address

streetaddress
Postal address

city
Customer's city

zipcode
Postal code

#### SPECIFIC OUTPUT PARAMETERS

Parameter
Description

forward_url
Url to redirect the consumer (Redirect flow)

### ENDPOINTS

Environment URL

Stage https://stage-secure-gateway.hipay-tpp.com/rest/v1/order
Production https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

### BANCOMAT PAY SAMPLE REQUEST

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization:*****'\
--data-urlencode 'payment_product=bancomatpay' \
--data-urlencode 'orderid=1769530975' \
--data-urlencode 'amount=1.50' \
--data-urlencode 'currency=EUR' \
--data-urlencode 'description=description Bancomat Pay' \
--data-urlencode 'firstname=John' \
--data-urlencode 'lastname=Doe' \
--data-urlencode 'country=IT' \
--data-urlencode 'phone=+393349276423'
```

### Best practices

* Verify that the phone number is in international format

* Set a client-side timeout corresponding to the maximum validation duration (5 min)

* Use server-to-server notifications to track status changes in real time

* Test in the Stage environment before production

* Handle refunds within the allowed 13-month window

* Monitor disputes and respond within 15 calendar days with appropriate supporting documents

* Track chargebacks and account for associated fees

* Ensure the customer has an active Bancomat Pay account and the application installed

* Check error codes and technical messages (general): HiPay Error Messages
