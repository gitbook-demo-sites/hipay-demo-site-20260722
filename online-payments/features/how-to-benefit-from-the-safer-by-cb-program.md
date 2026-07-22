---
description: "March 26, 2025 What is Safe'R by CB? Safe'r by CB is a program that offers a frictionless and secure payment journey without customer authentication o"
icon: file-lines
---

# How to Benefit from the Safe'R by CB Program?

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/features/how-to-benefit-from-the-safer-by-cb-program](https://developer.hipay.com/online-payments/features/how-to-benefit-from-the-safer-by-cb-program)
{% endhint %}

March 26, 2025

### What is Safe'R by CB?

Safe'r by CB is a program that offers a frictionless and secure payment journey without customer authentication on e-commerce sites. The program offers eligible e-merchants exemptions from strong customer authentication for CIT up to 250, excluding subscriptions and recurring payments.

### Why Join Safe'R by CB?

By joining Safe'R by CB, e-merchants can take advantage of several benefits:
Enhanced transaction security with strict compliance requirements.
Optimized payment success rates , reducing fraud-related declines.
Improved customer experience with smoother and better-targeted authentication.

### Eligibility Criteria

The Safe'R by CB program is divided into two levels , depending on the transaction amount:

Prerequisites For CB payments up to 100 For CB payments between 100 and 250 Transaction volume +120,000 CIT transactions per year on Fast'R by CB Same Monthly fraud rate 1 < 0.11% over 4 full months, within the last 6 months < 0.05% each month Eligibility for Acquirer TRA Not required Required Required data in the 3D Secure protocol 2 IP address + 3 data points IP address + 3 data points

1 The fraud rate is calculated using the amounts reported by issuers and cardholders, considering the transaction date. CB reviews the overall fraud rate to assess a merchant's eligibility, without providing specific details in cases of multi-acquisition/PSPs .

2 These data must have a significant value and must be shared in at least 80% of the monthly activity in the transaction flows

### Mandatory Data to Provide

To be eligible, each e-merchant must provide specific information via the 3D Secure protocol:

#### 1. Customer IP Address

Field Description Expected Format brower_info
{
ipaddr:
} Customer's ipaddress IPv4 or IPv6

#### 2. Three Data Points from the Following List :

Field Description Expected Format email Customer's email address String (max 254 characters ) - Compliant with IETF RFC 5322 phone Home or mobile phone number String (max 15 characters )
Format E.123, international notation without spaces
e.g. +33212345678
zipcode Postal code of the billing address String (max 16 characters ) streetaddress First line of the billing address String (max 50 characters ) shipto_zipcode Postal code of the shipping address String (max 16 characters ) shipto_streetaddress First line of the shipping address String (max 50 characters ) Merchant_risk_statement {
shipping_indicator :
} Shipping method chosen for the transaction String (12 character) - Accepted values: 1 to 7
e.g :
1 = Ship to cardholder's billing address
2 = Ship to another verified address on file with merchant
3 = Ship to address that is different than cardholder's billing address
4 = Ship to Store / Pick up at local store (Store address shall be populated in shipping address fields)
5 = Digital goods (includes online services, electronic gift cards and redemption codes)
6 = Travel and Event tickets, not shipped
7 = Other (for example, Gaming, digital services not shipped, emedia subscriptions, etc.) account _ info
{
address_usage_duration :
} How long the customer account has existed with the merchant String (1 character) - Accepted values: 1 to 5
e.g.
1 = No account (guest check-out)
2 = Created during this transaction
3 = Less than 30 days
4 = 30-60 days
5 = More than 60 days

### How to Enroll?

The e-merchant or their PSP must request enrollment through their CB-acquiring bank . Once approved, the program applies to all CB payments processed by the merchant.

### Program Exit Conditions

A merchant loses the benefit of the Safe'R by CB programme if its fraud rate exceeds the thresholds required by CB and/or if it does not submit the data expected by CB.
