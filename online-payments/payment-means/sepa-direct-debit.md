---
description: "This payment mean can be used with the HiPay Enterprise Gateway API . Recurring payment Request To initiate a new SEPA mandate that will be used for f"
icon: file-lines
---

# SEPA Direct Debit

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/sepa-direct-debit](https://developer.hipay.com/online-payments/payment-means/sepa-direct-debit)
{% endhint %}

This payment mean can be used with the HiPay Enterprise Gateway API .

## Recurring payment

### Request

To initiate a new SEPA mandate that will be used for future recurring payments you must add the following parameters to a basic payment request:

The bank account owner must be present to complete the SEPA registration.

Specific required fields if your are using order API : (bank info fields in your page)

Parameter name

Value

payment_product

sdd

eci

7 (e-commerce)

recurring_payment

1

iban

Iban

firstname

First name

lastname

Last name

Specific required fields if your are using hpayment API : (bank info fields in HiPay hosted page)

Parameter name

Value

payment_product

sdd

eci

7 (e-commerce)

recurring_payment

1

### Response

See below the received response. Please pay attention to the field debit_agreement_id, which is the most important here. Merchants must save its value to make new recurring transactions on the same mandate. In case of Hpayment (HiPay hosted page), this value is sent in the Authorization requested notification and not in the API response.

Response in XML format using order API

XML

XML

```

completed

false
00001328877
1

132256656670
142
Authorization Requested
. . .

18505
available

```

Response in XML format using hpayment API

XML

XML

```

https://stage-secure-gateway.hipay-tpp.com/payment/web/pay/12...55
true
00001328877
. . .

5630ccbe32951
2016-10-28T13:30:47+0000
0
113.25
4.50
0.50
2
EUR
test
fr_FR
[email protected]

```

The merchant will redirect the customer to the HiPay payment page to complete the registration, as shown here.

After completing the registration, the customer is redirected to the success page specified by the merchant in the initial payment request (or to the error page in case of failure).

The transaction status will change to Authenticated, then to Authorization requested. A few days later (approximately 10 bank working days for a first transaction and 5 bank working days for a recurring transaction), the transaction status will change from Authorization requested to Captured directly (due to the lack of information about the status change between the transmission and the receipt of the payment).

Notification response in XML format

XML

XML

```

completed

true
00001328877
1

730844386388
. . .

599
available

```

## Existing mandate

Initiating a transaction on an existing mandate

When a merchant wants to make a payment on an existing mandate, the bank account owner doesn't need to be present.

To proceed, the merchant has to send the value of the aforementioned field debit_agreement_id to HiPay.

Specific required fields

Parameter name

Value

payment_product

sdd

eci

9 (recurring e-commerce)

debit_agreement_id

574 (example)

recurring_payment

1

### Response

See below the received response. This time, the transaction status is set to Authorization requested directly, as a confirmation is not required to make another payment on an existing mandate.

XML

XML

```

pending

false
00035167042
1

937783482019

2016-10-05T16:40:21+0000
2016-10-05T16:40:29+0000

142
Authorization Requested
. . .

574
available

```

## Debit agreement statuses

Status

Description

pending

Created but not yet confirmed

available

Agreement correctly created

terminated

The agreement is no longer available

suspended

The agreement was suspended by the customer

error

An error occurred on agreement creation

## Mandate without transaction

This is intended for merchants who want to create a debit agreement without any first payment for further recurring payments.

Endpoint

Production : https://secure-gateway.hipay-tpp.com/rest/v2/debit-agreement

Specific required fields

Parameter name

Value/Example value/info

payment_product

sdd

currency

EUR

iban

DE23100000001234567890 (this is an example)

issuer_bank_id

MARKDEF1100 (this is an example)

bank_name

World bank (this is an example)

gender

F / M

firstname

First name

lastname

Last name

authentication_indicator

0

agreement_reference

4465545 (this field is not mandatory; it is used to import an old mandate reference)

At this point, the merchant can initiate an SDD transaction with the given debit agreement.

XML

XML

```

0

992

```
