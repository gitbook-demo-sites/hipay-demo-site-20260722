---
description: "The accounting definition of capture is to convert an authorized transaction into an invoiceable transaction. The capture can be either automatic, man"
icon: file-lines
---

# Capture

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/maintenance/capture](https://developer.hipay.com/online-payments/maintenance/capture)
{% endhint %}

The accounting definition of capture is to convert an authorized transaction into an invoiceable transaction.

The capture can be either automatic, manual or delayed.

## Automatic

When making a purchase in capture mode, the capture is automatically requested right after authorization.

You have two ways of specifying that you want an automatic capture:

* TPP BO : Go to Integration > Payment Procedure and set the Default payment procedure to Automatic data capture.
* API Request : when calling either the Order API or the Hpayment API , you should the parameter operation to sale .

## On-demand

When making a purchase in automatic mode, the transaction status will be AUTHORIZED until you ask for the capture. Customers are not charged directly: you have 7 days to capture the order and charge the customer. Otherwise, the order is canceled.

You have two ways of specifying that you want an automatic capture:

* TPP BO : Go to Integration > Payment Procedure and set the Default payment procedure to On-demand data capture.
* API Request : when calling either the Order API or the Hpayment API , you should the parameter operation to authorization .

## Delayed

When making a purchase in delayed mode, our system requests the capture automatically after x days (if the authorization was not cancelled).

You can set up the number of days directly on TPP BO : Go to Integration > Payment Procedure and set the Default payment procedure to delayed capture, and set the number of days.

## Capture a transaction

HiPay Backoffice

In order to capture an authorized transaction you should go to the Transaction Preview.

Here, you will have a capture button , click on it to do a manual capture of the funds after a service has been rendered or a product has been sold.

API Request

In order to capture an authorized transaction you will need to use the Maintenance API .

F ull capture : you can only send the parameter operation set to capture.

P artial capture : you should send the parameter operation set to capture, the amount you want to capture and the currency.
