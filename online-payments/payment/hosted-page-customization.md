---
description: "You can customize your Hosted Page v2 directly from HiPay's Console. This will help you provide a better user experience to your customers, and potent"
icon: file-lines
---

# Hosted Page Customization

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment/hosted-page-customization](https://developer.hipay.com/online-payments/payment/hosted-page-customization)
{% endhint %}

You can customize your Hosted Page v2 directly from HiPay's Console. This will help you provide a better user experience to your customers, and potentially increase the conversion rate.

## Customize

To start the customization, please go to the Hosted Page section of the Console Menu .

Business choice

If you have access to more than one HiPay Business, firstly, choose the Business that you want to create a new theme for.

If you only have access to one business, you won't see this step.

Business Theme Library

Once you select a business, you will see all the themes of the business, as seen in the screenshot below.

The themes are divided in two sections:

* Active Themes : Themes that are linked to one or more HiPay Accounts.
* Other Available Themes : Themes that have been created for this business but are not linked to an HiPay account at this moment.

Create a new Theme

If you want to create a new theme you have two options:

* Duplicate an existing theme : hover over the theme that you want to duplicate, then click Theme Actions, then Duplicate Theme.
* Create a new theme : click the + New Theme button. Customizable Elements

You can customize different elements of your Hosted Page:

* Theme Name : The title of the theme.
* Merchant Name : Name displayed at the top of the Payment form if you don't add a logo. It is important to add the real name as it will also be used for the Tab Title.
* Logo : Image that will be displayed at the top of the Payment form. The image must be on a SVG, JPEG or PNG format and smaller than 50Kb. On the Hosted Page, the Logo will have a max. height of 160px (ratio 16/9), but we will automatically adjust the image if you use another ratio.
* Form Design : position and height of the Payment Form.
* Background : Image used for the background. The image must be JPEG or PNG format and smaller than 400Kb. We recommend a 1 920 x 1080 image or smaller with a 16:9 ratio.
* Primary Color : Color used for the pay button.
* Secondary Color : Color used for the focused fields.
* Font : Font family used on the Hosted Page.

## Enable

Once you have created a theme, you can link it to an HiPay account.

To do so, you need to go to the Theme Visualisation page and click on the ACCOUNTS button, at the top right hand side of the screen.

Once you click the button, you will see the accounts of that business. Then select the accounts where you want to display the Theme and save the modifications. If an Hipay account doesn't have a theme linked to it, we will display the default theme.

## FAQ

I linked a theme to my HiPay account, but the style didn't change on my Hosted Page. What did I do wrong?

In order to display the theme that you created on the Hosted Page, you need to make sure that these two steps are done before creating the payment page:

* Link the theme to the account that you are using to generate the Hosted Page.
* Complete the technical integration of the Hosted Page v2 .
