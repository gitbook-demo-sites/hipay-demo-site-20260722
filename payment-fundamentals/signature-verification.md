---
description: "Verify HiPay server notifications before updating merchant systems."
icon: signature
---

# Signature verification

Signature verification protects merchants from accepting forged notifications.

{% stepper %}
{% step %}
## Capture the raw payload

Read the exact request body and headers sent by HiPay. Do not normalize or reorder fields before verification.
{% endstep %}

{% step %}
## Recompute the signature

Use the shared secret configured for the account to compute the expected signature.
{% endstep %}

{% step %}
## Compare safely

Use a constant-time comparison function when available.
{% endstep %}

{% step %}
## Process idempotently

Only update the order if the signature is valid and the status transition has not already been applied.
{% endstep %}
{% endstepper %}

{% tabs %}
{% tab title="Node.js" %}
```js
import crypto from "node:crypto";

function verifyHipaySignature(rawBody, receivedSignature, secret) {
  const expected = crypto
    .createHmac("sha256", secret)
    .update(rawBody)
    .digest("hex");

  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(receivedSignature)
  );
}
```
{% endtab %}

{% tab title="PHP" %}
```php
function verifyHipaySignature(string $rawBody, string $received, string $secret): bool {
    $expected = hash_hmac('sha256', $rawBody, $secret);
    return hash_equals($expected, $received);
}
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
The exact signing algorithm and header names should be confirmed against the merchant account configuration during implementation.
{% endhint %}
