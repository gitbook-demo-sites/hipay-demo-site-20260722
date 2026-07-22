---
description: "iDEAL Payment Method - HiPay This payment method is exclusively dedicated to transactions in the Netherlands. iDEAL is the most popular online payment"
icon: file-lines
---

# iDEAL 2.0

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/ideal](https://developer.hipay.com/online-payments/payment-means/ideal)
{% endhint %}

iDEAL Payment Method - HiPay

* This payment method is exclusively dedicated to transactions in the Netherlands. iDEAL is the most popular online payment method in the Netherlands, enabling customers to pay directly through their own bank. ## PRESENTATION Brand iDEAL Payment Flow Redirect Integration Hosted Payments / Hosted Page / Hosted Fields / Order API Product Code ideal Country Netherlands Currency EUR Minimum amount 0.01 Maximum amount Set by the customer's bank 3DS Yes Refund / Partial refund Yes iDEAL provides a trusted and secure online payment method by redirecting customers to their online banking environment. It is supported by all major Dutch banks. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY iDEAL is the leading online payment method in the Netherlands, widely used and trusted by Dutch consumers. ### PAYMENT PROCESS Payment is made via redirection to the customer's online banking interface, where they can authorize the payment directly. ### SECURITY iDEAL transactions are processed within the secure environment of the customer's bank, complying with PCI-DSS standards. No sensitive banking data is stored by the merchant. ### COMPATIBILITY iDEAL is compatible with all major browsers and mobile devices. ### CONFIGURATION AND COMPLIANCE Before integration, ensure that your HiPay account is correctly configured and that the redirection URLs are properly set. Only transactions in EUR are supported. For more details, please visit the Redirect Pages Requirements . ### USE CASES Ideal for instant and secure payments, iDEAL is perfectly suited for merchant sites targeting a Dutch customer base. ## INTEGRATION ### INTEGRATION METHODS Method Description Hosted Payments Managed via HiPay's Hosted Payments solution. Hosted Fields Allows for a customized checkout experience. Hosted Page Uses a pre-designed payment page. Order API Enables direct creation and management of transactions. ### USER EXPERIENCE The customer selects iDEAL on the merchant site.

* Redirection to the customer's online banking interface.

* The customer authenticates and authorizes the payment within their banking environment.

* Instant validation of the transaction.

* A confirmation page is displayed on the merchant site.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

payment_product
ideal

orderid
Unique identifier (e.g., ORDER_1583157210)

description
Brief description (e.g., Summer Sale)

amount
Total amount (e.g., 99.99)

currency
ISO 4217 code (e.g., EUR)

firstname
Customer's first name

lastname
Customer's last name

country
Customer's country (e.g., NL)

#### SPECIFIC INPUT PARAMETERS (OPTIONAL BUT RECOMMENDED)

Parameter
Description

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
Url to redirect the consumer to their bank.

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### iDEAL Sample request

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencode' \
--header 'Authorization:******' \
--form 'payment_product="ideal"' \
--form 'orderid="1742305003"' \
--form 'description="your description"' \
--form 'amount="3.00"' \
--form 'currency="EUR"' \
--form 'firstname="Eric"' \
--form 'lastname="DUPONT"' \
--form 'email="[email protected]"' \
--form 'streetaddress="2 rue du Test"' \
--form 'city="Amsterdam"' \
--form 'zipcode="1011AB"'\
--form 'country="NL"'
```
