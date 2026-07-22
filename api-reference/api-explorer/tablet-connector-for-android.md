---
description: "WARNING: this documentation is intended for the Smart Terminal offer (standalone payment terminals) and dedicated to the scenarios based on Android de"
icon: file-lines
---

# Tablet Connector for Android

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/api-explorer/tablet-connector-for-android](https://developer.hipay.com/api-explorer/tablet-connector-for-android)
{% endhint %}

WARNING: this documentation is intended for the Smart Terminal offer (standalone payment terminals) and dedicated to the scenarios based on Android devices. If you are looking for the documentation related to iOS devices, please consult the dedicated page .

## Description

The Tablet Connector for Android allows you to trigger in-store payments from an Android device (smartphone or tablet), by sending a payment request to a specific POS payment terminal through the Cloud API , thanks to a simple and dedicated Software Development Kit (SDK).

When a payment request is sent via the SDK, it then :
- sends a payment request to the Cloud API
- awakes the targeted payment terminal by forwarding the payment request to the provided IP address / port
- waits for the payment processing
- receives the payment response with the payment information

Please note this documentation introduces the Tablet Connector by presenting its requirements and how to implement it (endpoints, request parameters, response parameters, error codes, etc.).
If you are looking for a presentation overview, please check the dedicated page .

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Tablet Connector for Android:

REQUIREMENT
DETAILS

POS payment terminal
A payment terminal supporting Concert protocol version 3.1 or 3.2 (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable Internet (Wi-Fi) connection
- A fixed public IP address for the network router is needed to join the payment terminal. In case your public IP address changes over time, it is usually possible to fix it by contacting your Internet access provider (please notice additional costs may be applied)

Android device
An Android device (smartphone or tablet) with Android 5.0 Lollipop (API 21) or later

IDE
Android Studio with version 4.1 or later

Dependency manager
Gradle (Maven)

Security
Public API credentials enabled (please consult this page to get details about HiPay credentials).

## Installation

The SDK is hosted on HiPay's repository.
In order to install it, you need to add the dependencies to your Android app:

build.gradle (project file)

```
allprojects { repositories { maven { url "https://artifactory.hipay.com/repository/maven-public/" } }}
```

build.gradle (module app file)

```
dependencies { implementation 'com.hipay:hipay-omnichannel-concertv3:2.1.0'}
```

## Initialization

### Concept overviews

Some configuration is necessary to be able to communicate with a POS payment terminal via the Tablet Connector for Android.
This configuration can be set via the SDK thanks to two main object classes:
- Configuration
- Contract

### Configuration

The configuration object defines the main information that will be used to communicate with the POS payment terminal.

ATTRIBUTE
DESCRIPTION
M/O
TYPE
DEFAULT VALUE
EXAMPLES

protocol

Version of the Concert protocol to use to communicate with the POS payment terminal.

Possible values:
- ConcertV31 = Protocole Concert V3.1
- ConcertV32 = Protocole Concert V3.2

O
Enum
N/A
- ConcertV31
- ConcertV32

host
IPv4 address or domain name of the POS payment terminal
M
String
N/A
- 192.168.1.10
- your.domain.com

port
Port used by the POS payment terminal to listen to ConcertV3 payment request.
O
Integer
8888
- 8888
- 5000

contracts
Collection of contracts configured on the POS payment terminal (cf. dedicated Contract section).
M
Contract array
N/A
N/A

apiUsername
Public username API on HiPay's side, used to perform authentication.
M
String
N/A
123456789.stage-secure-gateway.hipay-tpp.com

apiPassword
Public password API on HiPay's side, used to perform authentication.
M
String
N/A
Test_AB1238903bd5eg457

environment

Target environment (allows to target a stage environment for test purposes).

Possible values:
- production = Production
- stage = Stage (testing environment)

O
Enum
production
- production
- stage

authorizationThreshold
When the amount is above this threshold, the authorization request is automatically forced.
O
Float
N/A
- 100.00
- 50.00

debug
Whether the debug mode is enabled or not.
When the debug mode is enabled, debug messages are printed.
O
Boolean
False
- True
- False

healthCheckFrequency
Delay between health check in seconds, to check if the communication with the POS payment terminal is working.
This feature can be disabled by setting its value to 0.
O
Integer
N/A
- 0
- 60
- 300

healthCheckCallback
Callback function triggered when the healthCheckFrequency attribute is set (value different of 0).
This function will receive every healthCheckFrequency seconds a boolean indicating whether the communication with the POS payment terminal is working or not.
O
Callback
N/A
N/A

deviceSerialNumber
Serial number of the POS payment terminal.
This information is required to perform health checks.
O
String
N/A
- 123-456-789
- WL01234567

Notes:
- M/O means Mandatory / Optional.

### Contract

A contract is composed with 3 attributes:
- the merchant contract (also named MID for Merchant Identification Number)
- the payment application identifier
- the rank of the payment terminal

All these attributes are necessary to be able to associate the payment information with the payment request information in Console - HiPay's Back Office.

That's why it is important to make sure these attributes match with the POS payment terminal configuration.

ATTRIBUTE
DESCRIPTION
M/O
TYPE
EXAMPLES

merchantContract
The MID (Merchant Identification Number) provided by the acquirer.
M
String
1234567

paymentApplication

The payment application identifier that will be used to process the operation.

Possible values:
- 000 = Indifferent
- 001 = CB (VISA/MASTERCARD) with contact mode
- 002 = American Express with contact mode
- 003 = CB ENSEIGNE (CETELEM instalment payment)
- 004 = CETELEM
- 005 = COFINOGA
- 006 = DINNER'S CLUB
- 007 = PASS
- 008 = FRANFINANCE
- 009 = JCB
- 101 = CB VAD (Payment by entering the CB card numbers)
- 201 = quasi-Cash
- 301 = PLBS (Product Location Goods and Services)
- 401 = OPTALION (Credit Lyonnais instalment payment)
- 501 = Cash-Agence
- 601 = PNF (Credit Mutuel instalment payment)
- 602 = P3F
- 603 = OPTALION
- 604 = Preauto-CM
- 605 = PRCME
- 607 = Paiement-QR (Payment by QR-Code)
- 608 = TOP3-3XCB
- 609 = PNF-HPS
- 701 = PPFCA (Credit Agricole)
- 00A = Banque Accord EMV
- 00B = CB (VISA/MASTERCARD) contactless
- 00C = CHEQUE
- 00D = American Express contactless
- 00E = CONECS with contact mode
- 00F = DCC (Dynamic Currency Conversion)
- 00G = QuickPass
- 00I = CPEI-EMV
- 00S = SOFINCO (private card)
- 00U = UPI (China Union Pay)
- 10E = CONECS contactless
- 30F = PLBS-DCC-GB

M
String
001

rank
The rank of the payment terminal
M
String
001

Notes:
- M/O means Mandatory / Optional.

### Example

Java

Java

```
public class MainActivity extends AppCompatActivity {
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

ArrayList contracts = new ArrayList();
Contract contactMid = new Contract("1234567", 001", "005");
Contract contactlessMid = new Contract("1234568", 001", "005");
contracts.add(contactMid);
contracts.add(contactlessMid);

HealthCheckCallback healthCheckCallback = new HealthCheckCallback() {
@Override
public void getTerminalStatus(boolean isUp) {
// Check the status
}
};

try {
Configuration.getInstance().setConfiguration(
Protocol.CONCERTV32, // protocol
"192.168.1.1", // host
8888, // port
"username", // apiUsername
"password", // apiPassword
Environment.STAGE, // environment
10.0f, // authorizationThreshold
contracts, // contracts
true, // debug
10, // healthCheckFrequency
healthCheckCallback, // healthCheckCallback
"123456", // deviceSerialNumber
this
);

// THEN USE THIS CONFIGURATION TO SEND PAYMENT REQUESTS
} catch (InvalidHostException e) {
// Handle invalidIpAddressException
} catch (InvalidPortException e) {
// Handle InvalidPortException
} catch (InvalidUsernamePasswordAPIException e) {
// Handle InvalidUsernamePasswordAPIException
} catch (InvalidContractsException e) {
// Handle InvalidContractsException
}
}
}
```

## Payment request

### Concept overview

For each payment request to send to a POS payment terminal, you have to create a RequestPayment object. When your RequestPayment is created, you execute it with the corresponding Android method execute(this). Your class has to conform to the RequestPaymentDelegate delegate to receive a response.

### Parameters

ATTRIBUTE
DESCRIPTION
M/O
TYPE
DEFAULT VALUE
EXAMPLES

amount
Total order amount.
It is defined as the sum of all the purchased item amounts, plus shipping fees (if relevant), plus tax fees (if relevant).
M
Float
N/A
- 9.99
- 123.45

transactionType

Type of transaction to be performed.

Possible values:
- Debit
- Credit
- Cancellation
- Duplicata

O
Enum
Debit
- Debit
- Credit
- Cancellation
- Duplicata

forceAuthorization
Whether an authorization request should be forced or not.
O
Boolean
False
True
False

currency
Base currency used for the transaction.
This three-character currency alpha must comply with ISO 4217 format .
O
Enum
EUR
EUR
USD

orderId
Merchant transaction identifier used to uniquely identify each transaction from every merchant transaction.
O
String
N/A
- ORD_20221015_123

cart

Collection of cart items that compose the customer cart (cf. dedicated Cart section).

If the cart content is not correctly fulfilled or doesn't match the total amount of the order, the order will be created with an empty cart.

O
Cart
N/A
N/A

customer
Customer's information (id, first name, last name, email address, etc.).
O
Customer
N/A
N/A

customData

Additional data to share any relevant information.

Only the following types of information are accepted:
- Boolean
- Integer
- Float
- String

O
HashMap
N/A
N/A

receiptSendingOption

Channel used to send the customer receipt.

This attribute works only with the version 3.2 of ConcertV3 protocol.

O
Enum
All
- All
- SMS
- Email

Notes:
- M/O means Mandatory / Optional.

### Example

Java

Java

```
@Override
public void onClick(View view) {
try {
/***********************************************************************/
/* Prepare the cart object with two items: 2 tables and 4 chairs */
/***********************************************************************/
Item table = new Item(
"A2343SSS",
ItemType.GOOD,
"Table",
2,
30.50f,
0.0f,
58.00f
);
table.setDiscount(-3.00f);
table.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
table.setEuropeanArticleNumbering("4711892728946");
table.setImageUrl("https://wwww.hipay.com");

Item chair = new Item(
"B7762NN",
ItemType.GOOD,
"Chair",
4,
10.20f,
0.0f,
40.80f
);
chair.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
chair.setProductDescription("A wooden chair");
chair.setEuropeanArticleNumbering("4713716322385");
chair.setImageUrl("https://wwww.hipay.com");

ArrayList itemArrayList = new ArrayList();
itemArrayList.add(table);
itemArrayList.add(chair);
Cart cart = new Cart(itemArrayList);

/************************************/
/* Prepare the customer object */
/************************************/
Customer customer = new Customer(
"1234",
"John",
Doe",
[email protected]",
"0602020202",
"1",
"1 rue John Doe",
"Appt 202",
"75000",
"Paris",
null,
"FR"
);

/***************************************************/
/* Prepare the custom additional information */
/***************************************************/
HashMap customData = new HashMap();
customData.put("foo1", "foo2");
customData.put("price", 12.30);
customData.put("event", 34);
customData.put("newCustomer", true);

/***********************************/
/* Create the payment request */
/***********************************/
RequestPayment requestPayment = new RequestPayment(
98.80f, // amount
TransactionType.TRANSACTION_TYPE_DEBIT, // transactionType
false, // forceAuthorization
Currency.EUR, // currency
"order_12345", // orderId
cart, //cart
customer, // customer
customData // customData
);

/*******************************************************************/
/* Send the payment request to the POS payment terminal */
/*******************************************************************/
requestPayment.execute(this);
} catch (InvalidAmountException e) {
// Handle InvalidAmountException
}
}
```

## Payment reponse

### Concept overview

After the transaction has been processed through the HiPay's servers, you will receive a response from the Omnichannel SDK.

### Attributes

ATTRIBUTE
DESCRIPTION
TYPE
EXAMPLES

paymentStatus

Payment result after the processing of the operation by the POS payment terminal.

Possible values:
- Success
- Failure

Enum
- Success
- Failure

errorDescription
In case of failure, this message describes the error.
String
- An unknown error occurred
- The network is unavailable

errorCode

In case of failure, this code identifies the error type.

The exhaustive list of error codes is available in the Error codes section.

String
- 1000
- 1003

amount
Amount really paid by the customer (authorized amount).
It can be lower than the requested amount.
Float
- 9.99
- 123.45

currency
Base currency used to process the payment request.
This three-character currency code must comply with ISO 4217 alpha format .
Enum
- EUR
- USD

orderId
Merchant transaction identifier used to uniquely identify each transaction from every merchant transaction.
String
- ORD_20221015_123

notificationHipaySent
Whether Hipay was notified about the transaction.
Boolean
- True
- False

customer
Customer's information (id, first name, last name, email address, etc.).
Customer
N/A

receipt
The customer receipt, base64 encoded.
String

Note: all these attributes are read-only.

### Example

Java

Java

```
@Override
public void onFinish(ResponsePayment responsePayment) {
if (responsePayment.getPaymentStatus() == PaymentStatus.SUCCESS) {
// Handle success response
} else {
// Handle failed response
}
}
```

## Duplicata

### Introduction

Duplicata is one of the supported transaction types.
Thanks to this transaction type you can send a request to the payment terminal to get the result of the previous payment attempt.

It can be useful when the payment attempt has been processed by the payment terminal, but the payment response was not received, or the payment response was invalid. Such situation might happen in case of network connectivity issues, for example.

Notes: - The Duplicata feature has only been tested with the Verifone V240m payment terminal

### Response

The response in case of a Duplicata request depends on the last payment result :

LAST PAYMENT RESULT
RESPONSE
PAYMENT TERMINAL

Payment success
- paymentStatus: Success
- amount: the amount actually paid
- currency: the payment currency
Duplicata receipt printed

Payment failure
- paymentStatus: Failed
- amount: the amount set in the payment request
- currency: the currency set in the payment request
- No duplicata receipt printed
- Message displayed on the screen: DERNIERE TRANSACTION NON ABOUTIE PAS DE DUPLICATA

Payment abandonment
- paymentStatus: Failed
- amount: the amount set in the payment request
- currency: the currency set in the payment request
- No duplicata receipt printed
- Message displayed on the screen: DERNIERE TRANSACTION NON ABOUTIE PAS DE DUPLICATA

No payment attempt since the last remote collection
- paymentStatus: Failed
- amount: the amount set in the payment request
- currency: the currency set in the payment request
- No duplicata receipt printed
- Message displayed on the screen: DUPLICATA IMPOSSIBLE

### Request

Only the following parameters must be fuffilled to request the last payment result to the payment terminal: - the transaction type: Duplicata
- the amount: it can be any amount (no need to send the previous payment request amount)
- the currency: it can be any currency (no need to send the previous payment request amount)

## Full code sample

Java

Java

```
public class MainActivity extends AppCompatActivity {
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

ArrayList contracts = new ArrayList();
Contract contactMid = new Contract("1234567", 001", "005");
Contract contactlessMid = new Contract("1234568", 001", "005");
contracts.add(contactMid);
contracts.add(contactlessMid);

HealthCheckCallback healthCheckCallback = new HealthCheckCallback() {
@Override
public void getTerminalStatus(boolean isUp) {
// Check the status
}
};

try {
Configuration.getInstance().setConfiguration(
Protocol.CONCERTV32, // protocol
"192.168.1.1", // host
8888, // port
"username", // apiUsername
"password", // apiPassword
Environment.STAGE, // environment
10.0f, // authorizationThreshold
contracts, // contracts
true, // debug
10, // healthCheckFrequency
healthCheckCallback, // healthCheckCallback
"123456", // deviceSerialNumber
this
);

// THEN USE THIS CONFIGURATION TO SEND PAYMENT REQUESTS
} catch (InvalidHostException e) {
// Handle invalidIpAddressException
} catch (InvalidPortException e) {
// Handle InvalidPortException
} catch (InvalidUsernamePasswordAPIException e) {
// Handle InvalidUsernamePasswordAPIException
} catch (InvalidContractsException e) {
// Handle InvalidContractsException
}
}

public void onClick(View view) {
try {
/***********************************************************************/
/* Prepare the cart object with two items: 2 tables and 4 chairs */
/***********************************************************************/
Item table = new Item(
"A2343SSS",
ItemType.GOOD,
"Table",
2,
30.50f,
0.0f,
58.00f
);
table.setDiscount(-3.00f);
table.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
table.setEuropeanArticleNumbering("4711892728946");
table.setImageUrl("https://wwww.hipay.com");

Item chair = new Item(
"B7762NN",
ItemType.GOOD,
"Chair",
4,
10.20f,
0.0f,
40.80f
);
chair.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
chair.setProductDescription("A wooden chair");
chair.setEuropeanArticleNumbering("4713716322385");
chair.setImageUrl("https://wwww.hipay.com");

ArrayList itemArrayList = new ArrayList();
itemArrayList.add(table);
itemArrayList.add(chair);
Cart cart = new Cart(itemArrayList);

/************************************/
/* Prepare the customer object */
/************************************/
Customer customer = new Customer(
"1234",
"John",
Doe",
[email protected]",
"0602020202",
"1",
"1 rue John Doe",
"Appt 202",
"75000",
"Paris",
null,
"FR"
);

/***************************************************/
/* Prepare the custom additional information */
/***************************************************/
HashMap customData = new HashMap();
customData.put("foo1", "foo2");
customData.put("price", 12.30);
customData.put("event", 34);
customData.put("newCustomer", true);

/***********************************/
/* Create the payment request */
/***********************************/
RequestPayment requestPayment = new RequestPayment(
98.80f, // amount
TransactionType.TRANSACTION_TYPE_DEBIT, // transactionType
false, // forceAuthorization
Currency.EUR, // currency
"order_12345", // orderId
cart, //cart
customer, // customer
customData // customData
);

/*******************************************************************/
/* Send the payment request to the POS payment terminal */
/*******************************************************************/
requestPayment.execute(this);
} catch (InvalidAmountException e) {
// Handle InvalidAmountException
}
}

@Override
public void onFinish(ResponsePayment responsePayment) {
if (responsePayment.getPaymentStatus() == PaymentStatus.SUCCESS) {
// Handle success response
} else {
// Handle failed response
}
}
}
```

## Error codes

CODE
DESCRIPTION

1000
An unknown error occurred

1001
Timeout expired
This error pops up when the whole payment process takes longer than 180 seconds.

1002
Authentication failed with HiPay

1003
The network is unavailable

1004
POS terminal Not Connected

1005
Parsing transaction status failed

1006
Canceled transaction (REASON)
There are more than 15 reasons why the transaction can be canceled. The most common ones are canceling the transaction on the terminal and the customer taking too long to pay.

1007
Parsing received frame failed

1008
Parsing created frame from POS terminal failed

1009
Unknown MID
