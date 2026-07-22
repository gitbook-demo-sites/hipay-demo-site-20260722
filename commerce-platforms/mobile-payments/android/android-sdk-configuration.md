---
description: "Accept payments in your own Android application thanks to the HiPay Android SDK. This integration allows you to accept payments in your Android app ve"
icon: file-lines
---

# Android - SDK Configuration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/android/android-sdk-configuration](https://developer.hipay.com/mobile-payments/android/android-sdk-configuration)
{% endhint %}

Accept payments in your own Android application thanks to the HiPay Android SDK. This integration allows you to accept payments in your Android app very quickly.

## Prerequisites

Build settings

The project minSdkVersion is 14 (Ice Cream Sandwich), which means that the SDK won't build on applications targeting a lower version of Android.

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

In order for our Android SDK to process transactions with users' payment details on the HiPay Enterprise platform, you must provide the SDK with credentials (Configuration section).

Also, for each order processed by the Android SDK, the HiPay Enterprise platform must authenticate the call and validate that the merchant has allowed it. To do so, HiPay Enterprise leverages a signature mechanism. Once your app needs to process a payment, it must contact your own server in order to get a signature, specific to the order to be processed. (Signature section)

Order processing

Order information should not be generated on the client side. Most of the time, orders are generated on the server side (on your servers), following actions performed by your users on your mobile app. The HiPay Enterprise Android SDK allows you to present a payment page to your users and process transactions directly on your mobile app.

Thus, your mobile app will receive a confirmation with a transaction status indicating that the payment was successfully completed. You may display a confirmation screen upon this confirmation, but you must not process order on the server side following this confirmation. For security reasons, orders must always be confirmed on your systems following the server-to-server notification.

## Signature calculation

The signature is the hash of these four parameters concatenation:

* Order ID
* Amount (formatted with two decimal places, example: 72.10)
* Currency
* Secret passphrase The signature has to be generated beforehand on the server side in order not to show the secret passphrase in client code. This is the reason why the code examples below are executed in PHP/Python on your servers and not embedded in the Android app directly.

Please find below some code examples for signature generation.

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

The codes above generate a signature which is to be used by the HiPay Enterprise SDK for Android.

To get the secret passphrase of your account, go to the Integration section of your HiPay Enterprise back office, then to Security Settings.

You may choose a secret passphrase if you don't have one already. This passphrase is also used to process server-to-server notifications.

Mobile App Implementation

The Android SDK needs to use the signature in order to make transactions.
Please find below an Android code example querying the merchant's server (yours) to get the signature and then initializing the SDK's payment page with the signature.

For the sake of this example, we assume that the response is in JSON format. Once you get the signature, you can create a PaymentPageRequest with the necessary parameters and then present the PaymentScreenActivity screen. You will get more details about the payment screen in the next sections.

Java

Java

```
public void onClick(View view) {

final String orderId = "TEST_89897";

/* Assuming that the server url takes the orderId as argument
* and generates the signature after retrieving
* the required data in the database */

String url = String.format(getString(R.string.server_url), orderId);

RequestQueue requestQueue = Volley.newRequestQueue(getActivity());

// Assuming that the server's response is in JSON format
JsonObjectRequest jsObjRequest = new JsonObjectRequest
(Request.Method.GET, url, null, new Response.Listener () {

@Override
public void onResponse(JSONObject response) {
try {

String signature = response.getString("signature");
String amount = response.getString("amount");
String currency = response.getString("currency");

/* Once we get the signature, we can instantiate
* and present the payment screen */

PaymentPageRequest request = new PaymentPageRequest();

request.setOrderId(orderId);
request.setAmount(Float.parseFloat(amount));
request.setCurrency(currency);

PaymentScreenActivity.start(MyActivity.this,
request,
signature,
null);

} catch (JSONException e) {
e.printStackTrace();
}
}

}, new Response.ErrorListener() {

@Override
public void onErrorResponse(VolleyError error) {
// handle the error
}
});

requestQueue.add(jsObjRequest);
}
```

## Installation

Before starting the installation, please read all instructions and make sure you've gone through the Prerequisites section.

It's recommended to use Gradle to install the HiPay Enterprise SDK for Android.

Add this line to your project's build . gradle :

```
dependencies {
compile 'com.hipay.fullservice:hipayfullservice:1+'
}
```

Then synchronize the project with Gradle files. This will install the core wrapper components as well as the built-in payment screen and other utility components.

## Configuration

You need to provide the SDK with a few parameters, such as the credentials and targeted environment.

The following code allows you to configure the SDK. We recommend putting it in your App Launcher Activity s onCreate() method implementation.

Java

Java

```
public class DemoActivity extends AppCompatActivity {
...

protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);

ClientConfig.getInstance().setConfig(

ClientConfig.Environment.Stage,
"YOUR API USERNAME",
"YOUR API PASSWORD"
);
}

//optional features

ClientConfig.getInstance().setPaymentCardStorageEnabled(true);

ClientConfig.getInstance().setPaymentCardScanEnabled(true);

ClientConfig.getInstance().setPaymentCardNfcScanEnabled(true);
}
```

Do not forget to replace the username and password arguments with your API username and password .

The Payment card storage option is also called One-click payment. The camera scan and NFC scan options help create a more fluid mobile payment process.

Once your app goes live, you need to set the environment to Environment.Production .

## PSD2 & SCA

Thanks to our Android SDK we handle most of the data without you having to code anything. You can see all the new parameters on our explorer API .

Adding or overriding PSD2 data

The accuracy of the information sent is key for making sure that your customers have a frictionless payment process. That's why we provide you the possibility to add or override all the information related to the PSD2.

We added 3 new variables in PaymentPageRequest object :

* merchant_risk_statement
* previous_auth_info
* account_info Each variables is a string type corresponding to a JSON Object. Your server send user informations to your Android application, so you just have to retrieve these JSON data and convert them in string format and set the specific variable. If you don't set account_info variable, we automatically generate it with 3 fields ( name_indicator / enrollment_date / card_stored_24h ).
