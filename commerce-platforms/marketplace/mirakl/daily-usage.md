---
description: "The HiPay Marketplace cash-out integration for Mirakl is intended to be used with a cron , but can be used directly from the command line. In fact, th"
icon: file-lines
---

# Mirakl - Daily Usage

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/mirakl/daily-usage](https://developer.hipay.com/marketplace/mirakl/daily-usage)
{% endhint %}

The HiPay Marketplace cash-out integration for Mirakl is intended to be used with a cron , but can be used directly from the command line. In fact, this software is supposed to execute tasks automatically, which is why you need to configure cron jobs (or any other alternative) that will execute commands at the appropriate time automatically.

Please note that default values for command line arguments/parameters are defined in the parameters.yml file.

There are 4 main commands that need to be run automatically by relying on cron jobs:

* Vendor processing ,
* Cash-out generation ,
* Transfer processing ,
* Withdrawal processing . There are also two debug and one update commands that do not need to be run using a cron job:

* Listing wallet accounts ,
* Getting bank information ,
* Recovering vendor logs from past executed cron .

## Notifications

In some cases, the HiPay integration for Mirakl can encounter errors or issues that cannot be managed automatically. In such a case, a notification is sent by email in order to inform you about the issue. The email recipient can be configured in the parameters.yml file. When this documentation refers to a notification being sent upon error, it means an email notification.

## Vendor processing

Command call

$ php bin/console vendor:process

Execution

* Retrieves the vendors from Mirakl.
* Saves the vendors: creates the HiPay account, if not already created, or gets the HiPay account number from HiPay.
* Validates them.
* Transfers the KYC files from Mirakl to the HiPay platform.
* Adds the bank information on the HiPay account, if not already done, or checks HiPay's bank information against the data from Mirakl to make sure they match. If these are not the same, an error notification is sent. Once the HiPay Marketplace cash-out integration for Mirakl is installed, you may call this method without the lastUpdate argument , just as below:

$ php bin/console vendor:process

This will make the command retrieve all the stores of your Mirakl instance and will synchronize all of them into the connector and into the HiPay platform. Then, the command may be run regularly with the lastUpdate parameter in order to only retrieve the new stores or the recently updated ones (please see the cron example).

Argument

Name Type Required Description lastUpdate Date No Date of the last update of Mirakl stores. If not provided, all stores will be retrieved. Options

Name Type Description tmpPath String Path where the documents should be saved temporarily before being sent to HiPay. Cron example

Please see below an example of how your cron job may be configured. Replace path/to/bin/console by the proper path to the console file. This command should be run as often as the vendors update their data.

0 */6 * * * php path/to/bin/console vendor:process 24 hour ago

In this cron example, the command will be run every 6 hours, retrieving the stores which have been updated in the last 24 hours. Retrieving the stores updated in the last 24 hours instead of the last 6 hours allows to handle some rare issues (for example, in case the command failed once because of a network issue disallowing it from reaching Mirakl or HiPay). In such a case, the stores would be synchronized on the next command call.

## Cash-out generation

Command call

$ php bin/console cashout:generate

Execution

* Retrieves the PAYMENT transactions from Mirakl to get all the invoices of the cycle.
* Gets the amount due to the vendors and the operator from the invoices.
* Creates the operations to be executed afterwards, validates and saves them.
* Adjusts operations amount to deal with past negative operations. Argument

Name Type Required Description cycleDate Date No Sets the cycle date Options

Name Type Description executionDate String Date to consider for cycle date computing intervalBefore Interval Interval to subtract from cycleDate intervalAfter Interval Interval to add to cycleDate Cron example

Please see below an example of how your cron job may be configured. Replace path/to/bin/console by the proper path to the console file. This command should be run right after the payment cycle has been made in Mirakl.

30 0 * * * php path/to/bin/console cashout:generate `date +%Y-%m-%d`

## Transfer processing

Command call

$ php bin/console cashout:transfer

Execution

* Executes, on the HiPay platform, the transfer of operations in statuses TRANSFER_NEGATIVE , TRANSFER_FAILED and CREATED (in this order). Arguments

This command doesn't have any argument.

Options

This command doesn't have any option.

Cron example

Please see below an example of how your cron job may be configured. Replace path/to/bin/console by the proper path to the console file.

This command should be run when you have payments you want to transfer to your sellers (basically, after completion of the cashout:generate command). Moreover, this command also handles the operations in error. For example, if an operation failed because the HiPay account was not identified at that time, the operation processing should be retried later. Therefore, it's a good practice to run this command once a day . In that case, this command will be run after the cashout:generate command and will also be run any other day in the month, in case operations would be in error.

0 2 * * * php path/to/bin/console cashout:transfer

## Withdrawal processing

Command call

$ php bin/console cashout:withdraw

Execution

* Executes, on the HiPay platform, the withdrawal of operations in statuses WITHDRAW_NEGATIVE , WITHDRAW_FAILED and TRANSFER_SUCCESS (in this order). Arguments

This command doesn't have any argument.

Options

This command doesn't have any option.

Cron example

Please see below an example of how your cron job may be configured. Replace path/to/bin/console by the proper path to the console file.

This command should be run when you have payments you want to withdraw from your sellers' wallet account and transfer to their bank account (basically, after completion of the cashout:transfer command). Moreover, this command also handles the operations in error. For example, if an operation failed because the HiPay account was not identified at that time, the operation processing should be retried later. Therefore, it's a good practice to run this command once a day .

0 4 * * * php path/to/bin/console cashout:withdraw

## Listing wallet accounts

Command call

$ php bin/console vendor:wallet:list

Execution

* Retrieves the HiPay account information associated with a merchant group ID (associated with an entity).
* Displays it in a table. Argument

Name Type Required Description merchantGroupId Integer No Merchant group ID for retrieving HiPay accounts Options

This command doesn't have any option.

## Getting bank information

Execution

* Retrieves the bank information status for a specific HiPay account ID.
* If that status is validated, displays the information stored by HiPay. Argument

Name Type Required Description hipayId Integer Yes HiPay account ID used to retrieve the bank information status Options

This command doesn't have any option.

## Recovering vendor logs

Command call

$ php bin/console logs:vendors:recover

Execution

* Retrieves every saved vendor in the database.
* If a vendor has no log, creates one. Argument

This command doesn't have any argument.

Options

This command doesn't have any option.

Parameters The following table describes the data in the parameters.yml file. The user you run the commands with should have write access to all the paths you use in this file.

Mirakl web service

Name Type Default value Description mirakl.frontKey String Mirakl API Front key (provided by Mirakl) mirakl.operatorKey String Mirakl API Operator key (provided by Mirakl) Mirakl cycles

Name Type Default value Description cycle.days Array [1, 11, 21] Array of days (1 to 28) on which the cycle is run in the month cycle.hour Integer 0 Hour on which the cycle is run cycle.minute Integer 0 Minute on which the cycle is run cycle.interval.before String 12 hours Time to subtract from the cycle time to form an interval from which to fetch the transactions from Mirakl cycle.interval.after String 12 hours Time to subtract from the cycle time to form an interval from which to fetch the transactions from Mirakl HiPay

Name Type Default value Description hipay.wsLogin String HiPay web service login key for the technical account hipay.wsPassword String HiPay web service password key for the technical account hipay.baseUrl String Base URL to HiPay web service hipay.entity String Provided by HiPay hipay.locale String fr_FR Locale of created accounts. Format should be: languageCode_ISO3166-1 alpha-2 country code hipay.timezone String Europe/Paris Time zone of created accounts. Please see the php manual for a list of time zones. hipay.merchantGroupId Integer Provided by HiPay hipay.transfer.withdraw.rest Boolean true Use REST api instead of SOAP api HiPay accounts

Name Type Default value Description account.technical.email String Email of the HiPay technical account account.technical.hipayId Integer ID of the HiPay technical account account.operator.email String Email of the HiPay operator's account account.operator.hipayId Integer ID of the HiPay operator's account HiPay labels

Name Type Default value Description label.public String Public {{miraklId}} - {{hipayId}} - {{cycleDate}} Public label for HiPay transfers. Please see hereafter for more details. label.private String Private {{miraklId}} - {{hipayId}} - {{cycleDate}} Private label for HiPay transfers. Please see hereafter for more details. label.withdraw String Withdraw {{miraklId}} - {{hipayId}} - {{cycleDate}} Withdrawal label for HiPay withdrawals. Please see hereafter for more details. Database

Name Type Default value Description db.driver String pdo_mysql PHP PDO driver. Please refer to the php manual for a list of PDO drivers. db.host String DB hostname db.username String DB username db.password String DB password db.name String DB name db.port Integer DB port Miscellaneous

Name Type Default value Description debug Boolean false Activates Debug mode db.logger.level Integer 300 Minimum logging level at which this handler will be triggered default.tmp.path String /tmp Default path to save the downloaded zip file log.file.path String /var/log/hipay.log Path to the log file cashout.transactionFilterRegex String null Used to filter cash-out transactions. Leave null if you don't know what to do with it. dashboard.locale String fr Default locale for the dashboard Log level

Label Value DEBUG 100 INFO 200 NOTICE 250 WARNING 300 ERROR 400 CRITICAL 500 ALERT 550 EMERGENCY 600

## Labels

Labels give a description of the transaction (transfer or withdrawal) and appear on the account statement. For label parameters (label.public, label.private, label.withdraw), the following placeholder strings can be used, which will be replaced before sending the data to HiPay. Each string must be surrounded by {{ and }} to be replaced.

Placeholder Description miraklId Store ID if it exists, or operator ID in case of an operator's operation amount Amount of the operation hipayId HiPay account ID cycleDate Cycle date of the operation cycleDateTime Cycle date and time of the operation cycleTime Cycle time of the operation date Execution date of the operation dateTime Execution date and time of the operation time Execution time of the operation

## Appendix

Please find below the description of each operation status listed in the operations table.

Name Value Description CREATED 1 The operation has been created. ADJUSTED_OPERATIONS 2 The operation has been adjusted (concerns past negative operations). TRANSFER_SUCCESS 3 The transfer has been executed with success. TRANSFER_REQUESTED 4 The transfer has been requested with success. WITHDRAW_REQUESTED 5 The withdrawal has been requested with success. WITHDRAW_SUCCESS 6 The withdrawal has been executed with success. INVALID_AMOUNT -1 The amount of the operation is invalid (lower than or equal to 0), it will not be processed. TRANSFER_VENDOR_DISABLED -5 Payments for this vendor are disabled on Mirakl back-office, the transfer is blocked. WITHDRAW_VENDOR_DISABLED -6 The vendor is disabled on Mirakl back-office, the withdraw is blocked. WITHDRAW_FAILED -7 The withdrawal has been executed and failed. WITHDRAW_CANCELED -8 The withdrawal has been canceled. TRANSFER_FAILED -9 The transfer has been executed and failed. TRANSFER_NEGATIVE -10 The transfer has not been executed because there are not enough funds in the HiPay technical account. WITHDRAW_NEGATIVE -11 The withdrawal has not been executed because there are not enough funds in the wallet account. WITHDRAW_PAYMENT_BLOCKED -12 Payments for this vendor are disabled on Mirakl back-office, the withdraw is blocked.
