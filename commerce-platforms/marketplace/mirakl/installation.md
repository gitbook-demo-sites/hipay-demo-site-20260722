---
description: "Before starting the installation, please read all instructions and make sure you've gone through the Prerequisites article. Please note that all relat"
icon: file-lines
---

# Mirakl - Installation

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/mirakl/installation](https://developer.hipay.com/marketplace/mirakl/installation)
{% endhint %}

Before starting the installation, please read all instructions and make sure you've gone through the Prerequisites article.

Please note that all relative paths are relative to the root directory of the installation .

## Application deployment

This section describes how to install the HiPay Marketplace cash-out integration for Mirakl using Git and Composer , the PHP package manager. The software being installed is based on the Silex PHP micro-framework .

* Connect to your web server using SSH.

* Go to your web project directory (example: $ cd /var/www or $ cd /srv ).

* Download and install Composer (if you haven't already done so): $ curl -sS https://getcomposer.org/installer | php - -filename=composer - -install-dir=/usr/local/bin

* Download the project using Git: $ git clone https://github.com/hipay/hipay-wallet-cashout-mirakl-integration hipay_mirakl

* Go to the project directory: $ cd hipay_mirakl .

* Install the project dependencies using Composer: $ composer install This step may take a few minutes to complete as the project and its dependencies are being downloaded and configured.

* (Optional) If you use the default log file ( /var/log/hipay.log ), run the following commands: $ touch /var/log/hipay.log

* $ chmod 755 /var/log/hipay.log

* (Optional) If you want to enable updates from GUI, run the following commands: $ chown -R :

* $ chmod 755 -R

Please note: if you don't want to set these specific rights on your install folder, updates from GUI will be disabled. However, updates from command line will still be available.

During the installation, Composer will ask you to provide some parameters, including your HiPay account credentials and your Mirakl API credentials. Please go to the Prerequisites article if you need more information about these parameters.

## Webserver configuration

This configuration depends on the web server software you rely on (Apache, Nginx, etc.).

This software is based on the Silex PHP micro-framework .

Therefore you can find a guide to configure your webserver at the following link .

Make sure your webserver is pointing to the web folder at the root of the application.

Note: if you are using Apache, .htaccess file must be created in the web folder of the application

## HiPay cash-out notifications

This section describes how to provide HiPay with information on how to reach your server in order to automatically inform your application upon transaction status update (for example, when a withdrawal has been validated). HiPay notifies your application through HTTP requests.

* Configure your web server so that HiPay can reach the web/index.php through HTTP ( previous section ).

* Note the URL from which the web/index.php/ is reachable (example: https://cashout.merchant-example.com/index.php/ or https://cashout.merchant-example.com/ depending of your webserver configuration). Then, contact HiPay's Business IT Services by submitting a request to configure this URL as your marketplace notification URL.

## Initialization and final check

Go to the project directory:

$ cd hipay_mirakl .

Run the following command:

$ php bin/console orm:schema-tool:update --dump-sql --force .

This command will initialize the database with the needed tables. You should get this database schema:

## Vendors

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

miraklId
int(11)
NO
UNI
NULL

email
varchar(255)
NO
UNI
NULL

hipayId
int(11)
NO
UNI
NULL

hipayUserSpaceId
int(11)
NO
UNI
NULL

hipayIdentified
int(11)
NO
UNI
NULL

vatNumber
VARCHAR(255)
NO
UNI
NULL

callbackSalt
VARCHAR(255)
NO
UNI
NULL

enabled
TINYINT(1)
NO
UNI
NULL

country
VARCHAR(255)
NO
UNI
NULL

paymentBlocked
TINYINT(1)
NO
UNI
NULL

## Operations

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

miraklId
int(11)
YES

NULL

hipayId
int(11)
YES

NULL

amount
double
NO

NULL

originAmount
double
YES

NULL

cycleDate
datetime
NO

NULL

withdrawId
varchar(255)
YES
UNI
NULL

transferId
varchar(255)
YES
UNI
NULL

status
int(11)
NO

NULL

updatedAt
datetime
NO

NULL

paymentVoucher
varchar(255)
NO

NULL

adjustementIds
varchar(255)
YES

NULL

## Documents

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

vendor_id
int(11)
YES

NULL

miraklDocumentId
int(11)
YES

NULL

miraklUploadDate
datetime
NO

NULL

documentType
varchar(255)
NO

NULL

## Batches

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

name
longtext
NO

NULL

error
longtext
YES

NULL

started_at
datetime
NO

NULL

ended_at
datetime
YES

NULL

### log_general

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

miraklId
int(11)
YES

NULL

action
longtext
YES

NULL

message
longtext
NO

NULL

context
longtext
NO

NULL

level
smallint(6)
NO

NULL

level_name
varchar(50)
NO

NULL

extra
longtext
NO

NULL

created_at
datetime
NO

NULL

### log_operations

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

miraklId
int(11)
YES

NULL

hipayId
int(11)
YES

NULL

paymentVoucher
varchar(255)
NO

NULL

dateCreated
datetime
YES

NULL

amount
double
NO

NULL

originAmount
double
YES

NULL

statusTransferts
int(11)
YES

NULL

statusWithDrawal
int(11)
YES

NULL

message
longtext
YES

NULL

balance
varchar(255)
YES

NULL

### log_vendors

Field
Type
Null
Key
Default
Extra

id
int(11)
NO
PRI
NULL
auto_increment

miraklId
int(11)
NO

NULL

hipayId
int(11)
NO

NULL

login
varchar(255)
YES

NULL

statusWalletAccount
int(11)
NO

NULL

status
int(11)
NO

NULL

message
varchar(255)
YES

NULL

nbDoc
int(11)
NO

NULL

date
datetime
NO

NULL

enabled
TINYINT(1)
NO
UNI
NULL

country
VARCHAR(255)
NO
UNI
NULL

paymentBlocked
TINYINT(1)
NO
UNI
NULL

To verify that your software is properly installed and configured, please go to the URL you sent to HiPay (example: https://cashout.merchant-example.com/index.php/dashboard ). The login page of the dashboard should be displayed . If that's not the case, make sure that you properly configured the parameters.yml file and that all the information provided in it is correct.
