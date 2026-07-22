---
description: "This integration intends to facilitate cash-out operations between HiPay and Mirakl. This software is based on the Silex PHP micro-framework and integ"
icon: file-lines
---

# Mirakl - Prerequisites

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/mirakl/prerequisites](https://developer.hipay.com/marketplace/mirakl/prerequisites)
{% endhint %}

This integration intends to facilitate cash-out operations between HiPay and Mirakl. This software is based on the Silex PHP micro-framework and integrates the HiPay Marketplace cash-out connector for Mirakl PHP library.

Name

Nature

Description

HiPay

Third-party and web service provider

Payment solution handling payment processing between the operator and the different stores available on your marketplace

Mirakl

Third-party and web service provider

Marketplace solution handling the stores, with a read-only web service

Cron

System service

Unix task scheduler, which may be replaced by a Windows alternative if needed (not tested with Windows)

Integrator

Human

The developer, who wishes to easily interface HiPay and Mirakl

General

* The config/parameters.yml file must be a YAML file with one top key named parameters. A default example can be seen in the config/parameters.yml.dist file.

* The parameters.yml file should not be committed nor transmitted to any third party.

System

* You must have at least PHP 5.6. The library has dependencies that need at least this version of PHP.

* You should have Composer, which is the best way to install the library or do the integration.

* You should use MySQL. Even though the integration should function with most RDBMSs, it was only tested with MySQL 5.5 through Doctrine.

* A web server is required, with a URL accessible by HiPay with the HTTP verb POST so that server-to-server notifications can be sent by HiPay. It can be Apache, Nginx or any other choice, as long as the other mandatory requirements are met.

Mirakl

* Each store must have a unique email address, as a HiPay account is created with and tied to an email address.

* Even though Mirakl does not require filling in the phone number section, it must be completed to create a HiPay account.

* Even though Mirakl only requires filling in the IBAN and the BIC in the banking information section, all form fields must be completed to provide banking information to HiPay.

* Only alphanumeric characters should be used for filling in the fields, especially for banking information, as HiPay only accepts this category of characters.

* The version of the API should be at least 3.*.*.

* Should the API version be higher, as long as the concerned API being called remains backwards compatible, there won't be any problem.

HiPay

* Some operations require HiPay's assistance: please contact HiPay's Business IT Services for technical support on the HiPay Support Center .

* A HiPay account for the operator must be created beforehand. An email address that will not be used for another store on the marketplace is required.

* A good understanding of APIs for cash-out transactions may be useful: please refer to the HiPay Marketplace - APIs overview guide.

## Mirakl configuration

In order for us to validate the HiPay accounts, the connector needs to upload KYC documents allowing us to identify your merchants.

Thus, you need to configure your Mirakl back office in order to be able to upload these documents for each of your stores. Then, these documents will be retrieved by the HiPay Marketplace cash-out integration for Mirakl and sent to the HiPay platform.

Furthermore, you need to specify which stores should be processed.

### Documents

Go to the Manage document types section by following these steps.

* Log in to your Mirakl operator account.

* In the Settings tab, click on Stores (in the Advanced parameters column).

* Click on Documents.

You need to provide the following list of document types by clicking on Add a document type .

Label

Description

Code

Bank

Bank account details (RIB/IBAN) / Account statement /... (for all professionals)

ALL_PROOF_OF_BANK_ACCOUNT

Identity card

Copy of the front of a valid identification document of the legal representative (professionals - only for corporations )

LEGAL_IDENTITY_OF_REPRESENTATIVE

Identity card rear

Copy of the back of a valid identification document of the legal representative (professionals - only for corporations )

LEGAL_IDENTITY_OF_REP_REAR

Company Registration

Document certifying company registration issued within the last three months (Kbis extract) (professionals - only for corporations )

LEGAL_PROOF_OF_REGISTRATION_NUMBER

Distribution of power

Signed Articles of Association with the division of powers (professionals - only for corporations )

LEGAL_ARTICLES_DISTR_OF_POWERS

ID proof

Copy of the front of a valid identification document of the legal representative (professionals - only for persons )

SOLE_MAN_BUS_IDENTITY

ID proof rear

Copy of the back of a valid identification document of the legal representative (professionals - only for persons )

SOLE_MAN_BUS_IDENTITY_REAR

Company Registration

Document certifying registration issued within the last three months (Kbis extract) (professionals - only for persons )

SOLE_MAN_BUS_PROOF_OF_REG_NUMBER

Tax status

Document certifying tax status (auto-entrepreneur / independent /...) (professionals - only for persons )

SOLE_MAN_BUS_PROOF_OF_TAX_STATUS

You can put whatever you want in the description field. In any case, the codes must be exactly as displayed in the table.

Then, you will need to upload the documents on each of the store pages.

Documents must be image (jpg, jpeg, png...) or PDF files: otherwise, the HiPay Marketplace cash-out integration for Mirakl will not process them.

Please note: when uploading your documents (on a store page), only upload files corresponding to the type of your store. For example, if the store is managed by a person, you can only upload the required documents flagged as being only for persons as well as the bank account details, but not the documents flagged as being only for corporations.

If your marketplace only has corporations as stores and no stores managed by persons (most probable scenario), you should not upload the document types flagged as being only for persons.

For more information on the types of KYC documents, please check HiPay Marketplace - REST API to upload KYC documents .

### Custom Fields

Go to the Manage custom fields section by following these steps.

* Log in to your Mirakl operator account.

* In the Settings tab, click on Stores (in the Advanced parameters column).

* Click on Custom Fields.

You need to provide the following custom field by clicking on Add a Custom Field:

Code

Label

Description

Type

Stores permission

Required

Default Value

hipay-process

HiPay Process

Store that will be processed

Yes/No

Read write

true

Yes

Please note: if the custom field hipay-process is not set, no store will be processed by the HiPay Marketplace cash-out integration for Mirakl.

### Shop Accounts

In order to comply with regulations and have a proper vendor status management, you need to enable the option of Suspend Shop Accounts at creation.

You can find this option here: {your_company}.mirakl.net/mmp/operator/setting/settings/all

Once the KYC, UBO and Bank informations will be validated by HiPay, the HiPay Mirakl connector will automatically change the vendor's payment status to Active on Mirakl.

It is also important for you to know that, if after having enabled it, the vendor decides to update the bank information, we will disable the payments temporarily, until the documents are validated by HiPay.
