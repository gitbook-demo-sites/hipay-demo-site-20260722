---
description: "The HiPay Enterprise platform is protected to: Ensure that only authorized merchants use it, Prevent payment information from being compromised. PCI D"
icon: file-lines
---

# Security Considerations

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/requirements/security](https://developer.hipay.com/payment-fundamentals/requirements/security)
{% endhint %}

The HiPay Enterprise platform is protected to:

* Ensure that only authorized merchants use it,
* Prevent payment information from being compromised.

## PCI DSS requirements

HiPay Enterprise allows sending payment data, which means that the system will be transmitting, and possibly storing, card data.

Storage (SAD) information: The Card Schemes (American Express, Discover Financial Services, JCB International, MasterCard Worldwide and Visa Inc.) have never permitted the storage of sensitive data (track data and/or CVV2). It is prohibited under Requirement 3 of the Payment Card Industry Data Security Standard (PCI DSS).

Warning : Merchants who store Sensitive Authentication Data (SAD) are exposed to fines from the Card Schemes.

Data secure management: If the Tokenization API is used, merchants must demonstrate that the system can handle these data securely and that they are taking full responsibility for their PCI DSS compliance.

For further information on PCI security standards, please visit pcisecuritystandards.org .

## Encrypted communication

HiPay Enterprise provides all REST API methods over TLS (Transport Layer Security). Please note that TLS 1.0 will be deprecated and that it is strongly recommended to use TLS 1.1 or 1.2.

Guarantees : All data transmitted between HiPay Enterprise and the merchants' system are encrypted (256-bit encryption using a DigiCert certificate).

## IP restriction

When a request is sent to the platform, the IP address or IP address range from where the connection was made is verified. If it matches with the IP address supplied by the merchant at a previous stage (in the HiPay Enterprise back office: Integration section), the request will be processed.

In case of missing or incorrect information, the server will respond with an appropriate error message, indicating the error in the request.

Important : When your IP address is changed, do not forget to ensure that all new IP addresses are configured for your account. If not, your server requests will be rejected.

## Authentication

Only authenticated users and system components are allowed to access the Gateway API.
