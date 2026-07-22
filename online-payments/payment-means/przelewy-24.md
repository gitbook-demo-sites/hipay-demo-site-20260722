---
description: "Przelewy24 Payment Method - HiPay This payment method is exclusively dedicated to transactions in Poland. Przelewy24 is a very popular payment method "
icon: file-lines
---

# Przelewy 24

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/przelewy-24](https://developer.hipay.com/online-payments/payment-means/przelewy-24)
{% endhint %}

Przelewy24 Payment Method - HiPay

* This payment method is exclusively dedicated to transactions in Poland. Przelewy24 is a very popular payment method among Polish consumers, enabling secure payments via redirection to the user's online banking interface. ## PRESENTATION Brand Przelewy24 Payment Flow Redirect Integration Hosted Payments / Hosted Fields / Hosted Page / Order API Product Code przelewy24 Country Poland Currency PLN, EUR Minimum amount 1.00 PLN Maximum amount 55 000.00 PLN 3DS Yes (if required by the bank) Refund / Partial refund Yes Przelewy24 is a Polish online payment method that redirects customers to their online banking portal to complete payments securely. It supports a wide range of Polish banks. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY Przelewy24 is one of the most popular online payment methods in Poland, widely used and trusted by Polish consumers. It offers a comprehensive solution for online payments, supporting numerous Polish banks. ### PAYMENT PROCESS The payment process involves redirecting the customer to their bank's online banking interface, where they authorize the payment directly. This ensures a high level of security and familiarity for the user. ### SECURITY Przelewy24 adheres to high security standards. Transactions are processed through the secure banking environment of the user's chosen bank, ensuring data protection and minimizing the risk of fraud. PCI-DSS compliance is maintained. ### COMPATIBILITY Przelewy24 is compatible with all major web browsers and mobile devices, ensuring a consistent user experience across different platforms. ### CONFIGURATION AND COMPLIANCE Before integration, ensure your HiPay account is correctly configured and the redirection URLs are properly set. Transactions are typically supported in PLN. For more details, please visit the Redirect Pages Requirements . ### USE CASES Ideal for businesses targeting the Polish market, Przelewy24 is suitable for e-commerce, online services, and any business requiring secure online payments from Polish customers. ## INTEGRATION ### INTEGRATION METHODS Method Description Hosted Payments Managed via HiPay's Hosted Payments solution. Hosted Fields Allows for a customized checkout experience. Hosted Page Uses a pre-designed payment page. Order API Enables direct creation and management of transactions. ### USER EXPERIENCE The customer selects Przelewy24 on the merchant site.

* The customer is redirected to the Przelewy24 gateway.

* The customer selects their bank from the list provided by Przelewy24.

* The customer is redirected to their bank's online banking login page.

* The customer logs in and authorizes the payment.

* The customer is redirected back to the merchant's site.

* A confirmation page is displayed on the merchant site.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

payment_product
przelewy24

orderid
Unique identifier (e.g., ORDER_1583157211)

description
Brief description (e.g., Summer Sale)

amount
Total amount (e.g., 99.99)

currency
ISO 4217 code (e.g., PLN or EUR)

email
Customer's email address

#### SPECIFIC INPUT PARAMETERS (OPTIONAL BUT RECOMMENDED)

Parameter
Description

firstname
Customer's first name

lastname
Customer's last name

country
Customer's country (e.g., PL)

#### SPECIFIC OUTPUT PARAMETERS

Parameter
Description

forward_url
URL to redirect the consumer to the Przelewy24 payment gateway.

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### PRZELEWY24 SAMPLE REQUEST

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Authorization:*****' \
--form 'payment_product="przelewy24"' \
--form 'orderid="1742308765"' \
--form 'description="description P24"' \
--form 'amount="1000"' \
--form 'currency="PLN"' \
--form 'email="[email protected]"' \
--form 'firstname="John"' \
--form 'lastname="Doe"' \
--form 'country="PL"'
```
