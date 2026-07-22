---
description: "MyBank Payment Method - HiPay MyBank is a European-wide payment solution that allows customers to pay via their online banking. It's a bank transfer-b"
icon: file-lines
---

# MyBank

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/mybank](https://developer.hipay.com/online-payments/payment-means/mybank)
{% endhint %}

MyBank Payment Method - HiPay

* MyBank is a European-wide payment solution that allows customers to pay via their online banking. It's a bank transfer-based method, offering secure and immediate transactions without the need for cards. MyBank connects the customer's bank account directly to the merchant's, ensuring a streamlined payment process. ## PRESENTATION Brand MyBank Payment Flow Redirect (Bank Transfer) Integration Hosted Payments / Hosted Fields / Hosted Page / Order API Product Code mybank Country Italy, Belgium, Spain, Portugal Currency EUR Minimum amount 0.01 Maximum amount No limit (Based on bank limits) 3DS Yes (if required by the bank) Refund / Partial refund Yes MyBank facilitates secure online bank transfers. When a customer chooses MyBank, they are redirected to their own online banking portal, where they log in and authorize the payment. The transaction details are pre-filled, reducing the risk of errors. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY MyBank is widely used across Europe, particularly in Italy, and is supported by a growing number of banks across the continent. It is a preferred method for customers who prioritize security and prefer not to use credit cards online. ### PAYMENT PROCESS The payment process involves a redirection to the customer's online banking environment. The customer authenticates the transaction directly with their bank, providing an extra layer of security. ### SECURITY MyBank transactions are highly secure, leveraging the existing security infrastructure of the customer's bank. No sensitive banking details are shared with the merchant. MyBank complies with all relevant European security regulations. ### COMPATIBILITY MyBank is compatible with all major browsers and devices that support online banking access. ### CONFIGURATION AND COMPLIANCE Ensure your HiPay account is configured for MyBank and that the redirection URLs are correctly set up. Only EUR transactions are supported. Refer to the Redirect Pages Requirements for more details. ### USE CASES MyBank is ideal for merchants targeting European customers who prefer bank transfers. It's suitable for all types of online businesses, particularly those selling higher-value goods or services where security is paramount. ## INTEGRATION ### INTEGRATION METHODS Method Description Hosted Payments Managed via HiPay's Hosted Payments solution. Hosted Fields Allows for a customized checkout experience. Hosted Page Uses a pre-designed payment page. Order API Enables direct creation and management of transactions. ### USER EXPERIENCE The customer selects MyBank on the merchant site.

* The customer is redirected to the MyBank selection page where they choose their bank.

* The customer is then redirected to their online banking portal.

* The customer logs in and authorizes the pre-filled payment details.

* Instant validation of the transaction.

* A confirmation page is displayed on the merchant site.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

payment_product
mybank

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
Customer's country (e.g., IT, FR, ES, etc.)

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
Url to redirect the consumer to the MyBank portal.

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### MyBank SAMPLE REQUEST

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order'
--header 'Content-Type: application/x-www-form-urlencode'
--header 'Authorization:******'
--form 'payment_product="mybank"'
--form 'orderid="1742305002"'
--form 'description="your description"'
--form 'amount="3.00"'
--form 'currency="EUR"'
--form 'firstname="Eric"'
--form 'lastname="DUPONT"'
--form 'email="[email protected]"'
--form 'streetaddress="2 rue du Test"'
--form 'city="Rome"'
--form 'zipcode="00100"'
--form 'country="IT"'
```
