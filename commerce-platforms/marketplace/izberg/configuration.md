---
description: "You don't need to install any software in order to make this integration work. You just need to configure it through the Izberg operator back office. "
icon: file-lines
---

# Izberg - Configuration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/izberg/configuration](https://developer.hipay.com/marketplace/izberg/configuration)
{% endhint %}

You don't need to install any software in order to make this integration work. You just need to configure it through the Izberg operator back office.

Follow the steps below in order to have the whole solution working for both cash-in and cash-out.

1. Izberg back office

* Log in to the Izberg back office
* Go to the payment section .
* Click on Settings then App setup
* Then, click on the Payment Config tab: 2. Backend provider

* In the backend provider section, select HiPay .
* Then, click on Save . 3. Configuration

* In the configuration section, you may provide a description of the integration for the record.
* Make sure that the integration is active.
* Make sure the sandbox mode is set to the proper value. If you provide HiPay test account credentials, this box must be checked. However, if you provide production HiPay account credentials, this box must not be checked. 4. Cash-out

In the cash-out section, you need to provide your HiPay Marketplace (e-wallet platform) details:

* HiPay Wallet entity (named E-Wallet Api Entity on the screenshot)
* HiPay Wallet web service login (named E-Wallet Api Login on the screenshot)
* HiPay Wallet web service password (named E-Wallet Api Password on the screenshot)
* HiPay Wallet technical account ID (named Account ID on the screenshot) All these information should have been provided to you beforehand by HiPay. If you don't have them, please submit a ticket or contact the HiPay IT Support team.

5. Cash-in

HiPay Enterprise back office

* Sign in to your HiPay Enterprise merchant back office .
* Go to the Integration section
* Then, go to the security settings section. REST API passphrase

* On the HiPay Enterprise back office, if the Secret Passphrase field is empty, choose one by typing a secret string here. If the passphrase is already defined, do not modify it (unless it's not already in use).
* Then, copy and paste this secret passphrase into the REST API passphrase field on the Izberg operator back office. REST API login and password

* On your HiPay Enterprise back office, find the API credentials section (still in Security settings )
* Choose the credentials you want to use for cash-in management in Izberg. You may select an existing set of credentials or generate a new one.
* Make sure they are granted for each API action . If you are not sure, click on the edit icon and verify that all boxes are checked.
* Then copy and paste the Username value into the REST API Login field and copy and paste the Password value into the REST API Password field in the Izberg back office: 6. Payment form

You may customize the cash-in payment page by uploading your own CSS (cascading style sheet) file. For more information, refer to the HiPay Enterprise Hosted Page .

The Payment Form Template option allows you to choose whether you want the end user to be fully redirected to our payment page or if you want the payment form to be integrated into the checkout.

You can also choose whether you want the payment methods list to be displayed on the payment page. If you have many payment methods (not only credit or debit cards), you should check this box.

7. Redirect URLs

In the Redirect URL fields, make sure to insert your proper Izberg marketplace shop URLs. If you are not sure of what to insert in the fields above, contact the Izberg support.

That's it. Your Izberg payment configuration is all set up. Test your integration to make sure everything is OK.
