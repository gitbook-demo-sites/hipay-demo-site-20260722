---
description: "The ECI indicates the security level at which the payment information is processed between the cardholder and the merchant. The table below lists all "
icon: file-lines
---

# Electronic Commerce Indicator

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/essentials/eci](https://developer.hipay.com/payment-fundamentals/essentials/eci)
{% endhint %}

The ECI indicates the security level at which the payment information is processed between the cardholder and the merchant.

The table below lists all the available Electronic Commerce Indicators as they are supposed to be sent along with each authorization request.

ECI

Name

Description

1

MO/TO (Mail Order/Telephone Order)

The merchant received the customer's financial details over the phone or via fax/mail, but does not have the customer's card at hand.

2

Recurring MO/TO

The first transaction of the customer was a Mail Order / Telephone Order transaction (financial details were given to the merchant over the phone or via mail/fax). These details are either stored by the merchant or stored in our system in order to use an alias to make recurring transactions for the same customer.

3

Installment Payment

Partial payment for goods/services that have already been delivered but that will be paid for in several spread payments.

4

Manually Keyed (Card Present)

The customer is physically present in front of the merchant. The merchant has the customer's card within easy reach. The card details are manually entered; the card is not swiped through a machine.

7

Secure E-commerce with SSL/TLS Encryption

The payment transaction was conducted over a secure e-commerce channel (e.g.: TLS).

9

Recurring E-commerce

The first transaction of the customer was an e-commerce transaction; which means that financial details were entered by the customer on a secure website (either the merchant's website or our secure platform). These details are either stored by the merchant or stored in our system in order to use an alias to make recurring transactions for the same customer.

10

Point of sale payment

Payment processed in a physical store, generally from a payment terminal.
