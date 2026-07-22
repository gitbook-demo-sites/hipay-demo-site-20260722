---
description: "This guide will walk you through the creation of a fully integrated payment form with multiple payment products using the HiPay Hosted Fields. You wil"
icon: file-lines
---

# Hosted Payments

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/hosted-payments](https://developer.hipay.com/online-payments/payment/hosted-payments)
{% endhint %}

This guide will walk you through the creation of a fully integrated payment form with multiple payment products using the HiPay Hosted Fields.

You will see how to create your payment form, customize it, interact with it, and securely get data from it. These data will enable you to make a transaction using the HiPay Order API .

The HiPay Hosted Payments feature internally uses the HiPay Hosted Fields.

Please follow these 7 steps to create your payment form with the HiPay Hosted Payments:

* Set up the HiPay Enterprise JavaScript SDK
* Set up your HTML form
* Create the Hosted Payments instance
* Customize your payment form
* Interact with the Hosted Payments instance
* Get payment data
* API ORDER

## SDK Set Up

To get started, include the HiPay Enterprise JavaScript SDK on your HTML page. The following link exposes a global variable, HiPay , as a function to initialize the SDK with your public credentials and your configuration.

HTML

HTML

```

```

Then, create an instance of the HiPay Enterprise JavaScript SDK.

You must replace HIPAY-PUBLIC-LOGIN and HIPAY-PUBLIC-PASSWORD with your own public credentials.

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

Go to: HiPay Enterprise JavaScript SDK reference

## HTML Set Up

In order to collect sensitive information in a secure way, the HiPay Enterprise JavaScript SDK will generate components hosted by HiPay on your page.

With these components, sensitive information filled in by customers never hits your page or your web server.

You can now integrate your HTML page. You just need to place a div with a unique id in your page. The form will be injected inside automatically.

HTML

HTML

```

/* The whole form will be inserted in this div */

PAY

```

## Payment Product Instance

Now that the HTML div is ready, we can generate the whole form inside. Set config with the hipay-hostedpayments-form selector and call the create function with hosted-payments parameter .

HTML

HTML

```

var config = {
selector: 'hipay-hostedpayments-form' // form container div id
};

var hostedPaymentsInstance = hipay.create('hosted-payments', config);

```

Go to: hipay.create(type, options) to see all supported configurations.

## Customize

Override default configuration

Hosted Payments form uses default parameters for each payment product. You can override them by adding custom configuration in the config object.

Here is an example of credit card and Sepa Direct Debit customization. Like Hosted Fields, you can also customize the internal styling of the fields.

HTML

HTML

```

var config = {
selector: 'hipay-hostedpayments-form',
card: {
multi_use: false,
fields: {
cardHolder: {
defaultValue: 'John Doe'
}
}
},
sdd: {
fields: {
firstname: {
defaultValue: 'John'
},
lastname: {
defaultValue: 'Doe'
}
}
},
styles: {
base: { // default field styling
color: "#000000",
fontSize: "15px",
fontWeight: 400,
placeholderColor: "#999999",
iconColor: 'green',
caretColor: "green"
},
invalid: { // invalid field styling
color: '#D50000',
caretColor: '#D50000'
}
}
};

var hostedPaymentsInstance = hipay.create('hosted-payments', config);

```

Go to: Create configuration

Override default stylesheet

You can override the default CSS by adding your custom CSS file.

CSS

CSS

```
.HiPayField--focused + .hipay-field-label {
color: green;
}

.HiPayField--focused + .hipay-field-label + .hipay-field-baseline {
border-bottom: solid 1px green;
}

[data-hipay-id='hipay-help-cvc'] {
color: green;
background-color: palegreen;
border: solid 1px green;
}
```

Go to: Base stylesheet reference

## Interact

You can interact with the Hosted Payments instance previously initialized by listening to events on it.

Here is how to enable your submit button when your form is valid.

HTML

HTML

```

/* Listen to change event on Hosted Payments instance */
hostedPaymentsInstance.on('validityChange', function(event){
/* Enable / disable submit button */
document.getElementById("hipay-submit-button").disabled = !event.valid;
});

```

Go to: instance.on(event', callback)

## Get Payment Data

To securely transmit sensitive information, the HiPay Hosted Payments converts it into an object to be sent to the HiPay Order API to process your payment.

You can get information by calling the getPaymentData() function of the Hosted Payments instance.

The best way to do that is to add an event listener on the submit event of your form.

The hostedPaymentsInstance.getPaymentData() function returns a Promise . When successful, it returns an object with the payment product and data. When rejected, it returns error as an array.

HTML

HTML

```

/* Get form */
let hostedForm = document.getElementById("hipay-form");

/* Add event listener on the submit button when clicked */
hostedForm.addEventListener("submit", function(event) {
event.preventDefault();
/* Get payment data when the submit button is clicked */
hostedPaymentsInstance.getPaymentData().then(
function(response) {
/* Send response.datas to your server to process payment */
handlePayment(response.datas);
},
function(error) {
/* Display error */
}
);
});

```

Here is a response from getPaymentData() :

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

Go to: instance.getPaymentData()

## Payment

Once you have the response from the getPaymentData() , you should use the following parameters to call the HiPay Entreprise Order API.

getPaymentData() Order API parameter Comment payment_product payment_product The payment method used for the transaction. Depending on the payment product, parameters specific to the payment method are required.

token cardtoken Specific to credit or debit card payment products . This is the token obtained from the HiPay Enterprise Secure Vault API when tokenizing a credit or debit card.

browser_info browser_info Specific to the PSD2 . Object containing the browser information.The ipaddr and http_accept of the browser_info Order API parameter have to be added by your server.

You must enter the client's IP and not the IP of your server or any other equipment. (Reverse-proxy)

Most CMS and frameworks have methods to get this IP.

device_fingerprint device_fingerprint This element should contain the value of the ioBB hidden field.
