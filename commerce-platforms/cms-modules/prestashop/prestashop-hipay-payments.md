---
description: "The HiPay Enterprise module for PrestaShop 1.7.x / 8.x / 9.X is a PHP module which allows you to accept payments in your PrestaShop online store, offe"
icon: file-lines
---

# Prestashop HiPay Payments

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/prestashop/prestashop-hipay-payments](https://developer.hipay.com/cms-modules/prestashop/prestashop-hipay-payments)
{% endhint %}

The HiPay Enterprise module for PrestaShop 1.7.x / 8.x / 9.X is a PHP module which allows you to accept payments in your PrestaShop online store, offering innovative features to reduce shopping cart abandonment rates, optimize success rates and enhance the purchasing process on merchants' sites to significantly increase business volumes without additional investments in the PrestaShop e-commerce CMS solution.

Please make sure you go through the CMS Prerequisites article before stating the integration.

The HiPay Payments connector is available in three versions, each corresponding to a generation of PrestaShop. Download the version that matches your installation:

PrestaShop Version Connector Version Architecture 1.7.6+ 3.X.X Legacy 8.x 4.X.X Partial Symfony 9+ 5.X.X Full Symfony

The plugin and its changelog are available on our GitHub .

### Step 1 - Open the Module Manager

In the PrestaShop back office, go to Modules Module Manager , then click Install a module (top-right button).

### Step 2 - Upload the module archive

Drag and drop the hipaypayments.zip archive into the upload area, or click select a file to browse to the downloaded file. The archive is a .zip file.

### Step 3 - Confirm installation

PrestaShop installs the module automatically. Once complete, a Module installed! confirmation is displayed. Click Configure to go directly to the connector settings.

Installation confirmed. Click Configure to proceed to configuration.

## Configuration Migration

If a previous HiPay connector (HiPay Enterprise) is detected on your store, the module automatically offers to migrate your existing configuration.

If a previous HiPay module is detected, this banner appears when opening the configuration.

Two options are available:

Option What happens YES, MIGRATE DATA The previous module's configuration is automatically copied: credentials, payment methods and their settings, advanced preferences. The old module is disabled once migration is complete. No, go to module's configuration You are taken directly to the new connector's blank configuration. You will need to enter your HiPay credentials manually.

### Migration result

When you choose automatic migration, the connector runs five operations and confirms each step in real time:

* Credentials import

* Payment methods update

* Card payment settings update

* Advanced payment options update

* Database update

All five migration steps are validated. The page automatically reloads to the new connector's configuration.

## My Account

The My Account tab centralises your HiPay credentials and the transaction processing environment settings.

Connector navigation: Introduction, My Account, Main Settings, Card Payment, Other Payment Methods. The green banner indicates the production environment is active - payments are real.

### Environment

Select Test or Production depending on your store's context:

* Test : transactions are simulated. Use this during integration and UAT.

* Production : transactions are real and result in actual bank settlements. A green banner reminds you of this mode as soon as it is enabled.

The connector uses the test or production credentials for all transactions based on the selected environment.

### Credentials

Environment selection (Test / Production) and entry of private production credentials.

Enter your private production credentials available in your HiPay back office (username, password, secret key).

#### Apple Pay credentials (optional)

The Apple Pay fields only need to be filled in if you have a dedicated merchant account for Apple Pay transactions . In that case, Apple Pay payments will be processed on that specific account. If you do not have a dedicated Apple Pay account, leave these fields empty.

#### MOTO credentials (optional)

MOTO (Mail Order / Telephone Order) credentials allow your team to process payments on behalf of a customer who is not present online.

Apple Pay, MOTO, and public credentials sections in the My Account tab.

### CRON - Transaction status updates

We strongly recommend setting up a CRON job on your server to ensure regular synchronisation of transaction statuses. The recommended frequency is every 10 minutes .

The connector automatically generates the CRON command tailored to your store. You can copy it directly from the interface:

The CRON command is generated automatically. Click Copy line then add it to your server's CRON configuration.

Example command (yours will differ):

```
*/10 * * * * curl -s "https://[your-store]/module/hipaypayments/notifycron?action=processQueue&key=[your-key]" >/dev/null 2>&1
```

### Verify and save

Once your credentials are entered, click Verify credentials and save to validate the connection to the HiPay API before saving. The Save button saves without prior verification.

## Main Settings

Main Settings tab: capture type configuration and logging.

### Capture type

Mode Behaviour Automatic As soon as a transaction is authorised, the capture is performed automatically. No manual action is required in PrestaShop or the HiPay back office. Manual A manual action is required from PrestaShop or the HiPay back office to trigger the capture, in full or partially. Use this if you want to review orders before charging the customer.

### Detailed logs

If you experience issues during order processing, enable detailed logs . The log level switches to Debug and files are retained for 30 days. You can download the latest log file directly from this interface to share with our support team.

Recommendation: disable this option in production once the diagnosis is complete to avoid any performance impact.

## Card Payment

The Card Payment tab lets you configure how the card payment form is displayed and its associated settings.

### Operating mode

Mode Description Hosted fields The card input fields (number, expiry date, CVV) are displayed directly within your store's checkout flow, with no redirect. The customer stays on your site throughout the payment. Hosted page The customer is redirected to a payment page hosted by HiPay. Once the payment is validated, they are automatically sent back to your store.

Hosted fields mode: the card form is displayed inline within the PrestaShop checkout, without any redirect.

Hosted page mode: the customer is redirected to a dedicated HiPay payment page to complete the transaction.

#### Hosted fields customisation

In Hosted fields mode, you can customise the appearance of the input fields: font family, size, weight, text colour, cursor colour, and icon colour.

Hosted fields customisation options: font (e.g. Roboto), size, text colour, and cursor colour.

#### One-Click payment

When this option is enabled, customers can save their card during a first payment and reuse it for future purchases without re-entering their details.

* A card is only saved if the transaction is successfully validated.

* Expired cards are automatically removed from the user's saved card list.

* One-Click is not available in Hosted page mode. This feature only works with Hosted fields.

One-Click at checkout: the customer can select a previously saved card or pay with a new one. The Save this card toggle is visible for new card entries.

#### Hosted page options

In Hosted page mode: display mode (Redirect or Iframe), cancel button option, and 3DS mode configuration.

Setting Options Description Display Redirect / Iframe Redirect : the customer is sent to a new HiPay page. Iframe : the payment page is embedded directly in the checkout without leaving your store. Cancel button Yes / No Displays a Cancel button on the HiPay payment page, which returns the customer to your store's checkout. 3DS mode Dropdown Configures the 3D Secure authentication behaviour according to your contractual requirements.

### Card settings (accepted networks)

The connector automatically retrieves the card networks active on your HiPay account (CB, Visa, Mastercard, Amex, Bancontact, etc.). For each network, you can:

* Enable or disable the network.

* Set a minimum and maximum transaction amount for which this network is offered.

Active card networks retrieved from your HiPay contract. Each network can be expanded to configure min/max amounts and currency or country restrictions.

Note: if a customer attempts to pay with a card network that is not enabled on your account, they will be notified and the transaction will not go through.

## Other Payment Methods

Alternative payment methods active on your account, ordered via drag & drop. Each method can be expanded to configure its settings.

This tab lists all alternative payment methods active on your HiPay account (Alma, iDEAL, Bancontact, PayPal, etc.). Only methods enabled in your HiPay back office are displayed here.

If a payment method you want to offer is not shown, contact your HiPay Technical Account Manager.

### Display customisation

* Display order: drag and drop payment methods to set the order in which they appear at checkout.

* Enable / disable: each method can be individually enabled or disabled, independently of its status in the HiPay back office.

* Min / max amounts: set the thresholds below or above which a method is not offered. Exception: Alma - min/max amounts cannot be changed from PrestaShop; they are managed directly by Alma.

### Geographic restrictions

Some payment methods are only available in certain countries - this restriction is inherent to the method and cannot be modified from PrestaShop. The connector enforces these restrictions automatically: for instance if a customer attempts to pay with iDEAL from France, that method will not be offered to them at checkout.

## Apple Pay Multi-Browser

The HiPay connector for PrestaShop is compatible with Apple Pay Multi-Browser , which allows you to offer Apple Pay on all browsers, not just Safari.

### How it works

When a customer uses a non-Safari browser (Chrome, Firefox, Edge...) and clicks the Apple Pay button:

* A QR code is displayed on screen.

* The customer scans the QR code with their iPhone or iPad.

* They complete the payment from their Apple device.

* Once the payment is validated, the order status is automatically updated in PrestaShop and the customer is redirected to the order confirmation page.

### Configuration options

Option Description Modal The QR code is displayed in a modal window overlaying the checkout page. Popup The QR code opens in a separate popup window.

Prerequisite: if you have a dedicated Apple Pay merchant account, enter the Apple Pay credentials in the My Account tab. Without a dedicated account, Apple Pay transactions are processed through your main HiPay account.
