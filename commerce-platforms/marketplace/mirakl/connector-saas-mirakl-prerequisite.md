---
description: "To use our HiPay connector for your Marketplace platform, you need a Mirakl account for your marketplace. We recommend that you have multiple Mirakl e"
icon: file-lines
---

# Connector Saas - Mirakl Prerequisite

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/mirakl/connector-saas-mirakl-prerequisite](https://developer.hipay.com/marketplace/mirakl/connector-saas-mirakl-prerequisite)
{% endhint %}

To use our HiPay connector for your Marketplace platform, you need a Mirakl account for your marketplace.

We recommend that you have multiple Mirakl environments with dedicated test environments. Contact your Mirakl account manager to get a test environment if you do not have one.

If your workflow has specificities, contact your HiPay account manager to know whether the connector is compatible with it or not.

The onboarding process on the HiPay SaaS connector has a list of tests to perform in order to confirm that the cash-out process is operating smoothly.

* The merchant must have a Mirakl account.
* Each marketplace must have a unique Mirakl account associated with it.
* Each store must have a unique email address, as a HiPay account is created with and tied to an email address.
* Even though Mirakl does not require filling in the phone number section, it must be completed to create a HiPay account.
* Mirakl only requires filling in the IBAN and the BIC in the banking information section, however, all form fields must be completed to provide banking information to HiPay.
* Only alphanumeric characters should be used in the fields, especially for banking information, as HiPay only accepts this category of characters.

## Manual Configuration

To ensure the HiPay Mirakl connector is operating smoothly, some configuration steps are mandatory.

These operations must be performed manually during onboarding.

Follow the procedure below to complete this preliminary configuration.

### Manage documents

The KYC/KYB identification of your sellers by HiPay is achieved through the documents you provide for each of your stores.

Mirakl does not have a native interface dedicated to this process. It is therefore necessary to add the proper documents that will allow the connector to retrieve the documents you uploaded to Mirakl, so that HiPay can identify each seller.

* Log in to your Mirakl operator account.
* Go to Settings > Advanced Parameters > Shops.
* Click on the Documents tab.
* Click on Add a document type and provide the following list of documents.

LABEL

CODE

DESCRIPTION

[ COMPANY/PERSON/ASSOCIATION ] ID proof front

INDIVIDUAL_IDENTITY

Copy of the front of a valid ID of the legal representative

(identity card or passport) of the legal representative

Only for companies/persons and associations.

[ COMPANY/PERSON/ASSOCIATION ] ID proof rear

INDIVIDUAL_IDENTITY_REAR

Copy of the back of a valid ID of the legal representative

(identity card or passport) of the legal representative

[COMPANY ] Registration

LEGAL_PROOF_OF_REGISTRATION_NUMBER

Document certifying the registration of the company issued in the last three months (Kbis extract)

Only for companies

[ COMPANY ] Distribution of power

LEGAL_ARTICLES_DISTR_OF_POWERS

Signed articles of association with the distribution of powers

Only for companies

[ PERSON ] Registration

SOLE_MAN_BUS_PROOF_OF_REG_NUMBER

Document certifying the registration issued in the last three months (Kbis extract)

Only for the persons

[ COMPANY WITH LICENSE ] License

LEGAL_LICENSE

License document (gambling or alcohol)

Only for licensed companies

[ ASSOCIATION ] Status

ASSOCIATION_STATUS

A copy of the association's statutes

Only for the association

[ ASSOCIATION ] Official Journal

ASSOCIATION_OFF_JOURNAL

Publication in the dedicated register (or equivalent) or a receipt of the association's registration issued by the public authorities

Only for associations

[ ASSOCIATION ] President of association

ASSOCIATION_PRESIDENT_INFO

Document attesting to the position and name of the association's legal representative

Only for associations

[ ALL ] Bank info

ALL_PROOF_OF_BANK_ACCOUNT

Bank account details (RIB/IBAN) / Statement of account ...

If you are using the old Hipay connector, here are the documents you should no longer use.

You can depreciate or delete them at your convenience:

#### Depreciation

Add [DO NOT USE] in the label and description field.

This allows you to avoid having to delete the documents on each store.

#### Delete

Delete the document by clicking on the cross corresponding to the document line.

You must first delete all the associated documents on all the stores of your platform.

LABEL

CODE

DESCRIPTION

ID proof

SOLE_MAN_BUS_IDENTITY

Copy of the front of a valid ID of the legal representative (professionals - only for persons)

ID proof rear

SOLE_MAN_BUS_IDENTITY_REAR

Copy of the back of a valid ID of the legal representative (professionals - only for persons)

Identity card

LEGAL_IDENTITY_OF_REPRESENTATIVE

Copy of the front of a valid ID of the legal representative (professionals - only for companies)

Identity card rear

LEGAL_IDENTITY_OF_REP_REAR

Copy of the back of a valid ID of the legal representative (professionals - only for companies)

### Manage custom fields

Adding a custom field allows you to modify certain behaviors of the connector in the management of your stores.

Access the Manage Custom Fields section by following these steps:

* Log in to your Mirakl operator account.
* Go to Settings > Advanced Parameters > Shops.
* Go to the Custom Fields tab. Create new fields using the following values:

#### Custom fields 1: Hipay Process

This field is used to block the processing of invoices from this store in the Hipay cash-out process.

SETTINGS

DESCRIPTION

Code

hipay-process

Label

Hipay cash out process

Description

Store that will be processed in Hipay cash out process.

Type

Yes/No

Store permission

Invisible

Required

true

Default Value

Yes

#### Custom fields 2: Hipay shop type

The HiPay KYC/KYB verification process relies on the legal structure of your sellers.

This information does not exist in Mirakl by default, this field allows you to fill in the structure of each of your sellers.

SETTINGS

DESCRIPTION

Code hipay-shop-type Label Account type Description Account legal status Type Single values list

Accepted values :
- Coporation
- Person
- Association
- Corporation_License Store permission Read write Required True Default Value Corporation

## Configure Shop account set up

To comply with current regulations, you must activate the Suspend store accounts at creation option.

The store is suspended on your marketplace platform when it is created and goes automatically live when the HiPay identification process is done.

When the store is suspended, product sales are not possible.

* Login to your Mirakl operator account.
* Go to Settings > Advanced Parameters > Mirakl Quality Control. Go to the Options tab.
* Check the Suspend shop account at creation option.
* Save the form

## Configure Billing cycle

Mirakl controls the amount and the frequency of payments made to your sellers, based on your settings.

By default, billing cycles start on the 1st, 11th and 21st of each month.

For testing purposes, you can create an every day billing cycle. For more information, please read Mirakl's documentation .

## Payment confirmation option

The HiPay SaaS connector allows you to automatically update the status of invoices to Paid when all payments have been made. This option is not enabled by default on your Mirakl instances, so you must send a request to enable it.

For more information, please read Mirakl's documentation .
