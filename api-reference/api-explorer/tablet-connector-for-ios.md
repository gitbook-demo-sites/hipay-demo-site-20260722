---
description: "WARNING: this documentation is intended for the Smart Terminal offer (standalone payment terminals) and dedicated to the scenarios based on iOS device"
icon: file-lines
---

# Tablet Connector for iOS

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/api-explorer/tablet-connector-for-ios](https://developer.hipay.com/api-explorer/tablet-connector-for-ios)
{% endhint %}

WARNING: this documentation is intended for the Smart Terminal offer (standalone payment terminals) and dedicated to the scenarios based on iOS devices. If you are looking for the documentation related to Android devices, please consult the dedicated page .

## Description

The Tablet Connector for iOS allows you to trigger in-store payments from an iOS device (smartphone or tablet), by sending a payment request to a specific POS payment terminal through the Cloud API , thanks to a simple and dedicated Software Development Kit (SDK).

When a payment request is sent via the SDK, it then :
- sends a payment request to the Cloud API
- awakes the targeted payment terminal by forwarding the payment request to the provided IP address / port
- waits for the payment processing
- receives the payment response with the payment information

Please note this documentation introduces the Tablet Connector by presenting its requirements and how to implement it (endpoints, request parameters, response parameters, error codes, etc.).
If you are looking for a presentation overview, please check the dedicated page .

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Tablet Connector for iOS:

REQUIREMENT
DETAILS

POS payment terminal
A payment terminal supporting Concert protocol version 3.1 or 3.2 (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable Internet (Wi-Fi) connection
- A fixed public IP address for the network router is needed to join the payment terminal. In case your public IP address changes over time, it is usually possible to fix it by contacting your Internet access provider (please notice additional costs may be applied)

Android device
An iOS device (smartphone or tablet) with iOS 11 or later

IDE
XCode with version 12 or later

Dependency manager
CocoaPods with version 1.10 or later

Security
Public API credentials enabled (please consult this page to get details about HiPay credentials).

## installation

First of all, you need to install and configure CocoaPods.

CocoaPods is a dependency manager for Swift and Objective-C Cocoa projects.
CocoaPods is built with Ruby and it will be installable with the default Ruby available on macOS.

Please, execute the following commands to install and configure it:

Bash

Bash

```
# Install it with this command if you haven't done before :
sudo gem install cocoapods
# Then, execute this command at the root of your project to initialize the required files :
pod init
# Add this line to your project's Podfile:
pod 'HiPayOmnichannelConcertV3'
# Then, run the following command in the same directory as your Podfile.
pod install
```

Open the Xcode workspace (*.xcworkspace) instead of the project file.

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

Notes:
- M/O means Mandatory / Optional.

## Contract

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

Swift

Swift

```
import HiPayOmnichannelConcertV3

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
// Override point for customization after application launch.

var contracts = [Contract]()
let contactMid =Contract(
merchantContract: "1234567",
rank: "005",
acquirerCode: "222",
paymentApplication: "001")
);
let contactlessMid = Contract(
merchantContract: "1234568",
rank: "005",
acquirerCode: "222",
paymentApplication: "001"
)
contracts.append(contactMid)
contracts.append(contactlessMid)

do {
try Configuration.shared.setConfiguration(
protocolVersion: .ConcertV32,
host: "192.168.1.1",
port: 8765,
apiUsername: "username",
apiPassword: "password",
contracts: contracts,
environment: .Stage,
authorizationThreshold: 10.0,
debug: true
)

// THEN USE THIS CONFIGURATION TO SEND PAYMENT REQUESTS
} catch ConfigurationError.invalidHost {
// Invalid Host
} catch ConfigurationError.invalidPort {
// Invalid Port
} catch ConfigurationError.invalidUsernamePasswordAPI {
// Invalid API password or API Username
} catch ConfigurationError.invalidContract {
// Invalid Contract
} catch {

}

return true
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

O
Enum
Debit
- Debit
- Credit
- Cancellation

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

Swift

Swift

```
@IBAction func payTapped(_ sender: Any) {
do {
/***********************************************************************/
/* Prepare the cart object with two items: 2 tables and 4 chairs */
/***********************************************************************/
var cart = Cart()
var table = Item(
productReference: "A2343SSS",
type: .Good,
name: "Table",
quantity: 2,
unitPrice: 30.50,
taxRate: 0.0,
totalAmount: 58.00
)
table.discount = 3.00
table.productCategory = .HomeAppliances
table.europeanArticleNumbering = "4711892728946"
table.imageUrl = "https://www.hipay.com/yourImage"

var chair = Item(
productReference: "B7762NN",
type: .Good,
name: "Chair",
quantity: 4,
unitPrice: 10.20,
taxRate: 0.0,
totalAmount: 40.80
)
chair.productCategory = .HomeAppliances
chair.productDescription = "A wooden chair"
chair.europeanArticleNumbering = "4713716322385"
chair.imageUrl = "https://www.hipay.com/yourImage"

cart.items.append(table)
cart.items.append(chair)

/************************************/
/* Prepare the customer object */
/************************************/
let customer = Customer(
id: "1234",
firstName: "John",
lastName: "Doe",
email: "[email protected]",
mobilPhone: "0602020202",
houseNumber: "1",
streetAddress: "1 rue John Doe",
streetAddress2: "Flat 101",
zipCode: "75000",
city: "Paris",
state: nil,
country: "FR"
)

/***************************************************/
/* Prepare the custom additional information */
/***************************************************/
var customData = [String:Any]()
customData["foo1"] = "foo2"
customData["price"] = 12.30
customData["event"] = 34
customData["newCustomer"] = true

/***********************************/
/* Create the payment request */
/***********************************/
let requestPayment = try RequestPayment(
amount: 98.80,
transactionType: .Debit,
forceAuthorization: false,
currency: .EUR,
orderId: "order_12345",
cart: cart,
customer: customer,
customData: customData
)

/*******************************************************************/
/* Send the payment request to the POS payment terminal */
/*******************************************************************/
requestPayment.delegate = self
requestPayment.execute() // Request execution
} catch RequestPaymentError.invalidAmount {
// handle invalid amount
} catch {
// Others
}
}
```

## Payment response

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

Swift

Swift

```
class ViewControlller: UIViewController, RequestPaymentDelegate {
// ... code example above

// Mandatory function from RequestPaymentDelegate delegate
func requestDidEnd(_ response: ResponsePayment) {
print(response)

if (response.paymentStatus == .Success) {
// Handle Success
} else {
// Handle Failure
}
}
}
```

## Full code sample

Swift

Swift

```
import UIKit
import HiPayOmnichannelConcertV3

class ViewController: UIViewController, RequestPaymentDelegate {
override func viewDidLoad() {
super.viewDidLoad()
// Do any additional setup after loading the view.
}

@IBAction func payTapped(_ sender: Any) {
/// Cart
var cart = Cart()
var table = Item(
productReference: "A2343SSS",
type: .Good,
name: "Table",
quantity: 2,
unitPrice: 30.50,
taxRate: 0.0,
totalAmount: 58.00
)
table.discount = 3.00
table.productCategory = .HomeAppliances
table.europeanArticleNumbering = "4711892728946"
table.imageUrl = "https://www.hipay.com/yourImage"

var chair = Item(
productReference: "B7762NN",
type: .Good,
name: "Chair",
quantity: 4,
unitPrice: 10.20,
taxRate: 0.0,
totalAmount: 40.80
)
chair.productCategory = .HomeAppliances
chair.productDescription = "A wooden chair"
chair.europeanArticleNumbering = "4713716322385"

cart.items.append(table)
cart.items.append(chair)

/// Customer
let customer = Customer(
id: "1234",
firstName: "John",
lastName: "Doe",
email: "[email protected]"
)

/// Custom data
var customData = [String:Any]()
customData["foo1"] = "foo2"
customData["price"] = 12.30
customData["event"] = 34
customData["newCustomer"] = true

do {
let requestPayment = try RequestPayment(
amount: 98.80,
transactionType: .Debit,
forceAuthorization: true,
currency: .EUR,
orderId: "order_12345",
cart: cart,
customer: customer,
customData: customData,
receiptSendingOption: .Email
)

requestPayment.delegate = self
requestPayment.execute() // Request execution
} catch RequestPaymentError.invalidAmount {
// handle invalid amount
} catch {
// Others
}
}

func requestDidEnd(_ response: ResponsePayment) {
// Handle the reponsePayment object
print(response)

if (response.paymentStatus == .Success) {
// Handle Success
} else {
// Handle Failure
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
