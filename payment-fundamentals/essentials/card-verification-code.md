---
description: "The CVC is available on the following credit and debit cards: Visa (Card Verification Value CVV2), MasterCard (Card Validation Code CVC2), Maestro, Di"
icon: file-lines
---

# Card Verification Code

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/essentials/card-verification-code](https://developer.hipay.com/payment-fundamentals/essentials/card-verification-code)
{% endhint %}

The CVC is available on the following credit and debit cards: Visa (Card Verification Value CVV2), MasterCard (Card Validation Code CVC2), Maestro, Diners Club, Discover (Card Identification Number CID), and American Express (Card Identification Number CID).

When the acquirer enables you to perform a CVC check, a result code (returned along with the response to the authorization request) informs you on the CVC check status.You then evaluate the CVC result code that you received with the transaction authorization and take appropriate action based on all transaction characteristics.

Warning : Only a few acquirers return specific CVC check results. For most acquirers, the CVC is assumed to be correct if the transaction is successfully authorized.

The table below lists the available result codes as returned in the API response messages.

Code

Message

Description

Blank

Not applicable

The CVC check was not possible.

M

Match

The CVC matches.

N

No Match

The CVC does not match.

P

Not processed

The CVC request was not processed.

S

Missing

The CVC should be on the card, but the cardholder has reported that it is not.

U

Not supported

The card issuer does not support CVC.
