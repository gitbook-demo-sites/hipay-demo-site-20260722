---
description: "In order to have a better understanding of a transaction and its different steps, here you have a detailed workflow. Transaction Creation Once the cus"
icon: file-lines
---

# Transaction lifecycle

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/essentials/transaction-lifecycle](https://developer.hipay.com/payment-fundamentals/essentials/transaction-lifecycle)
{% endhint %}

In order to have a better understanding of a transaction and its different steps, here you have a detailed workflow.

## Transaction Creation

Once the customer clicks the payment button, HiPay will create a transaction.

The first question HiPay will verify is if we have an acquirer to process this transaction. If HiPay cannot find an Acquirer for the transaction, the transaction stops here as we won't be able to process it.

## Authentification

Once HiPay has found an acquirer for the transaction, the HiPay Fraud Protection Service (FPS) reviews the transaction in order to identify the risk associated.

Depending on the risk determined by the FPS the transaction will either be forced, accepted or need an authentification (ask or force).

In case the authorization is accepted by the FPS, the merchant can override this by sending a different Authenticator Indicator. When adding this to the risk, we will have a score:

* 0 : Transaction accepted, no need of 3-D Secure.
* 1 : Trigger 3-D Secure if possible, but not needed to continue with the transaction.
* 2 : Trigger 3-D Secure, if the authentication cannot be processed the transaction will be stopped. If the 3-D Secure is triggered, the transaction can be either accepted or refused.

## Authorization

Once the authentication process is over, HiPay will request an authorization. The authorization places the customer's balance on hold to ensure that you can capture the funds.

This request can be:

* Accepted: The transaction is authorized and can be captured.
* Refused: The transaction cannot be authorized, so it stops here.
* Challenged: The transaction needs manual fraud review by the merchant. In this case, the merchant can either:

* Accept the challenge.
* Deny the challenge.
* If no action is performed after 7 working days, the transaction will automatically be expired.

## Capture

The next step after the authorisation is the capture. The merchant can choose to do the capture either in an automatic or a manual way. Also, each transaction can be fully or partially captured.

## Finance

The two last steps on the transaction lifecycle are collection, the act of collecting the money from the client's account, and settlement, the act of transferring the client's money to your account.
