---
description: "Accept payments in your own iOS (iPhone/iPad) application thanks to the HiPay iOS SDK. This integration allows you to accept payments in your iOS app "
icon: file-lines
---

# iOS - SDK Configuration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/ios/ios-sdk-configuration](https://developer.hipay.com/mobile-payments/ios/ios-sdk-configuration)
{% endhint %}

Accept payments in your own iOS (iPhone/iPad) application thanks to the HiPay iOS SDK.

This integration allows you to accept payments in your iOS app very quickly.

## Prerequisites

Build settings

The iOS target version is 9.0, which means that the SDK won't build on applications targeting a lower version of iOS.

Credentials

You need to generate API credentials in order for the SDK to send requests to the HiPay Enterprise platform.

Warning : credentials included in the iOS SDK must have a public accessibility, NOT a private accessibility.

To be sure that your credentials have the proper accessibility:

* Go to the Integration section of your HiPay Enterprise back office.
* Then, click on Security Settings .
* Scroll down to Api credentials .
* Click on the edit icon next to the credentials you want to use.
* Finally, make sure that the credentials are set up . Credentials accessibility

Your credentials must be granted to:

* Tokenize a card
* Get transaction details
* Process an order
* Create a payment page

## Workflow

Authentication

In order for our iOS SDK to process transactions with users' payment details on the HiPay Enterprise platform, you must provide the SDK with credentials (Configuration section).

Also, for each order processed by the iOS SDK, the HiPay Enterprise platform must authenticate the call and validate that the merchant has allowed it. To do so, HiPay Enterprise leverages a signature mechanism. Once your app needs to process a payment, it must contact your own server in order to get a signature, specific to the order to be processed. ( Signature section)

Order processing

Order information should not be generated on the client side. Most of the time, orders are generated on the server side (on your servers), following actions performed by your users on your mobile app. The HiPay Enterprise SDK for iOS allows you to present a payment page to your users and process transactions directly on your mobile app.

Thus, your mobile app will receive a confirmation with a transaction status indicating that the payment was successfully completed. You may display a confirmation screen upon this confirmation, but you must not process order on the server side following this confirmation. For security reasons, orders must always be confirmed on your systems following the server-to-server notification.

## Signature calculation

The signature is the hash of these four parameters concatenation:

* Order ID
* Amount (formatted with two decimal places, example: 72.10)
* Currency
* Secret passphrase The signature has to be generated beforehand on the server side in order not to show the secret passphrase in client code. This is the reason why the code examples below are executed in PHP/Python on your servers and not embedded in the iOS app directly.

Please find below some code examples for signature generation. Note that we chose the SHA-1, you need to adapt your server side code accordingly to the hashing algorithm you selected.

PHP
Python

PHP

```

Python

```
import hashlib
orderId = 'TEST_89897'
amount = 14.1
currency = 'EUR'
passPhrase = '32JUWB3veDWWmHySNJvtvPyBnqrDFEHbaP3jr'
signature = hashlib.sha1(orderId + '{0:.2f}'.format(amount) + currency + passPhrase)
print(signature.hexdigest())
```

The codes above generate a signature which is to be used by the HiPay Enterprise SDK for iOS.

To get the secret passphrase of your account, go to the Integration section of your HiPay Enterprise back office, then to Security Settings.

You may choose a secret passphrase if you don't have one already. This passphrase is also used to process server-to-server notifications.

## Installation

You have to use CocoaPods to install the HiPay Enterprise SDK for iOS.

Using CocoaPods

Add this line to your project's Podfile :

```
pod 'HiPayFullservice'
```

Then, run the following command in the same directory as your Podfile :

```
pod install
```

This will install the core wrapper components as well as the built-in payment screen and other utility components.

## Configuration

You need to follow all the steps below before integrating the payment workflow.

### Import header files

First and foremost you need to add this line in order to use the SDK in an Objective-C app:

Objective-C

Objective-C

```
#import
```

In the case of a Swift project, you must rely on an Objective-C bridging header to expose this framework (Objective-C files).

### Configure the SDK

Then, you need to provide the SDK with a few parameters, such as the credentials and targeted environment.

Credentials

Get a valid HiPay Enterprise API username and password. If you don't have any, please refer to the Prerequisites and recommendations section.

Determine your app URL scheme

Sometimes, your users may be redirected to web pages, for example to follow the 3-D Secure workflow or to process payments with payment methods which cannot be natively supported by the SDK.

To do so, the SDK presents your users with a SafariViewController web page. Eventually, your users will be redirected back to your app using an app URL scheme .

To find your app URL schemes, open your Xcode project settings:

* Make sure that your app project is selected

* Open the Info tab

* Expand the URL Types section

* You can then either re-use an existing scheme or create a new one. To do so, click on the + button

* Fill out the form by setting a proper identifier and a URL scheme

* Eventually, you will need to use one of the values defined in the URL Schemes field.

Set up the configuration

The following code allows you to configure the SDK. We recommend putting it in your App Delegate s application:didFinishLaunchingWithOptions: method implementation.

Objective-C
Swift

Objective-C

```
// AppDelegate.m - application:didFinishLaunchingWithOptions:

[[HPFClientConfig sharedClientConfig] setEnvironment:HPFEnvironmentStage
username:@"YOUR API USERNAME"
password:@"YOUR API PASSWORD"
appURLscheme:@"myshoppingapp"];

/** Optional
[[HPFClientConfig sharedClientConfig] setPaymentCardStorageEnabled:YES withTouchID:YES];

[[HPFClientConfig sharedClientConfig] setPaymentCardScanEnabled:YES];
**/
```

Swift

```
// AppDelegate.swift - application:didFinishLaunchingWithOptions:

HPFClientConfig.shared()
.setEnvironment(HPFEnvironment.stage,
username: "YOUR API USERNAME",
password: "YOUR API PASSWORD",
appURLscheme: "myshoppingapp")

/** Optional
HPFClientConfig.shared().setPaymentCardStorageEnabled(true, withTouchID: true)

HPFClientConfig.shared().isPaymentCardScanEnabled = true
**/
```

Do not forget to replace the username and password arguments with your API username and password . Also, pass your own URL scheme (determined in the previous section).

### Handle callback redirection

If the SDK presents your users with a web page (for 3-D Secure or specific payment methods), they will eventually be redirected back to your app thanks to the app URL scheme.

In order for the SDK to be aware of the redirection and to receive the callback data, you need to implement the application:handleOpenURL: method in your App Delegate , as follows:

Objective-C
Swift

Objective-C

```
// AppDelegate.m

- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url {
return [[HPFGatewayClient sharedClient] handleOpenURL:url];
}
```

Swift

```
// AppDelegate.swift

func application(application: UIApplication, handleOpenURL url: NSURL) -> Bool {
return HPFGatewayClient.shared().handleOpen(url)
}
```

## PSD2 & SCA

Thanks to our iOS SDK we handle most of the data without you having to code anything. You can see all the new parameters on our explorer API.

Adding or overriding PSD2 data

The accuracy of the information sent is key for making sure that your customers have a frictionless payment process. That's why we provide you the possibility to add or override all the information related to the PSD2.

We added 3 new variables in HPFPaymentPageRequest object :

* merchantRiskStatement
* previousAuthInfo
* accountInfo Each variables is a string type corresponding to a JSON Object. Your server send user informations to your Android application, so you just have to retrieve these JSON data and convert them in string format and set the specific variable. If you don't set accountInfo variable, we automatically generate the associated NSDictionary with 3 values ( name_indicator / enrollment_date / card_stored_24h ).
