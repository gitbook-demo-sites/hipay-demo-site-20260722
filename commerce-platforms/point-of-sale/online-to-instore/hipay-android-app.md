---
description: "Description The HiPay Android application, named HiPay POS , acts as an entry point to trigger in-store payments via the Nepting payment gateway with "
icon: file-lines
---

# HiPay Android app

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/online-to-instore/hipay-android-app](https://developer.hipay.com/point-of-sale/online-to-instore/hipay-android-app)
{% endhint %}

## Description

The HiPay Android application, named HiPay POS , acts as an entry point to trigger in-store payments via the Nepting payment gateway with several payment scenarios by:
- manually initiating payments
- sending a payment request through an HTTP REST API to a specific POS payment terminal
- sending a payment request to a specific POS payment terminal located in the same LAN (Local Area Network).

## Screenshots

-

## Feature overview

FEATURE
DETAILS

Operation types
- Debit
- Credit

Currencies
- Euro

Customer receipt destination
- Printer
- Mail
- SMS

Payment initiator
- Manual entry
- HTTP REST API (Cloud API)
- Local API
- Cegid Y2 (via a dedicated Cegid Y2 connector)

Languages
- French
- English
- Italian
- Portuguese

## Requirements

REQUIREMENT
DESCRIPTION

Officially supported devices
PAX terminals (A920Pro, A80, A50, A35)

OS
Android 8.0+

Miscellaneous
- Paiement app (Nepting) installed
- Paiement app (Nepting) configured with your merchant account

Payment initiator
- Manual entry
- HTTP REST API (Cloud API)
- Local API
- Cegid Y2 (via a dedicated Cegid Y2 connector)

Languages
- French
- English
- Italian
- Portuguese

According to your payment scenario, additional requirements may also need to be fulfilled.
To get more details about these specific requirements, please consult the dedicated page that describes the appropriate integration type.

## Installation

HiPay POS can be installed on PAX devices via the MAXSTORE platform .
Please contact your maintainer to perform its installation if it is not available yet on your devices.

## Configuration

HiPay POS is a ready-to-use application.

It also includes some settings to be able to adapt to your context and needs:

Entry points

* Enable/Disable manual entry

* Enable/Disable Cloud API

* Enable/Disable Local API (+ select the port used to listen to payment requests)

Customer receipt preferences

* Enable/Disable showing a button to print it

* Enable/Disable showing a button to send it by mail

* Enable/Disable showing a button to send it by SMS

## Documentation

-
