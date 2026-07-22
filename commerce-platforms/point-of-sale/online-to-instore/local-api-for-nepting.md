---
description: "The Local API for Nepting allows you to trigger in-store payments via the Nepting payment gateway simply by sending a payment request to a specific PO"
icon: file-lines
---

# Introduction to the Local API for Nepting

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/online-to-instore/local-api-for-nepting](https://developer.hipay.com/point-of-sale/online-to-instore/local-api-for-nepting)
{% endhint %}

The Local API for Nepting allows you to trigger in-store payments via the Nepting payment gateway simply by sending a payment request to a specific POS payment terminal located in the same LAN (Local Area Network) .

It has been designed to deal with dead zone scenarios : situations where the POS payment terminal has no or bad Internet access, but a LAN connection shared by the payment initiator (a cash register system installed on a tablet or smartphone).

It is also intended for scenarios where the sales assistants in the store offer nomad payments to their customers via a payment terminal associated with a tablet .

Contrary to the Cloud API, Internet access is not required (but a network access is) to join the POS payment terminal, because there will be no intermediate between the request initiator and the POS payment terminal.

Basically, when the Local API receives a payment request, it:
1. awakes the payment terminal
2. waits for the payment processing
3. responds to the payment request initiator with the payment result information

## Processing flow of a payment request

The processing flow of a payment request depends on whether an authorization request is sent to the emitter or not.

WITH authorization request

1. The POS cash register system sends a payment request to Local API
2. Local API awakes the payment terminal and displays the payment screen (amount + currency)
3. The customer performs the payment attempt and the payment information (card information) are sent to the Nepting payment gateway
4. The Nepting payment gateway processes the payment attempt
5. The Nepting payment gateway sends the authorization request to the acquirer
6. The acquirer forwards the authorization request to the issuer
7. The issuer sends the authorization response to the acquirer
8. The acquirer forwards the authorization response to the Nepting payment gateway
9. The Nepting payment gateway stores the transaction in its server database
10. The Nepting payment gateway sends the payment response to the payment terminal
11. Local API receives the payment response and forwards it to the payment request initiator

Step 2': a notification is automatically sent to the HiPay platform with all the order information provided in the payment request (customer basket, customer information, custom data).

Once the payment attempt processing is done, an Instant Payment Notification (IPN) is sent by the Nepting payment gateway to HiPay.
When the HiPay platform receives an IPN from Nepting, a process is triggered to create the transaction on HiPay side.
It is only once this notification has been processed that the transaction is available in Console.

NB1: the transactions are automatically created in the Captured state .
NB2: To get more details about the server-to-server notifications, please consult the dedicated page .

WITHOUT authorization request

1. The POS cash register system sends a payment request to Local API
2. Local API awakes the payment terminal and displays the payment screen (amount + currency)
3. The customer performs the payment attempt and the payment information (card information) are sent to the Nepting payment gateway
4. The Nepting payment gateway processes the payment attempt
5. The Nepting payment gateway stores the transaction in its server database
6. The Nepting payment gateway sends the payment response to the payment terminal
7. Local API receives the payment response and forwards it to the payment request initiator

Once the payment attempt processing is done, an Instant Payment Notification (IPN) is sent by the Nepting payment gateway to HiPay.
When the HiPay platform receives an IPN from Nepting, a process is triggered to create the transaction on HiPay side.
It is only once this notification has been processed that the transaction is available in Console.

NB1: the transactions are automatically created in the Captured state .
NB2: To get more details about the server-to-server notifications, please consult the dedicated page .

## Features

FEATURE
DETAILS

Operation types
- Debit
- Credit

CURRENCIES
- Euro

AUTHORIZATION REQUEST
- Always
- Only in standard cases

DATA HANDLED
- Custom data: any data of your choice, with a maximum of 67 characters

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Local API for Nepting:

REQUIREMENT
DESCRIPTION

POS payment terminal
An Android POS payment terminal (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable LAN or wifi network connection in the store between the ECR and the terminal
- A fixed IP address
- The last version of the Nepting Android app installed
- The last version of the HiPay POS Android app installed
- The Local API service enabled

## Documentation

- API description
