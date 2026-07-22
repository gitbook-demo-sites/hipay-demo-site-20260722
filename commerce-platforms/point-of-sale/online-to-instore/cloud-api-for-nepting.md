---
description: "Overview The Cloud API for Nepting is an HTTP REST API that forwards incoming payment requests to a POS payment terminal . Basically, when the Cloud A"
icon: file-lines
---

# Introduction to the Cloud API for Nepting

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/online-to-instore/cloud-api-for-nepting](https://developer.hipay.com/point-of-sale/online-to-instore/cloud-api-for-nepting)
{% endhint %}

## Overview

The Cloud API for Nepting is an HTTP REST API that forwards incoming payment requests to a POS payment terminal .

Basically, when the Cloud API receives a payment request, it:
{% stepper %}
{% step %}
## Step 1

contacts the payment terminal
{% endstep %}

{% step %}
## Step 2

waits for the payment processing
{% endstep %}

{% step %}
## Step 3

responds to the payment request initiator with th payment result information
{% endstep %}
{% endstepper %}

The Cloud API works synchronously.
It means that it responds to the request initiator only after a payment response has been received from the payment terminal, or in case the payment terminal can't be joined.

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

Cloud API forwards the payment request to the payment terminal referenced in the payment request via its serial number and its manufacturer's name
{% endstep %}

{% step %}
## Step 3

The payment terminal awakes and displays the payment screen (amount + currency)
{% endstep %}

{% step %}
## Step 4

The customer performs the payment attempt and the payment information (card information) are sent to the Nepting payment gateway
{% endstep %}

{% step %}
## Step 5

The Nepting payment gateway processes the payment attempt
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

The Nepting payment gateway stores the transaction in its server database
{% endstep %}

{% step %}
## Step 11

The Nepting payment gateway sends the payment response to the payment terminal
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

Once the payment attempt processing is done, an Instant Payment Notification (IPN) is sent by the Nepting payment gateway to HiPay.
When the HiPay platform receives an IPN from Nepting, a process is triggered to create the transaction on HiPay side with the information in the IPN + the information in the HiPay notification (step 2').
It is only once this notification has been processed that the transaction is available in Console.

NB1: the transactions are automatically created in the Captured state .
NB2: To get more details about the server-to-server notifications, please consult the dedicated page .

WITHOUT authorization request

{% stepper %}
{% step %}
## Step 1

The POS cash register system sends a payment request to Cloud API
{% endstep %}

{% step %}
## Step 2

Cloud API forwards the payment request to the payment terminal referenced in the payment request via its serial number and its manufacturer's name
{% endstep %}

{% step %}
## Step 3

The payment terminal awakes and displays the payment screen (amount + currency)
{% endstep %}

{% step %}
## Step 4

The customer performs the payment attempt and the payment information (card information) are sent to the Nepting payment gateway
{% endstep %}

{% step %}
## Step 5

The Nepting payment gateway processes the payment attempt
{% endstep %}

{% step %}
## Step 6

The Nepting payment gateway stores the transaction in its server database
{% endstep %}

{% step %}
## Step 7

The Nepting payment gateway sends the payment response to the payment terminal
{% endstep %}

{% step %}
## Step 8

The payment terminal sends the payment response to Cloud API
{% endstep %}

{% step %}
## Step 9

Cloud API receives the payment response and forwards it to the POS cash register system
{% endstep %}
{% endstepper %}

Step 2': a notification is automatically sent to the HiPay platform with all the order information provided in the payment request (customer basket, customer information, custom data).

Once the payment attempt processing is done, an Instant Payment Notification (IPN) is sent by the Nepting payment gateway to HiPay.
When the HiPay platform receives an IPN from Nepting, a process is triggered to create the transaction on HiPay side with the information in the IPN + the information in the HiPay notification (step 2').
It is only once this notification has been processed that the transaction is available in Console.

NB1: the transactions are automatically created in the Captured state .
NB2: To get more details about the server-to-server notifications, please consult the dedicated page .

## Features

FEATURE DETAILS Operation types - Debit
- Credit CURRENCIES - Euro AUTHORIZATION REQUEST - Always
- Only in standard cases DATA HANDLED - Customer basket: the detailed list of the products that are part of the customer basket
- Customer information: id, email, phone, first name, last name
- Custom data: any data of your choice

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Cloud API for Nepting:

REQUIREMENT
DESCRIPTION

Devices
An Android POS payment terminal (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable Internet through a Wi-Fi connection OR a SIM card*
- The last version of the Nepting Android app installed
- The last version of the HiPay POS Android app installed
- The Cloud API service enabled

* Prerequisite: the SIM card needs to be configured to allow the communication with the HiPay server IP address and port

Security
Private API credentials enabled (please consult this page to get details about HiPay credentials).

## Documentation

- API description (swagger)
