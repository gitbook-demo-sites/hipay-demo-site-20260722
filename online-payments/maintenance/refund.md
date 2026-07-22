---
description: "The accounting definition of a refund is an amount of money that is given back to the customer. You have two ways of refunding a transaction. HiPay Ba"
icon: file-lines
---

# Refund

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/maintenance/refund](https://developer.hipay.com/online-payments/maintenance/refund)
{% endhint %}

The accounting definition of a refund is an amount of money that is given back to the customer.

You have two ways of refunding a transaction.

## HiPay Backoffice

In order to refund a captured transaction you should go to the Transaction Preview .

Here, you have a capture button , click on it to do a manual refund. You can refund a transaction fully or partially.

## API Request

In order to refund a captured transaction you need to use the maintenance API .

Full refund : you can only send the parameter operation set to refund .

Partial refund : you should send the parameter operation set to refund , the amount you want to refund and the currency .
