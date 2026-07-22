---
description: "Overview The Cloud API for standalone payment terminals is an HTTP REST API that forwards incoming payment requests to a standalone POS payment termin"
icon: file-lines
---

# Introduction to the Cloud API for standalone payment terminals

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/smart-terminal/cloud-api-for-standalone-payment-terminals](https://developer.hipay.com/point-of-sale/smart-terminal/cloud-api-for-standalone-payment-terminals)
{% endhint %}

## Overview

The Cloud API for standalone payment terminals is an HTTP REST API that forwards incoming payment requests to a standalone POS payment terminal via the ConcertV3 protocols .

Basically, when the Cloud API receives a payment request, it:
{% stepper %}
{% step %}
## Step 1

contacts the payment terminal
{% endstep %}

{% step %}
## Step 2

waits for the payment processin
{% endstep %}

{% step %}
## Step 3

responds to the payment request initiator with the payment result information
{% endstep %}
{% endstepper %}

The Cloud API works synchronously.
It means that it responds to the request initiator only after a payment response has been received from the payment terminal.

It should be used in the following situations:
- your ECR Software is a SAAS solution
- your payment terminal is connected to Internet via a SIM card

## Processing flow of a payment request

The processing flow of a payment request depends on whether an authorization request is sent to the emitter or not.

WITH authorization request

{% stepper %}
{% step %}
## Step 1

The POS cash register system sends a payment request to Cloud API
{% endstep %}

{% step %}
## Step 2

Cloud API forwards the payment request to the payment terminal referenced in the payment request via its IP address and listening port
{% endstep %}

{% step %}
## Step 3

The payment terminal awakes and displays the payment screen (amount + currency)
{% endstep %}

{% step %}
## Step 4

The customer performs the payment attempt and the payment information are sent to the Preludd payment gateway
{% endstep %}

{% step %}
## Step 5

The Preludd payment gateway processes the payment attempt
{% endstep %}

{% step %}
## Step 6

The Nepting payment gateway sends the authorization request to the acquirer
{% endstep %}

{% step %}
## Step 7

The acquirer forwards the authorization request to the issuer
{% endstep %}

{% step %}
## Step 8

The issuer sends the authorization response to the acquirer
{% endstep %}

{% step %}
## Step 9

The acquirer forwards the authorization response to the Nepting payment gateway
{% endstep %}

{% step %}
## Step 10

The Preludd payment gateway sends the payment response to the payment terminal
{% endstep %}

{% step %}
## Step 11

The transaction is directly stored in the payment terminal
{% endstep %}

{% step %}
## Step 12

The payment terminal sends the payment response to Cloud API
{% endstep %}

{% step %}
## Step 13

Cloud API receives the payment response and forwards it to the POS cash register system
{% endstep %}
{% endstepper %}

Step 2': a notification is automatically sent to the HiPay platform with all the order information provided in the payment request (customer basket, customer information, custom data).

Once the payment attempt processing is done, a push notification is sent by the Preludd payment gateway to HiPay with the authorization request information.

When the HiPay platform receives both notifications (a push notification from Preludd AND the HiPay notification), a process is triggered to create the transaction on HiPay side, to make it available in Console.

Please notice the transactions are automatically created in the Authorized state.

The status will be updated to Captured when the remote collection process will be triggered.

WITHOUT authorization request

{% stepper %}
{% step %}
## Step 1

The POS cash register system sends a payment request to Cloud API
{% endstep %}

{% step %}
## Step 2

Cloud API forwards the payment request to the payment terminal referenced in the payment request via its IP address and listening port
{% endstep %}

{% step %}
## Step 3

The payment terminal awakes and displays the payment screen (amount + currency)
{% endstep %}

{% step %}
## Step 4

The customer performs the payment attempt
{% endstep %}

{% step %}
## Step 5

The transaction is directly stored in the payment terminal
{% endstep %}

{% step %}
## Step 6

The payment terminal sends the payment response to Cloud API
{% endstep %}

{% step %}
## Step 7

Cloud API receives the payment response and forwards it to the POS cash register system
{% endstep %}
{% endstepper %}

Step 2': a notification is automatically sent to the HiPay platform with all the order information provided in the payment request (customer basket, customer information, custom data).

Please notice in this situation without authorization request, the transactions are not created on HiPay side, which means they are not available in Console. This is because, at this state, HiPay did not receive any payment information, which is a prerequisite to any transaction creation.

The transactions will be created to the Captured state when the remote collection process will be triggered.

## Processing flow of a remote collection

{% stepper %}
{% step %}
## Step 1

The POS payment terminal triggers the remote collection process to the Preludd payment gateway
{% endstep %}

{% step %}
## Step 2

The Preludd payment gateway forwards the remote collection data to the acquirer
{% endstep %}

{% step %}
## Step 3

The acquirer acknowledges the remote collection data
{% endstep %}

{% step %}
## Step 4

The Preludd payment gateway sends the remote collection data to Hipay via a push notification
{% endstep %}

{% step %}
## Step 5

The HiPay platform acknowledges the notification
{% endstep %}

{% step %}
## Step 6

The HiPay platform creates or updates the transaction (in case an authorization notification was previously received)
{% endstep %}

{% step %}
## Step 7

[Optional] The HiPay platform sends a server-to-server notification to the POS merchant Information System
{% endstep %}

{% step %}
## Step 8

[Optional] The merchant Information System acknowledges
{% endstep %}
{% endstepper %}

To get more details about the server-to-server notifications, please consult the dedicated page .

## Features

FEATURE
DETAILS

Operation types
- Debit
- Debit reversal
- Credit

CURRENCIES
- Euro

AUTHORIZATION REQUEST
- Always
- Only in standard cases

DATA HANDLED
- Customer basket: the detailed list of the products that are part of the customer basket
- Customer information: id, email, phone, first name, last name
- Custom data: any data of your choice

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Cloud API for Nepting:

REQUIREMENT
DESCRIPTION

POS payment terminal
A payment terminal supporting Concert protocol version 3.1 or 3.2 (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable Internet (Wi-Fi) connection
- A fixed public IP address for the network router is needed to join the payment terminal. In case your public IP address changes over time, it is usually possible to fix it by contacting your Internet access provider (please notice additional costs may be applied)

Security
Private API credentials enabled (please consult this page to get details about HiPay credentials).

## Documentation

- API description (swagger)
