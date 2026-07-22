---
description: "This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Cheque-Vacances"
icon: file-lines
---

# Cheque-Vacances Connect

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/cheque-vacances-connect](https://developer.hipay.com/online-payments/payment-means/cheque-vacances-connect)
{% endhint %}

This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by Cheque-Vacances connect.

Cheques-Vacances Connect Payment Method - HiPay

* This payment method is exclusively dedicated to transactions in France. Cheques-Vacances Connect allows customers to pay for travel and leisure services using their digital holiday voucher balance provided by ANCV. ## PRESENTATION Brand Cheque-Vacances Connect Payment Flow Redirect Integration Hosted Payments / Hosted Page / Hosted Fields / Order API Product Code ancv Country France Currency EUR Minimum amount 0.01 Maximum amount Customer's available balance 3DS No Refund / Partial refund No Cheque-Vacances Connect offers a modern and secure way to pay, redirecting the user to the ANCV application to authorize the payment from their personal account. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY Cheque-Vacances Connect is a widely used payment solution in France for tourism and leisure activities, supported by the national agency ANCV. ### PAYMENT PROCESS Payment is made via redirection to the ANCV platform, where the customer authenticates via their mobile application to validate the transaction. ### SECURITY Transactions with Cheque-Vacances Connect are highly secure, managed directly within the ANCV ecosystem. No sensitive data is stored by the merchant. ### COMPATIBILITY Cheque-Vacances Connect is compatible with all major browsers and requires the customer to have the ANCV mobile application. ### CONFIGURATION AND COMPLIANCE Before integration, ensure your HiPay account is correctly configured. This method only supports transactions in EUR. For more details, please visit the Redirect Pages Requirements . ### USE CASES Ideal for merchants in the tourism, culture, and leisure sectors targeting a French customer base. ## INTEGRATION ### INTEGRATION METHODS Method Description Hosted Payments Managed via HiPay's Hosted Payments solution. Hosted Fields Allows for a customized checkout experience. Hosted Page Uses a pre-designed payment page. Order API Enables direct creation and management of transactions. ### USER EXPERIENCE The customer selects Cheque-Vacances Connect on the merchant site.

* The customer enters their email address of their ANCV account.

* The customer receives a notification on their mobile phone.

* The customer confirms the transaction amount within their ANCV application.

* Instant validation of the transaction.

* A confirmation page is displayed on the merchant site.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

payment_product
ancv

orderid
Unique identifier (e.g., ORDER_1583157210)

description
Brief description (e.g., Hotel Booking)

amount
Total amount (e.g., 125.50)

currency
ISO 4217 code (e.g., EUR)

email
Customer's email address

#### SPECIFIC INPUT PARAMETERS (OPTIONAL BUT RECOMMENDED)

Parameter
Description

firstname
Customer's first name

lastname
Customer's last name

#### SPECIFIC OUTPUT PARAMETERS

Parameter
Description

forward_url
Url to redirect the consumer to the ANCV payment page.

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### Cheques-Vacances Connect Sample request

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencode' \
--header 'Authorization:******' \
--form 'payment_product="ancv"' \
--form 'orderid="1742305004"' \
--form 'description="your description"' \
--form 'amount="55.50"' \
--form 'currency="EUR"' \
--form 'email="[email protected]"' \
--form 'firstname="Jean"' \
--form 'lastname="MARTIN"' \
```
