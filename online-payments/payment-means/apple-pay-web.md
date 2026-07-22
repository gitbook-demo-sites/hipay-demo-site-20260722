---
description: "Apple Pay offers a secure and smooth payment experience, which can be utilized in apps, physical stores, and online. It employs network tokenization a"
icon: file-lines
---

# Apple Pay - Web

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/apple-pay-web](https://developer.hipay.com/online-payments/payment-means/apple-pay-web)
{% endhint %}

Apple Pay offers a secure and smooth payment experience, which can be utilized in apps, physical stores, and online. It employs network tokenization and securely stores payment details on the user's eligible Apple device, with payments confirmed via Touch ID or Face ID.

Thanks to this documentation you will be able to start accepting Apple Pay payments on your website.

## Integration Process

### Prerequisites

#### Devices

To use Apple Pay on your devices, you need to pay attention to several things:

* The device must be on iOS 11 and later or macOS 10.13 and later.
* Your environment must be HTTPS protocol (if you want to test in development mode, use https://ngrok.com/).
* Your device must have a wallet with at least one card configured. Note

If you want to test Apple Pay in your staging environment, you need to be logged into a test Apple account and have test cards configured.

#### HiPay enablement

Apple Pay is on a supervised rollout phase, and you will need to request your Account Manager to enable it.

#### Apple Pay certificates

To accept Apple Pay on your website you need to have a certificate. As partner of Apple, we have a Payment Service Provider Certificate, that will simplify your integration. The table below shows you when you can use our certificate.

Integration

HiPay Certificate

Your own Certificate

Web Only App Only App & Web If you want to use HiPay's certificate please, check the domain validation step , if you want to use yours, please follow this documentation .

#### Default certificates

Domain validation When you have chosen to use HiPay Certificate, the only thing that you will need to do is to:

1 - Host the file Download this file and host it at /.well-known/apple-developer-merchantid-domain-association on your site.

For example, if you're validating https://test.com, make that file available at https://test.com/.well-known/apple-developer-merchantid-domain-association .

2 - Whitlist IPs Allow these Apple IP Addresses.

3 - Communicate Communicate to your Technical Account Manager once this is done.

#### Custom certificates

Step 1: Create the Merchant ID and Validate Your Domain This first step involves creating your unique merchant identifier with Apple and then proving that you own the website where Apple Pay will be offered.

1.1 - Create the Merchant ID To accept Apple Pay, you must first register a unique identifier, called a Merchant ID , for each website or app where you offer this payment method.

* Log in to your Apple Developer account .
* Navigate to the Certificates, Identifiers & Profiles section, then click on Identifiers.
* Next to the Identifiers title, click the + button.
* Select Merchant IDs from the list and click Continue.
* Fill in the Description and Identifier fields: Description: An internal name for you to easily recognize it (e.g., HiPay Production Store).
* Identifier: This ID must be globally unique. The standard convention is to use a reverse-domain name style, for example: merchant.com.hipay.{sitename}.
* Once created, your Merchant ID will appear in your list of identifiers. Best Practice

We strongly recommend creating two separate Merchant IDs:

* One for your production environment.
* One for your staging/testing environment.This ensures a secure and complete separation between your tests and live transactions. 1.2 - Add and Validate Your Domain To use Apple Pay on your website, Apple requires you to prove you control each domain where the payment button will be displayed.

* In your list of Identifiers , click on the Merchant ID you just created.
* Scroll down to the Merchant Domain Validation section and click Add Domain .
* Enter the fully qualified domain name of your site (e.g., www.your-store.com ).
* Click Download to get the verification file. The filename is apple-developer-merchantid-domain-association .
* Host this file on your server at the exact location required by Apple. It must be publicly accessible at the following URL: https://YOUR-DOMAIN.com/.well-known/apple-developer-merchantid-domain-association
* Once the file is in place, return to the Apple Developer portal and click the Verify button.
* A Verified status should now appear next to your domain name. Step 2: Generate Apple Pay certificates Two types of certificates are required to secure transactions. They are linked to your Merchant ID and must be renewed periodically.

Information

To ensure uninterrupted Apple Pay service, it is critical to renew your certificates before they expire. Please note that the two types of certificates have different validity periods:

* Payment Processing Certificate: This certificate, used by HiPay to decrypt payment data, is valid for 25 months .
* Merchant Identity Certificate: This certificate, used by HiPay to authenticate your sessions with Apple, has a shorter lifespan and must be renewed every 12 months . We strongly advise you to proactively contact your Technical Account Manager (TAM) at least one month before an upcoming expiration to coordinate a smooth renewal process and prevent any service disruption.

A. Payment processing certificate This certificate is used by HiPay to decrypt the payment data sent by Apple. Without it, we cannot process the transaction.

Creation Processe to the Certificates, Identifiers & Profil

* Log in to your Apple Developer account and go to Certificates, Identifiers & Profiles.
* In the left-hand menu, click Certificates, then click the + button.
* Under the Services section, select Apple Pay Payment Processing Certificate and click Continue.
* From the drop-down menu, select the Merchant ID you created in Step 1, then click Continue.
* Read the following instructions to create a CSR file.
* Save the CSR on your disk and continue.
* Click Choose File on the Apple Developer portal to upload it.
* Click Continue.
* The next page allows you to download your certificate. Click Download. You will receive a file named apple_pay.cer.
* You must provide this .cer file to HiPay through your back-office or the channel specified by your TAM (Technical Account Manager). B. Merchant identity certificate This certificate is used to authenticate your website session with Apple's servers. It proves that a payment session initiated from your domain is legitimate. It is used for direct communication between your server and Apple's APIs, particularly for merchant validation.

Creation Process:

* Log in to your Apple Developer account and go to Certificates, Identifiers & Profiles.
* In the left-hand menu, click Certificates, then click the + button.
* This time, under the Services section, select Apple Pay Merchant Identity Certificate and click Continue.
* Select the same Merchant ID as before and click Continue.
* Read the following instructions to create a CSR file.
* Save the CSR on your disk and continue.
* Upload this .csr file to the Apple Developer portal.
* Click Continue, then Download to get the certificate (.cer file).
* Double-click the downloaded .cer file. It will automatically be added to your Keychain Access and paired with the private key you created when generating the CSR. Step 3: Exporting and securely transmitting the certificates For our platform to process Apple Pay payments on your behalf, HiPay requires both certificates you created. Our system will use these credentials to authenticate transaction sessions and securely decrypt payment data.

You will need to provide us with two separate files.

This certificate, which includes your private key, is required for our servers to authenticate each transaction with Apple on your behalf. You must send it to us in the .p12 format.

Export Procedure (from macOS):

* Launch the Keychain Access application on your Mac.
* In the My Certificates category, find the Apple Pay Payment Processing Certificate and Apple Pay Merchant Identity Certificate you created. It should have a private key nested underneath it (indicated by a small key icon).
* Click the arrow to expand the certificate and view the private key.
* Select both the certificate and the private key line items. (Hold the Command key to select both).
* Right-click on the selected items and choose Export 2 items....
* A save dialog will appear. Choose the Personal Information Exchange (.p12) file format.
* Give the file a name and choose a location to save it.
* You will be prompted to create a strong password to protect the file. You must take note of this password, as it will need to be securely shared with HiPay via email : [email protected]

## SDK setup

To get started, include the HiPay JavaScript SDK on your HTML page. Here is the documentation to do so.

Then, create an instance of the HiPay JavaScript SDK by reading this documentation .

Now, to determine where to place the Apple Pay button, the SDK needs to know in which div to instantiate the button.

So first, add in your payment web page, a new div container where the Apple Pay button will be displayed. Make sure that the selector div is empty. And ensure that your div has a clear ID, as we will need this ID later.

HTML

HTML

```

```

Now, we need to inform the SDK that we want to instantiate an Apple Pay button. To do this , you have to call the create function with the first argument paymentRequestButton and a second one with the configuration of your Apple Pay button.
All parameters below in applePayConfig are required.

JavaScript

JavaScript

```
// Configuration
const total = {
label: 'Total',
amount: '222.50'
};

const request = {
countryCode: 'FR',
currencyCode: 'EUR',
total: total,
supportedNetworks: ['cartesBancaires','visa', 'masterCard']
};

const applePayStyle = {
type: 'plain',
color: 'black'
};

const options = {
displayName: 'YOUR COMPANY NAME',
request: request,
applePayStyle: applePayStyle,
selector: 'apple-pay-button'
};

var instanceApplePayButton = hipay.create(
'paymentRequestButton',
options
);
```

Note
The order in which you place your networks in supportedNetwork parameter will determine which netw ork will be u sed by default in the case of a cobranded board. Note that, instanceApplePayButton can be null if you display the page on an incompatible browser (e.g. Firefox, Chrome, Brave, Edge), so you should check the existence of the instance.

Below is a basic example. However, you are free to handle this case as you wish.

JavaScript

JavaScript

```
if (instanceApplePayButton) {
// The Apple Pay button is displayed
} else {
// Hide Apple Pay button
document.getElementById('apple-pay-button').style.display = 'none';
}
```

OPTIONAL

If you want to display the Apple Pay button only if a user has an active card provisioned into Wallet, you should use the onlyActiveCard parameter with your own merchant identifier or the one created by HiPay. It will automatically check if the customer has an active card and will return a nullish instance if the customer does not have an active card.

JavaScript

JavaScript

```
const options = {
...options,
onlyActiveCard: true,
merchantIdentifier: 'your-merchant-identifier'
};

const instanceApplePayButton = hipay.create('paymentRequestButton', options);
if (instanceApplePayButton) {
// Display the Apple Pay button
} else {
// Hide Apple Pay button
}
```

At the end of this step, you should see the Apple Pay button appear. However, be aware that you cannot make a payment yet.

If you don't see the Apple Pay button, please check the troubleshooting part.

### Customize the button height

By default, the JS SDK enforces a minimum and maximum height limit on the Apple Pay button of 40px and 50px , respectively.

However, these constraints can be overridden by applying a dedicated CSS rule to the HTML iframe element generated for the Apple Pay button.

You can override the minimum and/or maximum height in your CSS as follows:

CSS

CSS

```
/* we recommend to use this HTML selector */
.hipay-payment-request-button-iframe {
min-height: 25px; /* default: 40px */
max-height: 64px; /* default: 50px */
}
```

## Payment

### Explanations

To ensure HiPay has the necessary information to manage the transaction, there are several steps. Some of these steps are invisible to you but help you understand what is happening behind the scenes.

1 - Upon clicking the Apple Pay button, the Apple Pay official payment sheet appears and prompts you to authenticate using FaceID, TouchID, or your password. You can then authenticate, which will initiate the payment process. During this step, in the background, we have sent the payment information such as the amount and currency to Apple. In return, we receive an Apple Pay Token that contains everything we need. This step is invisible to you.

2 - Using your public credentials and the Apple Pay token received just before, we will generate a HiPay token, which will then be used to create the final order of the transaction within HiPay. To decrypt the Apple Pay token, we use the well-known Apple certificates. If an error occurs during steps 1 or 2, the payment will fail.

3 - Once the HiPay token is received, you can manage the creation of the order within your backend using the HiPay PHP SDK or NodeJS SDK .

### Handle payment processes

To receive a HiPay token, you need to integrate several events: a success event ( paymentAuthorized) , a failure event ( paymentUnauthorized) , and a cancellation event ( cancel ).

JavaScript

JavaScript

```
if (instanceApplePayButton) {
instanceApplePayButton.on('paymentAuthorized', function(hipayToken) {
// Handle the HiPay Token
});

instanceApplePayButton.on('cancel', function() {
// The user has cancelled its payment
}

instanceApplePayButton.on('paymentUnauthorized', function(error) {
// The payment is not authorized (Token creation has failed, domain validation has failed...)
});
}
```

* The paymentAuthorized event is triggered when the entire process has completed successfully. You will then receive the HiPay token that you should pass to your backend server.
* The paymentUnauthorized event is triggered when a problem occurs during the process.
* The cancel event is triggered when the user closes the Apple Pay payment window. To send a feedback message to the user, you need to complete the payment based on the status of the payment process. Calling completePaymentWithSuccess() will display a success message on the Apple Pay popup. Calling completePaymentWithFailure() will display a failure message on the Apple Pay popup. Therefore, you should call one or the other depending on what happens during the payment. Ensure that you call completePaymentWithSuccess() only if the creation of the order on the backend has been successful.

completePaymentWithSuccess()

completePaymentWithFailure()

You can find a basic example below

JavaScript

JavaScript

```
if (instanceApplePayButton) {
instanceApplePayButton.on('paymentAuthorized', function (hipayToken) {
// Call your backend method to create the order.
// Here, handlePayment() is just an example method.
handlePayment(hipayToken)
.then(function (response) {
// Order processed with success
// Handle response here
// and complete the payment with success state
instanceApplePayButton.completePaymentWithSuccess();
})
.catch(function (error) {
// Error during order creation
// Handle error here
// and complete the payment with failure state
instanceApplePayButton.completePaymentWithFailure();
});
});

instanceApplePayButton.on('cancel', function () {
// The user has cancelled its payment
// Handle this case here
// and complete the payment with failure state
instanceApplePayButton.completePaymentWithFailure();
});

instanceApplePayButton.on('paymentUnauthorized', function(error) {
// The payment is not authorized (Token creation has failed, domain validation has failed...)
// Handle error here
// and complete the payment with failure state
instanceApplePayButton.completePaymentWithFailure();
});
}
```

Once the events are created, make sure to retrieve the HiPay token. If that's the case, then you have completed the front-end integration.

To find out how to handle the payment on the backend, you can refer to one of these documentations:

* PHP SDK

* NodeJS SDK

## Apple Pay Multi-browsers option

HiPay's multi-browser functionality allows you to offer Apple Pay as a payment method across various web browsers (Chrome, Firefox, Edge), and not just on Safari.

### How the feature works

In browsers other than Safari, the Apple Pay button displays normally and becomes clickable for the user. Unlike Safari, the system cannot natively verify whether the user has a card stored in their Wallet before the interaction.

#### User experience

* Selection : The user selects Apple Pay on your payment page.
* QR Code : A QR code appears on the merchant's website.
* Scan & Authentication : The user scans the code with their iPhone (running iOS 18+) and confirms the payment on their mobile via the native pop-up.
* Completion : Once authenticated, tokenisation and the order process begin automatically.
Result

User mobile experience

E-commerce experience

Success

Confirmation displayed, then the pop-up closes.

The payment window closes and the user is redirected to the success page.

Failure

A red cross is displayed, then the pop-up closes.

The payment window closes and the user returns to the checkout (payment method selection).

### Integration prerequisites

* Prerequisite: You must have already integrated Apple Pay Web using the standard HiPay documentation.
* Protocol: Your environment must be HTTPS-enabled.
* iOS version: The mobile device used for scanning must be running iOS 18 or later.
* Browser: Use a browser other than Safari to enable multi-browser mode.

### Technical configuration (SDK JS)

If you are using the HiPay JS SDK, the Multi-browser' option is not enabled by default , you will need to enable it yourself.

#### Configuration options

You can customise the display via the SDK's options object:

* multiBrowsers (boolean) (default: false ): Allows you to explicitly disable the option if set to false .
* displayMode (string): Defines how the payment page is displayed in the browser. popup (default): Opens a new, separate window. Recommended to avoid conflicts with your own modals.
* modal : Displays in a modal window within your page.
* onlyActiveCard (boolean) (default: false ): If true , the button is only displayed if a card is active in the Wallet (only on Safari; returns false on other browsers). This option replaces the deprecated canMakePaymentWithActiveCard() method.
* merchantIdentifier (string) : ApplePay merchant identifier to use with the option onlyActiveCard . You can retrieve it after validating your domain with your Technical Account Manager at HiPay.

#### Example of implementation

Example of integration with Apple Pay using the multi-browser option :

JavaScript

JavaScript

```
const total = { label: 'Total', amount: '222.50' };
const request = { countryCode: 'FR', currencyCode: 'EUR', total: total, supportedNetworks: ['cartesBancaires','visa', 'masterCard'] };
const options = { displayName: 'YOUR COMPANY NAME', request: request, selector: 'apple-pay-button', multiBrowsers: true, displayMode: 'modal' };
var instanceApplePayButton = hipay.create('paymentRequestButton', options);
```

Example of integration with Apple Pay using the multi-browser option, which only displays the button to users with an active card (on Safari only):

JavaScript

JavaScript

```
const total = { label: 'Total', amount: '222.50' };
const request = { countryCode: 'FR', currencyCode: 'EUR', total: total, supportedNetworks: ['cartesBancaires','visa', 'masterCard'] };
const options = { displayName: 'YOUR COMPANY NAME', request: request, selector: 'apple-pay-button', onlyActiveCard: true, merchantIdentifier: 'com.your-store.www' };
var instanceApplePayButton = hipay.create('paymentRequestButton', options);
```

### Further information

CSP (Content Security Policy) :

No changes to your CSP rules are required . The Apple Pay SDK is loaded into an iframe managed by HiPay.

## JS SDK Reference

### hipay.canMakePaymentsWithActiveCard(merchantID)

Deprecated : This method is deprecated. You have to use the option onlyActiveCard of the paymentRequestButton instance now.
The parameter merchantID is also replaced by the option merchantIdentifier of the same instance.

Call this method in order to check if the customer's device supports Apple Pay and if the customer has an active card in his ApplePay Wallet.

This method requires a merchant identifier as parameter. You can retrieve it after validating your domain with your Technical Account Manager at HiPay.

JavaScript

JavaScript

```
var merchantId = 'your_apple_merchant_id'; // in the form of 'merchant.com.hipay.yourmerchantname'
hipay.canMakePaymentsWithActiveCard(merchantId).then((canMakePayments) => {
if(canMakePayments) {
var instance = hipay.create('paymentRequestButton', options);
} else {
// Apple Pay is not available on this device or no active card is set up in the Apple Pay Wallet
}
});
```

### hipay.create(type, options)

Create a hostedfield instance for Apple Pay.

JavaScript

JavaScript

```
var instance = hipay.create('paymentRequestButton', options);
```

### instance.update(options)

Update Apple Pay instance options.

JavaScript

JavaScript

```
var instance = hipay.create('paymentRequestButton', options);

options.request.total.amount = "10.09"; // New amount

instance.update(options)
```

### Options

Name Type Description request

required

object A request which includes information about the payment. applePayStyle object The Apple Pay button can have multiple appearances (buy, subscribe, donate...) See the ApplePayStyle section below for more details. displayName string A string of 64 or fewer UTF-8 characters containing the canonical name for your store, suitable for display. selector string Unique div id to generate the button.
multiBrowsers boolean Allow ApplePay on multi browsers (other than Safari). Defaults is false .
displayMode string Dis
