---
description: "The HiPay SFRA Integration is pretty simple and straightforward. Here you have the configuration that you need to set in the backoffice in order to st"
icon: file-lines
---

# SFCC Configuration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/salesforce/sfcc-configuration](https://developer.hipay.com/cms-modules/salesforce/sfcc-configuration)
{% endhint %}

The HiPay SFRA Integration is pretty simple and straightforward. Here you have the configuration that you need to set in the backoffice in order to start using it.

## Set up

Go to: Administration > Organization > Roles > Administrator - Business Manager Modules

* Select your site context and press Apply
* Check HiPay Integration module and press Update.
* Go to the Business Manager> Merchant Tools > HiPay module should be displayed.

## Module Configuration

### Site Preferences

Go to: Merchant Tools > Site Preferences > Custom Site Preferences > HiPay Settings

Property name

Possible values

Default

Description

Hipay Enabled

true / false

false

Enable/disable HiPay functionality

Enable One-Click payments

true / false

false

Enable/disable One-Click payments

HiPay Operation Mode

hosted (Hosted page)

iframe (IFrame)

api (API)

hosted

Defines the payment integration to be used.

Enable Tokenization Test Mode

true / false

false

If enabled, the module will use the Hipay TPP test platform

3D Secure

0 (Bypass 3-D Secure 3-D authentication)

1 (3-D Secure authentication if available)

2 (3-D Secure authentication mandatory)

0

Allows the activation of 3D secure if available on used card

3D Secure Threshold Rule

Integer

0

If the Order total is higher than the specified sum, then 3D Secure will be forced. If 0 is specified, the rule is disabled.

HiPay API Signature Passphrase

String

API Signature passphrase configured in HiPay backoffice. Use to verify the requests made to SFCC.

Payment Action

Sale (Authorization + Capture)

Authorization (Authorization Only)

More information about the capture here . iFrame Height

Integer

750

If iFrame operating mode is chosen, you can select your iFrame height to fit with your CSS

iFrame Width

Integer

950

If iFrame operating mode is chosen, you can select your iFrame width to fit with your CSS

HiPay CSS content

Text

CSS applied to either Hosted or iFrame page

Display card selector

true / false

false

Enable/disable the payment methods selector on iFrame and Hosted page

Hung Order Cleanup Time

Integer

30

The time in minutes after which all Orders hung in status CREATED that are left by the payment processing are cleaned.

List of shipping methods

String

A comma-separated list of the shipping methods that should be in use for the Oney payment method.

In the HiPay CSS content field enter the CSS that is to be used on the payment page . After completing this configuration, the applied CSS should be visible. The content of this preference is printed via a controller called HiPayResource-Style and its URL (e.g. http://*domain.name*/on/demandware.store/Sites-*site.name*-Site/default/HiPayResource-Style ) is sent when calling the HiPay service, which in turn adds this CSS in the header section of the iFrame or hosted page so it can be applied.

The CSS used must be plain (@include syntax is not supported) and any <style> tags must be omitted.

### Payment means

Go to: Merchant Tools > Ordering > Payment Methods

All possible HiPay payment methods have been added to the BM. In order to function in Salesforce Commerce Cloud, they must also be activated in the HiPay application. In addition, every payment method has a custom field HiPay Product Name' which is sent with every order request to HiPay service.

For example, there are 8 payment methods available for Oney Facility Pay. 4 of them (with HOSTED prefix in payment method name) are in use in case if a custom site preference HiPay Operation Mode' is set to Hosted or Iframe. The payment-product depends on the contract the merchant has with Oney or with any other payment method. It will be the merchant responsibility to configure the right one. Every payment method must be configured and enable on the HiPay side first.

### Payment processors

Go to: Merchant Tools > Ordering > Payment Processors

There are two payment processors added for HiPay - HIPAY_HOSTED and HIPAY. The hosted is used only for the hosted and iframe solution. HIPAY processor is used for the HiPay API integration. It is used for all different types of payments like credit cards, IDEAL, ING HomePay, Giropay, KLARNA, etc.

### Logs

Go to: Administration > Site Development > Development Setup

The following logs can be found related to the HiPay implementation:

* service-HIPAY-REST-*service*-blade1-3-appserver-*date*.log - logs HiPay services specific information
* error-blade1-3-appserver-*date*.log - logs Salesforce Commerce Cloud errors
* customerror-blade1-3-appserver-*date*.log - logs Salesforce Commerce Cloud custom errors Select logs and enter you BM credentials if needed.

HiPay Fullservice sends notifications for each event that occurs. In order to handle all notifications, notes are added to the order. There should be one event logged for each notification.

## Product Configuration

Go to: Merchant Tools > Products and Catalogs > Products .

For the PSD2 security standards, orders with dematerialized products (immediate delivery) needs to be identified during the payment. The module adds a custom attribute Product Dematerialized in a new section called Dematerialization Attributes, dedicated to this requirement. All your dematerialized products must have this custom attribute value set to Yes.

Open the product of your choice and scroll to the bottom of the page to add on of the following 3 possible values:

* -None- : The default value, when it is not defined yet. Acts as No value.
* No : The product is not dematerialized. It needs to be physically delivered to the customer, generally in days.
* Yes : The product is dematerialized. It could be electronically delivered to the customer, generally in minutes. In order to set the value, Lock your product for edition. Then, at the right of Product Dematerialized , click the select list and choose the correct value. Then, click Apply button at the bottom of the screen. Do not forget to Unlock your product for other BM users.

## Business Manager

### Capture

Go to: HiPay Integration > Order capture

The Order capture page of the HiPay Integration allows you to capture amounts for already authorized orders. In order to capture a transaction you need to e nter an order ID and press Load.

Partial or full capture can be requested. If the requested amount is captured, this will send a HiPay notification to Salesforce Commerce Cloud and the Capture amount will be updated.

### shipping

Go to: HiPay Integration > Shipping Configuration.

In order to make sure Oney works, you need to complete this mapping. In case if a SFCC shipping method is not configured - the Oney payment method will not be rendered if the not-configured shipping method selected on the shipping page.

This page allows to configure SFCC shipping methods with HiPay's delivery methods. The Order preparation estimated time' and Delivery estimated time' fields use Integer, meaning 1 is one day, 2 is two days etc. Once shipping methods, save configuration.

### Category

Go to: HiPay Integration > Category Configuration.

In order to make sure Oney works, you need to complete this mapping. In case if a SFCC category is not mapped - the Oney payment method will not be rendered if basket contains at least one product with not configured category.

This page allows to map SFCC product categories with HiPay's categories. Once categories mapped, save configuration.

## Services

Go to : Administration > Operations > Services

Salesforce B2C Commerce provides a web services framework that helps you manage calls to web services and analyze service performance. You need custom code to interact with a web service. We recommend that you use secure protocols as web service types, such as HTTPS, SFTP, and SOAP over TLS. A web service can also use a service credential, such as username and password, to perform HTTP basic authentication.

### Credentials

You will need to update the services credentials values User and Password. You can take these values from the Hipay Dashboard, under Integration > Security Settings > Api credentials. Please note that two kind of values exists:

Private Accessibility

* hipay.hosted.cred
* hipay.maintenance.cred
* hipay.order.cred Public Accessibility

* hipay.token.cred

### Profile

By default, all services are using the below Profile configuration.

Name : hipay.prof

Timeout (ms) : 5.000

Enable Circuit Breaker : True

Max Circuit Breaker calls : 10

Circuit Breaker Intervals (ms) : 5.000

Enable Rate Limit : True

Max Rate Limit Calls : 10

Rate Limit Interval (ms) : 10.000

The circuit breaker suspends platform calls to a web service if a certain number of calls fail within a specified time interval. It can be easily changed for different merchants. A different/ a separate Profile can be added for each service.

### Service creation

There are four services implemented. Each one corresponds to a different HiPay service, as follows:

* hipay.rest.createtoken - handles the credit card tokenization (credentials hipay.token.cred)
* hipay.rest.hpayment - handles the hosted payment calls (credentials hipay.hosted.cred)
* hipay.rest.maintenance - handles the order updates after being placed (credentials hipay.maintenance.cred)
* hipay.rest.order - handles placing order (credentials hipay.order.cred)

### Multiple account

In order to configure sandbox for multiple HiPay accounts you need duplicate previous services with new names:

* hipay.rest.createtoken.{siteID}
* hipay.rest.hpayment.{siteID}
* hipay.rest.maintenance.{siteID}
* hipay.rest.order.{siteID}

Where siteID is the ID of the site for which you wish to add a new HiPay account. Services without a siteID in the service name should be deleted as, they will not become default services, in case a specific service cannot be found in BM. You can use the hipay.prof profile for those services or you can create a new one in order to make customizations in future for specific site. Also, you will need duplicate default credential.

Update them with a new name, HiPay account username and credentials. This is an example mapping for each service which credential should be assigned:

* hipay.rest.hpayment.SiteGenesis service - hipay.hosted.cred.SiteGenesis credential
* hipay.rest.createtoken.SiteGenesis service - hipay.token.cred.SiteGenesis credential
* hipay.rest.order.SiteGenesis service - hipay.order.cred.SiteGenesis credential
* hipay.rest.maintenance.SiteGenesis service - hipay.maintenance.cred.SiteGenesis credential

## Schedules

Two new job processes are implemented for HiPay.

Go to: Administration > Operations > Jobs (previously Job Schedules).

### ClearHungOrder

A ClearHungOrder job process is implemented, which is used to clear all orders that have been started with a HiPay hosted solution but have not been completed within the configured time period.

Under the Job Steps tab (previously Step Configurator), change the scope in order to assign the job to your site. Under the Schedule and History tab, you can also check that the job is active and review the Run Time settings for its automatic execution.

### HiPayClear

A HiPayClear job process is also implemented, which is used to clear custom objects that are useless after a time period.

Under the Job Steps tab (previously Step Configurator), change the scope in order to assign the job to your site. Under the Schedule and History tab, you can also check that the job is active and review the Run Time settings for its automatic execution.

## Out of scope

With the current version you cannot refund the orders or cancel them. Y ou can use HiPay Backoffice and HiPay APIs to do it.
