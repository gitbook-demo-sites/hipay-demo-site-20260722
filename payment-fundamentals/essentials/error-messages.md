---
description: "Should an error occur, here is a list of all the possible related codes and messages as well as an indication on how to correct it. Configuration erro"
icon: file-lines
---

# Error messages

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/essentials/error-messages](https://developer.hipay.com/payment-fundamentals/essentials/error-messages)
{% endhint %}

Should an error occur, here is a list of all the possible related codes and messages as well as an indication on how to correct it.

## Configuration errors

Transactions with configuration errors shall not be retried.

Code
Message
Description
How to correct this error
Retry possible?

1000001
Incorrect Credentials
Incorrect username and/or password
This error can be caused by an incorrect API username or an incorrect API password. Make sure that all these values are correct. For your security, HiPay Enterprise does not report exactly which value might be erroneous.
No

1000002
Incorrect Signature
The signature that was sent does not match the requested format.

No

1000003
Account Not Active
The account is inactive.

No

1000004
Account Locked
The account is locked.

No

1000005
Insufficient Permissions
You do not have permission to make this API call.

No

1000006
Forbidden Access
The API access is disabled for this account.

No

1000007
Unsupported Version
The API version is not supported.

No

1000008
Temporarily Unavailable
The gateway is temporarily unavailable.
Please try again later.
No

1000009
Not Allowed
The request was rejected due to IP restriction.
Make sure that the IP addresses of your servers are configured for your account.
No

## Validation errors

Transactions with validation errors shall not be retried until the incorrect parameters are fixed.

Code
Message
Description
Retry possible?

1010001
Method Not Allowed
The specified HTTP method is not allowed for this API call.
No

1010101
Required Parameter Missing
A required parameter is missing.

No

1010201
Invalid Parameter
A parameter is in an invalid format.
No

1010202
Invalid Parameter
A parameter value exceeds the maximum number of characters allowed.
No

1010203
Invalid Parameter
A parameter contains non-alphabetic characters.
No

1010204
Invalid Parameter
A parameter contains non-numeric characters.
No

1010205
Invalid Parameter
The specified parameter is expected to be in decimal format, but does not appear to be a valid decimal value.
No

1010206
Invalid Date
The specified parameter does not seem to be a valid date.
No

1010207
Invalid Time
The specified parameter does not seem to be a valid time.
No

1010208
Invalid IP Address
The merchant entered an IP address that was in an invalid format. The IP address must be in a format such as 123.456.123.456.
No

1010209
Invalid Email Address
The merchant entered an email address that was in an invalid format.
No

1010301
Invalid Soft Descriptor
The soft descriptor contains invalid characters.
No

1010401
UTF-8 Encoding error
The merchant sent parameters which are not UTF-8 encoded.
No

## Checkout process

Code
Message
Description
How to correct this error
Retry possible?

1020001
No route to acquirer
The requested payment product is not configured for your account.
Please contact your account manager to solve this issue.
Once requested payment method has been added

1020002
Unsupported ECI
The specified ECI is not supported by the gateway.

No

1020003
Unsupported Payment Product
The specified payment product is not valid.
Please make sure that you have specified a valid product code.
No

Code
Message
Description
How to correct this error
Retry possible?

3000001
Unknown Order
The order was not found.

No

3000002
Unknown Transaction
The transaction was not found.

No

3000003
Unknown Merchant
The merchant account does not exist.

No

3000101
Unsupported Operation
The operation is not supported.
Please retry the request with a supported operation.
Once operation has been corrected

3000102
Unknown IP Address
The IP address cannot be detected. The transaction cannot be processed without a valid IP address.

Once IP address has been corrected

3000201
Suspicion of fraud
The transaction has been rejected by the financial institution due to suspected fraud.

Yes, max 5 times within 30 days

3030001
Fraud Suspicion
The transaction has been rejected by HiPay due to suspected fraud.

No

3040001
Unknown Token
The specified token was not found in the Secure Vault.

No

3010001
Unsupported Currency
The currency is not supported.
Please retry the request with a supported currency.
Once currency has been corrected

3010002
Amount Limit Exceeded
The amount exceeds the maximum amount allowed for a single transaction.
Please retry the request with a lower amount.
Yes, with lower amount

3010003
Max Attempts Exceeded
You have exceeded the maximum number of payment attempts for this order.

No

3010004
Duplicate Order
The order has already been processed.

Yes, with another order number

3010005
Checkout Session Expired
This session has expired. The order is no longer valid.

Yes, with another order number

3010006
Order Completed
The order has already been completed.

Yes, with another order number

3010007
Order Expired
The order has expired.

Yes, with another order number

3010008
Order Voided
The order has been voided.

Yes, with another order number

## Maintenance operations

Code
Message
Description
How to correct this error
Retry possible?

3020001
Authorization Expired
The authorization has expired.

No

3020002
Amount Limit Exceeded
The amount specified exceeds the allowable limit.
Please retry the request with a lower amount.
Yes, with lower amount

3020101
Not Enabled
The Capture feature is not enabled for the merchant.
Please contact your account manager to solve this issue.
Once capture has been enabled

3020102
Not Allowed
You cannot capture this type of transaction.

No

3020103
Not Allowed
You cannot partially capture this type of transaction.

No

3020104
Permission Denied
You do not have permission to capture this transaction
You are not the owner of this transaction.
No

3020105
Currency Mismatch
The currency must be the same for Capture and Authorization.
Make sure that currencies are the same and retry the request.
Once currency has been corrected

3020106
Authorization Completed
The authorization has already been completed.

No

3020107
No More
The maximum number of allowable captures has been reached.No more capture for the authorization.

No

3020108
Invalid Amount
The capture amount must be positive.
Please retry the request with a positive amount.
Once amount has been corrected

3020109
Amount Limit Exceeded
The capture amount must be less than or equal to the original transaction amount.
Please retry the request with a lower amount
Yes, with lower amount

3020110
Amount Limit Exceeded
The partial capture amount must be less than or equal to the remaining amount.
Please retry the request with a lower amount.
Yes, with lower amount

3020111
Operation Not Permitted
The transaction is closed.

No

3020112
Operation Not Permitted
Transaction Declined (Transaction not permitted)

No

3020201
Not Enabled
The Refund feature is not enabled for the merchant.
Please contact your account manager to solve this issue.
Once refund has been allowed

3020202
Not Allowed
You cannot refund this type of transaction.

No

3020203
Not Allowed
You cannot partially refund this type of transaction.

No

3020204
Permission Denied
You do not have permission to refund this transaction.
You are not the owner of this transaction.
No

3020205
Currency Mismatch
The refund must be in the same currency as the original transaction.
Make sure that the currencies are the same and retry the request.
Once currency has been corrected

3020206
Already Refunded
This transaction has already been fully refunded.

No

3020207
No More
The maximum number of allowable refunds has been reached. No more refund for the transaction.

No

3020208
Invalid Amount
The refund amount must be positive.
Please retry with a positive amount.
Once amount has been corrected

3020209
Amount Limit Exceeded
The refund amount must be less than or equal to the original transaction amount.
Please retry the request with a lower amount.
Yes, with lower amount

3020210
Amount Limit Exceeded
The partial refund amount must be less than or equal to the remaining amount.
Please retry the request with a lower amount.
Yes, with lower amount

3020211
Operation Not Permitted
The transaction is closed.

No

3020212
Too Late
You are over the time limit to perform a refund on this transaction.

No

3020301
Not Enabled
The re-authorization feature is not enabled for the merchant.
Please contact your account manager to solve this issue.
Once re-authorization has been enabled

3020302
Not Allowed
Re-authorization is not allowed for this type of transaction.

No

3020303
Cannot Reauthorize
You can only re-authorize the original authorization, not a re-authorization.

No

3020304
Max Limit Exceeded
The maximum number of re-authorizations allowed for the authorization has been reached.

No

3020401
Not Allowed
You cannot void this type of transaction.

No

3020402
Cannot Void
You can only void the original authorization, not a re-authorization.

No

3020403
Authorization Voided
The authorization has already been voided.

No

## Acquirer's reason codes

Code
Message
Description
Retry possible?

4000001
Declined
The transaction has been declined by the acquirer.
Yes, max 5 times within 30 days

4000002
Declined
The payment has been refused by the financial institution.
Yes, max 5 times within 30 days

4000003
Insufficient Funds
The customer's account does not have sufficient funds.
Yes, max 5 times within 30 days

4000004
Technical Problem
There was a problem processing this transaction.
Yes, max 5 times within 30 days

4000005
Communication Failure
This transaction cannot be processed.
Yes, max 5 times within 30 days

4000006
Acquirer Unavailable
This transaction cannot be processed because the acquirer is temporarily unavailable.
Yes, max 5 times within 30 days

4000007
Duplicate Transaction
The transaction has already been processed.
No

4000008
Payment cancelled by the customer
The transaction has been cancelled by the customer.
No

4000009
Invalid transaction
The transaction type is not valid.
No

4000010
Please call the acquirer support call number
An issue occurred with the acquirer: please contact your HiPay account manager.
No

4000011
Authentication failed. Please retry or cancel.
The authentication requested by the payment method has failed.
Yes, max 5 times within 30 days

4000012
No UID configured for this operation
The payment method used for this transaction is not supported on current account configuration.
No

4010101
Refusal (No Explicit Reason)
The transaction has been declined by the card issuer with no given explanation.
Yes, max 5 times within 30 days

4010102
Issuer Not Available
The authorization centre of the card issuer is not operational at this time.
Yes, max 5 times within 30 days

4010103
Insufficient Funds
The cardholder does not have enough funds to make this payment.
Yes, max 5 times within 30 days

4010201
Transaction Not Permitted
The transaction is not permitted for this type of card.
No

4010202
Invalid Card Number
The transaction failed due to an invalid credit card number.
No

4010203
Unsupported Card
The type of card is not supported or is unknown.
No

4010204
Card Expired
The transaction has been declined because the expiry date on the card used for payment has already passed.
No

4010205
Expiry Date Incorrect
The transaction has been declined because the expiry date entered for the card used for payment is incorrect.
No

4010206
CVC Required
The transaction cannot be processed because no Card Verification Code was provided.
No

4010207
CVC Error
The transaction has been declined because the CVC entered does not match the credit card.
No

4010301
AVS Failed
The transaction has been refused because the AVS response returned an N value and the merchant account is not able to accept such transactions.
No

4010302
Retain Card
The bank put a hold on purchases due to an issue with the cardholder's account.
No

4010303
Lost or Stolen Card
The card has been blocked by the card issuer because the cardholder reported it as being lost or stolen (potential fraud).
No

4010304
Restricted Card
The credit card is blacklisted by the card association.
No

4010305
Card Limit Exceeded
The transaction would exceed the monthly limit of the card.
Yes, max 5 times within 30 days

4010306
Card Blacklisted
The card has been rejected by the bank's fraud system.
No

4010307
Unauthorized IP address country
The IP address country used is not authorized.
No

4010309
Card not in authorizer's database
The credit card number is not in an authorized cards database.
No

4010310
3DS required but not used
The transaction requires 3DS authentication but the credit card is not enrolled.
No

4010312
Soft Declined
The authorization was declined by the issuer because the transaction was not authenticated
No, make sure MITs are correctly sent after a successfully authenticated CIT using the same multi-use token
