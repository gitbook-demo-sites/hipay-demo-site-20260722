---
description: "Bancontact Payment Method - HiPay This payment method is exclusively dedicated to transactions in Belgium. Very popular among Belgian consumers, Banco"
icon: file-lines
---

# Bancontact

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/bancontact](https://developer.hipay.com/online-payments/payment-means/bancontact)
{% endhint %}

Bancontact Payment Method - HiPay

* This payment method is exclusively dedicated to transactions in Belgium. Very popular among Belgian consumers, Bancontact enables secure payments either by redirection to the banking interface or via a QR Code for a streamlined mobile experience. ## PRESENTATION Brand Bancontact Payment Flow Redirect / QR Code Integration Hosted Payments / Hosted Fields / Hosted Page / Order API Product Code bancontact & bancontactqrcode Country Belgium Currency EUR Minimum amount 0.01 Maximum amount No limit for standard transactions / 1500.00 EUR for mobile QR Code payments 3DS Yes Refund / Partial refund Yes Bancontact offers two products: the classic version with redirection and the QR Code version. While the standard method redirects the customer to their banking interface, the QR Code solution generates a scannable code optimized for mobile payments, offering a quick and contactless process. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY Bancontact is the most widely used payment solution in Belgium, massively adopted for its speed and security. The QR Code version, in particular, meets the needs of mobile and in-store transactions. ### PAYMENT PROCESS For the classic version, payment is made via redirection to the banking interface. With Bancontact QR Code, a unique code is generated and displayed for the customer to scan with their banking app to complete the transaction. ### SECURITY Both products comply with PCI-DSS standards and do not store any banking data with the merchant, ensuring the protection of sensitive information. ### COMPATIBILITY Both Bancontact and Bancontact QR Code are compatible with most browsers and mobile devices, ensuring an optimal user experience across all platforms. ### CONFIGURATION AND COMPLIANCE Before integration, ensure that your HiPay account is correctly configured and that the redirection URLs are properly set. Only transactions in EUR are supported. For more details, please visit the Redirect Pages Requirements . ### USE CASES Ideal for instant and secure payments, Bancontact is perfectly suited for merchant sites targeting a Belgian customer base. The QR Code solution is especially useful for mobile and in-store payments. ### QR CODE EXPERIENCE The Bancontact QR Code solution allows users to complete their payments by simply scanning a code displayed on the website or in-store. This mode promotes a fast and seamless process while maintaining high security standards. ## INTEGRATION ### INTEGRATION METHODS Method Description Hosted Payments Managed via HiPay's Hosted Payments solution. Hosted Fields Allows for a customized checkout experience. Hosted Page Uses a pre-designed payment page. Order API Enables direct creation and management of transactions. ### USER EXPERIENCE The customer selects Bancontact or Bancontact QR Code on the merchant site.

* For the classic version: redirection to the banking interface. For the QR Code version: generation and display of a scannable code.

* In the classic version, the customer authenticates directly on the banking interface. In the QR Code version, the customer scans the code using their banking app.

* Instant validation of the transaction.

* A confirmation page is displayed on the merchant site.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

payment_product
bancontact / bancontactqrcode

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

country
Customer's country (e.g., BE)

#### SPECIFIC OUTPUT PARAMETERS

Parameter
Description

forward_url
Classic: Url to redirect the consumer

QR Code: Url with Qr Code to display to customer

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration for both the classic and the QR Code versions.

#### BANCONTACT SAMPLE REQUEST

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencode' \
--header 'Authorization:******' \
--form 'payment_product="bancontact"' \
--form 'orderid="1742305002"' \
--form 'description="your description"' \
--form 'amount="3.00"' \
--form 'currency="EUR"' \
--form 'firstname="Eric"' \
--form 'lastname="DUPONT"' \
--form 'email="[email protected]"' \
--form 'streetaddress="2 rue du Test"' \
--form 'city="Bruxelles"' \
--form 'zipcode="1130"'\
--form 'country="BE"'
```
