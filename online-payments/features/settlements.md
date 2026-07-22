---
description: "Settlement file transfer In order to notify financial events related to your payment system, such as a new settlement file created, the HiPay Enterpri"
icon: file-lines
---

# Settlements

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/features/settlements](https://developer.hipay.com/online-payments/features/settlements)
{% endhint %}

## Settlement file transfer

In order to notify financial events related to your payment system, such as a new settlement file created, the HiPay Enterprise platform can send your application a settlement file by FTP/SFTP.

To set up your financial file transfer system, you must login into your HiPay Enterprise back office and go to Integration -> File Transfer.

Configuration parameters

Field name

Description

File Server

Hostname or IP address on which you want to receive your files

Path

Path where the file will be submitted

Server Type

Type of server you will use: FTP / SFTP

Username

Username to log into your server

Password

Password to log into your server

Desired files

Files you want to receive

Settlement file data

To get a list of fields included in settlement files, please refer to the HiPay Enterprise Finance API .

Settlement file fields

The following table lists and describes all the fields included in each settlement file.

Field name

Description

Account

HiPay's account number

Account name

HiPay's account name

Date

Date of collection

Date value

Acquirers' value date

Invoice reference

HiPay's invoice reference

Settlement ID

Settlement ID

Transaction ID

HiPay's transaction ID

Order

Unique identifier of the order as provided by the merchant

Product name

Payment method

Invoiced

Invoiced transaction (0/1)

Settled

Settled transaction (0/1)

Original amount

Original amount of the operation

Original currency

Original currency of the operation

Amount (Excl. Tax)

Amount of the operation excluding taxes

Tax amount

Tax amount of the operation

Amount (Incl. Tax)

Amount of the operation including taxes

Currency

Invoice currency

Operation

Operation type. Please refer to Operation types below.

Settled amount

Settled amount

Settlement currency

Settlement currency

Original settlement ID

Original settlement ID (if applicable)

Customer ID

Unique identifier of the customer as provided by the merchant

Merchant operation ID

Operation ID sent in maintenance operation

Reporting data 1

Settlement custom data 1

Reporting data 2

Settlement custom data 2

Reporting data 3

Settlement custom data 3

Reporting data 4

Settlement custom data 4

Reporting data 5

Settlement custom data 5

Collect Mode

Transaction collect mode

Transfer

Settlement transfer date

Operation date

Date of operation request

## Operation types

Here are the different operation types that can appear on a list of operations.

Operation type

Description

Adjustment in favor of merchant

Amount credited on the merchant's balance (E.g.: adjustment of commission billing errors, commercial incentives)

Adjustment in favor of TPP

Amount deducted from the merchant's balance (E.g.: adjustment for fees not charged)

Already settled

Statement of an amount already paid by HiPay to the merchant

Asset settlement

Operation following a negative balance, indicating that it has been paid off on the merchant's account

Chargeback

Credit/debit card charge paid by the merchant to a customer after he/she successfully disputed an item on his/her bank statement

Chargeback refund

Amount of a chargeback credited back to the merchant after giving evidence that the product or service was duly delivered

Deferred settlement

Settlement file issued in case the merchant's HiPay Enterprise account shows a negative balance

Fixed fee

Commission charged on transactions when collecting amounts

Fixed reserve capture

Amount transferred by the merchant or debited from the merchant's balance and withheld for protection against potential risks

Fixed reserve release

Fixed reserve amount released back to the merchant 180 days after its capture

IFF (Fraud Financial Impact)

Fraudulent blocked transactions fee on the Carte Bancaire's network paid by the merchant

Invoice carry-over (formerly Invoice asset)

Operation created to transfer the merchant's remaining invoice amount to the next billing cycle

Invoice to be paid by TPP

Not applicable (old status)

Invoice payment

Not applicable (old status)

Deferred invoice (formerly Invoice report)

Invoice deferred, in whole or in part, to the next billing cycle

Offsetting entry (formerly Merchant's balance credit)

Entry on a balance sheet that sets another entry to zero. Does not impact billing.

Monthly fee

Fee charged every month

Refund

Reimbursement of a transaction

Rolling reserve capture

Amount withdrawn from every payout and withheld for protection against potential risks

Rolling reserve release

Amount released back to the merchant after being held for 180 days

Sale

Sale or transaction amount

Settlement

Payout amount on D-day

Setup fee

Fee for the implementation of the project and account. It is billed on the first HiPay Enterprise invoice.

Split settlement

Amount to be paid out on a specific bank account when allocating payouts among several bank accounts

Splitting settlement

Total amount to be paid out when allocating payouts among several bank accounts

Transferred from merchant

Transfer sent from a HiPay Enterprise account to another HiPay Enterprise account (between accounts of a same merchant). This operation is displayed on the sending account's operations.

Transferred to merchant

Transfer sent from a HiPay Enterprise account to another HiPay Enterprise account (between accounts of a same merchant). This operation is displayed on the receiving account's operations.

Variable

Commission based on a percentage and calculated on amounts collected on the HiPay Enterprise account.

## Settlement notifications

This document is designed to provide you with details on how to integrate your business to the HiPay Enterprise Financial Gateway Notifications. It gives step-by-step instructions on how to simply and quickly get up and running with our services as well as detailed reference material.

In order to notify financial events related to your payment system, such as a new settlement file created, the HiPay Enterprise platform can send your application a server-to-server notification.

Setup

Procedure To set up your Financial Feedback Notification URL, you must login into your HiPay Enterprise back office and go to Integration -> Notifications -> Financial Feedback .

Configuration parameters

Field name

Description

Notification URL

URL or IP address on which you want to receive financial server-to-server notifications

Request method

Method used to send you requests: XML / JSON / HTTP POST

Hash algorithm

Algorithm used to hash the password that will sign all sent notifications

Password

Password used to generate a unique character string (signature) hashed with the defined algorithm. The security level of the password depends on its length. A long password is more secure.

Desired notifications

Financial notifications you want to receive

Response fields

Field name

Description

notification_type

Type of notification (only in POST request)

account

Account ID

reference

Settlement ID

sales

Sales amount

refunds

Refunds amount

fees

Fees amount

chargeback

Chargebacks amount

rolling

Rolling reserve amount

other

Other amount

amount

Settlement amount

currency

Settlement currency

Examples

XML
JSON
HTTP

XML

```

987654
123456
2839.000
0
90.040
0
0
0
0
2748.040

```

JSON

```
{
"settlement":{
"account":"987654",
"reference":"123456",
"sales":2839,
"refunds":0,
"fees":90.040,
"chargeback":0,
"rolling":0,
"other":0,
"amount":2748.040,
"currency":"EUR"
}
}
```

HTTP

```
notification_type=settlement&account=987654&reference=123456&sales=2839&refunds=0&fees=90&chargeback=0&rolling=0&other=2748.040&amount=0.000cy=EUR
```
