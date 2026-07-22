---
description: "The device fingerprint identifies devices through information collected by a client run on an end user's computer. This client generates a black box t"
icon: file-lines
---

# Device Fingerprint Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/requirements/device-fingerprint-integration](https://developer.hipay.com/payment-fundamentals/requirements/device-fingerprint-integration)
{% endhint %}

The device fingerprint identifies devices through information collected by a client run on an end user's computer. This client generates a black box that contains all the available device information.

Web applications obtain device information by sourcing dynamically generated JavaScript from HiPay Enterprise. The JavaScript determines what information is available and generates a black box from all available sources.

A black box will typically:

* Range up to 4,000 bytes (the average length being just under 1,000 bytes)
* Contain alphanumeric values and the following special characters: + / ; =
* Begin with 0200, 0400, 0500 or 0600

## Generate black box content

To integrate the client, you must specify a hidden field that the JavaScript will populate. This adds the black box as another field to be submitted along the other details in the form.

What TO DO:

* You MUST include a hidden form field with a ioBB ID that will be populated with the value.
* You MUST call the HiPay Enterprise fingerprint JavaScript function to get the black box content: https://secure-gateway.hipay-tpp.com/gateway/toolbox/fingerprint What NOT TO DO:

* DO NOT call HiPay Enterprise fingerprint JavaScript BEFORE including the hidden ioBB form field.
* DO NOT cache or use local copies of the JavaScript (JavaScript is dynamically generated for each customer and caching the script may cause unrelated devices to be identified as the same computer. The script also uses domain cookies to identify devices across subscribers.)
