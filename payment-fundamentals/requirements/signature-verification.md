---
description: "It is strongly recommended to use a signature mechanism to verify the contents of a request or redirection made to your servers. This prevents custome"
icon: file-lines
---

# Signature Verification

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/payment-fundamentals/requirements/signature-verification](https://developer.hipay.com/payment-fundamentals/requirements/signature-verification)
{% endhint %}

It is strongly recommended to use a signature mechanism to verify the contents of a request or redirection made to your servers. This prevents customers from tampering with the data in the data exchanges between your servers and our payment system.

A unique signature is sent each time HiPay contacts any merchant's URL, notification or redirection.

## Setup

Section: BO TPP > INTEGRATION > SECURITY SETTINGS .

First of all, you need to set a secret passphrase in your HiPay Enterprise back office. The secret passphrase is used to generate a unique character string (signature) hashed with SHA algorithm. The security level of the password depends on its length. The longer the better.

The SHA that would be used for the signature verification depends on your configuration. By default we use the SHA-256, but you can change it to SHA-1 or the SHA-512.

## Verification

There are two types of requests you'll need to verify : Notifications sent to your servers, and Redirection URLs. The Signature Algorithm is different depending on the type of request you wish to verify.

#### Notification URL

For the notification URL, the signature is sent on the HTTP header under the x-allopass-signature parameter. To check this point, you just need to concatenate the passphrase with the POST content of the query.

Notification signature algorithm

SHA signature = SHA(Raw POST Data + Secret Passphrase)

#### Redirection URL

For each redirection page (accept page, decline page, etc.), the signature is sent under the hash parameter. To check this point, you must concatenate the parameters, the values of each of them and the passphrase under the following conditions:

* The parameter must be predefined,
* The value can't be empty,
* The parameters must be sorted in alphabetical order. Please note: you must remove any personal parameter from the query to only include the HiPay parameters.

Redirection URL signature algorithm

* paramC = val3
* paramA = val1
* paramB = val2
* passphrase = passphrase
* SHA signature = SHA(paramAval1passphraseparamBval2passphraseparamCval3passphrase) Please note :

* if your URL contains custom_data parameters, you'll need to use simple quotes in order to concatenate the json object.
* any url_encoded parameter must be decoded before hashing the string. For example, cid=test id will be returned as cid=test+id in the redirect url. This parameter should be used as cidtest idSecretPassphrase in the string to be hashed.
* the response parameter must not be taken into account in the string to be hashed Concatenation example

Parameters :

* amount = 125.7
* currency = EUR
* custom_data = {testing:true}
* orderid = 15424657
* passphrase = SecretPassphrase The concatenated string will be :

amount125.7SecretPassphrasecurrencyEURSecretPassphrasecustom_data{testing:1}SecretPassphraseorderid15424657SecretPassphrase'

(note that the true boolean value was changed to a stringified 1, as will be any integer values. For example, {data:55) must be changed to {data:55} before applying the sha algorithm)

For example, the resulting sha1 hash will be :

3cb7285da5a0342930f4a56774de7fa168ef42d9

PHP

PHP

```
$secretPassphrase = 'mypassphrase';
//Secret Passphrase
$string2compute = '';

if (isset($_GET['hash'])) {
// If it is a redirection
$signature = $_GET['hash'];
$parameters = $_GET;
unset($parameters['hash']);
ksort($parameters);
foreach ($parameters as $name => $value) {
if (strlen($value)>0) {
$string2compute .= $name . $value . $secretPassphrase;
}
}
}
else {
// If it is a notification
$signature = $_SERVER['x-allopass-signature'];
$string2compute = file_get_contents("php://input"). $secretPassphrase;
}
$computedSignature = sha1($string2compute);

// true if OK, false if not
if ($computedSignature == $signature) {
$message = 'OK';
}
else {
$message = 'KO';
}
```
