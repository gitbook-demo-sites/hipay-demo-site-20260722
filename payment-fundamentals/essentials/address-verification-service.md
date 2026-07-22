---
description: "The Address Verification Service (AVS) allows e-commerce merchants to check a cardholder's billing address. AVS provides merchants with a key indicato"
icon: file-lines
---

# Address Verification Service

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/essentials/address-verification-service](https://developer.hipay.com/payment-fundamentals/essentials/address-verification-service)
{% endhint %}

The Address Verification Service (AVS) allows e-commerce merchants to check a cardholder's billing address. AVS provides merchants with a key indicator that helps verify whether or not a transaction is valid. The table below lists the available result codes as returned in the API response messages.

Code

Message

Description

Blank

Not applicable

No AVS response was obtained (Default value).

Y

Exact Match

Street addresses and postal codes match.

A

Partial Match

Street addresses match; but postal codes don't.Either the request does not include the postal codes or postal codes are not verified due to incompatible formats.

P

Partial Match

Postal codes match; but street addresses don't.Either the request does not include the street addresses or street addresses are not verified due to incompatible formats.

N

No Match

Neither the street addresses nor the postal codes match.

C

Not Compatible

Street addresses and postal codes are not verified due to incompatible formats.

E

Not Allowed

AVS data is invalid or AVS is not allowed for this card type.

U

Unavailable

Address information is unavailable for that account number, or the card issuer does not support AVS.

R

Retry

The issuer's authorization system is unavailable; please try again later.

S

Not Supported

The card issuer does not support AVS.
