---
description: "The HiPay integration cartridge is compatible with the latest Salesforce Commerce Cloud API version, currently 19.10 and the Storefront Reference Arch"
icon: file-lines
---

# SFCC Integration

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/cms-modules/salesforce/sfcc-integration](https://developer.hipay.com/cms-modules/salesforce/sfcc-integration)
{% endhint %}

The HiPay integration cartridge is compatible with the latest Salesforce Commerce Cloud API version, currently 19.10 and the Storefront Reference Architecture version 4.4.1. It might require updates and reviews for future versions and releases of the Storefront Reference Architecture.

Make sure you already have the a configured HiPay account before installing the module.

The plugin and its changelog are available on our GitHub .

## Installation

Install the int_hipay_sfra, bm_hipay_controllers cartridges from the distributive zip-archive in the standard way using the Salesforce Commerce Cloud UX-studio.

## Metadata Import

Open the folder metadata' in the installation package. Please review the site_template_sfra' folder, do the necessary modifications if required:

* Rename the RefArchGlobal folder (under the site_template_sfra/sites folder) to the ID of your site.
* In the file jobs.xml, change the RefArchGlobal in the markups to the ID of your site.
* In the file services.xml, change the RefArchGlobal in the markups to the ID of your site.
* If you don't need pin-price-lists.xml' with pricebook, you may just remove this file and the pricebooks' folder. For multiple sites integration, you will also need to repeat these steps for each site.

Then, archive the site_template_sfra' folder into a file named site_template_sfra.zip.

Before importing the site-template_sfra.zip', check and save the cartridge paths of your site and Business Manager, because these will be modified. By saving them elsewhere you will be able to configure them manually if something goes wrong. Also, check the fields which will be updated after importing the file site-template_sfra.zip' and be sure that there will be no conflict with any existing fields.

Finally, import it through BM Administration > Site Development > Site Import & Export section: Browse your local file and click Upload, then select it and click Import and confirm the import by clicking OK. The import lasts a few minutes only.
