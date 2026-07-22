---
description: "Reach an engaged and loyal network of more than 400 million active accounts looking to pay with PayPal. Presentation Brand Payment flow API Product Co"
icon: file-lines
---

# PayPal V2

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/paypal](https://developer.hipay.com/online-payments/payment-means/paypal)
{% endhint %}

Reach an engaged and loyal network of more than 400 million active accounts looking to pay with PayPal.

## Presentation

Brand
Payment flow
API Product Code
Countries
Currencies
3DS
Refund / Partial refund
Recurring

PayPal
Popup
paypal
Worldwide
Worldwide

/

### Activation

Ask our support or your HiPay Account Manager to enable PayPal v2 for your account.

### SDK setup

To get started, include the HiPay JavaScript SDK on your HTML page. Here is the documentation to do so.

Then, create an instance of the HiPay JavaScript SDK by reading this documentation .

Now, to determine where to place the PayPal button, the SDK needs to know in which div to instantiate the button.

So first, add in your payment web page, a new div container where the PayPal button will be displayed. Make sure that the selector div is empty. And ensure that your div has a clear ID, as we will need this ID later.

HTML

HTML

```

```

Now, we need to inform the SDK that we want to instantiate a PayPal button.
To do this, you have to call the
create
function with the first argument
paypal
and a second one with the configuration of your PayPal button.

JavaScript

JavaScript

```
// Configuration
const request = {
amount: '32.99', // required
currency: 'EUR', // required
locale: 'en_US'
};

const paypalButtonStyle = {
shape: 'rect',
color: 'blue'
};

const options = {
canPayLater: false,
request: request,
paypalButtonStyle: paypalButtonStyle,
template: 'auto',
selector: 'paypal-button'
};

var instancePayPal = hipay.create(
'paypal',
options
);
```

At the end of this step, you should see the PayPal button appear. However, be aware that you cannot make a payment yet.

If you don't see the PayPal button but the following screenshot, that means your account is not configured to support PayPal v2.

Please, check the Activation part to enable PayPal v2 on your account.

## Payment

To ensure HiPay has the necessary informations to manage PayPal v2 transactions, you have to setup a frontend solution by using our SDK JS and a backend solution by using one of our backend SDK.

### Frontend

When a customer wants to pay for an order with the PayPal payment method by clicking on the PayPal button, a PayPal popup will be shown up on the same page in order to complete the order on Paypal.

In this popup, the customer needs to login in with his PayPal account, then the popup will show a summary of this order and provide different choices to the customer he could pay for it.

Here is an exemple of this popup, once logged in :

Note that you have to inform amount and currency informations when you need to generate a PayPal button. So it's not possible to update the amount of the PayPal payment session.
If you want to display a new amount in the PayPal popup, you have to destroy and recreate the PayPal instance so it will recreate a new PayPal button.

Once the customer clicks on the Pay button in the PayPal popup, and if the order is accepted, the popup will close and here the next steps to follow to track the order to HiPay.

JavaScript

JavaScript

```
instancePayPal.on('paymentAuthorized', function(paypalData) {
// Call your backend method to create the order.
// Here, handlePayment() is just an example method.
handlePayment(paypalData);
});
```

The paymentAuthorized event is triggered when the PayPal process has completed successfully. You will then receive some PayPal informations that you should pass to your backend server.

You could also implement the following events :

JavaScript

JavaScript

```
instancePayPal.on('paymentUnauthorized', function(error) {
// The payment is unauthorized for some reasons.
});

instancePayPal.on('cancel', function() {
// The customer has cancelled its payment.
});
```

The paymentUnauthorized event is triggered when a problem occurs during the process.

The cancel event is triggered when the customer closes the PayPal popup.

#### Click & Collect

In a Click&Collect scenario, you have to specify a new field customerShippingInformation in your request options as the following example :

JavaScript

JavaScript

```
// Configuration
const request = {
amount: '32.99', // required
currency: 'EUR', // required
customerShippingInformation: { // optional
shippingType: 'CLICK_AND_COLLECT',
zipCode: '75001', // required
city: 'Paris', // required
country: 'FR', // required
streetaddress: '123 Avenue des Champs-Elysees', // required
streetaddress2: 'Appartement 4B, 2eme etage',
firstname: 'John',
lastname: 'Doe',
recipientinfo: 'Test Store' // takes precedence over firstname and lastname
}
};

const options = {
request: request,
template: 'auto',
selector: 'paypal-button'
};

var instancePayPal = hipay.create(
'paypal',
options
);
```

### Backend

Now, you need to handle the payment on the backend. You can refer to one of these documentations :

* PHP SDK
* NodeJS SDK However, for PayPal v2 transactions, you have to provide a specific parameter provider_data in your Order request .

The provider_data parameter is a stringified object you have to build with the following property paypal_id that has the value of the PayPal order ID that could be retrieved in the sent data from your frontend.

Here is an exemple by using our PHP SDK :

PHP

PHP

```
$credentials['private']['login'],
'password' => $credentials['private']['password'],
];

$data = [
'orderid' => 'POC_PAYPAL_V2_' . rand(),
'operation' => 'Sale',
'accept_url' => $FRONDEND_URL . '/?type=accept',
'decline_url' => $FRONDEND_URL . '/?type=error',
'cancel_url' => $FRONDEND_URL . '/?type=error',
'language' => 'fr_FR',
'custom_data' => '{"item 1":"Large Mocha Latte", "item 2":"Banana Nut Muffin"}',
// ...
];

try {
//Get JSON data from front-end
$receivedData = json_decode(file_get_contents('php://input'), true);

//Set reponse code at 200
http_response_code(200);

$config = new \HiPay\Fullservice\HTTP\Configuration\Configuration([
'apiUsername' => $logins['login'],
'apiPassword' => $logins['password']
]);
$clientProvider = new \HiPay\Fullservice\HTTP\SimpleHTTPClient($config);
$gatewayClient = new \HiPay\Fullservice\Gateway\Client\GatewayClient($clientProvider);

//Instantiate order request
$orderRequest = new \HiPay\Fullservice\Gateway\Request\Order\OrderRequest();
$orderRequest->orderid = $data['orderid'];
$orderRequest->operation = $data['operation'];
$orderRequest->description = $data['description'];
$orderRequest->long_description = $data['long_description'];
$orderRequest->accept_url = $data['accept_url'];
$orderRequest->decline_url = $data['decline_url'];
$orderRequest->pending_url = $data['pending_url'];
$orderRequest->exception_url = $data['exception_url'];
$orderRequest->cancel_url = $data['cancel_url'];
$orderRequest->notify_url = $data['notify_url'];
$orderRequest->language = $data['language'];
$orderRequest->custom_data = $data['custom_data'];
$orderRequest->payment_product = $receivedData['payment_product'];
// Set provider_data parameter if the payment method is PayPal and if the frontend sent an orderID parameter
if ($orderRequest->payment_product === 'paypal' && isset($receivedData['orderID'])) {
$providerData = ['paypal_id' => $receivedData['orderID']];
$orderRequest->provider_data = json_encode($providerData);
}

//Send the request order
$transaction = $gatewayClient->requestNewOrder($orderRequest);

$response = [
'transaction_number' => $transaction->getTransactionReference(),
'order_id' => $transaction->getOrder()->getId(),
'forward_url' => (!$transaction->getReason() ? $data['accept_url'] : $data['cancel_url']),
];

// This response is send to the front-end at the success of AJAX call
echo json_encode($response);

} catch (\Exception $e) {
$response = [
'error_message' => $e->getMessage(),
];

// This response is send to the front-end at the failure of AJAX call
echo json_encode($response);
}
```

#### Click & Collect

In a Click&Collect scenario, you also have to provide another specific parameter delivery_method in your Order request with a specific value for the delivery mode as STORE .

Here is an example by using our PHP SDK :

PHP

PHP

```
delivery_information = new DeliveryShippingInfoRequest();
/* delivery_method can be string or object */
$orderRequest->delivery_information->delivery_method = 'STORE';
// OR
$orderRequest->delivery_information->delivery_method = json_encode(['mode' => "STORE", 'shipping' => 'STANDARD']);

//Send the request order
// ...
```

## JS SDK Reference

CREATE

JavaScript

JavaScript

```
var instance = hipay.create('paypal', options);
```

Name
Type
Description

request
object

A request which includes information about the payment.
This parameter is required if your account is configured to support PayPal v2.

paypalButtonStyle
object

The PayPal button can have multiple appearances. See the PaypalButtonStyle section below for more details.

canPayLater
boolean

If true , another PayPal button will appear below the basic one in order to purchase an order in installments.

This button is only available if the order amount is between 30 and 2000 and if the currency is EUR ().

Default is true .

selector
string

Unique div id to generate the button.

Here is a screenshot when enabling the
canPayLater
parameter :

### request

A request includes all information about the current payment.

Name Type Description amount

required string or number

string recommended

The order amount which will be displayed in the PayPal popup.
It must be greater than zero, and can contain a maximum of 2 decimal places. currency

required string The three-letter ISO 4217 currency code for the payment. locale string The locale code to use for the label of the PayPal button.st
Example: en_US
Default is a locale based on the HiPay instance
language . customerShippingInformation object All the information needed for delivery

### paypalButtonStyle

This configuration customizes the PayPal button appearance which includes a shape, a color, a label and a height.

Name Type Description shape string The shape of the PayPal button :
pill or
rect .
Default is pill . color string The color of the PayPal button :
gold ,
blue ,
black ,
silver or
white .
Default is gold . label string The label of the PayPal button :
pay ,
paypal ,
subscribe ,
checkout or
buynow .
Default is pay . height number The height of the PayPal button.
Minimum : 25
Maxiumum : 55
Default is 40 .

### customershippinginformation

All the information needed for delivery

Name Type Description shippingType string The type of delivery.

SHIPPING for home delivery. CLICK_AND_COLLECT for delivery to a relay point.

Default : SHIPPING

zipCode

required string Postal code of the delivery destination (pickup location). city

required string City of the delivery destination (pickup location). country

required string Country code of the destination, following the ISO 3166-1 alpha-2 format (or C2' for a specific case). streetaddress

required string First line of the physical address (e.g., number and street name). streetaddress2 string Second line of the address (e.g., apartment, suite, P.O. box). firstname string First name of the recipient or the person picking up the order. lastname string Last name of the recipient or the person picking up the order. recipientinfo string Additional information about the recipient (e.g., company name or special instructions).

### Events

JavaScript

JavaScript

```
instance.on(event', callback)
```

Name

Description

Response

paymentAuthorized

Emitted when the user has validated the payment inside the PayPal popup.

paypalData : object

paymentUnauthorized

Emitted when an error occured during the process in the PayPal popup.

error : object

It will return an Error variable that indicates the reason of the failed payment with your PayPal instance. cancel

Emitted when the user clicks on the cancel button of the PayPal popup.
