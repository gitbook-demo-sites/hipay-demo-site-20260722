---
description: "Apple Pay gives a secure and easy way to pay within apps and websites. Thanks to this documentation you will be able to start accepting Apple Pay paym"
icon: file-lines
---

# Apple Pay - Mobile APP

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/apple-pay-app](https://developer.hipay.com/online-payments/payment-means/apple-pay-app)
{% endhint %}

Apple Pay gives a secure and easy way to pay within apps and websites. Thanks to this documentation you will be able to start accepting Apple Pay payments on your mobile app.

## Integration Process

The integration process has 3 steps:

HIPAY ENABLEMENT

Apple Pay is on a supervised rollout phase, and you will need to request your Account Manager to enable it.

APPLE PAY CERTIFICATE

To accept Apple Pay on your website you need to have a payment processing certificate.

TECHNICAL INTEGRATION

The last phase is the technical integration. To test your integration please follow these steps.

## Configuration

MERCHANT ID CREATION

To use Apple Pay, you have to create an unique identifier, named Merchant ID.

* Log in to your Apple developer account

* Go to Register a Merchant ID page

* Choose an identifier and a description

The Identifier field has to be unique, we recommend you to use the reverse domain name like the following example : merchant.com.hipay.{yourcompany}.

We recommend you to use two merchant IDs, one for the production environment and one for the staging environment.

PAYMENT PROCESSING CERTIFICATE

This certificate is associated with the merchant ID and used to encrypt payment information between Apple Pay servers and HiPay. Every 25 months, this certificate expires. So you should revoke it before it expires and recreate it.

* Log in to your Apple developer account

* Go to the Certificate creation section .

* Choose Apple Pay Payment Processing Certificate

* Select the right Merchant ID

* Read the following instructions to create a CSR file

* Save the CSR on your disk and continue

* Click on the Choose File button

* Select the certificate file with the .certSigningRequest extension

* Click on the Continue button

* Click on the Download button and add the certificate (.cer) to your keychain by clicking on it

* Click Done

Your new Apple Pay Payment Processing certificate can be found in the certificate list .

EXPORT THE CERTIFICATE

HiPay will decrypt the token sent by Apple Pay thanks to your Apple Pay Payment Processing certificate. In order, to do that, you have to send your private and public key to HiPay.

* Launch Keychain on your Mac.

* Search your Apple Pay Payment Processing certificate with the private key associated, generated when you created the CSR file.

* Right click on the private key and the certificate to select the items and export them.

* Name the created file and export it in a .p12 extension.

* Protect the file with a strong password.

* Send an email to [email protected] including the file and the password.

EDIT APP ID

After creating the Merchant ID and the Apple Pay Processing certificate, you must add the Apple Pay Payment Processing capability to your iOS application.

* Log in to your Apple developer account

* Go to the Identifiers section

* Click on your App ID

* Enable the Apple Pay Payment Processing capability

* Click the Edit button next to the Apple Pay Payment Processing capability

* Assign your Merchant ID/s to it

* Save the configuration

REGENERATE PROVISIONING PROFILES

After adding the Apple Pay Payment Processing capability, Provisioning Profiles must be regenerated as they are invalided.

* Log in to your Apple developer account

* Go to the Profiles page

* Select the Profile

* Click on Edit

* Click on Generate

* Click on it to add to XCode

## SDK Setup

ADD CAPABILITY

In your XCode project settings, on the capabilities tab, enable Apple Pay.

Then add the same Merchant ID that you created before by clicking on the plus button.

#### AppDelegate

In your AppDelegate file, add this following method to enable Apple Pay with the HiPay SDK :

Swift
Objective-C

Swift

```
HPFClientConfig
.shared()
.setApplePayEnabled(true,
usernameApplePay: "UsernameApplePay",
privateKeyPassword: "YOUR P12 CERTIFICATE PASSWORD",
merchantIdentifier: "merchant.com.your.company.app")
```

Objective-C

```
[[HPFClientConfig sharedClientConfig] setApplePayEnabled:YES
usernameApplePay:@"UsernameApplePay"
privateKeyPassword:@"YOUR P12 CERTIFICATE PASSWORD"
merchantIdentifier:@"merchant.com.your.company.app"];
```

usernameApplePay : The public credentials username of the HiPay account used for Apple Pay.

privateKeyPassword : Password used in Certificate export section.

merchantIdentifier : Your Apple Pay Merchant ID (stage/production).

APPLE PAY BUTTON

You should read these Apple Pay's guidelines provided by Apple before continuing.

We use the PKPaymentButton class to show the official Apple Pay button. You can customize it with its type PKPaymentButtonType and its style PKPaymentButtonStyle parameters.

In this example below, we use the canMakePayments method of the PKPaymentAuthorizationViewController class to determine the button's style in accordance with the capacity of the device to make payments with particular networks.

Swift
Objective-C

Swift

```
import PassKit

class MyApplePayViewController: UIViewController, PKPaymentAuthorizationViewControllerDelegate {
override func viewDidLoad() {
super.viewDidLoad()

var type : PKPaymentButtonType
if PKPaymentAuthorizationViewController.canMakePayments(usingNetworks: [PKPaymentNetwork.visa, PKPaymentNetwork.masterCard]) {
type = PKPaymentButtonType.buy;
}
else {
type = PKPaymentButtonType.setUp
}
let button = PKPaymentButton(paymentButtonType: type, paymentButtonStyle: PKPaymentButtonStyle.whiteOutline)
// TODO: Add button to view and set its constraints
}
}
```

Objective-C

```
#import
#import

@interface MyApplePayViewController

@end

@implementation MyApplePayViewController

- (void)viewDidLoad {
[super viewDidLoad];
PKPaymentButtonType type;
if ([PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:@[PKPaymentNetworkVisa, PKPaymentNetworkMasterCard]]) {
type = PKPaymentButtonTypeBuy;
}
else {
type = PKPaymentButtonTypeSetUp;
}
PKPaymentButton *button = [[PKPaymentButton alloc] initWithPaymentButtonType:type paymentButtonStyle:PKPaymentButtonStyleWhiteOutline];
// TODO: Add button to view and set its constraints
}
```

PAYMENT SCREEN

Then, we create an object of type PKPaymentSummaryItem which contains a description of the purchased item with its price.

To initialize the payment controller, you must create a request of the PKPaymentRequest class first. You can configure its attributes : merchantIdentifier , countryCode , supportedNetworks , paymentSummaryItems and many more.

After the request creation, we present the PKPaymentAuthorizationViewController Apple Pay controller to the user with this request. More information about the request here .

Swift
Objective-C

Swift

```
let item = PKPaymentSummaryItem.init(label: "Item description", amount: )

let paymentRequest = PKPaymentRequest.init()
paymentRequest.paymentSummaryItems = [item]
paymentRequest.merchantIdentifier = HPFClientConfig.sharedClientConfig.merchantIdentifier
paymentRequest.countryCode = "FR"
paymentRequest.currencyCode = "EUR"
paymentRequest.supportedNetworks = [ .masterCard, .visa]

if let paymentAuthorizationVC = PKPaymentAuthorizationViewController(paymentRequest: paymentRequest) {
paymentAuthorizationVC.delegate = self
present(paymentAuthorizationVC, animated: true, completion: nil)
} else {
print("Error : init PKPaymentAuthorizationViewController")
}
```

Objective-C

```
PKPaymentSummaryItem *item = [PKPaymentSummaryItem summaryItemWithLabel:@"Item description" amount: ];

PKPaymentRequest *paymentRequest = [[PKPaymentRequest alloc] init];
paymentRequest.paymentSummaryItems = @[item];
paymentRequest.merchantIdentifier = [[HPFClientConfig sharedClientConfig] merchantIdentifier];
paymentRequest.merchantCapabilities = PKMerchantCapability3DS;
paymentRequest.countryCode = @"FR";
paymentRequest.currencyCode = @"EUR";
paymentRequest.supportedNetworks = @[PKPaymentNetworkMasterCard, PKPaymentNetworkVisa];

PKPaymentAuthorizationViewController *paymentAuthorizationVC = [[PKPaymentAuthorizationViewController alloc] initWithPaymentRequest:paymentRequest];
paymentAuthorizationVC.delegate = self;
[self presentViewController:paymentAuthorizationVC animated:YES completion:nil];
```

APPLE PAY TOKEN

When the user authorizes a payment request, the PassKit framework creates a payment token by coordinating with Apple's server and the Secure Element. This token has to be sent to our HiPay's servers.

To obtain Apple Pay's token, your Apple Pay controller should conform to the PKPaymentAuthorizationViewControllerDelegate protocol. You should use the paymentAuthorizationViewController:didAuthorizePayment:completion delegate's method to retrieve this token. More precisely, this method returns an object of type PKPayment when the user validates his payment by Touch ID or Face ID.

This object of type PKPayment contains an attribute of PKPaymentToken class named token, which contains paymentData attribute.

This response can be serialized in a JSON file and sent to the apple-pay/token endpoint with the generateTokenWithApplePayToken: privateKeyPassword:andCompletionHandler SecureVaultClient method. The return object of the method is a HPFPaymentCardToken token type.

Then, you will be able to create an Order and complete the payment. To decrypt the Apple Pay token and retrieve payment information, HiPay uses the private key of the certificate Apple Pay Payment Processing.

Swift
Objective-C

Swift

```
func paymentAuthorizationViewController(controller: PKPaymentAuthorizationViewController,
didAuthorizePayment payment: PKPayment, completion: @escaping (PKPaymentAuthorizationStatus) -> Void) {

let decodedToken = String(data: payment.token.paymentData, encoding: .utf8)

HPFSecureVaultClient.shared().generateToken(withApplePayToken: decodedString,
privateKeyPassword: "YOUR P12 CERTIFICATE PASSWORD") { (hipayToken, error) in

/* Create HPFOrderRequest if tokenization was completed successfully.
* Otherwise, handle the error object */
}

}
```

Objective-C

```
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller
didAuthorizePayment:(PKPayment *)payment
completion:(void (^)(PKPaymentAuthorizationStatus))completion
{
NSString *decodedString = [[NSString alloc] initWithData:payment.token.paymentData
encoding:NSUTF8StringEncoding];

[[HPFSecureVaultClient sharedClient] generateTokenWithApplePayToken:decodedString
privateKeyPassword:@"YOUR P12 CERTIFICATE PASSWORD"
andCompletionHandler:^(HPFPaymentCardToken * _Nullable cardToken, NSError * _Nullable error) {

/* Create HPFOrderRequest if tokenization was completed successfully.
* Otherwise, handle the error object */
}];
}
```

CREATE AN ORDER

Once you have tokenized, you can create a new order. To do this you must follow the following payment instructions adding the isApplePay: true condition to your request, as follows:

Swift
Objective-C

Swift

```
HPFGatewayClient.shared().requestNewOrder(request,
signature: signature,
isApplePay: true,
withCompletionHandler: { (transaction, error) in

/* Check the transaction object, particularly transaction.state.
* Or check the error object if the request failed. */

})
```

Objective-C

```
[[HPFGatewayClient sharedClient] requestNewOrder:request
signature:signature
isApplePay:YES
withCompletionHandler:^(HPFTransaction *theTransaction, NSError *error) {
// Check payment result
}];
```

SIGNATURE WARNING

When you use Apple Pay with HiPay, we need to create an extra HiPay account. This implies that you will have one account for classic payments and another one exclusively for Apple Pay.

To process an order, you need a unique signature, calculated on your server using these 4 parameters (OrderId, amount, currency, passphrase). As you will have a new HiPay account, you will need to make sure you correctly handle the passphrase of each account. To do so, you can use one of these solutions:

* Using the same passphrase in both HiPay accounts with only one endpoint.
* Using a different passphrase for each HiPay account
* Creating two endpoints with a different passphrase for each endpoint
* Using one endpoint with a boolean parameter to determine if the payment is using an Apple Pay authentication to choose the correct passphrase.
