---
description: "The HiPay Omnichannel SDK allows you to process in store payments and create a transaction on HiPay Console. The payment workflow is the following one"
icon: file-lines
---

# Tablet - Omnichannel SDK

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/point-of-sale/smart-terminal/omnichannel-sdk](https://developer.hipay.com/point-of-sale/smart-terminal/omnichannel-sdk)
{% endhint %}

The HiPay Omnichannel SDK allows you to process in store payments and create a transaction on HiPay Console.

The payment workflow is the following one:

* The point-of-sale software sends a request payment to the Omnichannel SDK.

* SDK initialize the payment on the POS Terminal e.g the amount is displayed on the screen and the customer should process the payment.

* POS Terminal sends the result payment to the Omnichannel SDK in its format.

* Omnichannel SDK sends the result to the point-of-sale software with a custom object.

* Transaction request is sent to HiPay's server

## Requirements

Android
iOS

Android

* Android 5.0 Lollipop (API 21) or later

* Android Studio 4.1 or later

* POS terminal with Concert protocol version 3.1 or 3.2

iOS

* iOS 11 or later
* XCode 12 or later
* Cocoapods 1.10 or later
* POS terminal with Concert protocol version 3.1 or 3.2

## Installation

Android
iOS

Android
HiPay's Android Omnichannel SDK is hosted on hipay.com. In order to install it, you have to add these lines to your Build.gradle Projet file :

```
allprojects {
repositories {
maven {
url "https://artifactory.hipay.com/repository/maven-public/"
}
}
}
```

Then, add this line in your build.gradle file of the module app :

```
dependencies {
implementation 'com.hipay:hipay-omnichannel-concertv3:2.0.0'
}
```

iOS
You have to use CocoaPods to install the HiPay Omnichannel SDK for iOS. CocoaPods is a dependency manager for Swift and Objective-C Cocoa projects.

CocoaPods is built with Ruby and it will be installable with the default Ruby available on macOS. Install it with this command if you haven't done before :

```
sudo gem install cocoapods
```

Then, execute this command at the root of your project to initialize the required files :

```
pod init
```

Add this line to your project's Podfile :

```
pod 'HiPayOmnichannelConcertV3'
```

Then, run the following command in the same directory as your Podfile .

```
pod install
```

Open the Xcode workspace ( *.xcworkspace ) instead of the project file.

## Initialization

First of all, to use the SDK, you have to set the Configuration object. An exception is thrown if your configuration is not set correctly.

authorizationThreshold When the amount is above this threshold, the authorization is set to true value Float e.g. 100.00

Variable name Description Type Values Default value protocol Protocol version (V3.1, V3.2) Enum ConcertV31

ConcertV32

ConcertV31 host* Terminal IPv4 address or domain name String e.g. 192.168.1.10
e.g. your.domain.com port Terminal port (1-65535) Integer 8888 contracts* List of contracts Contract array See Contract section apiUsername* Public HiPay API username used by authentication String e.g. 123456789.stage-secure-gateway.hipay-tpp[.]com apiPassword* Public HiPay API password used by authentication String e.g. Test_AB1234578903bd5eg environment Environment in which the transaction is going to be created Enum production

stage

production authorizationThreshold When the amount is above this threshold, the authorization is set to true value Float e.g. 100.00 debug Enable debug mode (display all prints) Boolean False healthCheckFrequency Delay between health check in seconds (To disable this feature, set 0)

Only on Android

Integer healthCheckCallback if healthCheckFrequency is set, you will receive a response every x seconds to get a boolean regarding the POS status.

Only on Android

Callback deviceSerialNumber Serial number of the terminal (Required for health check feature)

Only on Android

String * Mandatory parameters

Java
Swift

Java

```
public class MainActivity extends AppCompatActivity {

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

ArrayList contracts = new ArrayList();
contracts.add(new Contract("1234567",
"001",
"005"));

contracts.add(new Contract("1234568",
"001",
"005"));

HealthCheckCallback healthCheckCallback = new HealthCheckCallback() {
@Override
public void getTerminalStatus(boolean isUp) {
// Check the status
}
};

try {
Configuration.getInstance().setConfiguration(
Protocol.CONCERTV32,
"192.168.1.1",
8888,
"username",
"password",
Environment.STAGE,
10.0f,
contracts,
true,
10,
healthCheckCallback,
"123456",
this
);

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

Swift

```
import HiPayOmnichannelConcertV3

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
// Override point for customization after application launch.

var contracts = [Contract]()
contracts.append(Contract(merchantContract: "1234567",
rank: "005",
acquirerCode: "222",
paymentApplication: "001"))
contracts.append(Contract(merchantContract: "1234568",
rank: "005",
acquirerCode: "222",
paymentApplication: "001"))

do {
try Configuration.shared.setConfiguration(protocolVersion: .ConcertV32,
host: "192.168.1.1",
port: 8765,
apiUsername: "username",
apiPassword: "password",
contracts: contracts,
environment: .Stage,
authorizationThreshold: 10.0,
debug: true)

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

### Contract

To finalize the configuration, you have to create an array of your contracts (at least one contract). Each contract object contains a few information.

Variable name Description Type Values merchantContract * Merchant Identification Number String e.g. 123456 paymentApplication* Payment application identifier String e.g. 007 rank * Rank of your POS terminal String e.g. 001 * Mandatory parameters

Java
Swift

Java

```
Contract contract = new Contract("4988652",
"001",
"005");
```

Swift

```
let contract = Contract(merchantContract: "4988652",
rank: "005",
acquirerCode: "002",
paymentApplication: "001")
```

## Request Payment

For each payment, you have to create a RequestPayment object with theses variables below. When your RequestPayment is created, you execute it with the corresponding iOS method execute() or Android method execute(this) . Your class has to conform to the RequestPaymentDelegate delegate to receive a response.

Variable name Description Type Values Default amount * Total order amount, calculated as the sum of purchased items, plus shipping fees (if present), plus tax fees (if present). Float e.g. 9.99 transactionType Type of transaction to be processed Enum
Debit

Credit

Cancellation

Debit forceAuthorization Whether the authorization should be forced or not. Overwrites the authorizationThreshold parameter to enable authorization Boolean False currency ISO 4217 alpha currency code ( More information ) Enum EUR

USD

EUR orderId Order number of your request payment. If you don't send an identifier, we will generated it for you String e.g. Order_12345 cart** Cart object ( More information ) Cart - customer Customer's information object (id, firstName, lastName, email) Customer - customData Custom data (only value type Bool / Int / Float / String are accepted ) Dictionary - receiptSendingOption Which channel for sending receipt (only with Concert 3.2) Enum All

SMS

Email

All * Mandatory parameters

** If the cart content is not correctly fulfilled or doesn't match the total amount of the order, the order will be created with an empty cart.

Java
Swift

Java

```
@Override
public void onClick(View view) {
try {
RequestPayment requestPayment = new RequestPayment(
98.80f,
TransactionType.TRANSACTION_TYPE_DEBIT,
false,
Currency.EUR,
"order_12345",
null,
null,
null);

requestPayment.execute(this);
} catch (InvalidAmountException e) {
// Handle InvalidAmountException
}
}
```

Swift

```
@IBAction func payTapped(_ sender: Any) {
do {
let requestPayment = try RequestPayment(amount: 98.80,
transactionType: .Debit,
forceAuthorization: false,
currency: .EUR,
orderId: "order_12345",
cart: nil,
customer: nil,
customData: nil)

requestPayment.delegate = self
requestPayment.execute() // Request execution
} catch RequestPaymentError.invalidAmount {
// handle invalid amount
} catch {
// Others
}
}
```

### Cart

You can add the cart of the transaction, creating an Item for each article ( More informations about cart ).

Java
Swift

Java

```
Item table = new Item("A2343SSS",
ItemType.GOOD,
"Table",
2,
30.50f,
0.0f,
58.00f);
table.setDiscount(-3.00f);
table.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
table.setEuropeanArticleNumbering("4711892728946");
table.setImageUrl("https://wwww.hipay.com");

Item chair = new Item("B7762NN",
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
```

Swift

```
/// Cart
var cart = Cart()
var table = Item(productReference: "A2343SSS",
type: .Good,
name: "Table",
quantity: 2,
unitPrice: 30.50,
taxRate: 0.0,
totalAmount: 58.00)
table.discount = 3.00
table.productCategory = .HomeAppliances
table.europeanArticleNumbering = "4711892728946"
table.imageUrl = "https://www.hipay.com/yourImage"

var chair = Item(productReference: "B7762NN",
type: .Good,
name: "Chair",
quantity: 4,
unitPrice: 10.20,
taxRate: 0.0,
totalAmount: 40.80)
chair.productCategory = .HomeAppliances
chair.productDescription = "A wooden chair"
chair.europeanArticleNumbering = "4713716322385"
chair.imageUrl = "https://www.hipay.com/yourImage"

cart.items.append(table)
cart.items.append(chair)
```

### Customer

You can set all personal information such as his email, first name, last name, a unique identifier, address, city, country...

The country field should contain the country code of the customer. This two-letter country code complies with ISO 3166-1 (alpha 2).

Java
Swift

Java

```
// Customer
Customer customer = new Customer("1234",
"John",
"Doe",
"[email protected]",
"0602020202",
"1",
"1 rue John Doe",
"Appt 202",
"75000",
"Paris",
null,
"FR");
```

Swift

```
/// Customer
let customer = Customer(id: "1234",
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
country: "FR")
```

### Custom data

In the custom data parameter, you can set all the values of you want to retrieve in HiPay's backoffice.

Java
Swift

Java

```
HashMap customData = new HashMap();
customData.put("foo1", "foo2");
customData.put("price", 12.30);
customData.put("event", 34);
customData.put("newCustomer", true);
```

Swift

```
/// Custom data
var customData = [String:Any]()
customData["foo1"] = "foo2"
customData["price"] = 12.30
customData["event"] = 34
customData["newCustomer"] = true
```

## Payment Response

After the transaction has been processed through the HiPay's servers, you will receive a response from the Omnichannel SDK.

Java
Swift

Java

```
@Override
public void onFinish(ResponsePayment responsePayment) {
if (responsePayment.getPaymentStatus() == PaymentStatus.SUCCESS) {
// Handle success response
}
else {
// Handle failed response
}
}
```

Swift

```
class ViewControlller: UIViewController, RequestPaymentDelegate {

// ... code example above

// Mandatory function from RequestPaymentDelegate delegate
func requestDidEnd(_ response: ResponsePayment) {
print(response)

if (response.paymentStatus == .Success) {
// Handle Success
}
else {
// Handle Failure
}
}
}
```

The below table describes the ResponsePayment object properties, notice that all these properties are in read-only :

Variable name Description Type Values paymentStatus Status received from the TPE regarding the payment. Enum Success

Failure errorDescription Error description String e.g. : The network is unavailable errorCode Error code String e.g. : 1003 amount Amount of the transaction Float e.g. : 98.80 currency ISO 4217 alpha currency code Enum e.g. : .EUR orderId Order number String e.g. : order_12345 notificationHipaySent Indicates whether Hipay has been notified of the transaction Boolean e.g. false customer Personal information of the customer Customer receipt Receipt encoded in Base64

String e.g. UkVDRUlQVCA5OSBFVVI==

## Payment Example

Here you have a complete example of the code needed to request a payment and handle its response.

Java
Swift

Java

```
// All your imports
public class MainActivity extends AppCompatActivity implements View.OnClickListener, RequestPaymentDelegate {

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

ArrayList contracts = new ArrayList();
contracts.add(new Contract("1234567",
"001",
"005"));

contracts.add(new Contract("1234568",
"001",
"005"));

HealthCheckCallback healthCheckCallback = new HealthCheckCallback() {
@Override
public void getTerminalStatus(boolean isUp) {
// Check the status
}
};

try {
Configuration.getInstance().setConfiguration(
Protocol.CONCERTV32,
"192.168.1.1",
8888,
"username",
"password",
Environment.STAGE,
10.0f,
contracts,
true,
10,
healthCheckCallback,
"123456",
this
);

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

@Override
public void onClick(View view) {

// Cart
Item table = new Item("A2343SSS",
ItemType.GOOD,
"Table",
2,
30.50f,
0.0f,
58.00f);
table.setDiscount(-3.00f);
table.setProductCategory(ItemProductCategory.HOME_APPLIANCES);
table.setEuropeanArticleNumbering("4711892728946");
table.setImageUrl("https://wwww.hipay.com");

Item chair = new Item("B7762NN",
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

ArrayList itemArrayList = new ArrayList();
itemArrayList.add(table);
itemArrayList.add(chair);

Cart cart = new Cart(itemArrayList);

// Customer
Customer customer = new Customer("1234",
"John",
"Doe",
"[email protected]",
"0602020202",
"1",
"1 rue John Doe",
"Appt 202",
"75000",
"Paris",
null,
"FR");
);

// CustomData
HashMap customData = new HashMap();
customData.put("foo1", "foo2");
customData.put("price", 12.30);
customData.put("event", 34);
customData.put("newCustomer", true);

try {
RequestPayment requestPayment = new RequestPayment(
98.80f,
TransactionType.TRANSACTION_TYPE_DEBIT,
false,
Currency.EUR,
"order_12345",
cart,
customer,
customData,
ReceiptSendingOption.EMAIL
);
requestPayment.execute(this);
} catch (InvalidAmountException e) {
// Handle InvalidAmountException
}
}

@Override
public void onFinish(ResponsePayment responsePayment) {
if (responsePayment.getPaymentStatus() == PaymentStatus.SUCCESS) {
// Handle success response
}
else {
// Handle failed response
}
}
}
```

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
var table = Item(productReference: "A2343SSS",
type: .Good,
name: "Table",
quantity: 2,
unitPrice: 30.50,
taxRate: 0.0,
totalAmount: 58.00)
table.discount = 3.00
table.productCategory = .HomeAppliances
table.europeanArticleNumbering = "4711892728946"
table.imageUrl = "https://www.hipay.com/yourImage"

var chair = Item(productReference: "B7762NN",
type: .Good,
name: "Chair",
quantity: 4,
unitPrice: 10.20,
taxRate: 0.0,
totalAmount: 40.80)
chair.productCategory = .HomeAppliances
chair.productDescription = "A wooden chair"
chair.europeanArticleNumbering = "4713716322385"

cart.items.append(table)
cart.items.append(chair)

/// Customer
let customer = Customer(id: "1234",
firstName: "John",
lastName: "Doe",
email: "[email protected]")

/// Custom data
var customData = [String:Any]()
customData["foo1"] = "foo2"
customData["price"] = 12.30
customData["event"] = 34
customData["newCustomer"] = true

do {
let requestPayment = try RequestPayment(amount: 98.80,
transactionType: .Debit,
forceAuthorization: true,
currency: .EUR,
orderId: "order_12345",
cart: cart,
customer: customer,
customData: customData,
receiptSendingOption: .Email)

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
}
else {
// Handle Failure
}
}
}
```

## Error Codes

Should an error occur, here is a list of all the possible related codes and descriptions.

Code Description 1000 An unknown error occurred 1001 Timeout expired

This error pops up when the whole payment process takes longer than 180 seconds.

1002 Authentication failed with HiPay 1003 The network is unavailable 1004 POS terminal Not Connected 1005 Parsing transaction status failed 1006 Cancelled transaction (REASON).

There are more than 15 reasons why the transaction can be cancelled. The most common ones are cancelling the transaction on the terminal and the customer taking too long to pay.

1007 Parsing received frame failed 1008 Parsing created frame from POS terminal failed 1009 Unknown MID
