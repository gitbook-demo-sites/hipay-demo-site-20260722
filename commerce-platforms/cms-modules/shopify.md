---
description: "This article describes how to integrate HiPay as Gateway for your Shopify Store, how to set up the module and how to handle your transactions on a dai"
icon: file-lines
---

# Shopify

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/shopify](https://developer.hipay.com/cms-modules/shopify)
{% endhint %}

This article describes how to integrate HiPay as Gateway for your Shopify Store, how to set up the module and how to handle your transactions on a daily basis.

Module Features

* Hosted Payment Page Integration
* Manual or auto capture from Shopify
* Partial capture and refund from Shopify

## Prerequisites

Before adding HiPay as a gateway, you should make sure that you have an HiPay Entreprise account . If you haven't an HiPay account or you are using HiPay Professional, please contact our support team .

## HiPay as Gateway

The process to add HiPay as your Gateway for your Shopify Store is the following one:

* Go to the Hipay's Payment App on Shopify .
* Once you click the link, you'll be asked to log into their store.
* After logging in, you will be redirected to install hipay's payment screen. Scroll down and click on Install app.

## Configuration

The next step after having installed Hipay's payment app is to configure it. In order to do so click Manage button. You will be redirected to Hipay's Console.

Shopify

Console

Credentials

The first thing you need to configure are your private credentials username and passphrase. You can find this information on the TPP Backoffice : Integration > Security Settings .

Please make sure that the Hashing Algorithm of your HiPay Account is SHA-256.

After, come back on console to integrate the credential for live account and test account.

Payment Means

You can choose the payment means that you want to display on your checkout.

Please, make sure that you have contracted all the selected payment means on your HiPay Entreprise account. You can verify it on the TPP Back Office : Account > Payment Means .

Save your configuration and go back to the shopify admin.

If you hadn't close the shopify admin page, refresh it.

You will see the module in shopify with payment methods. Scroll down to see the button Activate our module.

Test your integration

Once you have configured the HiPay Module, we strongly recommend testing it on a testing environment, by activating the Test Mode on the HiPay Module.

Alternative installation method

It is possible to integrate our module in shopify. For that, we have to be in settings and in page Payment on your Store

To add our module, we can click on Add payment methods

In the tab Search by provider , Write Hipay Payment in the search and select our module Hipay Payment

Once the module is selected, you must click on the Activate button

## Customer Experience

Shopify Checkout

After filling the contact information, the customer is redirected to the Payment tab of the Shopify checkout.

In this tab, the customer can choose the payment processor that they want to use to pay. Once the review of the order is done, the customer will be redirected to the HiPay's Hosted Payment Page.

HiPay's Hosted Payment Page

HiPay's Hosted Page will display all the payment means of your HiPay TPP Account. Once the payment is done, HiPay will redirect the customer to the success or failure Shopify page.

You can customize the Hosted Page layout using HiPay Console .

## Order Management

You can manually capture, refund and cancel an order that has been created directly from Shopify. You can also do this using HiPay's Backoffice, but the status of the transaction won't be updated on Shopify.

Manual Capture

You can activate the manual capture on the Payment Capture section of the payment settings page.

Once this is done, you can manually capture an order, going into the authorized order (payment status: Payment authorized). More information about how to manually capture an order here .

Refund

Refunding an order results in the payment being sent back to the customer. You can refund an entire order or part of an order.

In order to refund an order you should:

* From your Shopify admin, go to Orders
* Open the order you want to refund.
* Once you are in the order page, click on Refund items at the top of the page.
* Choose the number of items that you want to refund.
* Optional. You can manually adjust the total amount you want to refund using the Refund Amount Field above the Refund button.
* Click Refund Order

Cancel an order

The most common reasons for canceling an order include the following:

* The customer changed their mind.
* The ordered items aren't available.
* The order was fraudulent. In order to cancel an order, you should:

* From your Shopify admin, go to Orders .
* Click the order that you want to cancel.
* Click More actions > Cancel order .
* If payment is captured: By default, a full refund is issued. If you want to issue a partial refund, then use the product quantity boxes, the shipping field, or the refund total field to edit the refund amount.
* If payment isn't captured: When you cancel the order, the payment is void and isn't collected from your customer. You can't issue a partial refund.
* Select the reason for cancellation from the drop-down menu.
* Click Cancel order.
