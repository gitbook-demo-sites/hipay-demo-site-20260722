---
description: "This module depends on HiPay Fullservice module for Magento 2 and cannot be used on its own. Before continuing, make sure you have followed the HiPay "
icon: file-lines
---

# Hyva

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/magento/hyva](https://developer.hipay.com/cms-modules/magento/hyva)
{% endhint %}

This module depends on HiPay Fullservice module for Magento 2 and cannot be used on its own.
Before continuing, make sure you have followed the HiPay Fullservice for Magento 2 module installation steps.

## 1. Installation guide

The plugin and its changelog are available on our GitHub .

First you need to go to your document root directory.

You can now install the module with the following command line:

Bash

Bash

```
composer require hipay/hipay-enterprise-magento2-hyva
```

After the Composer installation, you must run these command lines:

Bash

Bash

```
bin/magento module:enable --clear-static-content HiPay_FullserviceMagento
bin/magento setup:upgrade
bin/magento cache:clean
```

If no errors are displayed, the module is installed.

You can then go to your Magento Admin Panel.

## 2. Update guide

You can update the module with the following command line:

Bash

Bash

```
composer update hipay/hipay-enterprise-magento2-hyva
```

Then, you must run these command lines:

Bash

Bash

```
bin/magento setup:static-content:deploy
bin/magento setup:upgrade php
bin/magento cache:clean
```

## 3. Payment method compatibility

The HiPay Hyva compatibility module is compatible with the following
payment methods:

* Hipay Entreprise Hosted Page Credit Card

* Apple Pay

* Paypal

* Alma (3x et 4x)

* Credit Card Hosted Fields

* Apple Pay

* Paypal

* Alma (3x et 4x)

Other payment methods will be added in the near future. If you are interested by the compatibility of a specific payment method, please contact us.
