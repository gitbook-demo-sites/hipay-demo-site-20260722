---
description: "This feature enables you to create a specific user experience based on your digital strategy and your customers' needs by deploying different themes o"
icon: file-lines
---

# Hosted Page Multi Theme

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/hosted-page/hosted-page-multi-theme](https://developer.hipay.com/online-payments/hosted-page/hosted-page-multi-theme)
{% endhint %}

This feature enables you to create a specific user experience based on your digital strategy and your customers' needs by deploying different themes on your Hosted Page.

## CREATE YOUR MULTI THEMES

To start the creation other theme s, please go to the Hosted Page section of the Console Menu .

Business choice

If you have access to more than one HiPay Business, firstly, choose the Business that you want to create a new theme for.

Business Theme Library

Once you select a business, you will see all the themes of the business, as seen in the screenshot below.

The themes are divided in three sections:

* Active Themes (by default): Themes that are linked to one or more HiPay Accounts. It is the default theme for your account(s)
* Themes on demand : Those Themes that you have been created and activated, you can use it for any accounts. It will replace the theme by default if you integrate the theme code in your store for a specific brand or promotion for example.
* Other Available Themes : They have been created for this business but are not linked to an HiPay account at this moment.

Create a new Theme

If you want to create a new theme you have two options:

* Duplicate an existing theme: hover over the theme that you want to duplicate, then click Theme Actions, then Duplicate Theme.
* Create a new theme: click the + New Theme button. Use a theme on demand : How does it work ?

To display this theme, you have to go to the page of the theme to see this code.

This code is going to allow you to call your hosted page V2 with the hpayment API .

You can copy this code by clicking on it and integrate it in your development in order to send this code in the hpayment API for the attribute theme_code.
