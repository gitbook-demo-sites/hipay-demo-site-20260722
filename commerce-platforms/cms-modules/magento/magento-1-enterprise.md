---
description: "This module is no longer supported by HiPay. This document is designed to provide you with details on how to integrate your business to the HiPay Ente"
icon: file-lines
---

# Magento 1 Enterprise

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/magento/magento-1-enterprise](https://developer.hipay.com/cms-modules/magento/magento-1-enterprise)
{% endhint %}

This module is no longer supported by HiPay.

This document is designed to provide you with details on how to integrate your business to the HiPay Enterprise Payment Gateway. It gives you step-by-step instructions on how to simply and quickly get up and running with our services as well as detailed reference material.

Please make sure you go through the CMS Prerequisites article before starting the integration.

## Module features

* 3-D Secure enabling/disabling
* One-click option configuration with custom rules
* Management of multiple cards per customer for one-click payment
* iFrame integration, hosted page and custom card API
* Mail management for transactions pending fraud validation (challenged)
* Manual and automatic capture
* Partial capture and refund
* Payment in x installments without fees
* Custom data management (easily send and view your data in your HiPay Enterprise back office)
* Use order currency for transaction if your shop is multi-currency
* Payment Means

*

## Module installation

Magento Connect

You can get the official HiPay Enterprise payment extension for Magento here . To install it, just get the extension key. Then go to your Magento administrator back office, click on System > Magento connect > Magento connect manager .

Paste the extension key under Install New Extensions and follow the steps.

General configuration

### Technical configuration

Please increase the max_inputs_vars in the php.ini of your server. An acceptable value is 5000.

Ini

Ini

```
max_inputs_vars=5000
```

By default, this value is set to 1000 and is too low to support the saving of the HiPay module configuration.
General configuration

To configure your HiPay Enterprise API credentials, you must click on HiPay Enterprise in the Magento configuration section (System > Configuration > Sales). If you have administrative rights but are not allowed to access the configuration of the payment method, please log out and log back in.

You can find your HiPay Enterprise API credentials in your HiPay Enterprise back office, under Integration > Security Settings > Api credentials .

Once you have them, put them in the module configuration with your Passphrase . (Please refer to section 2.2).

When using the Multi-site or Multi-store feature: you can use different HiPay credentials and payment methods for each Store View using the Current Configuration Scope select box. Uncheck the Use Website checkbox and specify the desired value.

### Additional parameters

Name
Description

Device fingerprint
Defines if a fingerprint is sent with the transaction (YES by default)

Use order currency for transaction*
Defines the currency used for the order. By default, orders are always processed with the base currency of the store.

If you activate Use order currency for transaction , your payment method must be configured in Sale mode. If you want to use this feature in Authorize mode and do manual captures in your back office when invoicing orders, you must develop your own invoicing and make an override of Mage_Sales_Model_Order_Invoice and register method.

If you keep the default Magento process, the transaction authorization will be processed in the currency chosen by the customer, and the capture upon invoicing in the base currency of the store.

### Cart configuration

This section addresses customer's cart items sending to the HiPay Enterprise back office during the transaction.

Enabling this option applies to all enabled payment methods on your site. The information of the customer's basket, containing the method of delivery, the discounts and each product with the quantity, as well as the SKU and the tax, is sent with the transaction.

For some payment methods, sending this information is mandatory. This option is therefore ignored if the transactions are made with this payment method. The customer's line items will be sent whether the option is activated or not. The payment methods in question are Klarna Invoice and Oney Facily Pay .

Oney's Fraud system requires additional configuration for shipping method and product categories. The configuration is explained in the following paragraph.

Please note that this feature is still in beta version. For questions relating to installation and configuration, please don't hesitate to visit our Support Center or submit a request to our Support team.

Name
Description

Send cart items
Activates customer's cart items sending or not (NO by default)

Attribute ean
EAN is not a Magento attribute by default: you must define your custom attribute if you want to send it in the basket

Load attribute*
Because EAN is not a default attribute, product loading is necessary to get the value. You can avoid loading by adding the attribute to the order and quote.

Please assume that Adjustment Fee or Adjustment Refund are not supported with baskets for refunds.

Product loading is carried into HiPay's helper, which is Data.php , when information about the product is retrieved. If you want to avoid this loading, which is not fast, please add your EAN attribute in the Quote and Order model.

There are several ways to do so. For example, you can:

* Add your attribute in the order and quote tables.

* Save your attribute in the listening observer sales_quote_save_before .

* Upgrade your config.xml to transfer the attribute to the Order with:

XML

XML

```

*

```

You can test and see the code used in the Data.php .

PHP

PHP

```
// If the store supports EAN (please set the attribute in hipay config)
if (Mage::getStoreConfig('hipay/hipay_basket/attribute_ean', Mage::app()->getStore())) {
$attribute = Mage::getStoreConfig('hipay/hipay_basket/attribute_ean', Mage::app()->getStore());

if (Mage::getStoreConfig('hipay/hipay_basket/load_product_ean', Mage::app()->getStore())) {
$resource = Mage::getSingleton('catalog/product')->getResource();
$ean = $resource->getAttributeRawValue($product->getProductId(), $attribute,
Mage::app()->getStore());
} else {
// The custom attribute has to be present in quote and order
$ean = $product->getData($attribute);
}
}
```

### CATEGORIES MAPPING

Only the top level categories are displayed and must be mapped. As long as you have not mapped a category, a warning icon is displayed and prompts you to do the mapping. If the mapping is not done, then the transaction will be refused by Oney. It is therefore important to check your mapping regularly when adding or modifying a category.

### SHIPPING MAPPING

A list of all delivery methods activated on the site is displayed. This mapping is necessary to indicate a match between your delivery methods and the delivery methods defined by HiPay. For each customer's order, depending on the chosen configuration, this information is sent as a supplement to the customer's basket.

For each mapping, you have to fill out the following information:

* Preparation delay : Estimated day time for order preparation
* Delivery delay : Estimated day time for delivery From this information, an estimated delivery day is calculated and sent with the transaction. Non-working days are not taken into account in this calculation.

As with the mapping of categories, it is important that all payment methods be mapped . Therefore, it is important to see your list if you change the configuration of your payment methods.

## PAYMENT METHODS CONFIGURATION

To configure your HiPay Enterprise payment methods, click on Payment Methods in the Magento configuration section (System > Configuration).

You will then see a list of payment methods with all the HiPay Enterprise integration possibilities.

### CREDIT CARD API

(only available for credit card and debit card payment methods)

With the HiPay Enterprise Credit Card API integration (direct API integration), customers fill in their bank information directly on the merchants' website. The module calls the HiPay Enterprise API to validate the transaction and the merchant's website displays the transaction confirmation / refused / pending message.

If this integration mode is selected, you are required to be compliant with the PCI Data Security Standard. For more information, please go to PCI-DSS Compliance & validation guide .

### C.C. SPLIT PAYMENT

(only available for credit card and debit card payment methods)

This integration can be used to process recurring payments and split order payments through APIs. It is a variant of the HiPay Enterprise Credit Card API integration. Therefore, you are also required to be compliant with the PCI Data Security Standard.

Prior to activating this integration, at least one recurring profile must be created (Please refer to section 5.6 Split payment method).

### HOSTED PAGE

To process payments, cardholders are redirected to a secured payment page hosted by HiPay.

After payment validation, customers are redirected to the merchant's website, which displays a transaction confirmation / error / pending message.

When choosing this integration, we strongly recommend you to choose the Hosted Page version 2, as it provides a better payment experience. To do so, you need to:

1 - Make sure that your HiPay Module is updated to the latest version.

2 - Go to the HiPay Entreprise section of your Magento 1 (System > Configuration > HiPay Enterprise)

3 - On the HiPay Hosted Page Management section of the Other Configurations menu, choose the Hosted Page v2 option (as below).

4 - Save the configuration

You can customize the styling of the Hosted Page v2 on HiPay Console. You can find more information in this article.

Only available for debit and credit card payment methods.

### iFrame

You can activate the iFrame mode on your HiPay Enterprise Hosted Page if you want cardholders to fill in their payment card information on a secured payment page hosted by HiPay and displayed in an iFrame inside the merchants' payment page.

Your website must run with the HTTPS protocol to use an iFrame hosted page.

This page (hosted & iFrame) can be customized with the merchants' CSS stylesheet to fit their website look and feel.

### C.C. Hosted Fields

(only available for credit card and debit card payment methods)

With the HiPay Enterprise Credit Card API Hosted Fields (direct API integration), customers complete their banking information directly on the merchant's site but the form fields are hosted by HiPay. The module calls the HiPay Enterprise API to validate the transaction and the merchant's website displays the transaction confirmation / refused / pending message.

With the HiPay Enterprise Credit Card API Hosted Fields, PCI compliance is not required.

More about Hosted fields

You can configure the following parameters specific to the HiPay Enterprise Credit Card Hosted Fields payment method:

Name color fontFamily fontSize fontWeight placeholder Color caretColor iconColor Those parameters allows you to override default CSS properties in hosted form fields.

To override the default template, please refer to the magento 1 documentation ( doc. ) and the HiPay SDK JS documentation ( doc . ).

### H.P. Split Payment

(only available for credit card and debit card payment methods)

This integration can be used to process recurring payments and split order payments using a hosted page.

Prior to activating this integration, at least one recurring profile must be created (Please refer to section* 5.6 Split payment method).

### Other payment means

If you want to offer on your website other payment methods than credit card or debit card, you can choose them directly from the list of payment methods, indicated as follows: HiPay Enterprise {payment method} (e.g.: HiPay Enterprise Sofort Uberweisung, HiPay Enterprise Sisal, etc. ).

Configuration parameters

Name Description Enabled Allows the activation of the module Title Title displayed on the front-end for the payment method Payment Profile Profile allowed if split payment is used.
Please refer to section 5.6 Split payment method . Order status when payment accepted Status to be assigned to the order Order status when payment refused Status to be assigned to the order Order status when payment cancelled by customer Status to be assigned to the order HiPay status to validate order HiPay status for a Magento transaction to be validated Redirect page pending status If the transaction result is pending, the customer can be redirected to a pending, success or failure page. Payment Action Sets the payment mode: Authorization + Capture ( Sale ) or : Authorization Only .
Must be set to Sale for split payment method. Credit Card Types Card types allowed on the payment form Display card owner Enables/disables the cardholder input field on the payment form Credit Card Verification Enables/disables Magento credit card verification Css Url URL for merchant style sheet for iFrame or Hosted page operating modes.
Important, HTTPS protocol is required. Please refer to Hosted Payment Page Page payment template For iFrame and Hosted page operating modes, you can choose your basic template to show:
Basic: Basic responsive design.
Basic-js: Advanced responsive design. Display hosted page in iFrame Activates iFrame mode on hosted page. Please refer to chapter 4.2. iFrame Height If iFrame operating mode is chosen, you can select your iFrame height to fit with your CSS. iFrame Width If iFrame operating mode is chosen, you can select your iFrame width to fit with your CSS. Wrapper iFrame Style If iFrame operating mode is chosen, you can customize the wrapper around the iFrame with your CSS. iFrame Style If iFrame operating mode is chosen, you can select your iFrame integration style to fit with your CSS. Display card selector Enables/disables the payment method selector on iFrame and Hosted pages. Enable 3D Secure Allows the activation of 3-D Secure if available on the card being used. Rules 3D Secure If you enabled 3D Secure with specific rules , set up rules to trigger 3-D Secure only when you really need it with order, customer or product attributes. Use Oneclick Allows the use of Oneclick payment (only for credit cards) Rules Oneclick If Oneclick is used, configure the rules to activate Oneclick Add product to cart Reloads the cart when payment is cancelled or refused Cancel pending order Cancels pending orders over 30 minutes (by default) Delay before cancel order Adjustment of cancelling period Send fraud payment email Alerts the client if a transaction has been challenged and requires approval Payment from applicable countries Restricted access by country Payment from specific countries List of allowed countries Minimum Order Total Minimum amount to display the payment method Maximum Order Total Maximum amount to display the payment method Sort Order Sorts the payment method order in the front-end Enable debug log Logs requests and server responses on the var/log/payment_hipay_cc.log file Enable test mode If Test mode is enabled, the module will use the HiPay Enterprise test platform.

PSD2 & SCA
As of September 14, 2019, the issuer will decide if a payment is processed depending on the analysis of more than 150 data collected during the purchasing process. Thanks to our Magento 1 module we handle most of the data without you having to develop anything. You can see all the new parameters on our explorer API .

Adding or overriding PSD2 data

The accuracy of the information sent is key for making sure that your customers have a frictionless payment process. That's why we provide you the possibility to add or override all the information related to the PSD2.

We trigger the event hipay_order_before_request that can be listened to using an Observer.

It is called with two parameters: the request sent to the HiPay API and the current cart ordered by the customer.

You can either implement the observer in your own modules or use the one that we provide. You can find this additional module on our github repository .

You can install this module in a classic way, then directly modify the file Observer.php and the method afterMapRequest to add your information.

Be careful ! If there is an update of the data module, remember to save your data so that it is not overwritten.

Finally, although we do our best to retieve all relevant data for you, we are not capable of getting the following data as it depends on the modules installed on your CMS or your workflow.

Customer

Field
Comment

password_change
By default, magento does not save the password change dates for a user.
However, you can implement this feature and add this information in the observer.

Merchant risk statement

Field

Comment

delivery_time_frame

The field is managed but only for virtual products.
We send 1 = Electronic delivery if it is downloadable or virtual product.

Depending on your carrier and delivery methods, you can refine this data.

Possible values:

1 = Electronic delivery
2 = Same day shipping
3 = Overnight shipping
4 = Two-day or more shipping

shipping_indicator

This fields is managed but you can refine the value for dematerialized products.

If the basket contains only virtual products, please provide:

5 = Digital goods
6 = Travel and event tickets, no shipping
7 = Other (gaming, digital services without shipping, e-media subscription)

pre_order_date

If you provide the possibility of pre-ordering.

Retrieve the product availability date.

gift_card

If you sell gift card products

amount
Collect the amount of gift card type gift cards purchased.

count
Collect the count of gift card type gift cards purchased.

currency
Collect the currency of gift card type gift cards purchased.

If you want to see all the parameters you are able to override, please refer to the SDK PHP Reference .

## Payment configuration

### Sale mode

When making a purchase with the sale mode, the capture is automatically requested right after the authorization. Please refer to our requestNew Order API .

If the payment fails, the customer is redirected to the error page and the status is defined as configured in the module configuration.

If the payment is successful, the customer is redirected to the success page. The invoice is then created if the configuration allows it and the status is defined as follows:

* capture_waiting

* processing

### Authorization mode

When making a purchase with the Authorization mode, the transaction will be on waiting capture . Please refer to our requestNewOrder API .

The customer is not charged directly: you have 7 days to capture the transaction and charge the customer. Otherwise, the order will be cancelled.

If the payment fails, the customer is redirected to the error page and the status is defined as configured in the module configuration.

If the payment is successful, the customer is redirected to the success page. At this step, the order status is Waiting for capture . Once you're ready to capture the transaction:

* If the configuration does not allow the creation of the invoice, you must create it from the order overview. Click on Capture online : this will send the capture information to the HiPay Enterprise server. If successful, the invoice is created. The payment is then captured and you can create your shipment.

* If the configuration allows the creation of the invoice, click on the invoice and on the capture button. This will send the capture information to the HiPay Enterprise server. If successful, the invoice status changes to Paid .

You can also do the capture directly in your HiPay Enterprise back office. The invoice will then be automatically created in your Magento back office.

### Refund

HiPay Enterprise allows online refunds. For this purpose, simply create a credit memo on the invoice (not from the order).

You have two options: Refund Offline (not relevant in our case) or Refund .

Choose the amount and click on Refund . If successful, the credit memo is created and the refund is validated.
For notification to work as expected, please refer to this section

### One-click

If the one-click option is activated, it enables your system to create an alias of the credit card. That way, after their first transaction, customers can use a saved credit card without having to fill in all the payment data again.

This option is only available if customers have created an account on your site.

### MO/TO payment

Here are the instructions to follow when merchants need to create a new order and pay it using the customer's financial information given over the phone.
Configuration

Under System > Configuration > HiPay Entreprise , fill in specific credentials for MO/TO transactions in the HiPay Enterprise credentials MO/TO section. If they are not specified, standard credentials will be used.

You can also configure the following settings.

Name
Description

Send an email to customer for paying
If YES, an email with a payment link is sent to the customer for hosted payment. If NO, the payment has to be done by the administrator in the back office.

Payment Email Sender
Chooses the sender of the email with the payment link.

Payment Template
Chooses the email template.

Under System > Configuration > Payment Methods , make sure that the HiPay Enterprise Hosted MO/TO payment method is enabled.

MO/TO payment for hosted methods

Create a new order in your Magento back office.

* Go to Sales > Create New Order .

* Add your products, account information, billing address, shipping address, payment method, shipping method, etc.

* Submit your order.

* An email is sent to the customer with a link for paying the order.

* The customer clicks on the link in the email and is redirected to the hosted payment form.

* The customer pays and is redirected to your Magento front-end (success or error page).

* The status of the order is changed to processing .

### Split payment method

Payment profile

Prior to activating a split payment method, you must create one or more payment profiles under: Sales > HiPay > Split Payment Profiles > Add payment profile .

A payment profile defines the billing cycle of an order, fo
