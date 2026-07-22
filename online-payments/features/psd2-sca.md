---
description: "In effect since the beginning of 2018, the second Payment Services Directive (PSD2) redefines security standards for online payments. Given the strong"
icon: file-lines
---

# PSD2 & SCA

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/features/psd2-sca](https://developer.hipay.com/online-payments/features/psd2-sca)
{% endhint %}

In effect since the beginning of 2018, the second Payment Services Directive (PSD2) redefines security standards for online payments. Given the strong growth of e-commerce in Europe, it aims to increase security during payment processing, while fighting more actively against fraud attempts.

## PSD2

This is the goal of the PSD2: to strengthen and increase e-shoppers' trust.

With the enforcement of the Regulatory Technical Standards (RTS) arising from the PSD2 as of September 14, 2019, new requirements in terms of strong authentication must be applied to all transactions carried out over the Internet for a better protection of customers.

While a transition period with current payment systems has been planned, you must anticipate this change and comply with 3-D Secure 2, the new version of the protocol developed by EMVCo (organization bringing together representatives from the main card networks and leaders in the payment industry) which standardizes the process of strong authentication for online payments.

Please note: The 3-D Secure standard only applies to card payments (Visa, Mastercard, CB, American Express) and not to payments made with alternative or local payment methods (Klarna, iDEAL, Bancontact...).

As a payment service provider, HiPay is here to guide you and facilitate your transition to these new authentication methods.

## Change on September 14, 2019

As of September 14, 2019, the decision to apply strong authentication is made by the issuer, the cardholder's bank (end customer). The issuer makes this decision according to the numerous criteria set in the PSD2 (limits, exemptions, fraud rate management...) and based on the analysis of more than 150 data collected during each purchasing process.

Therefore, to comply with the new PSD2 requirements and improve user experience, the 3-D Secure 2 protocol has been developed to benefit from a more dynamic and more secure authentication, that integrates innovative authentication methods, such as biometric authentication solutions.

More importantly, version 2 of the protocol enables merchants to offer purchasing processes more integrated to their environment.

When the issuers deem that the data sent make it possible to identify the cardholder, or when transactions meets certain eligibility criteria, the authentication process is completely transparent for the end users.

However, when the analyzed data doesn't allow the cardholder to be identified, a strong customer authentication is required.

In both cases, responsibility is transferred to the issuer.

## Understanding SCA

This new requirement imposes strong authentication on customers when they finalize their purchases, by combining two independent authentication factors.

These authentication factors can be:

something known by the end customer (e.g.: password, secret question, secret code, etc.),

something owned by the end customer (e.g.: smartphone, connected device, token, chip card, etc.),

something inherent to the end customer (e.g.: fingerprint, facial or vocal recognition, iris recognition, etc.).

The technical answer to these new requirements relating to strong authentication involves the implementation of 3-D Secure 2.

To comply with this new regulation, it is thus necessary to :

* understand how 3-D Secure 2 works,
* evaluate if you can benefit from an exemption when making a transaction,
* collect the new types of data required by the regulation and provide them to your PSP for each transaction.

## Out of the scope and exemption

Certain transactions may be exempt from strong authentication, others are outside of the scope of PSD2.

Thanks to HiPay's anti-fraud tools, our teams will work together with merchants for optimal implementation of exemptions, with the goal of maximizing the fluidity of the customer journey, while actively fighting fraud.

For more information on possible exemptions, please refer to our web page dedicated to PSD2 .

## HiPay's help

To meet PSD2 requirements, HiPay will provide you guidance and support regarding the evolution of your technical integration.

Thus, HiPay makes it easier for you to implement 3-D Secure 2 by minimizing the constraints of integration on your end.

Implementing the new protocol does not modify the current architecture between the merchant and HiPay.

However, in order to maximize the success of your transactions and simplify your customer journey, it is strongly recommended to collect the new types of data described below and provide them to HiPay.
