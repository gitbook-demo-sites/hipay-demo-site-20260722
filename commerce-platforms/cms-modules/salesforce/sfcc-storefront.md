---
description: "The customer payment experience depends on the chosen HiPay Operation Mode. You can change it at any time on the Custom Site Preferences > HiPay Setti"
icon: file-lines
---

# SFCC Storefront

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/salesforce/sfcc-storefront](https://developer.hipay.com/cms-modules/salesforce/sfcc-storefront)
{% endhint %}

The customer payment experience depends on the chosen HiPay Operation Mode. You can change it at any time on the Custom Site Preferences > HiPay Settings.

## Credit Card payment

### Hosted Page

On the billing page, the customer selects Hosted Credit Cards. After the customer submits the order is redirected to a Payment page hosted and provided by HiPay, where the credit card form appears where the end-customer can enter the payment details

After completing payment with the HiPay, the customer is redirected back to the storefront. If the payment is successful or unknown, the customer is taken to the confirmation page.

### iFrame

On the billing page, the customer selects Hosted Credit Cards or other payment method. After Submitting the order from the summary page, the customer is then taken to a Payment page, where the HiPay credit card form appears inside an iFrame.

When payment is complete, the customer is directed to the confirmation page as usual. If the payment is successful or unknown, the customer is taken to the confirmation page. If the payment was unsuccessful, the customer is given an error message on the summary page and asked to select a different payment method.

### API

When using this method, the storefront functionality will be the same as the SFCC standard one for credit cards. The card is authorized inline during checkout directly on the merchant's website.

Once the payment is complete, the customer is directed to the confirmation page as usual

### 3D Secure

If you enable the 3DS option to your cartridge, the customer might be redirected to the 3D Secure page after clicking on the pay button. This only happen in the cases where the card is applicable by the customer's bank to 3D Secure.

When the strong authentification is complete, the customer is redirected to the confirmation page as per the normal flow.

## Other Payment Means

When using these methods, if the currency is applicable with one of these methods, the bank payment option will be shown (each one of them work only in specific currencies).

After Submitting the order from the summary page, the customer is redirected to the 3rd party website.

After completing payment with the 3rd party, the customer is redirected back to the storefront. If the payment is successful or unknown, the customer is taken to the confirmation page. If the payment was unsuccessful, the customer is given an error message on the summary page and asked to select a different payment method.

## Order Status

When making a payment, a Salesforce Commerce Cloud Order object changes its status as follows:

* CREATED - the iFrame or Hosted page has been shown; the basket has been cleared; the order may stay in this status if the process did not complete properly (bug) or if the user abandons the iFrame or the Hosted page and does not complete the payment.
* NEW - the order in the iFrame or Hosted page has been accepted - the order has changed its status.
* OPEN - the order has been viewed in SCC Business Manager after being in status NEW.
* FAILED - all cases of Cancel and Decline.
