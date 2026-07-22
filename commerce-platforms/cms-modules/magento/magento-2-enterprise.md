---
description: "The HiPay Enterprise module for Magento 2 is a PHP module which allows you to accept payments in your Magento 2 online store. It offers innovative fea"
icon: file-lines
---

# Magento 2 Enterprise

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/magento/magento-2-enterprise](https://developer.hipay.com/cms-modules/magento/magento-2-enterprise)
{% endhint %}

The HiPay Enterprise module for Magento 2 is a PHP module which allows you to accept payments in your Magento 2 online store. It offers innovative features to reduce shopping cart abandonment rates, optimize success rates and enhance the purchasing process on merchants' sites in order to significantly increase business volumes without additional investments in the Magento 2 e-commerce CMS solution.

Please make sure you go through the CMS Prerequisites article before stating the integration.

The plugin and its changelog are available on our GitHub .

Module Features

* Compliance with PSD2 requirements relating to Strong Customer Authentication

* More than 30 payment methods available

* 3-D Secure enabling/disabling

* One-click payment option configuration with custom rules

* Available integrations: Hosted Fields, Hosted Page and Hosted iFrame

* Email management for challenged transactions pending validation to fight against fraud

* Manual and automatic capture

* Partial capture and refund

* Payment in x installments without fees

* Custom data management to easily send and view your data from your HiPay Enterprise back office

Payment Means

## Module installation

Module installation

Go to your document root directory.

You can now install the module with the following command line:

Bash

Bash

```
composer require hipay/hipay-fullservice-sdk-magento2
```

After the Composer installation, you must run these command lines:

Bash

Bash

```
bin/magento module:enable --clear-static-content HiPay_FullserviceMagento
bin/magento setup:upgrade
bin/magento cache:clean
```

If no errors are displayed, the module is installed.

You can then go to your Magento Admin Panel.

Module update

You can now update the module with the following command line:

Bash

Bash

```
composer update hipay/hipay-fullservice-sdk-magento2
```

Then, you must run these command lines:

Bash

Bash

```
php bin/magento setup:static-content:deploy
php bin/magento setup:upgrade
php bin/magento cache:clean
```

## Module Configuration

Before using the HiPay Enterprise module for Magento 2, the following settings are required and must be configured:

Credentials configuration

In your Magento Admin Panel, select: Stores > Configuration > Sales (HiPay Entreprise)

Then, you need to enter your credentials. You will find them on your HiPay Entreprise back office ( Integration > Security Settings )

Anti-fraud emails configuration

Based on the screening results of HiPay Sentinel, our advanced anti-fraud solution, emails can be sent to end customers. There are 3 email templates.

* Fraudulent : This email is sent to the customer if the payment is fraudulent.
* Accepted : This email is sent to the customer if the payment is approved by the merchant.
* Denied : This email is sent to the customer if the payment is denied by the merchant. Field name Description Enabled Enables/disables sending Payment Fraud Email Sender Sets the email sender Payment Fraud Template Sets the email template. You can customize it in your Magento 2 Admin Panel. To do so, go to Marketing => Communications [Email Templates] . Click on Add New Template , then upload the HiPay email template you want and modify it. Send Payment Fraud Email Copy To Email addresses you want to add in copy Send Payment Fraud Email Copy Method Selects the email copy method (Cc or Bcc) Customer's cart items configuration

This section addresses customer's cart items sending to the HiPay Enterprise back office during the transaction.

Enabling this option applies to all enabled payment methods on your site. The information of the customer's cart, containing the shipping method, the discounts and each product with the quantity, as well as the SKU and the tax, is sent with the transaction.

For Oney Facily Pay , sending this information is mandatory. This option is therefore ignored if the transactions are made with this payment method.

Oney's anti-fraud system requires additional configuration for the shipping method and product categories. The configuration is explained in the following paragraph.

For questions relating to installation and configuration, please don't hesitate to visit our Support Center or submit a request to our Support team.

Please note that Adjustment Fee or Adjustment Refund are not supported with carts for refunds.

Mapping categories

Go to the setup screen HiPay Enterprise > Mapping Categories .

Only the top level categories must be mapped. If the mapping is not done, transactions will be refused by Oney. It is therefore important to check your mapping regularly when adding or modifying a category.

Mapping shipping method

Go to the setup screen HiPay Enterprise > Mapping Shipping method .

You can either choose a native or a custom shipping method. This mapping is necessary to indicate a match between your shipping methods and the shipping methods defined by HiPay. For each customer's order, depending on the chosen configuration, this information is sent as a supplement to the customer's cart.

For each mapping, you have to fill out the following information:

* Order preparation delay: Estimated time for order preparation,
* Delivery time estimated: Estimated time for delivery. From this information, an estimated delivery day is calculated and sent with the transaction. Non-working days are not taken into account in this calculation.

As with the mapping of categories, all shipping methods must be mapped . Therefore, it is important to update your list if you change the configuration of your shipping methods.

Other configurations

Field name Description Device fingerprint Defines if a fingerprint is sent with the transaction (YES by default) URL of HiPay's JavaScript Technical parameter not to be modified.

Send cart Activates customer's cart items sending or not (NO by default) EAN attribute EAN is not a Magento attribute by default: you must define your custom attribute if you want to send it in the cart

## PSD2 & SCA

Given the strong growth of the e-commerce in Europe, the second Payment Services Directive (PSD2) redefines the security standards for online payments, aiming to increase security during the payment process, while fighting more actively against fraud attempts. For more details on the regulations, we invite you to read our guide on PSD2 compliance.

As from September 14, 2019, the issuer will now decide if a payment is processed depending on the analysis of more than 150 data collected during purchasing. Thanks to our Magento 2 module, we handle most of the data without you having to develop anything. Discover all the new parameters on our API explorer.

Adding or overriding PSD2 data

The accuracy of the information sent is key for making sure that your customers have a frictionless payment process. That's why we give you the possibility to add or override PSD2 data, using a plugin on the HiPay\FullserviceMagento\Model\Request\Order class which can intercept the mapRequest method.

You can either implement the plugin in your own modules or use the one that we provide. You can find this additional plugin in our GitHub repository .

You can install this plugin in a standard way, then directly modify the ThreeDSPlugin.php file and the afterMapRequest method to add your information.

Please note: If there is an update of this plugin, remember to save your information so that it is not overwritten.

Finally, although we do our best to retrieve all relevant data for you, we cannot get the following information as it depends on the modules installed on your CMS or on your workflow.

Merchant risk statement

Field name Description delivery_time_frame By default, we send 1 (Electronic delivery) if it is a downloadable or an intangible product.

Depending on your carrier and delivery methods, you can refine this information.

Possible values:

1 = Electronic delivery
2 = Same day shipping
3 = Overnight shipping
4 = Two-day or more shipping

shipping_indicator We handle this field but you can override the value for intangible products.

If the cart contains only intangible products, please provide:

5 = Digital goods
6 = Travel and event tickets, no shipping
7 = Other (gaming, digital services without shipping, e-media subscription)

pre_order_date If you offer the possibility of pre-ordering, you must retrieve the product availability date. gift_card If you sell gift cards amount Collect the amount of gift cards purchased count Collect the count of gift cards purchased currency Collect the gift card currency To see all the parameters you can override, please refer to the PHP SDK Reference.

## Payment Means

Find this information on:

STORES > CONFIGURATION > SALES > PAYMENT METHODS

Before selecting the payment means that you want to enable, you will need to choose the type of integration. Here you have an article that explains the difference between the Hosted Fields, Hosted Page and the API only integrations.

We strongly recommend you to choose the Hosted Fields as it is the best integration in terms of Payment Experience and Security. When the Hosted Fields are not available, the Hosted Page is the right option, as it is as secured as the Hosted Fields.

General configuration

All payment methods have a basic configuration like the native Magento 2 payment methods configuration or the general HiPay Enterprise configuration.

Field name Description Enabled Enables/disables the payment method Title Desired name of the payment method as displayed during checkout Payment Action Authorization or Sale. See more configuration details below. New Order Status Order status to set when the order is created before payment. Pending by default. Order status when payment accepted Order status to set when the transaction is successful. Processing by default. Order status when payment refused Order status to set when the transaction fails. On Hold by default. Order status when payment cancelled Order status to set when the transaction is canceled by the user. Canceled by default. HiPay status to validate order By default, all orders are validated/invoiced upon notification when the Capture status (118) is sent from the HiPay Enterprise platform (around 10 min after capture is requested). You can change this pattern by selecting Capture Requested. In this case, the order is validated/invoiced directly upon the Capture Requested (117) status. Cancel pending order Cancels orders pending because the customer did not validate the payment. For more information, please refer to the Cron configuration and task information section. Payment products Allowed payment products. E.g.: Visa, Mastercard, SisalPay... Use 3D Secure Enables/disables 3-D Secure. See more configuration details below. Rules 3D Secure Configures custom rules to activate or not the 3-D Secure mode Use Oneclick Enables/disables One-click. See more configuration details below. Rules Oneclick Configures rules to activate or not the One-click mode Payment from Applicable Countries Limit allowed countries Payment from Specific Countries Select allowed countries Minimum Order Total Minimum order total amount to display the payment method Maximum Order Total Maximum order total amount to display the payment method Sort Order Configures the order of payment methods, as displayed during checkout Debug Enables/disables the debug mode (which logs queries) Environment Stage or Production. In Stage mode, the test API endpoint and your test credentials are used.

### Hosted Page

If you have chosen the Hosted Page as your integration, you will need to chose the version of the Hosted Page that you want to use.

Once you have chosen the Hosted Page, you can activate the version 2 by following the next steps:

1 - Make sure that your HiPay Module is updated to the latest version.

2 - Go to the STORES > CONFIGURATION > SALES > HIPAY ENTREPRISE section of the Magento module.

3 - On the HiPay Hosted Page Management section, choose the Hosted Page v2 option (see image below).

4 - Save the configuration

We strongly recommend you to to use the Hosted Page v2, as it provides a better payment experience and it is fully customizable on HiPay Console. You can find more information in this article.

If you have installed the module after October of 2021, the Hosted Page v2 is your default version. Otherwise, you can start using the V2 by setting the version to Hosted Page v2.

iFRAME

STORES > CONFIGURATION > SALES > PAYMENT METHODS

Once you have chosen the version of the Hosted Page, you can choose if you want to display the Hosted Page in your page using an iFrame.

If you choose this option, here you have a few fields that will help to do so:

Field name Description Display hosted page in iFrame By default, a hosted payment method redirects your customers to a hosted payment page, but in iFrame mode, this hosted page is displayed in an iFrame directly on your website. iFrame Width Width of the iFrame (if the iFrame mode is enabled) iFrame Height Height of the iFrame (if the iFrame mode is enabled) iFrame Style Style attribute's value of the iFrame (if the iFrame mode is enabled) Wrapper iFrame Style Style attribute's value of the iFrame wrapper (if the iFrame mode is enabled)

Hosted Page v1

STORES > CONFIGURATION > SALES > PAYMENT METHODS

If you are still using the Hosted Page v1, you can customize the page with the following fields:

Field name Description Display card selector Allows to display the card selector on a hosted page Custom CSS url Hosted pages can be customized with a CSS URL. Important: the HTTPS protocol is required.

### Hosted Fields

STORES > CONFIGURATION > SALES > PAYMENT METHODS

You can customize the styling of the Hosted Fields by using the following fields:

Field name color fontFamily fontSize fontWeight placeholder Color caretColor iconColor Those parameters allow you to override default CSS properties in hosted form fields.

To override the default template, please refer to the Magento 2 documentation and the HiPay Enterprise JavaScript SDK reference .

### API Only

STORES > CONFIGURATION > SALES > PAYMENT METHODS

You can customize the styling of the API Only integration by using the following field:

Field name Description Display card owner Displays form field for card owner's full name

## Capture

Sale Mode

When making a purchase with the Sale mode, the capture is automatically requested right after authorization.

If the payment fails, the customer is redirected to an error page and the status is defined as CANCELED .

If the payment is successful, the customer is redirected to the success page and the status is defined as CAPTURE REQUESTED .

Authorization mode

When making a purchase with the Authorization mode, the transaction status will be AUTHORIZED until you ask for the capture.

Customers are not charged directly: you have 7 days to capture the order and charge the customer. Otherwise, the order is cancelled.

If the authorization fails, the customer is redirected to an error page and the status is defined as CANCELED .

If the authorization is successful, the customer is redirected to the success page and the status is defined as AUTHORIZED .

To capture a transaction in your Magento Admin Panel, select Sales -> Orders -> View to see the details of the order and choose to submit an invoice.
On the New Invoice page, select Capture online and save your invoice.
Please note: If you select a custom item quantity, you can do a partial capture.

You can also do the capture directly in your HiPay Enterprise back office. The order will then be automatically updated in your Magento Admin Panel.
Please note: It only works for total captures (not partial).

## Refund

Some HiPay Enterprise payment methods allow for a refund. To do so, in your Magento Admin Panel, select Sales -> Orders -> View to see the details of the order, then choose an invoice to refund and click on Credit Memos .

On the Credit Memos page, select Refund and save your credit memo.

Please note: If you select a custom item quantity, you can do a partial refund.

You can also do the refund directly in your HiPay Enterprise back office. The order will then be automatically updated in your Magento Admin Panel.
Please note: It only works for total refunds (not partial).

For notifications to work as expected, please refer to this section.

## Additional Features

### 3-D Secure

You can choose between 5 options:

* Disabled (to bypass 3-D Secure authentication)
* Try to enable for all transactions
* Try to enable for configured 3ds rules
* Force for configured 3ds rules
* Force for all transactions Rules configuration follows the same process as Magento 2 price rules.

### One-click

If the One-click option is enabled, your system will create an alias for the credit card. Customers will thus be able to use a saved credit card for their second transaction and won't need to fill in all the payment data again.

Customers can delete their saved credit cards from their account.

### Split payments

When an order is created with a HiPay Enterprise split payment method, x installments are created (x depending on the selected payment profile).

A split order is validated when the payment is captured. Upon payment capture, x installments are generated for this order. The order is fully invoiced (but not fully captured in the HiPay Enterprise platform) and you can get ready for shipment.

The first installment is always debited on the payment date in Capture mode or when you capture manually in Authorization mode.

Then, with a Cron task, each installment is debited on its respective payment date.

Split payment methods

The HiPay Enterprise module for Magento 2 includes two payment methods for split payments:

* HiPay Enterprise Hosted Page Split Payment,
* HiPay Enterprise Credit Card Split Payment, based on the HOSTED or API mode.

Before using them, you need to create payment profiles.

Payment profiles

A payment profile defines how the payment is split.

In your Magento Admin Panel, select HiPay Enterprise > Payment Profiles .

Click on Create New Payment Profile .

Then fill in the form.

* Name : Public name for your payment profile
* Period Unit : Unit for billing during the subscription period
* Period Frequency : Number of billing periods that make up one billing cycle
* Period Max Cycles : Number of billing cycles for the payment period Here is an example if you want to split the amount in 3 installments with 1 billing per month.

* Period Unit: month
* Period Frequency: 1
* Period Max Cycles: 3 Split payment method configuration

Once you have at least one payment profile, you can configure a split payment method.

Specific configuration:

Field name Description Split Payment Profile Enables to select active split payment profiles, which will be displayed during checkout so that customers can choose one of them
Split payment overview

A split payment overview is available in your Magento Admin Panel in HiPay Enterprise > Split Payment .

For each installation, you can edit, delete or pay it immediately.
You can also change the payment date or the amount to pay.

Be careful: If you are not sure what to do, please submit a request ( https://support.hipay.com/hc/en-us/requests/new ) to our Support team.

### Custom data

It is possible to send additional information in the transaction that can then be viewed in the HiPay back office. To do so, you can use the functionality of Magento 2 which relies on the notion of plugin.

Please refer to the Magento PHP Developer Guide .

To add custom information to transactions, you need to create a plugin in your custom module. This plugin must observe HiPay\FullserviceMagento\Model\Request\Order and extend the method getCustomData with afterGetCustomData.

In your di.xml, define the plugin with:

HTML

HTML

```

```

Create a class CustomDataPlugin and implement a method:

PHP

PHP

```
/**
* Complete general getCustomData with HiPay's data
*
* @see \HiPay\FullserviceMagento\Helper\Data
* @param \HiPay\FullserviceMagento\Model\Request\Order $subject
* @param $result
* @return array
*/
public function afterGetCustomData(Order $subject, $result)
{
}
```

You can put what you want in the $result variable. You can get inspiration from our CustomDataPlugin plugin located in our module.

## Payment notifications

During the payment workflow, the order status is updated only through HiPay Enterprise notifications. The endpoint for notifications is http://yourawesomewebsite.com/hipay/notify/index .

It is protected by an encrypted passphrase: don't forget to enter it in your Magento Admin Panel and HiPay Enterprise back office.

For more information, please see the process in the Notify model.

Transaction statuses

All HiPay Enterprise transaction statuses are processed, but not all of them interact with Magento order statuses.
This process only occurs when a notification is received.

When a status is in process, a Magento payment transaction is created.
Otherwise, we just add a new order history record with notification information.

Actions according to statuses

BLOCKED (110) and DENIED (111)

* The transaction order Denied status is created.
* The transaction order is closed.
* Any invoice in Pending status is cancelled.
* The order status changes to the status selected in configuration for the current payment method. AUTHORIZED AND PENDING (112) and PENDING PAYMENT (200)

* The transaction order Authorization status is created.
* The transaction order is Pending .
* The order status changes to Pending Review .
* The invoice is not created. AUTHORIZATION REQUESTED (142)

* The transaction order is not created.
* The order status changes to Authorization Requested .
* Notification details are added to the order history. REFUSED (113), AUTHORIZATION_REFUSED (163), CAPTURE_REFUSED (163)

* The transaction order is not created .
* The order is set to the configured status.
* If an invoice exists, it is cancelled. CANCELLED (115)

* The transaction
