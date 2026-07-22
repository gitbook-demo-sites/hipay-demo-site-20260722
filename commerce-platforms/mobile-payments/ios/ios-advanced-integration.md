---
description: "Accept payments in your own iOS (iPhone/iPad) application thanks to the HiPay iOS SDK. This integration allows you to build your own payment workflow "
icon: file-lines
---

# iOS - Advanced Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/ios/ios-advanced-integration](https://developer.hipay.com/mobile-payments/ios/ios-advanced-integration)
{% endhint %}

Accept payments in your own iOS (iPhone/iPad) application thanks to the HiPay iOS SDK.

This integration allows you to build your own payment workflow and your own form, using the core wrapper. You can thus fully customize the payment experience to fit your needs. On the downside, you have to take care of building the whole user interface of the page and creating and sending the orders to HiPay so the payment can be made.

Advantages of this integration : Checkout page customization.

Before going through this part, make sure you have followed the SDK configuration .

The HiPay Enterprise SDK for iOS contains a layer referred to as the core wrapper , which is basically a helpful wrapper of the HiPay Enterprise platform's REST API. By using it, you won't have to send HTTP requests or deal with XML or JSON deserialization. The core wrapper will take care of this for you.

It exposes models and methods that allow you to easily send payment requests. In fact, the built-in payment screen itself relies on the core wrapper for performing order requests, retrieving transaction details, etc.

The sections below describe the main interfaces you can rely on to perform order requests, tokenize credit cards, retrieve transaction details, etc. The payment workflow implementation details and the user interface are up to you.

## Tokenizing a card

To tokenize a credit card, you need to leverage the Secure Vault client, as below.

This step is mandatory in order to make payments with credit or debit cards, either for one-shot or recurring payments.

Objective-C
Swift

Objective-C

```
[[HPFSecureVaultClient sharedClient]
generateTokenWithCardNumber:@"4111111111111111"
cardExpiryMonth:@"12"
cardExpiryYear:@"2020"
cardHolder:@"John Doe"
securityCode:@"496"
multiUse:YES
andCompletionHandler:^(HPFPaymentCardToken * _Nullable cardToken,
NSError * _Nullable error) {

/* The cardToken object should be defined with your token
* if the tokenization was completed successfully.
* Otherwise, the error object will be defined */

}];
```

Swift

```
HPFSecureVaultClient.shared()
.generateToken(withCardNumber: "4111111111111111",
cardExpiryMonth: "12",
cardExpiryYear: "2020",
cardHolder: "John Doe",
securityCode: "496",
multiUse: true,
andCompletionHandler: { (cardToken, error) in

/* The cardToken object should be defined with your token
* if the tokenization was completed successfully.
* Otherwise, the error object will be defined */
})
```

You can also update a token by using the Secure Vault method named updatePaymentCardWithToken:requestID:setCardExpiryMonth:cardExpiryYear:cardHolder:completionHandler: .

To get information about a token previously generated, use the Secure Vault method named lookupPaymentCardWithToken:requestID:completionHandler: .

## Payment

You can make payments using the Gateway Client and its requestNewOrder method. This request will both create a new order based on the information you provided and process the payment simultaneously.

Therefore, you need to provide your order ID, the amount of the transaction, the payment product (Visa, MasterCard, PayPal, etc.) and the related payment method information (i.e., the token if it's a credit or debit card). You can also provide a lot of other optional information.

Objective-C
Swift

Objective-C

```
/* Create an order request which
* contains information about your order */
HPFOrderRequest *request = [[HPFOrderRequest alloc] init];
request.amount = @(155.50);
request.currency = @"EUR";
request.orderId = @"TEST_9641952";
request.shortDescription = @"Outstanding shirt";
request.operation = HPFOrderRequestOperationSale;

/* Below, optional properties are defined as well.
* Check the HPFPaymentPageRequest documentation
* for the full list of parameters */
request.customer.country = @"FR";
request.customer.firstname = @"John";
request.customer.lastname = @"Doe";
request.customer.email = @"[email protected]";

/* Payment method info, in this case,
* we re-use the token which has been
* generated in the previous section */
request.paymentProductCode = HPFPaymentProductCodeVisa;
request.paymentMethod = [HPFCardTokenPaymentMethodRequest
cardTokenPaymentMethodRequestWithToken:@"f39bfab2b6c96fa30dcc0e55aa3da4125a49ab03"
eci:HPFECISecureECommerce
authenticationIndicator:HPFAuthenticationIndicatorBypass];

[[HPFGatewayClient sharedClient] requestNewOrder:request signature:signature
withCompletionHandler:^(HPFTransaction * _Nullable transaction,
NSError * _Nullable error) {
/* Check the transaction object, particularly transaction.state.
* Or check the error object if the request failed. */
}];
```

Swift

```
/* Create an order request which
* contains information about your order */
let request = HPFOrderRequest()
request.amount = 155.50;
request.currency = "EUR"
request.orderId = "TEST_859674"
request.shortDescription = "Outstanding shirt"
request.operation = HPFOrderRequestOperation.sale

/* Below, optional properties are defined as well.
* Check the HPFPaymentPageRequest documentation
* for the full list of parameters */
request.customer.country = "FR"
request.customer.firstname = "John"
request.customer.lastname = "Doe"
request.customer.email = "[email protected]"

/* Payment method info, in this case,
* we re-use the token which has been
* generated in the previous section */
request.paymentProductCode = HPFPaymentProductCodeVisa
request.paymentMethod = HPFCardTokenPaymentMethodRequest(
token: "f39bfab2b6c96fa30dcc0e55aa3da4125a49ab03",
eci: HPFECI.HPFECISecureECommerce,
authenticationIndicator: HPFAuthenticationIndicator.bypass)

HPFGatewayClient.shared().requestNewOrder(request,
signature: signature,
withCompletionHandler: { (transaction, error) in
/* Check the transaction object, particularly transaction.state.
* Or check the error object if the request failed. */
})
```

Implementation note

The signature parameter is required for security purposes. Please refer to the Signature section for details.

When requesting a new order, do not forget to check the state of the newly created transaction. Moreover, you may need to redirect your users to a web page if the forwardUrl property is defined. In this case, you need to define the redirect URL properties on your order request object: acceptURL , declineURL , etc. In order for the HiPay platform to properly redirect users to your app, we advise you to use redirect URLs based on iOS app URL schemes (e.g.: myapp://order-result ).

## Payment Products

In order to get the exact list of payment methods enabled on your account, you can leverage the getPaymentProductsForRequest:withCompletionHandler : method of the Gateway Client . You need to provide this endpoint with information about your order (by using HPFPaymentPageRequest because the list of payment products may change depending on order-related information (i.e. the currency)).

Objective-C
Swift

Objective-C

```
HPFPaymentPageRequest *request = [[HPFPaymentPageRequest alloc] init];
request.amount = @(155.50);
request.currency = @"EUR";

// We just want the payment card products
request.paymentProductCategoryList = @[HPFPaymentProductCategoryCodeCreditCard,
HPFPaymentProductCategoryCodeDebitCard];

[[HPFGatewayClient sharedClient] getPaymentProductsForRequest:request
withCompletionHandler:^(NSArray * _Nonnull paymentProducts,
NSError * _Nullable error) {
// Check the paymentProducts array
}];
```

Swift

```
let request = HPFPaymentPageRequest();
request.amount = 155.50;
request.currency = "EUR";

// We just want the payment card products
request.paymentProductCategoryList = [
HPFPaymentProductCategoryCodeCreditCard,
HPFPaymentProductCategoryCodeDebitCard
]

HPFGatewayClient.shared().getPaymentProducts(for: request,
withCompletionHandler: { (paymentProducts, error) in
// Check the paymentProducts array
})
```

## Transaction Details

You can get the transactions related to an order or get information about a specific transaction by using the following methods:

* getTransactionWithReference:withCompletionHandler:
* getTransactionsWithOrderId:withCompletionHandler: Please find below an example with the transactions linked to the merchant order ID TEST_89897:

Objective-C
Swift

Objective-C

```
[[HPFGatewayClient sharedClient] getTransactionsWithOrderId:@"TEST_89897" signature:signature
withCompletionHandler:^(NSArray * _Nullable transactions,
NSError * _Nullable error) {
// Check the transactions array
}];
```

Swift

```
HPFGatewayClient.shared().getTransactionsWithOrderId("TEST_89897",
signature: signature,
withCompletionHandler: { (transactions, error) in
// Check the transactions array
})
```

Implementation note

The signature parameter is required for security purposes. Please refer to the Signature section for details.

## Card Storage

The card storage feature allows to register a HPFPaymentCardToken object in the iOS device Keychain , necessary to use the 1-click payment for your customers.

Since the card storage option is turned ON, you have access to these three HPFPaymentCardTokenDatabase class methods:

* paymentCardTokensForCurrency : To get every tokens associated to a currency
* delete:forCurrency To remove a specific token associated to a currency
* clearPaymentCardTokens To remove every tokens located in the iOS device keychain Our SDK allows to present/push the HPFStoreCardViewController to make the payment card storage easier.

In the example above, we push a HPFStoreCardViewController to our navigation controller and handle the navigation stack with the implemented methods of the HPFStoreCardDelegate protocol.

The storeCardViewController:shouldValidateCardToken:withCompletionHandler : is an optional delegate method. Its purpose is to let the merchant check the payment card validity asynchronously.

The completionBlock takes a boolean as parameter.
NO causes a call to the storeCardViewController:didFailWithError : method, while
YES causes a call to the storeCardViewController:didEndWithCardToken : delegate method.

Objective-C
Swift

Objective-C

```
#import "HPFStoreCardViewController.h"

/* First we add our view
* controller as a delegate */
@interface HPFDemoTableViewController : UIViewController

[...]

/* We assume your paymentPageRequest
* is not empty at this moment */
HPFPaymentPageRequest *paymentPageRequest = [self paymentPageRequest];

// we assume your paymentPageRequest is not empty
HPFStoreCardViewController *storevc = [HPFStoreCardViewController storeCardViewControllerWithRequest:paymentPageRequest];
storevc.storeCardDelegate = self;

[self.navigationController pushViewController:storevc animated:YES];

[...]

/* Then we implement the
* delegate methods */

- (void)storeCardViewController:(HPFStoreCardViewController *)viewController didEndWithCardToken:(HPFPaymentCardToken *)theToken
{
// inspect the HPFPaymentCardToken object
[viewController.navigationController popViewControllerAnimated:YES];
}

- (void)storeCardViewController:(HPFStoreCardViewController *)viewController didFailWithError:(NSError *)theError
{
// inspect the NSError object
}

- (void)storeCardViewControllerDidCancel:(HPFStoreCardViewController *)viewController
{
[viewController.navigationController popViewControllerAnimated:YES];
}

// optional delegate method
- (void) storeCardViewController:(HPFStoreCardViewController *)viewController shouldValidateCardToken:(HPFPaymentCardToken *)theCardToken withCompletionHandler:(HPFStoreCardViewControllerValidateCompletionHandler)completionBlock {

// typically an async call to check the payment card validity before calling the completionBlock.
completionBlock(YES);
}
```

Swift

```
class HPFDemoTableViewController : UIViewController, HPFStoreCardDelegate {

//[...]

func foo() {

//[...]

/* We assume your paymentPageRequest
* is not empty at this moment */

let paymentPageRequest = self.paymentPageRequest()

let storeVC = HPFStoreCardViewController.init(request: paymentPageRequest)
storeVC.delegate = self

self.navigationController?.pushViewController(storeVC, animated: true)

//[...]
}

/* Then we implement the
* delegate methods */

func storeCardViewController(_ viewController: HPFStoreCardViewController, didEndWith theToken: HPFPaymentCardToken) {
// inspect the HPFPaymentCardToken object
viewController.navigationController?.popViewController(animated: true)
}

func storeCardViewController(_ viewController: HPFStoreCardViewController, didFailWithError theError: Error?) {
// inspect the NSError object
}

func storeCardViewControllerDidCancel(_ viewController: HPFStoreCardViewController) {
viewController.navigationController?.popViewController(animated: true)
}

// optional delegate method
func storeCardViewController(_ viewController: HPFStoreCardViewController, shouldValidate theCardToken: HPFPaymentCardToken, withCompletionHandler completionBlock: @escaping HPFStoreCardViewControllerValidateCompletionHandler) {
// typically an async call to check the payment card validity before calling the completionBlock.
completionBlock(true);
}
```
