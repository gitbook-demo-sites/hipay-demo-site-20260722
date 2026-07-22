---
description: "The PHP SKD simplifies HiPay Enterprise APIs integration . Requirements PHP >=7.2 Composer >= 1.0.0 HiPay Enterprise API Credentials Installation Befo"
icon: file-lines
---

# PHP SDK

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/sdk-reference/sdk-php](https://developer.hipay.com/online-payments/sdk-reference/sdk-php)
{% endhint %}

The PHP SKD simplifies HiPay Enterprise APIs integration .

## Requirements

* PHP >=7.2

* Composer >= 1.0.0

* HiPay Enterprise API Credentials

## Installation

* Before starting the installation, please read all the instructions and make sure you've gone through the Prerequisites and recommendations section.

It is recommended to use Composer to install the HiPay Enterprise SDK for PHP .

### Composer

If your project is not based on Composer, you must install it and create a composer.json file in your root project directory.

* Composer installation

* Composer project setup

For the next steps, you need a command line interface; all commands are executed in your root project directory.

### SDK installation

You can now install the SDK with the following command line:

Bash

Bash

```
composer require hipay/hipay-fullservice-sdk-php
```

If no errors are displayed, the module is installed.

### Autoloading

For libraries that specify autoload information, Composer generates a vendor/autoload.php file. You just need to include this file to get autoloading for free.

PHP

PHP

```
require __DIR__ . '/vendor/autoload.php';
```

For more information: https://getcomposer.org/doc/01-basic-usage.md#autoloading

## API Calls

You need to instantiate 4 objects to make a request:

* A configuration object which implements ConfigurationInterface
* A client provider inherited from abstract class \HiPay\Fullservice\HTTP\ClientProvider
* A Gateway client
* An Order request The SDK allows you to call the different HiPay APIs that allow you to perform a transaction.

You can therefore interact with our different APIS : /order , /hpayment and /maintenance . Whatever the request, you must instantiate a client gateway in the following way.

PHP

PHP

```
//Create a configuration object
// By default Configuration object is configured in Stage mode (Configuration::API_ENV_STAGE)
$config = new \HiPay\Fullservice\HTTP\Configuration\Configuration(
array(
"apiUsername" => "YOUR_API_USERNAME",
"apiPassword" => "YOUR_API_PASSWORD",
"apiEnv" => Configuration::API_ENV_STAGE,
"hostedPageV2" => true
)
);

//Instantiate client provider with configuration object
$clientProvider = new \HiPay\Fullservice\HTTP\SimpleHTTPClient($config);

//Create your gateway client
$gatewayClient = new \HiPay\Fullservice\Gateway\Client\GatewayClient($clientProvider);
```

To switch to Production mode, please init the configuration with: Configuration::API_ENV_PRODUCTION

### Timeout

We recommend you to use a client request timeout of 60 seconds.

Indeed, some API requests may take longer than expected because they rely on different actors.

If your client request timeout is too short and the response takes longer, the transaction will be paid and created at HiPay but your end user will have an error.

### Order

In this case, the payment page is hosted on your website, allowing you to have a unified and fully customized workflow. Please refer to the POST Order below for more information.

Please note that if you want to execute transactions with credit or debit card payment products, you will need to tokenize card numbers beforehand by using the HiPay Enterprise Tokenization API .

To have the function of each attribute, please refer to the technical documentation of each API.

Instantiate an OrderRequest object:

PHP

PHP

```
$orderRequest = new \HiPay\Fullservice\Gateway\Request\Order\OrderRequest();
$orderRequest->orderid = "ORDER #123456";
$orderRequest->operation = "Sale";
$orderRequest->payment_product = "visa";
$orderRequest->description = "ref_85";
$orderRequest->currency = "EUR";
$orderRequest->amount = "21.60";
$orderRequest->shipping = "0.00";
$orderRequest->tax = "3.6";
$orderRequest->cid = null;
$orderRequest->ipaddr = "172.20.0.1";
$orderRequest->accept_url = "http:/www.my-shop.fr/checkout/accept";
$orderRequest->decline_url = "http:/www.my-shop.fr/checkout/decline";
$orderRequest->pending_url = "http:/www.my-shop.fr/checkout/pending";
$orderRequest->exception_url = "http:/www.my-shop.fr/checkout/exeception";
$orderRequest->cancel_url = "http:/www.my-shop.fr/checkout/cancel";
$orderRequest->http_accept = "*/*";
$orderRequest->http_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36";
$orderRequest->language = "en_US";
$orderRequest->custom_data = "{\"shipping_description\":\"Flat rate\",\"payment_code\":\"visa\",\"display_iframe\":0}";
```

There are several complementary objects to complete the information required by the API order:

* CustomerShippingInfoRequest: Order related to the shipping information.
* CustomerBillingInfoRequest: Order related to the billing information.
* CardTokenPaymentMethod: Data related to payment with token system. CardTokenPaymentMethod

This parameter is specific to credit and debit card payment products. This is the token obtained from the HiPay Enterprise Secure Vault API when tokenizing a credit or debit card. To generate a token, please refer to the HiPay Enterprise Tokenization API documentation .

PHP

PHP

```
$paymentMethod = new \HiPay\Fullservice\Gateway\Request\PaymentMethod\CardTokenPaymentMethod();
$paymentMethod->cardtoken = "61f92d7a135db52dbd583b2aad208e73978196392357f674bacf39f549042f14";
$paymentMethod->eci = 7;
$paymentMethod->authentication_indicator = 0;

$orderRequest->paymentMethod = $paymentMethod;
```

CustomerShippingInfoRequest and CustomerBillingInfoRequest

These two objects are related to the delivery and billing addresses. You can find the same type of information on both objects.

PHP

PHP

```
$customerBillingInfo = new \HiPay\Fullservice\Gateway\Request\Info\CustomerBillingInfoRequest();
$customerBillingInfo->firstname = "Jane";
$customerBillingInfo->lastname = "Doe";
$customerBillingInfo->email = "[email protected]";
$customerBillingInfo->birthdate = "19901125";
$customerBillingInfo->recipientinfo = "Dr";
$customerBillingInfo->streetaddress = "56 avenue de la paix";
$customerBillingInfo->streetaddress2 = "";
$customerBillingInfo->city = "Paris";
$customerBillingInfo->state = "";
$customerBillingInfo->zipcode = "75000";
$customerBillingInfo->country = "FR";
$customerBillingInfo->phone = "0130811322";
$customerBillingInfo->gender = "M";

$orderRequest->customerBillingInfo = $customerBillingInfo;

$customerShippingInfo = new \HiPay\Fullservice\Gateway\Request\Info\CustomerShippingInfoRequest();
$customerShippingInfo->shipto_firstname = "Jane";
$customerShippingInfo->shipto_lastname = "Doe";
$customerShippingInfo->shipto_streetaddress = "56 avenue de la paix";
$customerShippingInfo->shipto_streetaddress2 = "";
$customerShippingInfo->shipto_city = "Paris";
$customerShippingInfo->shipto_state = "";
$customerShippingInfo->shipto_zipcode = "75000";
$customerShippingInfo->shipto_country = "FR";
$customerShippingInfo->shipto_phone = "0130811322";
$customerShippingInfo->shipto_msisdn = "0600000000";
$customerShippingInfo->shipto_gender = "M";

$orderRequest->customerShippingInfo = $customerShippingInfo;
```

Once everything is completed you can start the transaction.

PHP

PHP

```
//Make a request and return \HiPay\Fullservice\Gateway\Model\Transaction.php object
$transaction = $gatewayClient->requestNewOrder($orderRequest);
```

At the return of the API, the transaction can have one of the following status:

* completed
* pending
* declined
* error You must therefore perform a different treatment according to each status, and redirect the customer to the corresponding page of your website.

PHP

PHP

```
$forwardUrl = $transaction->getForwardUrl();
switch ($transaction->getState()) {
case TransactionState::COMPLETED:
case TransactionState::PENDING:
$redirectUrl = [YOUR_URL_FOR_PENDING_PAYMENT]
break;
case TransactionState::FORWARDING:
$redirectUrl = $forwardUrl;
break;
case TransactionState::DECLINED:
$reason = $transaction->getReason();
$this->logErrors('There was an error requesting new transaction: ' . $reason['message']);
throw new Payment_Exception('Sorry, your payment has been declined. Please try again with an other means of payment.');
case TransactionState::ERROR:
$redirectUrl = [YOUR_URL_FOR_ERROR_PAYMENT];
$reason = $transaction->getReason();
$this->logErrors('There was an error requesting new transaction: ' . $reason['message']);
throw new Payment_Exception('An error occured, process has been cancelled.')
default:
throw new Payment_Exception('An error occured, process has been cancelled.')
}

return $redirectUrl;
```

### Hosted Page

HiPay Enterprise hosts your payment page on a secured site. With this option you can benefit from a single point of contact, adaptable payment pages, and the PCI-DSS standard. You can therefore outsource heavy security requirements that are related to payment acceptance.

Unlike the API order, you must not perform a tokenization. Some parameters need to be added but the webservice relies on the same type of operation.

You must redirect the consumer to the URL forward provided in the webservice response.

Instantiate a HostedPaymentPageRequest object:

PHP

PHP

```
$hpaymentRequest = new \HiPay\Fullservice\Gateway\Request\Order\HostedPaymentPageRequest();
$hpaymentRequest->orderid = "ORDER #123456";
$hpaymentRequest->operation = "Sale";
$hpaymentRequest->description = "ref_85";
$hpaymentRequest->customerBillingInfo = new \HiPay\Fullservice\Gateway\Request\Info\CustomerBillingInfoRequest();
$hpaymentRequest->customerBillingInfo->firstname = "Jane";
$hpaymentRequest->customerBillingInfo->lastname = "Doe";
$hpaymentRequest->currency = "EUR";
$hpaymentRequest->amount = "21.60";
$hpaymentRequest->shipping = "0.00";
$hpaymentRequest->tax = "3.6";
$hpaymentRequest->cid = null;
$hpaymentRequest->ipaddr = "172.20.0.1";
$hpaymentRequest->accept_url = "http:/www.my-shop.fr/checkout/accept";
$hpaymentRequest->decline_url = "http:/www.my-shop.fr/checkout/decline";
$hpaymentRequest->pending_url = "http:/www.my-shop.fr/checkout/pending";
$hpaymentRequest->exception_url = "http:/www.my-shop.fr/checkout/exeception";
$hpaymentRequest->cancel_url = "http:/www.my-shop.fr/checkout/cancel";
$hpaymentRequest->http_accept = "*/*";
$hpaymentRequest->http_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36";
$hpaymentRequest->language = "en_US";
$hpaymentRequest->paymentMethod = new \HiPay\Fullservice\Gateway\Request\PaymentMethod\CardTokenPaymentMethod();
$hpaymentRequest->paymentMethod->authentication_indicator = 0;
```

In addition to these parameters, you can enter specific information related to the hpayment. To know:

PHP

PHP

```
$hpaymentRequest->payment_product_list = "visa,mastercard,cb,maestro,american-express";
$hpaymentRequest->payment_product_category_list = "";
$hpaymentRequest->css = "";
$hpaymentRequest->template = "basic-js";
$hpaymentRequest->display_selector = "1";
$hpaymentRequest->time_limit_to_pay = 3000;
$hpaymentRequest->multi_use = 0;
$hpaymentRequest->theme_code = 'ThDPIJs3yhMUxMNPGx8v';
$hpaymentRequest->display_cancel_button = 1;
```

Once everything is completed you can start the transaction.

PHP

PHP

```
//Make a request and return \HiPay\Fullservice\Gateway\Model\Transaction.php object
$transaction = $gatewayClient->requestHostedPaymentPage($hpaymentRequest);
$forwardUrl = $transaction->getForwardUrl();
```

And then process a redirection to this payment page generated by Hipay.

### Manage transactions

It performs a maintenance operation on a given transaction. Different operations are possible:

* capture
* refund
* cancel
* acceptChallenge
* denyChallenge An example to process a capture on a transaction:

PHP

PHP

```
$maintenanceRequest = new \HiPay\Fullservice\Gateway\Request\Maintenance\MaintenanceRequest();
$maintenanceRequest->amount = "21.60";
$maintenanceRequest->operation = "capture";
$maintenanceRequest->operation_id = "capture_1";
$maintenanceRequest->basket = "{}";

$transaction = $gatewayClient->requestMaintenanceOperation(
"capture"
"1000000000090909",
"21.60",
"capture_1",
$maintenanceRequest
);
```

The object maintenanceRequest is not necessary if you don't perform any operation with a basket.

## Signature Verification

In order to inform you of events related to your payment system, such as a new transaction or a 3-D Secure transaction, the HiPay Enterprise platform can send a server-to-server notification to your application.

It is strongly recommended to use a signature mechanism to verify the contents of a request or redirection made to your servers. This prevents customers from tampering with the data in the data exchanges between your servers and our payment system.

A unique signature is sent each time HiPay contacts any seller's URL, notification or redirection.

The PHP SDK provides a method to verify the signature. To use it you just have to pass the passphrase and hash algorithm set up in your account.

PHP

PHP

```
$isValidSignature = Signature::isValidHttpSignature($passphrase, $hashAlgorithm);
```

The content of the request comes from either the raw post data or the url parameters if it is a redirection.

## PSD2 & SCA

As of September 14, 2019, the issuer will decide if a payment is processed depending on the analysis of more than 150 data collected during the purchasing process. You can see all the new parameters on our explorer API .

Our PHP SDK allows you to feed all the information related to the PSD2. You will find all properties on the OrderRequest class and all classes in the HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo package.

The following classes are available:

\HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\PreviousAuthInfo ,
\HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\MerchantRiskStatement ,
\HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo and
\HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\RecurringInfo

You can easily feed the information, all the information is automatically converted into the correct format to HiPay payment API.

Here is an example with the feed information for PSD2.

PHP

PHP

```
use \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo\Customer as CustomerInfo;
use \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo\Purchase as PurchaseInfo;
use \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo\Payment as PaymentInfo;
use \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo\Shipping as ShippingInfo;

$orderRequest = new \HiPay\Fullservice\Gateway\Request\Order\OrderRequest();
$orderRequest->orderid = "ORDER #123456";
$orderRequest->operation = "Sale";
$orderRequest->payment_product = "visa";

// Set Device Channel
$orderRequest->device_channel = DeviceChannel::BROWSER;

///////////////////////////////////////////////////////
////////// ACCOUNT INFO //////////
///////////////////////////////////////////////////////
$accountInfo = new HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\AccountInfo();

// Customer info
$customerInfo = new CustomerInfo();
$customerInfo->account_change = 20190814;
$customerInfo->opening_account_date = 20190814;

$accountInfo->customer = $customerInfo;

// Purchase info
$purchaseInfo = new PurchaseInfo();
$purchaseInfo->count = 1;
$purchaseInfo->card_stored_24h = 1;
$purchaseInfo->payment_attempts_24h = 1;
$purchaseInfo->payment_attempts_1y = 1;
$accountInfo->purchase = $purchaseInfo;

// Payment info
$paymentInfo = new PaymentInfo();
$paymentInfo->enrollment_date = 20190814;
$accountInfo->payment = $paymentInfo;

// Shipping info
$shippingInfo = new ShippingInfo();
$shippingInfo->name_indicator = NameIndicator::IDENTICAL;
$accountInfo->shipping = $shippingInfo;

///////////////////////////////////////////////////////
////////// BROWSER INFO //////////
///////////////////////////////////////////////////////

$browserInfo = new \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\BrowserInfo();
$browserInfo->ipaddr = '127.0.0.1';
$browserInfo->http_accept = isset($_SERVER['HTTP_ACCEPT']) ? $_SERVER['HTTP_ACCEPT'] : null;
$browserInfo->javascript_enabled = true;
$browserInfo->java_enabled = true;
$browserInfo->language = 'fr';
$browserInfo->color_depth = 32;
$browserInfo->screen_height = 1900;
$browserInfo->screen_width = 1280;
$browserInfo->timezone = -120;
$browserInfo->http_user_agent = $_SERVER['HTTP_USER_AGENT'];
$orderRequest->browser_info = $browserInfo;

///////////////////////////////////////////////////////
////////// PREVIOUS INFO //////////
///////////////////////////////////////////////////////

$previousAuthInfo = new \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\PreviousAuthInfo();

$previousAuthInfo->transaction_reference = '192993384884';
$orderRequest->previous_auth_info = $previousAuthInfo;

///////////////////////////////////////////////////////
////////// MERCHANT RISK INFO //////////
///////////////////////////////////////////////////////
$merchantRiskStatement = new \HiPay\Fullservice\Gateway\Model\Request\ThreeDSTwo\MerchantRiskStatement();

$merchantRiskStatement->email_delivery_address = '[email protected]';
$merchantRiskStatement->delivery_time_frame = HiPay\Fullservice\Enum\ThreeDSTwo\DeliveryTimeFrame::ELECTRONIC_DELIVERY;

$merchantRiskStatement->purchase_indicator = HiPay\Fullservice\Enum\ThreeDSTwo\PurchaseIndicator::MERCHANDISE_AVAILABLE;

$merchantRiskStatement->reorder_indicator = \HiPay\Fullservice\Enum\ThreeDSTwo\ReorderIndicator::FIRST_TIME_ORDERED;

$merchantRiskStatement->shipping_indicator = HiPay\Fullservice\Enum\ThreeDSTwo\ShippingIndicator::DIGITAL_GOODS;

$orderRequest->merchant_risk_statement = $merchantRiskStatement;
```

## Unit Tests

All tests are included in the tests/ folder. You can run unit tests with phpunit.

Bash

Bash

```
phpunit -c tests/unit/phpunit.xml
```
