---
description: "Before integrating an HiPay Module on your CMS, it is required to first contact HiPay and request an account for the integration to work properly. HiP"
icon: file-lines
---

# CMS Prerequisites

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/cms-prerequisites](https://developer.hipay.com/cms-modules/cms-prerequisites)
{% endhint %}

Before integrating an HiPay Module on your CMS, it is required to first contact HiPay and request an account for the integration to work properly.

HiPay will guide you through the process and provide you a testing and production accounts.

You can either contact your account manager or our support team at [email protected]

## Entreprise Account

Your HiPay Enterprise account must be configured before installing your PrestaShop module in the HiPay Enterprise back office .

## Credentials

You need to generate API credentials to send requests to the HiPay Enterprise platform. To do so, go to the Integration section of your HiPay Enterprise back office, then to Security Settings.

To be sure that your credentials have the proper accessibility.

* From the Integration section of your HiPay Enterprise back office, in Security Settings, scroll down to Api credentials.
* Click on the edit icon next to the credentials you want to use. Private Credentials

Private credentials are mainly used for the authentication of the API calls that are done from a server. For exemple, the Order API. Your private credentials must be granted to:

Public Credentials

Public credentials are used for the authentication of the API calls that are done from a client side.For exemple, these are the credential that you will use for the tokenization. Your public credentials must be granted to:

## IP Addresses

When a request is sent to the HiPay Enterprise servers, the IP address or IP address range from where the connection was made is verified. If it matches with the IP address previously provided by the merchant, the request will be processed. In case of missing or incorrect information, the server will respond with an appropriate error message, indicating the error in the request.

To do this, you must log in your HiPay Enterprise back office ( https://merchant.hipay-tpp.com ), click on the Integration tab, then on Security Settings and enter your IP address(es) in the IP Restriction section.

When changing your IP address(es), make sure that all the new IP addresses are configured for your account. If not, your server requests will be rejected.

## Notification URLs

To use the HiPay Enterprise module, you need to configure the notification URLs in your HiPay Enterprise back office, from the Integration tab, in the Notifications section.

* Notification URL: http://www.{your-domain.com}/index.php?fc=module&module=hipay_enterprise&controller=notify
* Request method: HTTP POST
* I want to be notified for the following transaction statuses: Custom -> Select all notifications clicking in the first checkbox. Please make sure you replace {your-domain.com} by your own domain. You can also find this information in the configuration of the HiPay module in the MODULE INFORMATIONS area.

## Security

Please read the security articles before going live:

* Security Considerations
* Signature Verification
* Redirect Pages
