---
description: "Our solutions have been designed on a one-stop shop model to help you manage your transactions for all payment methods available in 150 currencies. Th"
icon: file-lines
---

# Marketplace - Overview

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/marketplace-overview](https://developer.hipay.com/marketplace/marketplace-overview)
{% endhint %}

Our solutions have been designed on a one-stop shop model to help you manage your transactions for all payment methods available in 150 currencies.

The implementation of HiPay Marketplace involves establishing connections between your marketplace platform and HiPay based on a simple integration through a set of APIs.

HiPay Marketplace is based on two complementary platforms: HiPay Entreprise and HiPay Professional.

## CASH IN

HiPay Entreprise

The cash in helps you accept payments and create transactions. HiPay Enterprise handles the fund acquisition process :

* Fund acquisition and processing
* Fraud monitoring
* Financial data reconciliation
* Fund injection. In order to integrate HiPay Enterprise for your cash in here you have the list of APIs to be used:

/hpayment

Used to generate a payment page

/order

Create a transaction without going through the payment page

/maintenance/transaction

Allows for partial or total capture, partial or full refunds and cancellation of the license

/transaction

Provides information about an existing transaction (status, date, ...)

More information about how to integrate the HiPay Enterprise cash In here .

## CASH OUT

The cash out helps you manage payments: collecting funds and allocating them.

HiPay Professional handles the fund management process:

* Funds held in escrow
* Fund representation within HiPay accounts
* Checking of and responsibility for KYCs
* Technical guarantee of the system and of fund allocation
* Fund transfer to third parties' bank accounts Please note that agents keep control of cash flows, managing e-tailers according to their own sales policy with merchants' and customers' trust in mind. To do so, agents must be able to manage financial flows with ease between all the stakeholders.

In order to integrate HiPay Professional for your cash out here you have the list of APIs to be used:

/user-account

Create a new account

/user-account/bank-info

Register new bank-details on an HiPay account.

/transfer

Allocate funds

/withdrawal

Request a withdrawal

More information about how to integrate the HiPay Professional cash out here .

## KYC/KYB DOCUMENTS

In accordance with the applicable anti-money laundering and anti-terrorist financing regulations, the KYC (Know Your Customer) and KYB (Know Your Business) documents requested from you as part of the identification process are used to verify the identity of the holder of a HiPay Marketplace seller account.

Warning! You also need to provide the beneficial owners via the HiPay Professional platform, in order to fully identify an account.

The identification documents (KYC/KYB) required vary according to the four categories of HiPay Marketplace accounts:

* Professionals (legal entities),
* Professionals (natural persons),
* Associations,
* Individuals. Here you have the list of APIs to be used to upload and update the identification documents:

/identification

Upload identification documents.

More information about how to upload the identification documents here .

## AGENT RESPONSIBILITIES

The marketplace agent will be responsible of handling the flow management process:

* Creation of HiPay accounts via HiPay's APIs
* Gathering of KYC/KYB
* 1st level control of KYC/KYB
* Provide the beneficial owners via the HiPay Professional platform
* Fund allocation via HiPay's APIs
* Accounting management consistent with funds in HiPay accounts
* Fund withdrawal requests via HiPay's APIs
