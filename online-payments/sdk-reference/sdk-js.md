---
description: "This is the API reference for the HiPay Enterprise JavaScript SDK in order to collect and tokenize customers' sensitive information securely. Includin"
icon: file-lines
---

# JS SDK

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/sdk-reference/sdk-js](https://developer.hipay.com/online-payments/sdk-reference/sdk-js)
{% endhint %}

This is the API reference for the HiPay Enterprise JavaScript SDK in order to collect and tokenize customers' sensitive information securely.

## Including the JS SDK

The first step to use the HiPay Enterprise JavaScript SDK is to include it on your page.

HTML

HTML

```

```

Important Security Notice : Always load the JS SDK dynamically from HiPay's official remote servers using the URLs provided above. Do not download, host, or bundle the sdkjs.js file locally within your application.

Hosting the file locally is a severe security risk that will freeze your integration version, meaning your checkout will miss critical PCI-DSS compliance patches, security updates, and automated fixes required for evolving browser architectures or third-party wallet updates (such as Google Pay and Apple Pay restrictions).

### Staging

You can also use the HiPay Enterprise JavaScript SDK of our staging environment. Here is the domain : https://stage-libs.hipay.com .

Use this environment if you want to test our upcoming features.

All the following links can be applied to our staging environment. Here is the link to include the SDK :

HTML

HTML

```

```

### Subresource Integrity (SRI)

To ensure the integrity and authenticity of our JavaScript SDK when integrating it into your environment, we recommend using the Subresource Integrity (SRI) feature. Here's how to proceed :

* Retrieve the SRI Hash : Before including the JS SDK, please request its integrity file (a cryptographic hash) from the following URL : https://libs.hipay.com/js/sdkjs.integrity

* Integrate the SDK with the integrity attribute : Once you have the hash, use a tag to include the JS SDK in your page. Add the integrity HTML attribute to this tag and populate it with the hash value you retrieved. For most common scenarios, set also the crossorigin HTML attribute to the value anonymous .

Important Note : Using SRI helps with compliance with the PCI-DSS (Payment Card Industry Data Security Standard), specifically requirement 6.4.3 , which mandates integrity controls for scripts executed on payment pages.

HTML

HTML

```
" crossorigin="anonymous">
```

You could fetch the integrity file using different solutions depending on your integration. For example, you could call it from your backend server if you have access and send the hash on your frontend as a template variable.

You could also request it directly from your frontend by using a custom JavaScript before including our JS SDK, as the following code example :

JavaScript

JavaScript

```
fetch('https://libs.hipay.com/js/sdkjs.integrity')
.then(response => {
if (!response.ok) {
throw new Error(`HTTP error ! Status: ${response.status}`);
}
return response.text();
})
.then(integrityHash => {
const script = document.createElement('script');
script.src = 'https://libs.hipay.com/js/sdkjs.js';
script.integrity = integrityHash;
script.crossOrigin = 'anonymous';
document.head.appendChild(script);
});
```

To avoid integrity errors due to a mismatch on the hash value, we recommend calling the integrity file as often as our JS SDK.

### Content Security Policy (CSP)

The Content Security Policy (CSP) is a crucial security feature that helps protect your web applications from various types of attacks, including Cross-Site Scripting (XSS). By defining a CSP, you instruct the browser on which sources of content are considered legitimate for your web page.

The HiPay JS SDK requires specific domains to be allowed in your application's CSP to work correctly. The following documentation outlines the necessary domains and provides guidance on how to configure your policy.

CSP Directive
Allowed Domains

script-src
*.hipay.com , *.paypal.com , mpsnare.iesnare.com

style-src
*.hipay.com

img-src
*.hipay.com , *.paypalobjects.com

connect-src
*.hipay.com , *.hipay-tpp.com , *.paypal.com , wss://mpsnare.iesnare.com

font-src
*.gstatic.com

frame-src
*.hipay.com , *.paypal.com

You can configure the CSP using either a Content-Security-Policy header HTTP header or a <meta> tag in your HTML. Note that while the <meta> tag is convenient, setting the CSP via the HTTP header is generally recommended as it is more secure and supported by a wider range of browsers.

The domains listed in this table are specific to the HiPay JS SDK. You may also need to include additional domain authorizations in your Content Security Policy based on your own application's requirements.

If you are using a nonce to authorize your inline scripts and styles, ensure you pass the corresponding value to the cspNonce parameter during the HiPay SDK initialization.

### The HiPay variable

The SDK is exposed as a function in a global variable named HiPay .

If you only use Hosted Fields via custom fields configuration, you can skip this step. Otherwise, you can manually include the base stylesheet to increase loading performance. It will be included automatically if you skip this step.

HTML

HTML

```

* ``` HiPay Options Once the HiPay Enterprise JavaScript SDK is included on your page, you can use the HiPay global variable to initialize the SDK. JavaScript JavaScript ``` var hipay = HiPay({ username: "YOUR_PUBLIC_USERNAME", password: "YOUR_PUBLIC_PASSWORD", environment: "stage", lang: "en", cspNonce: "EDNnf03nceLOfn39fn3e9h3sdfu" // The nonce generated by your server }); ``` Create an instance of the HiPay JavaScript SDK using your HiPay public credentials. You can add options to select your environment. Option Description username string required Public HiPay username password string required Public HiPay password environment string optional Corresponds to the HiPay API environment you want to use. Use stage to test your integration and use production to make real payments. values: stage , production default: production lang string optional Languages to translate placeholders or error messages in Hosted Fields. values: en , fr , es , it , de , pt , nl , cz , pl default: fr i18n object optional Override the default translations. See the Reference translations file . debug boolean optional Set to true if you want to display some debug logs in the browser console. Default is false . cspNonce string optional This parameter allows you to pass a nonce (a unique, cryptographically strong string generated by your server for each request) to the HiPay SDK. If your website implements a strict Content Security Policy (CSP) , the browser will block the execution of any inline scripts or styles by default. By providing the cspNonce during initialization, the SDK automatically applies this identifier to all dynamic elements (scripts or CSS) it needs to inject into the DOM. ## The HiPay Instance ### hipay.tokenize(params) Directly call the tokenization API in order to tokenize credit card information. The function calls the API only if parameters are valid. You may prefer the Hosted Fields integration with hipay.create() . Tokenization request The tokenize function accepts the following parameters. Parameter Description cardHolder string required Cardholder's name as it appears on the card cardNumber string required Card number, with a 12- to 19-digit length expiryMonth string required Card expiry month, expressed with two digits (e.g.: 01) expiryYear string required Card expiry year, expressed with two digits (e.g.: 22) cvc string 3- or 4-digit security code (called CVC2, CVV2 or CID depending on the card brand) as it appears on the credit card multiUse boolean optional Indicates if the token should be generated either for a single use or for multiple uses. While a single-use token is typically generated for a short time and for processing a single transaction, multi-use tokens are generally generated for recurring payments. Tokenization response When successful, the tokenize function returns an object with the following fields. Field name Description token Token that was created request_id Request ID linked to the token brand Card brand (e.g.: Visa, Mastercard, American Express, Maestro) We recommend to not use this field in favor of payment_product field ! domestic_network Card domestic network (if applicable, e.g. cb). pan Card number (up to 19 characters). Please note: due to PCI DSS security standards, our system has to mask credit card numbers in any output (e.g.: 549619 ** 4769). card_id Unique card identifier. card_holder Cardholder's name card_expiry_month Card expiry month (2 digits) card_expiry_year Card expiry year (4 digits) issuer Card-issuing bank's name Do not rely on this value to remain static over time. Bank names may change due to acquisitions and mergers. country Bank country code where the card was issued. This two-letter country code complies with ISO 3166-1 (alpha 2). card_type Card type (if applicable, e.g.: DEBIT, CREDIT) card_category Card category (if applicable, e.g.: PLATINUM) forbidden_issuer_country Indicates whether the card country is authorized. multi_use Indicates wheter the payment card token can be used for a single-use or a multi-use. payment_product HiPay Order API payment product code to pass to the order call browser_info Browser information of the final user for PSD2 In case of an error, the function returns an error code describing what went wrong. ### hipay.updateToken(params) Directly call the tokenization API in order to update the token previously created with hipay.tokenize() . Please refer to the following documentation for parameters ( update token API reference ). Please read this integration example of payment card with CVC forced. This example use updating token function. ### hipay.getDeviceFingerprint() Get the device fingerprint of the final user in order to send it to the HiPay API. ### hipay.getBrowserInfo() Get the browser information of the final user in order to send it to the HiPay API. For 3-D Secure purposes, you need to send this information when the device channel is 02 - Browser. ### hipay.injectBaseStylesheet() Inject the base stylesheet in your page dynamically. ### hipay.removeBaseStylesheet() Remove the base stylesheet from your page dynamically. ### hipay.create(type, options) The create function is the entry point of Hosted Fields instances. JavaScript JavaScript ``` var card = hipay.create(type, options); ``` Create function is the entry point to create Hosted Payments , Hosted Fields and Carousel instances. JavaScript JavaScript ``` var hostedPaymentInstance = hipay.create('hosted-payments', options); var cardInstance = hipay.create('card', options); ``` This function creates an instance of the payment product specified by type (card here). JavaScript JavaScript ``` var carouselInstance = hipay.create('carousel', options); ``` carousel is an Hosted Fields instance This function creates an instance of the payment product specified by type . #### Types The type of payment product has to be instantiated as a string. Please note that each type has required options. Hosted Payments Type Description / [Fields] hosted-payments Creates Hosted Payments instance with carousel and auto-generated payment form Hosted Fields Type Description / [Fields] carousel Creates swipeable carousel displaying available payment products card A credit card accepting multiple brands (mastercard, visa, american-express, maestro, bancontact). required fields: [ cardHolder , cardNumber , expiryDate , cvc ] 3xcb [] (redirection) 3xcb-no-fees [] (redirection) 4xcb [] (redirection) 4xcb-no-fees [] (redirection) alma-3x [] (redirection) alma-4x [] (redirection) bancomatpay required fields: [ phone ] bancontact [] (redirection) bcmc-mobile [] (redirection) bizum required fields: [ phone ] bnpp-3xcb [] (redirection) bnpp-4xcb [] (redirection) carte-cadeau [] (redirection) credit-long [] (redirection) giropay required fields: [ issuer_bank_id ] ideal optional fields: [ issuer_bank_id ] illicado required fields: [ prepaid_card_number , prepaid_card_security_code ] klarna [] (redirection) mbway required fields: [ phone ] multibanco Payment reference [] mybank [] (redirection) paypal [] (redirection) paysafecard [] (redirection) payshop required fields: [ email ] (redirection) postfinance-card [] (redirection) postfinance-efinance [] (redirection) przelewy24 [] (redirection) sdd SEPA form required fields: [ gender , firstname , lastname , iban , bank_name ] sisal Payment reference [] sofort-uberweisung [] (redirection) #### Options Hosted Payments Option Description selector string required Unique div id to generate the carousel and form in. Hosted Fields type objects optional Override a specific form by adding object named with Hosted Fields type and configure it as if you create an Hosted Fields instance. See options below for Hosted Fields config. request object optional Object with specific properties related to the payment order request. See the Request configuration section below for more details. styles object optional Object with your custom styling CSS properties. See the Styles configuration section below for more details. Hosted Fields There are two ways to create Hosted Fields configurations: using template , to generate the HTML form template automatically,
* using fields , to create a custom HTML template. You have to specify only one of these options.

styles
object optional Object with your custom styling CSS properties.
See the Styles configuration section below for more details.

Option Description template

string optional

If set to auto , it activates the generation of the HTML form template automatically. selector

string optional

Unique div id to generate the form when template: 'auto' is set. fields

object optional

Object with the fields to generate within your form. Each field has its own configuration.
See the Fields configuration section below for more details. request object

required for applepay

Object with specific properties related to the payment order request. See the Request configuration section below for more details. multi_use

boolean optional

Only for card type. This boolean activates the multi_use option to add the one-click payment feature. brand

array optional

Only for card type. Accepted credit card brands. (ex: [visa', mastercard']) payment_product

array optional

Only for carousel type. Payment products to display in the carousel. Ex: [card', sdd', paypal'] currency

string optional

Only for carousel type. Base currency to filter carousel payments products by. This three-character currency code complies with ISO 4217. (EUR', USD', GBP', ...) country

string optional

Only for carousel type. The country code of the customer to filter carousel payments product by. This two-letter country code complies with ISO 3166-1 (alpha 2). Fields configuration

Fields have a common set of options and some field-specific options. Some fields are required when you generate a payment product.

Option Description selector

string optional

Unique div id to generate the Hosted Fields.
All fields have a default selector hipay-{payment product}-field-{field name} . (cardHolder => hipay-card-field-cardHolder) placeholder

string optional

Customizes the placeholder text.
Be careful, default placeholders are translated according to the lang configuration. helpButton

boolean optional

Adds a clickable help button at the end of the field. An event is triggered on click.
For CVC, we also send a generic help message in this event.default: false uppercase

boolean optional
only text fields

Automatically capitalizes all alphabetical cardholder characters.

default: true

defaultFirstname

string optional
only cardHolder

Needs to be used together with defaultLastname . Used to prefill the cardholder field by concatenating defaultFirstname and defaultLastname. defaultLastname

string optional
only cardHolder

Needs to be used together with defaultFirstname . Used to prefill the cardholder field by concatenating defaultFirstname and defaultLastname. hideCardTypeLogo

boolean optional
only cardNumber

Hides the detected credit card type logo.
Default: false disableCobrandingSelection

boolean optional
only cardNumber

Disables the choice of the card network. Cobranding cards only (i.e. VISA/CB). Default: false styleCobrandingSelection

string optional
only cardNumber

Defines the style for the choice of the card network feature. Possible values: radio , logo or default . default is based on logo without outline.
Default: default displayAcceptedCards

boolean optional
only cardNumber

Displays on the cardNumber field the logo of the accepted cards.
Default: true defaultValue

boolean optional
except card fields

Used to prefill a given field with a default value.

#### Request configuration

This configuration specify payment order informations. These information will be used to adapt the autogenerated visual according to certain condition.

Option Description amount

string or number required for paypal
string recommended

The order amount of the request. It must be greater than zero, and can contain a maximum of 2 decimal places. currency

string required for paypal

See PayPal v2 JS reference locale

string optional See PayPal v2 JS reference countryCode

string required for applepay

See ApplePay Web JS reference currencyCode

string required for applepay

See ApplePay Web JS reference total

object required for applepay

See ApplePay Web JS reference supportedNetworks

array optional

See ApplePay Web JS reference customerShippingInformation

object optional

See PayPal JS reference

#### Styles configuration

This configuration customizes the field internal appearance. The external appearance depends on your parent CSS file.

Internal styling is divided into 4 optional categories , each defined with an object.

Category Description base Custom base style valid CSS applied when the field is valid invalid CSS applied when the field is invalid disable CSS applied when the field is disabled For each of the above categories, the following properties are available.

Property Description properties color , fontSize , fontFamily , fontStyle , fontVariant , fontWeight , textDecoration , iconColor , placeholderColor , caretColor , autofillBackgroundColor , loaderColor

#### Examples

Hosted Payments

HTML
JavaScript

HTML

```

```

JavaScript

```
var options = {
selector: 'hosted-payments',
carousel: {
currency: 'EUR'
},
card: {
multi_use: true
},
styles: {
base: {
color: "#000000"
}
}
}
var hostedPaymentsInstance = hipay.create('hosted-payments', options);
```

Hosted Fields

The following object provides a configuration example for a credit card form on your page.

HTML
JavaScript

HTML

```

```

JavaScript

```
var options = {
template: 'auto',
selector: 'card',
multi_use: true,
fields: {
cardHolder: {
uppercase: true,
placeholder: 'John Doe'
},
cvc: {
helpButton: true
}
},
styles: {
base: {
color: "#000000",
fontSize: "15px",
fontFamily: "Roboto",
fontWeight: 400,
placeholderColor: "#999999",
iconColor: '#00ADE9',
caretColor: "#00ADE9",
loaderColor: '#CDEDF7'
},
invalid: {
color: '#D50000',
caretColor: '#D50000'
}
}
}
var cardInstance = hipay.create('card', options);
```

### hipay.createReference(type, options)

Display a payment reference for some payment means of the category payment-reference .

#### Types

The type of payment product has to be instantiated as a string. Please note that each type has specific options.

Hosted Fields

Type Description / [Fields] multibanco Display a Multibanco reference.
required fields : [ reference , entity , amount , currency , expirationDate ]
mooney Display a Mooney reference with a barcode.
required fields : [ reference , barCode ]

#### Options

Option Description selector

string required

Unique div id to generate the reference.

#### Multibanco

Option Description reference

string required

Reference number of the Multibanco transaction. Available in the reference property of the referenceToPay field in the Order API response. entity

string required

Entity number of the Multibanco transaction. Available in the entity property of the referenceToPay field in the Order API response. amount

string required Amount of the Multibanco transaction. Available in the amount property of the referenceToPay field in the Order API response. currency

string optional Currency of the Multibanco transaction. Available in the currency field in the Order API response.
Default is EUR. expirationDate

string required Expiration date of the Multibanco transaction. Available in the expirationDate property of the referenceToPay field in the Order API response. Example of a Multibanco reference :

HTML
JavaScript

HTML

```

```

JavaScript

```
hipay.createReference('multibanco', {
selector: 'referenceContainer',
reference: '528272838',
entity: '11249',
amount: '1,125.99',
currency: 'USD',
expirationDate: '2027-09-29'
});
```

#### Mooney

Option Description reference

string required

Reference number of the Mooney transaction. Available in the reference property of the referenceToPay field in the Order API response. barCode

string required

Barcode number of the Mooney transaction. It will be used to generate the barcode. Available in the barCode property of the referenceToPay field in the Order API response. Example of a Mooney reference :

HTML
JavaScript

HTML

```

```

JavaScript

```
hipay.createReference('mooney', {
selector: 'referenceContainer',
reference: '800253437211',
barCode: '373680025343721191'
});
```

## Hosted payments instances

Hosted payments instances are created by hipay.create('hosted-payments', config) .

### instance.on(event', callback)

The only way to interact with your Hosted Payments instance is by listening to events . The following events are emitted by the Hosted Payments instance.

Category Description paymentProductChange Emitted when the payment product changes, i.e. when an item is clicked on the carousel.

You can use this event to reset your submit button state.

Response: "new_payment_product"

validityChange Emitted when the payment product validity changes, i.e. when it goes from invalid to valid
