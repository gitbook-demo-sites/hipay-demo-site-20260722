---
description: "This guide will walk you through the creation of a credit card payment form using the HiPay Hosted Fields. You will learn how to customize it, interac"
icon: file-lines
---

# Hosted Fields

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/hosted-fields](https://developer.hipay.com/online-payments/payment/hosted-fields)
{% endhint %}

This guide will walk you through the creation of a credit card payment form using the HiPay Hosted Fields.

You will learn how to customize it, interact with it, and securely obtain a token generated from sensitive card information. With it, you will be able to make a transaction using the HiPay Order API .

Follow these 5 steps to create your payment form with the HiPay Hosted Fields and request a new payment:

* Set up the HiPay JavaScript SDK.
* Create the payment product instance.
* Customize your payment form.
* Interact with the form.
* Send payment data to the HiPay Order API.

## Set up the HiPay JavaScript SDK

To get started, insert the HiPay JavaScript SDK on your HTML page. The following link exposes a global variable, HiPay, as a function to initialize the SDK with your public credentials and your configuration.

HTML

HTML

```

```

Then, create an instance of the HiPay JavaScript SDK. You must replace HIPAY-PUBLIC-LOGIN and HIPAY-PUBLIC-PASSWORD with your own public credentials.

HTML

HTML

```

var hipay = HiPay({
username: 'HIPAY-PUBLIC-LOGIN',
password: 'HIPAY-PUBLIC-PASSWORD',
environment: 'production',
lang: 'en'
});

```

Go to HiPay JavaScript SDK reference for more details.

## Create the payment product instance

To securely collect sensitive information, the HiPay JavaScript SDK generates components hosted by HiPay on your page. With these components, sensitive information filled in by customers never reaches your page or your web server.

Two ways of creating a payment product instance are available: automatic or custom.

### Automatic mode

This mode is the easiest one to integrate and maintain because HiPay can update it remotely. Just put a div with a unique id in your page. The form will be inserted automatically.

HTML

HTML

```

/* The whole form will be inserted in this div */

PAY

```

Now that the HTML div is ready, you can generate all the fields with their label inside. Set template to auto to activate automatic mode and set the id in selector.

HTML

HTML

```

var config = {
template: 'auto',
selector: 'hipay-hostedfields-form' // form container div id
};
var cardInstance = hipay.create('card', config);

```

In this example, the HiPay JavaScript SDK generates multiple Hosted Fields (Card holder - Card number - Card expiry date - Card CVC).

### Custom mode

With this mode, you can customize the order in which the fields are displayed. However, updates will require more development time on your side.

Just replace input elements with div elements. These elements need to have a unique id .

HTML

HTML

```

Card holder
/* Cardholder field will be inserted here */

Card number
/* Card number field will be inserted here */

Expiry date
/* Expiry date field will be inserted here */

CVC
/* CVC field will be inserted here */

PAY

```

In this example, the HiPay JavaScript SDK generates a Hosted Field in the hipay-card-holder, hipay-card-number, hipay-expiry-date, hipay-cvc divs.

Now that the HTML form is ready, you can generate its fields. To do so, create a credit card instance with the previously initialized HiPay JavaScript SDK instance.

HTML

HTML

```

var config = {
fields: {
cardHolder: {
selector: 'hipay-card-holder' // card holder div id
},
cardNumber: {
selector: 'hipay-card-number' // card number div id
},
expiryDate: {
selector: 'hipay-expiry-date' // expiry date div id
},
cvc: {
selector: 'hipay-cvc', // cvc div id
helpButton: true // activate the help button
}
}
};
var cardInstance = hipay.create('card', config);

```

Go to hipay.create(type, options) to see all supported configurations.

## Customize your payment form

There are two ways of customizing the Hosted Fields integration, as we separate internal styling from container styling.

### Container styling

To best match your style guides, the external styling (height, border, background, etc.) of the field completely depends on your Cascading Style Sheets (CSS).

To help you with this integration, the following classes have been added to the container field:

* HiPayField-empty
* HiPayField-focused
* HiPayField-valid
* HiPayField-invalid Go to Hosted Fields container for more details.

### Internal styling

Internal styling refers to the properties inside generated fields, like text or icon properties. Let's now add styles to our previous configuration.

HTML

HTML

```

var config = {
template: 'auto',
selector: 'hipay-hostedfields-form',
styles: {
base: {
// default field styling
color: '#000000',
fontSize: '15px',
fontWeight: 400,
placeholderColor: '#999999',
iconColor: '#00ADE9',
caretColor: '#00ADE9'
},
invalid: {
// invalid field styling
color: '#D50000',
caretColor: '#D50000'
}
}
};
var cardInstance = hipay.create('card', config);

```

Go to Styles configuration for more details.

## Interact with the form

You can interact with the previously initialized card instance by listening to events on it. Here is how to enable your submit button when your form is valid, and how to show the error(s) if it is not:

HTML

HTML

```

/* Listen to change event on card instance */
cardInstance.on('change', function (event) {
/* Display error(s), if any */
document.getElementById("hipay-error-message").innerHTML = event
.error; /* Enable / disable submit button */
document.getElementById("hipay-submit-button").disabled = !event.valid;
});

```

Go to instance.on(event', callback) for more details.

## Sending payment data to the HiPay Order API

To securely transmit sensitive card information, the HiPay Hosted Fields convert it into a token to be sent to the HiPay Order API in order to process your payment. With this token, you will never be able to retrieve the card information.

You can tokenize the information of the card you previously initialized by calling the getPaymentData() function. The best way to tokenize is to add an event listener on the submit button of your form.

The card.getPaymentData() function returns a Promise . When successful, it returns an object with the token and all the payment data. When rejected, it returns the list of errors.

HTML

HTML

```

/* Get the form */
let cardForm = document.getElementById("hipay-form"); /* Add event listener on the submit button when clicked */
cardForm.addEventListener("submit", function (event) {
event.preventDefault(); /* Tokenize your card information when the submit button is clicked */
cardInstance.getPaymentData().then(function (response) {
/* Send token to your server to process payment */
handlePayment(response.token);
}, function (errors) {
/* Display first error */
document.getElementById("hipay-error-message").innerHTML = errors[0].error;
});
});

```

Here is the response from getPaymentData():

JSON

JSON

```
{
"payment_product": "visa",
"token": "f12bfab3b4fs5q6der7895a98ab76",
"request_id": "0",
"brand": "VISA",
"pan": "411111xxxxxx1111",
"card_holder": "JOHN DOE",
"card_expiry_month": "12",
"card_expiry_year": "2031",
"issuer": "ANY BANK",
"country": "US",
"card_type": "CREDIT",
"device_fingerprint": "..."
}
```

Once you have the response from getPaymentData() , use the following parameters to call the HiPay Enterprise Order API.

## [OPTIONAL] One-Click & Recurring payments

By default, a card that is tokenized with the Hosted Fields cannot be reused as part of a recurring payment.

If your integration allows one-click payments, you must take the choice of the end user into account and set the option accordingly.

To activate the option, set the enabled property at true value of the one_click option during the card instance creation.

Here is an exemple :

JavaScript

JavaScript

```
var config = {
selector: 'card-container',
template: 'auto',
one_click: {
enabled: true
}
};

cardInstance = hipayInstance.create('card', config);
```

This will display a switch button at the end of the card form as the below screenshot.
