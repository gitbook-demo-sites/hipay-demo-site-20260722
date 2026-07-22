---
description: "The HiPay Enterprise module for PrestaShop 1.7.x / 8.x is a PHP module which allows you to accept payments in your PrestaShop online store, offering i"
icon: file-lines
---

# PrestaShop Enterprise

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/prestashop/prestashop-enterprise](https://developer.hipay.com/cms-modules/prestashop/prestashop-enterprise)
{% endhint %}

The HiPay Enterprise module for PrestaShop 1.7.x / 8.x is a PHP module which allows you to accept payments in your PrestaShop online store, offering innovative features to reduce shopping cart abandonment rates, optimize success rates and enhance the purchasing process on merchants' sites to significantly increase business volumes without additional investments in the PrestaShop e-commerce CMS solution.

Please make sure you go through the CMS Prerequisites article before stating the integration.

Compatible from Prestashop Version: 1.7.6.x

The plugin and its changelog are available on our GitHub .

## Module features

* 3-D Secure enabling/disabling
* One-click option configuration with custom rules
* Management of multiple cards per customer for one-click payment
* Available integration types: iFrame, Hosted Page, Hosted Fields and API
* Mail management for transactions pending fraud validation (challenged)
* Manual and automatic capture
* Partial capture and refund
* Custom data management (easily send and view your data in your HiPay Enterprise back office)
* Payment Means

## PrestaShop module management

Get the installation package

Recommended solution

Download the ZIP package package-ready-for-prestashop/hipay-enterprise-2.X.X.zip_ available in the hipay/hipay-enterprise-sdk-prestashop project.

Alternative solution

Download the latest release in the release section: https://github.com/hipay/hipay-enterprise-sdk-prestashop/releases .

* Open your ZIP package and extract the project on your desktop.
* Execute build-package.sh with a version number in the ./build-package.sh parameter.
* Voila! hipay-enterprise.zip is now in the folder. Upload the module via PrestaShop module management

To install it in your PrestaShop administrator back office, click on Modules -> Modules & Services -> Upload a module .

Choose the package and click on Upload this module .

Upload the module via FTP (SFTP)

You must have a file transfer software like FileZilla for example.

* Open your software and connect to your FTP (SFTP).
* Go to the root of your PrestaShop project.
* Transfer the hipay_enterprise source module in the /modules/ folder.
* Add write permissions recursively to the folder hipay_enterprise (766). Install the module in the PrestaShop back office

With PrestaShop 1.7.X or 8.X , the module is automatically installed after being uploaded via the back office.

## Module configuration

Access to configuration

PrestaShop 1.7 / 8

To configure your HiPay Enterprise module, click on Modules -> Modules in your PrestaShop back office, then on Installed modules :

## Gateway configuration

This setting is very important: it allows to define whether payments will be executed on the HiPay test or production platform. By default, the module is in TEST mode. In test mode, payments are therefore not actually executed.

We strongly advise you to perform tests before launching your site in production mode.

### Production configuration

Use this interface to specify the credentials linked to your HiPay account. These identifiers are used if your module is configured in production mode.

Generated in your HiPay Enterprise back office (go to Integration => Security Settings => Api credentials => Credentials accessibility), these API credentials are required to use the HiPay Enterprise module.

Account (Private)

Private credentials are used to process payments on the HiPay API. These identifiers are mandatory.

Tokenization (Public)

Public credentials are used as part of the JavaScript tokenization. These identifiers are to be specified only if you can use the module in API mode and if your infrastructure is PCI compliant.

MO/TO account credentials

If defined, these identifiers will be used when making payments via the back office.

### Sandbox configuration

The interface is similar to the production configuration. These identifiers are used if your module is configured in test mode.

### Hash Algorithm

The hash algorithm is used when checking the signature. You can configure it in your back office Hipay the algorithm of your choice.

This interface makes it easy to synchronize the configuration made on your back office HiPay.

Configurations are retrieved from your identifiers in Production configuration and Sandbox configuration

### Proxy settings

When your server is behind a proxy, you must populate the information so that the modules can communicate with the HiPay Gateway. Retrieve this information from your host and fill in the following information: Host, Port, Username and password.

### Notifications

When orders are created from your merchant website, HiPay will send some specific notifications to your server according to the provided URL during the API request to make orders.

These notifications are useful to update the orders of your side in order to synchronize the status between HiPay and your Prestashop. If you want to know more details, you can check the page about HiPay notifications .

When your server is receiving notifications, and if the notifications are handled without troubles, a message could be sent to the Prestashop order related to the notification. This message is sent only if you enable the Enable order message on notification option which is available in the Technical configuration section of your module settings.

Also, you can set up the Enable notification cron option in order to handle notifications asynchronously on your server side. Check the notification cron part to see more about this notification mode.

## PSD2 & SCA

As of September 14, 2019, the issuer will decide if a payment is processed depending on the analysis of more than 150 data collected during the purchasing process. Thanks to our Prestashop 1.7.x / 8.x module we handle most of the data without you having to develop anything. You can see all the new parameters on our explorer API .

Adding or overriding PSD2 data

The accuracy of the information sent is key for making sure that your customers have a frictionless payment process. That's why we provide you the possibility to add or override all the information related to the PSD2.

We trigger the event actionHipayApiRequest that can be listened to using another module .

It is called with two parameters: the request sent to the HiPay API and the current cart ordered by the customer.

You can either implement the observer in your own modules or use the one that we provide. You can find this additional module on our github repository .

You can install this module in a classic way, then directly modify the file hipay_enterprise_data.php and the method hookActionHipayApiRequest to add your information.

Be careful ! If there is an update of the data module, remember to save your data so that it is not overwritten.

Finally, although we do our best to retieve all relevant data for you, we are not capable of getting the following data as it depends on the modules installed on your CMS or your workflow.

Merchant risk statement

Field Comment delivery_time_frame The field is managed but only for virtual products.
We send 1 = Electronic delivery if it is downloadable or virtual product.Depending on your carrier and delivery methods, you can refine this data. Possible values:

1 = Electronic delivery
2 = Same day shipping
3 = Overnight shipping
4 = Two-day or more shipping

shipping_indicator This fields is managed but you can refine the value for dematerialized products.

If the basket contains only virtual products, please provide:

5 = Digital goods
6 = Travel and event tickets, no shipping
7 = Other (gaming, digital services without shipping, e-media subscription)

gift_card If you sell gift card products gift_card[amount] Collect the amount of gift card type gift cards purchased. gift_card[count] Collect the count of gift card type gift cards purchased. gift_card[currency] Collect the currency of gift card type gift cards purchased. If you want to see all the parameters you are able to override, please refer to the SDK PHP Reference .

## Module settings

### Mapping

The customer's basket information can be sent during the transaction if you enabled the option in the global settings. This mapping is necessary to establish a correlation between your data and HiPay's. It is mandatory to do all the mappings to use the Oney Facily Pay or Klarna payment methods. If you add new categories or delivery methods, make sure to match the new corresponding data.

Category mapping

Top-level product categories are displayed. You must match each of them with the corresponding HiPay categories.

All sub-categories will also be mapped when you commit your matchings.

Carrier mapping

All the delivery methods active on your shop are listed. For each of them, you must fill in the necessary corresponding information.

This information is used to calculate an approximate delivery date.

Name Description Value Order preparation estimated time Estimated time to prepare your orders Time of day Delivery estimated time Estimated time for delivery Time of day HiPay delivery mode Delivery mode - store : At the store
- carrier : Delivery by carrier
- relaypoint : Delivery in a pick-up location
- electronic : To be filled in
- travel : To be filled in HiPay delivery method Delivery method - standard
- express
- Priority 24H
- Priority 2H
- Priority 1H
- Instant

### Fraud screening

Based on the screening results of HiPay's Fraud Protection Service, when a transaction is suspected of being fraudulent, it is in challenged status.

## Payment methods

After configuring the necessary information, this interface allows you to set the payment methods that will be available to your customers.

### Global settings

This general configuration will be applied whatever the payment methods being used.

Name Description Value Operating mode Defines if the payment form is displayed on the merchant's site or on a HiPay payment page. - Hosted Page : Customers are redirected to a secured payment page hosted by HiPay.
- Hosted Fields : The customer completes his payment directly on the merchant's site. If the payment method requires some banking information, the form fields will be hosted by HiPay. Capture Defines if payments should be captured manually or automatically. Manual capture will be possible either on the order page of the PrestaShop back office or on the HiPay Enterprise back office. Please refer to the section on Capture mode . - Manual : All transactions will be captured manually either from your HiPay Enterprise back office or from your PrestaShop back office.
- Automatic : All transactions will be captured automatically. Use One-click If the One-click option is enabled, customers will be able to use a saved credit card for their next transactions and won't need to fill in all the payment data again. Yes/No Customer's cart sending The customer's basket will be sent during the transaction. If this option is enabled, you will be able to make captures and refunds on items from an order. Yes/No Keep cart when payment fails Defines if the client's basket must be reloaded when an error occurs during payment. Yes/No Enable technical logs Activates debug logs. Yes/No Preserve GPDR data in logs If so, then customer's informations will not be informed inside logs. Only available if technical logs are enabled. Yes/No Activate 3-D Secure Enables and configures 3DS rules. You can choose between 5 options:
- Disabled (to bypass 3-D Secure authentication)
- Try to enable for all transactions
- Try to enable for configured 3ds rules
- Force for configured 3ds rules
- Force for all transactions Send url Notification If so, then the URL of your website is sent during the payment and notifications will be sent to this URL. Yes/No

### Hosted page

You can choose the HiPay Hosted Page on the MODULE MANAGEMENT > HIPAY MODULE > PAYMENT METHODS section of the Prestashop BO.

Once you have chosen the Hosted Page, you can activate the version 2 by following the next steps:

1 - Make sure that your HiPay Module is updated to the latest version.

2 - Go to the MODULE MANAGEMENT > HIPAY MODULE > PAYMENT METHODS section of the Prestashop module.

3 - E nable the API V2 (see image below).

4 - Save the configuration.

We strongly recommend you to to use the Hosted Page version 2, as it provides a better payment experience and it is fully customizable on HiPay Console. You can find more information in this article.

If you have installed the module after October of 2021, the Hosted Page v2 is your default version. Otherwise, you can start using the V2 by setting the version to Hosted Page v2.

When you choose the Hosted page option as operating mode, you have access to additional settings.

Name Description Value Enable API V2 If so, then the new HiPay hosted payment page will be used instead of the old one.

Yes/No Display hosted page Defines if the hosted page is displayed in an iFrame or with a redirect.

Useful for the version 1 and 2.

-redirect
-Iframe Display card selector Shows card selector on the hosted page.

Only useful for the version 1.

Yes/No CSS URL URL of your CSS (cascading style sheet) to customize your hosted page or iFrame

Only useful for the version 1.

Https URL

### Hosted fields

When you choose the Hosted Fields option as operating mode, you have access to additional settings.

Name color fontFamily fontSize fontWeight placeholder Color caretColor iconColor Those parameters allows you to override default CSS properties in hosted form fields.

To override the default template, please refer to the PrestaShop documentation ( doc. ) and the HiPay SDK JS documentation ( doc. ).

### Credit card

This section allows you to configure payment cards. By default, all card types are enabled and set to default. For each type of card, you can then define a different configuration.

Name Description Value Activated Allows or not customers to use this type of card. Yes / No
If the card type is not activated, customers will have a warning message upon payment, inviting them to use another type of card. Minimum order amount Indicates a minimum threshold for the type of card available for payment. Amount with default currency
If the amount is not reached, customers will have a warning message upon payment, inviting them to use another type of card. Maximum order amount Indicates a maximum threshold for the type of card available for payment. Amount with default currency
If the amount is not reached, customers will have a warning message upon payment, inviting them to use another type of card. Currencies Currencies for which the card type will be activated. These are the installed and active currencies on your shop Selection of one or more currencies Countries Countries for which the card type will be activated Selection of one or more countries

### Local payments

Local payments include all payments other than bank cards. Through this interface, you can activate payment methods like Oney Facily Pay, PayPal, SEPA Direct Debit, etc.

Configuration is done as for credit cards, except for certain local payments: currencies and countries cannot be modified.

You can also define the following elements for each payment method:

Name Description Value Display name Name displayed on the PrestaShop checkout page String Front positioning Allows you to display payment methods. Number

## Payment Configuration

### Captures

With the HiPay module, you will have the choice between two capture modes: automatic mode and manual mode.

#### Automatic mode

When making a purchase in automatic mode, the capture is automatically requested right after authorization. You don't have to do anything. The money will be directly deducted.

* If the payment fails, the customer is redirected to an error page and the status is defined as CANCELED .
* If the payment is successful, the customer is redirected to the success page and the status is defined as CAPTURE REQUESTED . For more information about requesting a new order (operation), please refer to our Developer Portal .

#### Manual mode

When making a purchase in manual mode, the transaction status will be AUTHORIZED until you ask for the capture. Customers are not charged directly: you have 7 days to capture the order and charge the customer. Otherwise, the order is canceled.

* If the authorization fails, the customer is redirected to an error page and the status is defined as CANCELED .
* If the authorization is successful, the customer is redirected to the success page and the status is defined as AUTHORIZED . For more information about requesting a new order (operation), please refer to our Developer Portal .

#### How to Manual Capture

To manually capture a transaction in your PrestaShop back office, go to Orders -> Orders and select any order. The order status should be Payment authorized .

Further down the page, you will find the HiPay actions section, specifically the Capture management part. This is where you can manually capture your orders.

A capture can be complete or partial .

Complete capture Complete means that the entire order will be captured.

Partial capture Partial means that only part of the order will be captured. And there are two types of partial capture:

* Partial with basket : the amount to be captured will be determined based on the selection of items from the order. This type of capture maintains a link between the amount to be captured and the cart. T he products in the customer's basket are displayed with the unit prices and the number of products that can be captured. You can capture delivery charges and applicable discounts, and choose the number of products to capture. The amount is updated based on the number of selected items If the customer basket is not sent with the transaction, then the partial capture will be executed like a partial capture without basket. You can change this parameter in your HiPay module configuration

* Partial without basket : The amount to be captured is flexible. There is no longer a link with the basket. It is up to you to capture the amount you want. Once a partial capture without basket has been made, the amounts will be dissociated from the basket. It will no longer be possible to make captures with basket and refunds with basket.

Once the first capture is done, the order status changes to Payment accepted . The remaining amount to be captured and the amount already captured are updated.

You can also do the capture directly in your HiPay Enterprise back office. The order will be automatically updated in your PrestaShop back office. It only works for total captures or partial captures without basket.

#### Invoice

When the capture is complete, and only when the capture is complete, an invoice will be generated for the completed order. You will find it on the order page in the Documents section.

### Refunds

To refund a transaction in your PrestaShop back office, select Orders -> Orders and select any order. The order status should be Payment accepted .

According to your settings on our module, you could use the default refund formular of Prestashop or use our custom formular, and we recommend to use ours for more flexibility on your refunds.
If you want to use the Prestashop formular, you have to go to our module settings > Technical configuration , then enable the Use PrestaShop default refund form option.

Further down the page, you will find the HiPay actions section, specifically the Refund this order part. This is where you can refund your orders.

Like capture, a refund can be complete or partial :

#### Complete refunds

Complete refund means that the entire order will be refunded.

###

#### Partial refunds

Partial means that only part of the order will be refunded. And there are two types of partial capture:

* Partial with basket : the amount to be refunded will be determined based on the selection of items from the order. This type of refund maintains a link between the amount to be refunded and the cart. T he products in the customer's basket are displayed with the unit prices and the number of products that can be refunded. You can refund delivery charges and applicable discounts, and choose the number of products to refund. The amount is updated based on the number of selected items
*
* Partial without basket : The amount to be refunded is flexible. There is no longer a link with the basket. It is up to you to refund the amount you want. Once a partial refund without basket has been made, the amounts will be dissociated from the basket. It will no longer be possible to make refunds with basket and captures with basket.

Once the first refund is done, the order status changes to Partially refunded . The remaining amount to be refunded and the amount already refunded are updated.

You can also do the refund directly in your HiPay Enterprise back office. The order will be automatically updated in your PrestaShop back office. It only works for total refunds or partial refunds without basket.

#### Order slip

For each refund, an order slip is generated in the Documents section of the order page. A full refund, as well as a partial refund with basket, will generate a proper order slip. This means that the order slip will list the refunded items, quantities, and the various refunded amounts.

However, a partial refund without basket will generate an order slip with only the amount as the sole line item. Since in this type of refund the basket is decoupled from the amount, we use a random item and associate the indicated amount to allow the generation of this order slip.

To refund a gift wrapping, it is preferable to associate it with a product to have it appear on the final order slip.

### MO/TO Payment

To make an order for your customers in a MO/TO process and thus use the correct ECI and the identifiers you have entered in the module configuration you will need:

* In the Summary tab of the order before confirming the order, enter the value of Payment with Hipay Ent
