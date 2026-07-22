---
description: "Accept payments in your own Android application thanks to the HiPay Android SDK. The HiPay Enterprise Android SDK is a library that allows you to acce"
icon: file-lines
---

# Android - Fundamentals

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/mobile-payments/android/android-fundamentals](https://developer.hipay.com/mobile-payments/android/android-fundamentals)
{% endhint %}

Accept payments in your own Android application thanks to the HiPay Android SDK.

The HiPay Enterprise Android SDK is a library that allows you to accept payments in your Android application by leveraging the HiPay Enterprise payment platform. The library is written in Java and is based on Android framework.

## INTEGRATIONS

There are two ways of integrating the check out:

### FAST

Advantages: Simplicity and speed.

This integration allows you to accept payments in your Android app very quickly.

In this scenario, your customers are presented with a built-in native payment screen. Yet, you won't be able to do much customization of the payment workflow.

If you choose this integration, here you have the full documentation.

### ADVANCED

Advantages: Checkout page customization.

This integration allows you to build your own payment workflow and your own form, using the core wrapper. You can thus fully customize the payment experience to fit your needs

On the downside, you have to take care of building the whole user interface of the page and creating and sending the orders to HiPay so the payment can be made.

If you choose this integration, here you have the full documentation.

## DEMO APP

The HiPay Enterprise SDK for Android comes with a demo application which allows you to quickly test the built-in payment screen integration.

Our demo application helps you understand how to use the SDK by generating a simple payment screen based on many parameters such as: amount, payment product categories, etc.

This particular screen is not part of the SDK and your users will not see it. It is part of the demo application and has been created for testing purposes only.
