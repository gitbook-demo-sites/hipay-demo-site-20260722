---
description: "The HiPay Enterprise extension for WooCommerce is a PHP plugin which allows you to accept payments in your WooCommerce store, offering innovative feat"
icon: file-lines
---

# WooCommerce Enterprise

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/woocommerce/woocommerce-enterprise](https://developer.hipay.com/cms-modules/woocommerce/woocommerce-enterprise)
{% endhint %}

The HiPay Enterprise extension for WooCommerce is a PHP plugin which allows you to accept payments in your WooCommerce store, offering innovative features to reduce shopping cart abandonment rates, optimize success rates and enhance the purchasing process on merchants' sites to significantly increase business volumes without additional investments in WooCommerce, the e-commerce plugin for WordPress.

Please make sure you go through the CMS Prerequisites article before starting the integration.

The plugin and its changelog are available on our GitHub .

## Features

The main features of the module are:

* IFrame, Hosted Page and Hosted Fields integrations
* 3-D Secure enabling/disabling
* Manual and automatic capture
* Partial capture and refund
* Custom data management (easily send and view your data in your HiPay Enterprise back office) The extension supports the following payment methods:

Country Payment methods Worldwide Visa, Mastercard, Amex, Bancontact, Maestro Europe iDEAL, ING Home'Pay, PayPal, SEPA Direct Debit France Oney Facily Pay Switzerland PostFinance Card, PostFinance E-finance Belgium Belfius / Dexia Direct Net Italy SisalPay, MyBank Germany Giropay, SOFORT Uberweisung Brazil and Mexico Itau, Bradesco, Banco do Brasil, Santander HomeBanking, Aura, Caixa, OXXO, BBVA Bancomer, Banamex, Santander Cash Poland Przelewy24

## Installation

### Package

Download the ZIP package of the latest release at this address https://github.com/hipay/hipay-enterprise-sdk-woocommerce/releases .

The ZIP package is named hipay-enterprise-sdk-woocommerce-{version-number}.zip

### Plugin Upload

WORDPRESS

To install the plugin, log in to your WordPress dashboard: go to Plugins -> Add New and click on Upload plugin.

Choose the package and click on Install Now .

FTP (SFTP)

You must have a file transfer software like FileZilla for example.

* Open your software and connect to your FTP (SFTP).
* Go to the root of your WordPress project.
* Transfer the woocommerce_hipayenterprise source plugin in the /wp-content/plugins/ folder.
* Add write permissions recursively to the folder woocommerce_hipayenterprise (766).

### Activation

* Go to Plugins -> Installed Plugins .
* Search for the WooCommerce HiPay Enterprise plugin.
* Verify the plugin version.
* Click on Activate in the plugin description.

## Global Configuration

### Configuration Interface

To configure the HiPay Enterprise plugin, click on WooCommerce -> Settings -> Payments in your WordPress dashboard. Then click on HiPay Enterprise Credit Card :

First, you must activate the payment methods by clicking on the toggle.

The new configuration interface of the plugin is comprised of four tabs.

* Plugin settings : Configure API IDs to run HiPay services. You can also configure whether the plugin is in Production or Test mode.
* Payment methods : Configure the payment methods to be activated and how payments must be processed: Hosted Fields or Hosted Page.
* Fraud : Configure recipients' email addresses for challenged transaction notifications.
* FAQ : Find answers to frequently asked questions on how to use the plugin.

### Plugin Settings

This tab allows you to configure the API IDs required to run HiPay services.

It is comprised of the following components that you must set up first and foremost.

Plugin mode

This setting is very important as it allows you to define whether payments will be processed on the HiPay Test or Production platform. By default, the plugin is in Test mode, which means that payments will not be actually charged.

We strongly advise you to run tests before launching your site in Production mode.

Production configuration

Use this interface to specify the credentials linked to your HiPay account. These identifiers are used if your plugin is configured in Production mode.

Generated in your HiPay Enterprise back office (go to Integration => Security Settings => Api credentials => Credentials accessibility), these API credentials are required to use the HiPay Enterprise plugin.

For more information about credentials generation, please refer to the Credentials section.

Account (Private)

Private credentials are used to process payments through the HiPay APIs. These identifiers are mandatory.

Name Description Username Your HiPay Enterprise production account API username Password Your HiPay Enterprise production account API password Secret passphrase Your HiPay Enterprise secret passphrase Tokenization (Public)

Public credentials are used as part of the JavaScript tokenization. These identifiers are to be specified only if you want to use the plugin in Hosted Fields mode.

Name Description Username Your HiPay Enterprise production account API username Password Your HiPay Enterprise production account API password Test configuration

This interface is similar to the Production configuration. These identifiers are used if your plugin is configured in Test mode.

### Fraud screening

Based on the screening results of HiPay Sentinel, our advanced anti-fraud solution, when a transaction is suspected of being fraudulent, it is in challenged status. In your WooCommerce back office, the order is flagged as being On-Hold.

An email is then sent to the site administrator to warn him/her that a transaction has been challenged and that it must be accepted or declined.

With this interface, you can add recipients for email notifications about challenged transactions. You must enter a valid email address: when a transaction is being challenged, an email will be sent to this address.

Accepting or declining transactions

At the moment, it is only possible to do so from your HiPay Enterprise back office. Once a transaction is accepted or declined, the order is then updated in your WooCommerce back office.

## Credit Card

After setting up the previous required components, this interface allows you to define global payment settings and settings specific to the credit card payment method.

To activate a payment method, please refer to this example from the WooCommerce official documentation.

### Settings

This general configuration will be applied whatever the payment methods being used.

Name

Description

Value

Operating mode

Defines if the payment form is displayed on the merchant's site or on a HiPay payment page.

- Hosted Page : Customers are redirected to a secure payment page hosted by HiPay.

- Hosted Fields : Customers complete their banking information directly on the merchant's site but the form fields are hosted by HiPay. This mode is only valid for credit cards.

Capture

Defines if payments should be captured manually or automatically. Manual capture will be possible either on the order page of the WooCommerce back office or on the HiPay Enterprise back office. Please refer to the section on Capture mode .

- Manual : All transactions will be captured manually either from your HiPay Enterprise back office or from your WooCommerce back office.

- Automatic : All transactions will be captured automatically.

Customer's cart sending

The customer's cart will be sent during the transaction. This option is required for Oney transactions.

Yes/No

Logs information

Activates debug logs.

Activate 3-D Secure

Enables and configures 3DS rules.

You can choose between three options:

- Disabled (to bypass 3-D Secure authentication)

- Try to enable for all transactions

- Force for all transactions

Send url Notification

The URL used by HiPay to send the notifications is directly filled in the order transaction.

Yes/No

Hosted Page

When you choose the Hosted page as operating mode, you have access to additional settings.

Name Description Value Display hosted page Defines if the Hosted Page is displayed in an iFrame or with a redirect. -Redirect
-Iframe Display card selector Shows card selector on the Hosted Page. Yes/No CSS URL URL of your CSS (cascading style sheet) to customize your hosted page or iFrame Https URL Hosted Fields

When you choose the Hosted Fields as operating mode, you have access to additional settings: color, fontFamily, fontSize, fontWeight, placeholder Color, caretColor, iconColor.

These parameters allow you to override default CSS properties in the Hosted Fields form. For more information, please refer to the HiPay Enterprise JavaScript reference .

To override the default template, please refer to the WooCommerce documentation .

Credit card

All card types are enabled and set to default. For each type of card, you can then define a different configuration.

Name Description Value Activated Allows or not customers to use this type of card. Yes / No
If the card type is not activated, customers will have a warning message upon payment, inviting them to use another type of card. Minimum order amount Indicates a minimum threshold for the type of card available for payment. Amount in default currency
If the amount is not reached, customers will have a warning message upon payment, inviting them to use another type of card. Maximum order amount Indicates a maximum threshold for the type of card available for payment. Amount in default currency
If the amount is exceeded, customers will have a warning message upon payment, inviting them to use another type of card. Currencies Currencies for which the card type will be activated. These are the installed and active currencies on your store Selection of one or more currencies Countries Countries for which the card type will be activated. Selection of one or more countries

## Local Payment Means

Local payments include all payments other than credit cards. In this block, you can find the link to all local payments settings interfaces.

### Activation

To activate a payment method, please refer to this example from the WooCommerce official documentation.

### Configuration interface

To configure the HiPay Enterprise plugin, click on WooCommerce -> Settings -> Payments in your WordPress dashboard. Then click on the name of the payment method you want to configure ( HiPay Enterprise Bnppf-3xcb for example).

### Settings

Configuration is done as for credit cards, except for certain local payments: currencies and countries cannot be modified because they are imposed by each payment method.

You can also define the following element for each payment method.

Name Description Value Display name Name displayed on the WooCommerce checkout page String

## Capture

### Automatic mode

When making a purchase in automatic mode, the capture is automatically requested right after authorization.

* If the payment fails, the customer is redirected to an error page and the status is defined as Cancelled .
* If the payment is successful, the customer is redirected to the success page and the status is defined as Completed .

### Manual mode

When making a purchase in manual mode, the transaction status will be On-Hold until you ask for the capture. The customer is not charged directly: you have seven days to capture the order and charge the customer. Otherwise, the order is cancelled.

* If the authorization fails, the customer is redirected to an error page and the status is defined as Cancelled .
* If the authorization is successful, the customer is redirected to the success page and the status is defined as On-Hold . To capture a transaction in your WooCommerce back office:

* Go to your list of orders and select any one. The order status should be On-Hold. Manual and partial captures are not native WooCommerce features. If you are familiar with the WooCommerce system for captures, the principle of capture is based on manual capture.
* If the order is in the correct status and if the amount already captured does not reach the total of the order, you should have a Capture button to the right of the Refund button in the panel for the item.
* Click on the Capture button. Specify the quantity of product(s) to be captured in the text box(es) displayed for each item line. The capture amount will be automatically adjusted based on the product(s) captured. You can also capture delivery costs: make sure to fill in the tax.
* Then click on Capture XX via HiPay Enterprise Credit Card Once the capture is made, a line appears for each item, indicating Captured with HiPay or the quantities and amounts captured. The status of the order will evolve to:

- Partially captured if you have not captured all the items of the order,

- Processing if you have captured them all.

Partially captured is a status added by the HiPay extension that allows you to easily identify orders partially captured. It is similar to WooCommerce's On-Hold status. Therefore, all the actions relating to a change of status will be performed when the order status changes from Processing to Complete.

## Refund

The plugin supports the WooCommerce native feature for refunds. To make a refund:

* Go to: WooCommerce > Orders .
* Select the order you wish to refund.
* Click on the grey Refund button.
* Specify the quantity of product(s) to be refunded in the text box(es) appearing for each item line. The refund amount will be automatically adjusted based on the product(s) refunded. If inventory levels are not managed, you can also simply enter the Refund amount, without adjusting the product quantity. If the quantities of items are not set when issuing a refund, the order will not be marked as refunded and the email that is sent will say partial refund.
* Add refund notes, if desired.
* Click on Refund $X via HiPay. The status of the order will evolve to:

- Partially refunded if you have not refunded all the items of the order. This status has been added by the HiPay extension for allowing you to easily identify orders partially refunded.

- Refunded if you have refunded them all. You can also make a total refund directly from your HiPay Enterprise back office. The order will then be automatically updated in your WooCommerce back office.

For more information, please refer to the WooCommerce documentation on Refunds .

## Category & Carrier Mapping

The customer's cart information can be sent with the transaction details if you enabled the option in the global settings. This mapping is necessary to establish a correlation between your data and HiPay's. It is mandatory to do all the mappings to use the Oney Facily Pay payment method.

Category mapping

In your WordPress dashboard, go to HiPay Enterprise -> Category mapping .

WooCommerce product categories are displayed: you must match each of them with the corresponding HiPay category.

Carrier mapping

In your WordPress dashboard, go to HiPay Enterprise -> Delivery method mapping .

All the delivery methods available on your store are listed. For each of them, you must fill in the necessary corresponding information.

This information is used to calculate an approximate delivery date.

Name

Value

Order preparation estimated time

Expressed in days

Delivery estimated time

Expressed in days

HiPay delivery mode

- store : At the store

- carrier : Delivery by carrier

- relaypoint : Delivery in a pick-up location

- electronic

- travel

HiPay delivery method

- standard

- express

- Priority 24H

- Priority 2H

- Priority 1H

- Instant

## Logs

HiPay logs all the necessary information if there is a problem with the plugin. These logs will be requested by HiPay's technical teams in case of an issue. The HiPay Enterprise plugin uses the default log system from WooCommerce. To access your logs, go to WooCommerce -> Status -> logs .

There is no sensitive information in these logs (e.g: card numbers).

You will find different categories of logs in this interface.

* Error logs : All errors that occurred on the HiPay Gateway
* Info logs : Technical and debug logs
* Callback logs : HiPay Gateway notifications
* Request logs : Calls to the HiPay Gateway

## Custom Data

With this extension, you have the possibility of sending additional information with the transaction details that can then be viewed in your HiPay back office. To do so, you can use the filter functionality from WordPress. Custom data can be received through HiPay notifications and processed later.

For more information, please refer to the documentation on Devdocs .

To add custom data to transactions details, you must create a handler for the filter hipay_wc_request_custom_data in a custom module or in your theme.

This can be done as follows

PHP

PHP

```
/**
* HiPay Enterprise extension for WooCommerce
*
* 2019 HiPay
*
* NOTICE OF LICENSE
*
* @author HiPay
* @copyright 2019 HiPay
* @license https://github.com/hipay/hipay-enterprise-sdk-woocommerce/blob/master/LICENSE.md
*/

/**
* This is an example of how to add custom data to the transaction gateway.
* You can add your own function/class, you just have to hook the 'hipay_wc_request_custom_data' filter.
*
* If you want to use this example, copy/paste this file in your theme or custom plugin and require it.
*
*/
class Hipay_Custom_Data
{

private static $instance;

public function __construct()
{
add_filter('hipay_wc_request_custom_data', array($this, 'getCustomData'), 10, 3);
}

/**
* Returns your custom data in a JSON format for gateway transaction requests
*
* @param $customData
* @param $order
* @param $params
* @return mixed
*/
public function getCustomData($customData, $order, $params)
{
// This is an example of how to add custom data.
if ($order) {
$customData['my_field_custom_1'] = $order->id;
}

return $customData;
}

public static function get_instance()
{
if (null === self::$instance) {
self::$instance = new self();
}
return self::$instance;
}
}

Hipay_Custom_Data::get_instance();
```
