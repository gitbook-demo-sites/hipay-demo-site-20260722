---
description: "Accept payments in your own Android application thanks to the HiPay Android SDK. This integration allows you to build your own payment workflow and yo"
icon: file-lines
---

# Android - Advanced Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/android/android-advanced-integration](https://developer.hipay.com/mobile-payments/android/android-advanced-integration)
{% endhint %}

Accept payments in your own Android application thanks to the HiPay Android SDK.

This integration allows you to build your own payment workflow and your own form, using the core wrapper. You can thus fully customize the payment experience to fit your needs. On the downside, you have to take care of building the whole user interface of the page and creating and sending the orders to HiPay so the payment can be made.

Advantages of this integration : Checkout page customization.

Before going through this part, make sure you have followed the SDK configuration .

The HiPay Enterprise SDK for Android contains a layer referred to as the core wrapper , which is basically a helpful wrapper of the HiPay Enterprise platform's REST API. By using it, you won't have to send HTTP requests or deal with XML or JSON deserialization. The core wrapper will take care of this for you.

It exposes models and methods that allow you to easily send payment requests. In fact, the built-in payment screen itself relies on the core wrapper for performing order requests, retrieving transaction details, etc.

The sections below describe the main interfaces you can rely on to perform order requests, tokenize credit cards, retrieve transaction details, etc. The payment workflow implementation details and the user interface are up to you.

## Tokenize a card

To tokenize a card, you need to leverage the Secure Vault client, as follows. This step is mandatory in order to make payments with credit or debit cards, either for one-shot or recurring payments.

Java

Java

```
final SecureVaultClient secureVaultClient = new SecureVaultClient(this);
secureVaultClient.generateToken(

"4111111111111111", // card number
"12", // card expiry month
"2020", // card expiry year
"John Doe", // card holder
"496", // security code
true, // multi use

// request callback
new SecureVaultRequestCallback() {
@Override
public void onSuccess(PaymentCardToken paymentCardToken) {
// Tokenization completed successfully!

// Do not forget to close once we got the callback
secureVaultClient.cancelOperation(this);
}

@Override
public void onError(Exception error) {
// Tokenization failed, probe exception for details

secureVaultClient.cancelOperation(this);
}
}
);
```

Updating a token or retrieving information about a token

You can also update a token by using the Secure Vault method named updatePaymentCard(String, String, String, String, String, UpdatePaymentCardCallback) .

To get information about a previously generated token, use the Secure Vault method named lookupPaymentCardWithToken(String, String, LookupPaymentCardCallback) .

## Payment

You can make payments using the Gateway Client and its requestNewOrder(OrderRequest, OrderRequestCallback) method. This request will both create a new order based on the information you provided and process the payment simultaneously.

Therefore, you need to provide your order ID, the amount of the transaction, the payment product (Visa, MasterCard, PayPal, etc.) and the related payment method information (i.e., the token if it's a credit or a debit card). You can also provide a lot of other optional information.

When requesting a new order, do not forget to check the state of the newly created transaction.

Java

Java

```
/* Create an order request which
* contains information about your order */
OrderRequest request = new OrderRequest();

request.setAmount(155.50f);
request.setCurrency("EUR");
request.setOrderId("TEST_9641952");
request.setShortDescription("Outstanding shirt.");
request.setOperation(OrderRelatedRequest.OrderRequestOperation.Sale);

/* Below, optional properties are defined as well.
* Check the HPFPaymentPageRequest documentation
* for the full list of parameters */
request.getCustomer().setCountry("FR");
request.getCustomer().setFirstname("John");
request.getCustomer().setLastname("Doe");
request.getCustomer().setEmail("[email protected]");

request.setPaymentProductCode(PaymentProduct.PaymentProductCodeVisa);

/* Payment method info, in this case,
* we re-use the token which has been
* generated in the previous section */
CardTokenPaymentMethodRequest cardTokenPaymentMethodRequest = new CardTokenPaymentMethodRequest(
"f39bfab2b6c96fa30dcc0e55aa3da4125a49ab03",
Transaction.ECI.SecureECommerce,
CardTokenPaymentMethodRequest.AuthenticationIndicator.Bypass);

request.setPaymentMethod(cardTokenPaymentMethodRequest);

final GatewayClient gatewayClient = new GatewayClient(this);
gatewayClient.requestNewOrder(request, signature, new OrderRequestCallback() {

@Override
public void onSuccess(Transaction transaction) {
// Check the transaction object, particularly its state

// Do not forget to close once we got the callback
gatewayClient.cancelOperation(this);
}

@Override
public void onError(Exception error) {
// Transaction failed, probe exception for details

gatewayClient.cancelOperation(this);
}
});
```

Implementation note

The signature parameter is required for security purposes. Please refer to the signature section for details.

## Payment Products

In order to get the exact list of payment methods enabled on your account, you can leverage the getPaymentProductsForRequest method of the Gateway Client . You need to provide this endpoint with information about your order (by using a PaymentPageRequest , because the list of payment products may change depending on order-related information (i.e., the currency)).

Java

Java

```
PaymentPageRequest request = new PaymentPageRequest();
request.setAmount(155.50f);
request.setCurrency("EUR");

// We just want the payment card products
request.setPaymentProductCategoryList(
Arrays.asList(
PaymentProduct.PaymentProductCategoryCodeCreditCard,
PaymentProduct.PaymentProductCategoryCodeDebitCard))
);

final GatewayClient gatewayClient = new GatewayClient(this);
gatewayClient.getPaymentProducts(request, new OrderRequestCallback() {

@Override
public void onSuccess(List paymentProducts) {
// Check the PaymentProduct objects

// Do not forget to close once we got the callback
gatewayClient.cancelOperation(this);
}

@Override
public void onError(Exception error) {
// The request failed, probe exception for details

gatewayClient.cancelOperation(this);
}
});
```

## Transaction Details

You can get the transactions related to an order or get information about a specific transaction by using the following methods:

* getTransactionWithReference(String, TransactionDetailsCallback)
* getTransactionsWithOrderId(String, TransactionsDetailsCallback) Please find below an example with the transactions linked to the merchant order ID TEST_89897:

Java

Java

```
final GatewayClient gatewayClient = new GatewayClient(this);
gatewayClient.getTransactionsWithOrderId("TEST_89897", signature, new TransactionsDetailsCallback() {

@Override
public void onSuccess(List transactions) {
// Check the transactions list

// Do not forget to close once we got the callback
gatewayClient.cancelOperation(this);
}

@Override
public void onError(Exception error) {
// The request failed, probe exception for details

gatewayClient.cancelOperation(this);
}
});
```

Implementation note

The signature parameter is required for security purposes. Please refer to the signature for details.

## Card Storage

The card storage feature allows to register a PaymentCardToken object in the SharedPreferences object for your application, necessary to use the 1-click payment for your customers.

Since the card storage option is turned ON, you have access to these three PaymentCardTokenDatabase class methods:

To get every tokens associated to a currency :
getPaymentCardTokens(Context, String)

To remove a specific token associated to a currency :
delete(Context, PaymentCardToken, String)

To remove every tokens located in your SharedPreferences :
clearPaymentCardTokens(Context)
