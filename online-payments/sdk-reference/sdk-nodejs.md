---
description: "The NodeJS SDK simplifies HiPay Enterprise APIs integration. Requirements Node >= 14 npm yarn (optional) HiPay Enterprise API Credentials Installation"
icon: file-lines
---

# NodeJS SDK

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/sdk-reference/sdk-nodejs](https://developer.hipay.com/online-payments/sdk-reference/sdk-nodejs)
{% endhint %}

The NodeJS SDK simplifies HiPay Enterprise APIs integration.

## Requirements

* Node >= 14
* npm
* yarn (optional)
* HiPay Enterprise API Credentials

## Installation

Before starting the installation, please read all the instructions and make sure you've gone through the Prerequisites and recommendations section.

It is recommended to use npm or yarn to install the HiPay Enterprise SDK for NodeJS .

### NPM

If your project is not based on NPM, you must install it and create a package.json file in your root project directory.

* NPM installation
* Yarn installation (optional)
* NPM project setup For the next steps, you need a command line interface; all commands are executed in your root project directory.

### SDK installation

You can now install the SDK with the following command line:

Bash

Bash

```
npm i @hipay/hipay-enterprise-sdk-nodejs
```

Bash

Bash

```
yarn add @hipay/hipay-enterprise-sdk-nodejs
```

If no errors are displayed, the module is installed.

## API Calls

You need to import the SDK NodeJS library as a variable and instantiate a HiPay object with it.

The SDK allows you to call the different HiPay APIs that allow you to perform a transaction.

You can therefore interact with our different APIS : /order , /hpayment and /maintenance . Whatever the request, you must instantiate a gateway client in the following way.

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

// Instanciate a gateway client using HiPay class with a configuration
const hipayClient = new HiPay({
apiUsername: 'YOUR_API_USERNAME',
apiPassword: 'YOUR_API_PASSWORD',
apiEnv: HiPay.API_ENV_STAGE
});
```

To switch to Production mode, please init the configuration with: HiPay.API_ENV_PRODUCTION

### Timeout

We recommend you to use a client request timeout of 60 seconds.

Indeed, some API requests may take longer than expected because they rely on different actors.

If your client request timeout is too short and the response takes longer, the transaction will be paid and created at HiPay but your end user will have an error.

### Order

In this case, the payment page is hosted on your website, allowing you to have a unified and fully customized workflow. Please refer to the POST Order below for more information.

Please note that if you want to execute transactions with credit or debit card payment products, you will need to tokenize card numbers beforehand by using the HiPay Enterprise Tokenization API .

To have the function of each attribute, please refer to the technical documentation of each API.

Instantiate an OrderRequest object:

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

const order = new HiPay.OrderRequest({
orderid: 'ORDER #123456',
operation: 'Sale',
paymentProduct: 'visa',
description: 'ref_85',
currency: 'EUR',
amount: '21.60',
shipping: '0.00',
tax: '3.6',
cid: null,
ipaddr: '172.20.0.1',
acceptUrl: 'http:/www.my-shop.fr/checkout/accept',
declineUrl: 'http:/www.my-shop.fr/checkout/decline',
pendingUrl: 'http:/www.my-shop.fr/checkout/pending',
exceptionUrl: 'http:/www.my-shop.fr/checkout/exeception',
cancelUrl: 'http:/www.my-shop.fr/checkout/cancel',
httpAccept: '*/*',
httpUserAgent:
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
language: 'en_US',
customData:
'{"shipping_description":"Flat rate","payment_code":"visa","display_iframe":0}'
});
```

There are several complementary objects to complete the information required by the API order:

* CustomerShippingInfoRequest: Order related to the shipping information.
* CustomerBillingInfoRequest: Order related to the billing information.
* CardTokenPaymentMethod: Data related to payment with token system. CardTokenPaymentMethod

This parameter is specific to credit and debit card payment products. This is the token obtained from the HiPay Enterprise Secure Vault API when tokenizing a credit or debit card. To generate a token, please refer to the HiPay Enterprise Tokenization API documentation .

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');
const {
CardTokenPaymentMethod
} = HiPay.PaymentMethods.CardTokenPaymentMethod;

const paymentMethod = new CardTokenPaymentMethod({
cardtoken: '61f92d7a135db52dbd583b2aad208e73978196392357f674bacf39f549042f14',
eci: 7,
authentication_indicator: 0
});

const order = new HiPay.OrderRequest({
// use previous Order parameters
paymentMethod: paymentMethod
});
```

CustomerShippingInfoRequest and CustomerBillingInfoRequest

These two objects are related to the delivery and billing addresses. You can find the same type of information on both objects.

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

const customerBillingInfo = new HiPay.CustomerBillingInfoRequest({
firstname: 'Jane',
lastname: 'Doe',
email: '[email protected]',
birthdate: '19901125',
recipientinfo: 'Dr',
streetaddress: '56 avenue de la paix',
streetaddress2: '',
city: 'Paris',
state: '',
zipcode: '75000',
country: 'FR',
phone: '0130811322',
gender: 'M'
});

const customerShippingInfo = new HiPay.CustomerShippingInfoRequest({
shipto_firstname: 'Jane',
shipto_lastname: 'Doe',
shipto_streetaddress: '56 avenue de la paix',
shipto_streetaddress2: '',
shipto_city: 'Paris',
shipto_state: '',
shipto_zipcode: '75000',
shipto_country: 'FR',
shipto_phone: '0130811322',
shipto_msisdn: '0600000000',
shipto_gender: 'M'
});

const order = new HiPay.OrderRequest({
// previous Order informations
customerBillingInfo: customerBillingInfo,
customerShippingInfo: customerShippingInfo
});
```

Once everything is completed you can start the transaction.

JavaScript

JavaScript

```
// Make a request and return a object from Gateway/Response/Transaction class
const transaction = await hipayClient.requestNewOrder(order);
```

At the return of the API, the transaction can have one of the following status:

* completed
* pending
* declined
* error You must therefore perform a different treatment according to each status, and redirect the customer to the corresponding page of your website.

JavaScript

JavaScript

```
const {
TransactionState
} = HiPay.Transaction.TransactionState;

const transaction = await hipayClient.requestNewOrder(order);

switch (transaction.state) {
case TransactionState.COMPLETED:
case TransactionState.PENDING:
return 'YOUR_URL_FOR_PENDING_PAYMENT';
case TransactionState.FORWARDING:
return transaction.forwardUrl;
case TransactionState.DECLINED:
console.error(
`There was an error requesting new transaction: ${transaction.reason.message}`
);
throw new Error(
'Sorry, your payment has been declined. Please try again with an other payment mean.'
);
case TransactionState.ERROR:
console.error(
`There was an error requesting new transaction: ${transaction.reason.message}`
);
throw new Error('An error occured, process has been cancelled.');
default:
throw new Error('An error occured, process has been cancelled.');
}
```

### Hosted Page

HiPay Enterprise hosts your payment page on a secured site. With this option you can benefit from a single point of contact, adaptable payment pages, and the PCI-DSS standard. You can therefore outsource heavy security requirements that are related to payment acceptance.

Unlike the API order, you must not perform a tokenization. Some parameters need to be added but the webservice relies on the same type of operation.

You must redirect the consumer to the URL forward provided in the webservice response.

Instantiate a HostedPaymentPageRequest object:

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

const hpayment = new HiPay.HostedPaymentPageRequest({
orderid: 'ORDER #123456',
operation: 'Sale',
description: 'ref_85',
firstname: 'Jane',
lastname: 'Doe',
email: '[email protected]',
currency: 'EUR',
amount: '21.60',
shipping: '0.00',
tax: '3.6',
cid: null,
ipaddr: '172.20.0.1',
acceptUrl: 'http:/www.my-shop.fr/checkout/accept',
declineUrl: 'http:/www.my-shop.fr/checkout/decline',
pendingUrl: 'http:/www.my-shop.fr/checkout/pending',
exceptionUrl: 'http:/www.my-shop.fr/checkout/exeception',
cancelUrl: 'http:/www.my-shop.fr/checkout/cancel',
httpAccept: '*/*',
httpUserAgent:
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
language: 'en_US',
authenticationIndicator: 0
});
```

In addition to these parameters, you can enter specific information related to the hpayment. To know:

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

const hpayment = new HiPay.HostedPaymentPageRequest({
// use previous HostedPaymentPage parameters
paymentProductList: 'visa,mastercard,cb,maestro,american-express',
paymentProductCategoryList: '',
css: '',
template: 'basic-js',
displaySelector: '1',
timeLimitToPay: 3000,
multiUse: 0
});
```

Once everything is completed you can start the transaction.

JavaScript

JavaScript

```
// Make a request and return a object from Gateway/Response/Transaction class
const transaction = await hipayClient.requestHostedPaymentPage(hpayment);
const forwardUrl = transaction.forwardUrl;
```

And then process a redirection to this payment page generated by Hipay.

### Manage transactions

It performs a maintenance operation on a given transaction. Different operations are possible:

* capture
* refund
* cancel
* acceptChallenge
* denyChallenge An example to process a capture on a transaction:

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');

const maintenance = new HiPay.MaintenanceRequest({
amount: '21.60',
operation: 'capture',
operation_id: 'capture_1',
basket: '{}'
});

const operation = await hipayClient.requestMaintenanceOperation(
maintenance,
'1000000000090909'
);
```

## PSD2 & SCA

As of September 14, 2019, the issuer will decide if a payment is processed depending on the analysis of more than 150 data collected during the purchasing process. You can see all the new parameters on our explorer API .

Our NodeJS SDK allows you to feed all the information related to the PSD2. You will find all properties on the OrderRequest class and all classes in the HiPay.ThreeDSTwo property.

You can easily feed the information, all the information is automatically converted into the correct format to HiPay payment API.

Here is an example with the feed information for PSD2.

JavaScript

JavaScript

```
const HiPay = require('@hipay/hipay-enterprise-sdk-nodejs');
const {
DeviceChannel,
NameIndicator,
DeliveryTimeFrame,
PurchaseIndicator,
ReorderIndicator,
ShippingIndicator,
AccountInfo,
BrowserInfo,
PreviousAuthInfo,
MerchantRiskStatement,
} = HiPay.ThreeDSTwo;
const { Customer, Payment, Purchase, Shipping } = AccountInfo;

// Customer info
const customer = new Customer({
account_change: 20190814,
opening_account_date: 20190814
});

// Purchase info
const purchase = new Purchase({
count: 1,
card_stored_24h: 1,
payment_attempts_24h: 1,
payment_attempts_1y: 1
});

// Payment info
const payment = new Payment({
enrollment_date: 20190814
});

// Shipping info
const shipping = new Shipping({
name_indicator: NameIndicator.IDENTICAL
});

// Account info
const accountInfo = new AccountInfo({
customer: customer,
purchase: purchase,
payment: payment,
shipping: shipping
});

// Browser info
const browserInfo = new BrowserInfo({
ipaddr: '127.0.0.1',
http_accept: !!req.get('Accept'),
javascript_enabled: true,
java_enabled: true,
language: 'fr',
color_depth: 32,
screen_height: 1900,
screen_width: 1280,
timezone: -120,
http_user_agent: req.get('User-Agent')
});

// Previous Auth info
const previousAuthInfo = new PreviousAuthInfo({
transaction_reference: '192993384884'
});

// Merchant Risk info
const merchantRiskStatement = new MerchantRiskStatement({
email_delivery_address: '[email protected]',
delivery_time_frame: DeliveryTimeFrame.ELECTRONIC_DELIVERY,
purchase_indicator: PurchaseIndicator.MERCHANDISE_AVAILABLE,
reorder_indicator: ReorderIndicator.FIRST_TIME_ORDERED,
shipping_indicator: ShippingIndicator.DIGITAL_GOODS
});

const order = new HiPay.OrderRequest({
orderid: 'ORDER #123456',
operation: 'Sale',
paymentProduct: 'visa',
browserInfo: browserInfo,
previousAuthInfo: previousAuthInfo,
merchantRiskStatement: merchantRiskStatement,
// Set Device Channel
deviceChannel: DeviceChannel.BROWSER
});
```

## Unit Tests

All tests are included in the test/ folder. You can run unit tests with Jest.

Bash

Bash

```
npm run test test/unit/
```

Bash

Bash

```
yarn jest test/unit
```
