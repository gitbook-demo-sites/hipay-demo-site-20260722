---
description: "Bancontact WIP Documentation Secure Wallet Initiated Payment integration for Bancontact. Overview Bancontact WIP is an API module designed to enable m"
icon: file-lines
---

# Bancontact WIP

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/bancontact-wip](https://developer.hipay.com/mobile-payments/bancontact-wip)
{% endhint %}

Bancontact WIP Documentation

Secure Wallet Initiated Payment integration for Bancontact.

## Overview

Bancontact WIP is an API module designed to enable merchants to offer the Wallet Initiated Payment service for Bancontact. This solution streamlines the payment process by allowing an initial transaction to enroll a customer's card, generating a secure token for subsequent recurring or oneclick transactions.

## PRESENTATION

Brand Bancontact WIP
Payment Flow Redirect
Integration Hosted Payments / Hosted Page / Order API
Product Code bancontact
Country Belgium
Currency EUR
Minimum amount 0.01
Maximum amount (one clic) 500
Maximum amount (recurring) 1.500
3DS No
Authentication Clicking on the QR Code opens the Bancontact application
Refund Full and partial refund possible up to 13 months

## Prerequisites & Onboarding

The activation process for Bancontact WIP is manual. Merchants must be screened and approved by Bancontact and will receive the decision within 15 business days from the application date.

## Bancontact WIP UX Requirements for Merchant

To support Bancontact WIP, the Merchant must meet specific UX requirements on its checkout page:

* The Merchant shall have a simple and easily accessible procedure in place to allow the Cardholder to dispute a WIP Transaction or to ask the Merchant to cancel a WIP transaction through a refund.

* The Merchant shall have a simple and easily accessible procedure in place to allow the Cardholder to add, update or delete his Bancontact card(s) used to perform WIP Transactions. An electronic transaction receipt shall be sent to the Cardholder containing all mandatory transaction data as well as a clear procedure to ask the Merchant to refund this transaction or retain any future payments in the case of a recurring payment.

* The cardholder shall have established a relationship (As a minimum, the Cardholder shall have approved the Terms and Conditions of the WIP Merchant) with the Merchant to receive ongoing services and give permission to the WIP Merchant to debit his account on a recurring or ad-hoc basis.

## Integration API

### Customer Journey - Initial Transaction

* API Call - Order Initialization: The merchant initiates the transaction by calling the Hipay Order API with the following parameters: ``` payment_product: bancontact email: [email protected] description: tx init stage orderid: {{$timestamp}} amount: 3.00 currency: EUR firstname: Eric lastname: DUPONT streetaddress: 2 rue du Paradis city: Bruxelles zipcode: 1130 country: BE cardtoken: eci: 7 recurring_payment or one_click: 1 ```

* API Response - Redirection: The API returns a response with: ``` "acquirer_response_code": 200, "description_short": "Success", "provider_transaction_id": "150255297082", "acquirer_transaction_id": "150255297082", "redirection_url": "https://sandbox-redirect.example.com/?redirection_token=**********", "code": 100, "status": 201000, "authentication_data": { "redirectSecret": "**********" } ```

* Redirection & Enrollment: The buyer is redirected to the provided URL. On the HiPay payment page, the customer selects Bancontact and opts in by checking the enrollment box for the Bancontact Wallet Initiated Payment service.

* Order Summary & SCA: An order summary is displayed for the customer, who then confirms the transaction via Strong Customer Authentication (SCA).

* Transaction Confirmation & Token Notification: Upon confirmation, a notification containing the secure cardtoken is sent to the merchant. This token must be stored securely for use in subsequent transactions.

### Customer Journey - Subsequent Transactions

* Recurring Transaction: The merchant calls the Hipay Order API with the stored cardtoken and additional parameters: ``` eci: 9 recurring_payment: 1 ```

* OneClick Transaction: The merchant calls the Hipay Order API with the stored cardtoken and additional parameters: ``` eci: 7 one_click: 1 ```

* In both cases, the API responds with a SUCCEEDED status and a confirmation is displayed to the customer.

## API Parameters

### Initial Transaction Request

Parameter
Description
Example

payment_product
Payment method to be used
bancontact

email
Customer's email address
[email protected]

description
Transaction description
tx init stage

orderid
Unique order identifier
{{$timestamp}}

amount
Transaction amount
3.00

currency
Currency code
EUR

firstname
Customer's first name
Eric

lastname
Customer's last name
DUPONT

streetaddress
Full street address
2 rue du Paradis

city
City
Bruxelles

zipcode
Postal code
1130

country
Country code
BE

cardtoken
Payment token ( empty for initial transaction )
<empty>

eci
Electronic Commerce Indicator (7 for initial transaction)
7

recurring_payment / one_click
Flag for recurring or one-click payment
1

### Subsequent Transaction Request

Scenario
Additional Parameters

Recurring Transaction

eci: 9

recurring_payment: 1

OneClick Transaction

eci: 7

one_click: 1

### TRANSACTION STATUSES

Status Description

pending Transaction in progress, customer redirected
accepted Payment confirmed by the bank
refused Transaction refused by the bank
cancelled Customer cancelled the transaction
error Technical error

## Best practices

* Set a client-side timeout corresponding to the maximum validation duration (60 min)

* Use server-to-server notifications to track status changes in real time

* Test in the Stage environment before production

* Handle refunds within the allowed 13-month window

* Check error codes and technical messages (general): HiPay Error Messages

## Conclusion

Integrating Bancontact WIP via our API provides a comprehensive solution for secure and efficient payments. Whether it's for the initial enrollment transaction or for subsequent recurring and oneclick transactions, tokenization ensures a seamless and secure checkout experience.

For further assistance or technical inquiries, please consult our Help Center or contact our support team.
