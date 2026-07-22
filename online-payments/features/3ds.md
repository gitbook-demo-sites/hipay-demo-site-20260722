---
description: "The 3-D Secure process provides enhanced security when performing an authenticated transaction as well as a shift of liability in the event of fraudul"
icon: file-lines
---

# 3DS

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/features/3ds](https://developer.hipay.com/online-payments/features/3ds)
{% endhint %}

The 3-D Secure process provides enhanced security when performing an authenticated transaction as well as a shift of liability in the event of fraudulent transactions. Authentication should strengthen your existing anti-fraud strategy and help protect your business, but bear in mind that the coverage of authentication programs is currently limited to Internet transactions.

Restriction : This means that authentication programs do not cover fax, mail or phone orders (MO/TO), nor do they cover all card types. The additional security benefits and liability shift of authenticated transactions are currently only supported by Visa and MasterCard.

## 3-D Secure transaction workflow

Proceed as follows to carry out a transaction.

* The merchant calls the HiPay Enterprise API with an authentication_indicator value of 1 or 2 (or the Fraud Protection Service ( FPS ) asks for 3-D Secure). Please note that in case of an authentication_indicator value of 0 , 3-D Secure is not triggered.
* To complete the purchase, the cardholder clicks on the Pay button after filling in payment card details on the payment page: this activates the Merchant Plug-In ( MPI ) and initiates a transaction.
* The MPI identifies the card number and sends it to the Directory Server to determine if the card is in a participating card range.
* If the issuer is participating for the card range, the Directory Server sends a Verify Enrollment Request message to the issuer's Access Control Server ( ACS ) to determine if authentication is available for the account number.
* The ACS returns a Verify Enrollment Response to the Directory Server. If authentication is available for this card number, the response then provides the URL of the ACS where the cardholder can be authenticated. If the payment is on a hosted payment page, the redirection to the ACS will be done automatically.
* If authentication is not available, the HiPay server then receives a Cardholder Not Enrolled or Unable to Authenticate message and proceeds depending on the authentication_indicator value: 1 : Proceeds with standard transaction processing (skip to step 13).
* 2 : The transaction is refused.
* The Directory Server forwards the ACS response to the MPI .
* The MPI sends an Authentication Request message to the cardholder's browser for routing to the ACS .
* The cardholder's browser passes the Authentication Request to the ACS .
* The ACS authenticates the cardholder.
* The ACS creates, digitally signs and sends an Authentication Response to HiPay via the cardholder's browser. The ACS also sends a transaction record to the Authentication History Server for storage.
* The browser routes the Authentication Response back to the MPI .
* The MPI validates the digital signature in the response, verifying that it is from a valid participating issuer.
* HiPay formats and sends its acquirer an Authorization Request message, which includes information from the issuer's Authentication Response - including the CVV and the ECI. The acquirer passes the Authorization Request to the card network and the transaction completes through standard processing.
* HiPay sends a notification with the transaction status and 3-D Secure authentication result. Please refer to the Authentication Results section .

## Authentication results

The following table lists the enrollment messages and statuses.

Status

Enrollment message

Is 3-D Secure available?

ECI

Description

Y

Authentication Available

Yes

-

The card is enrolled in the 3-D Secure program and the payer is eligible for authentication processing.

N

Cardholder Not Enrolled

No

6

The card is not enrolled in the 3-D Secure program. Chargeback Liability Shift : If the cardholder later disputes the purchase, the issuer may not submit a chargeback to the merchant.

U

Unable to Authenticate

No

7

The card associations were unable to verify if the cardholder is enrolled in the 3-D Secure program. Merchants can choose to accept the card nonetheless and process the purchase as non-authenticated when submitting the authorization. Chargeback Liability Shift : The acquirer/merchant retains liability if the cardholder later disputes making the purchase.

E

Any error message here

No

7

An error occurred during the enrollment verification process. Chargeback Liability Shift : The card can be accepted for authorization processing, yet the merchant may not claim a liability shift on this transaction in case of a dispute with the cardholder.

The following table lists the authentication messages and statuses.

Status

Authentication message

ECI

Description

Y

Authentication Successful

5

The cardholder was successfully authenticated. The issuer has authenticated the cardholder by verifying the identity information or password.

A

Authentication Attempted

6

Authentication could not be performed but a proof of authentication attempt was provided.

U

Authentication Could Not Be Performed

7

The issuer is not able to complete the authentication request due to a technical error or another problem. Possible reasons include: invalid type of card such as a commercial card or any anonymous prepaid card. Unable to establish a TLS session with the cardholder's browser.

N

Authentication Failed

-

The cardholder did not complete authentication and the card should not be accepted for payment. The following are reasons of failing an authentication: the cardholder fails to correctly enter the authentication information; the cardholder cancels the authentication process. An authentication failure may be a possible indication of a fraudulent user. The authorization request should not be submitted.

E

Any error message here

-

An error occurred during the authentication process. The authorization request should not be submitted.
