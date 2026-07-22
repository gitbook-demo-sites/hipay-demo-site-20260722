---
description: "Hosted Page v2 is the new HiPay hosted payment page, where you can redirect your customers to securely process the payment. With this integration HiPa"
icon: file-lines
---

# Hosted Page Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/hosted-page](https://developer.hipay.com/online-payments/payment/hosted-page)
{% endhint %}

Hosted Page v2 is the new HiPay hosted payment page, where you can redirect your customers to securely process the payment.

With this integration HiPay will automatically display your company's information, the order and your chosen payment methods.

With this option you can benefit from a single point of contact, adaptable payment pages and the PCI-DSS Standard. You can therefore outsource heavy security requirements related to payment acceptance.

Available Languages : French / English / Portuguese / Dutch / German / Italian / Spanish

## Integration

In order to request a Hosted Page, you need to integrate the Hpayment API . We recommend you use the PHP SDK to simplify the API integration.

Example (required fields only):

orderid : unique order id. Ex: ORDER_1583157210

description : order short description. Ex. Sales

amount : Total order amount. Ex: 9.99

currency : Order ISO 4217 three-character currency code. Ex: EUR

Before calling the API, you need to make sure you have all the required information:

Private Credentials

Needed for making the API Call. You can find them here: BO TPP > Integration > Security Parameters.

IP Address Restriction

When using Hosted Page v2, you need to disable the IP Address restriction. You can change that here: BO TPP > Integration > Security Parameters.

Redirect Pages

We use the redirect pages to redirect the customer after a payment. You can either send the links on the hpayment API call, or set them on the BO TPP > Integration > Redirect Pages.

You can find more information in this article .

Server to server notifications

These notifications allow you to be notified, in a secured way, when a transaction is created and its status changes. You can configure them on the BO TPP > Integration > Notifications.

You can find more information in this article .

Signature

Useful for increasing the security of the exchanges between your server and HiPay. You can find them here: BO TPP > Integration > Security Parameters.

You can find more information in this article .

## iFrame

This is a hybrid solution in which the buyer remains on your website to make the payment. To use this integration you need to generate a hosted payment page (as above) with a special template. This allows you to display it in an iFrame.

In order to do so, set the parameter template with the iframe-js value on the Hpayment API .

When building the <iframe> HTML tag, we recommend you to apply the following attribute sandbox="allow-popups allow-top-navigation allow-same-origin allow-scripts allow-forms" .

## CMS Integration

If you use a CMS with a HiPay Module, you won't need to integrate the Hpayment API. Please follow the CMS Module documentation.

At the moment, Hosted Page v2 is only available on Magento 2, Prestashop & Shopify.

## e-Terminal

Hosted Page v2 is available for HiPay's eTerminal.

## Related Articles
