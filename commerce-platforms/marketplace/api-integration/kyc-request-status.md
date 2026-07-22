---
description: "This web service enables you to request the list of sent KYC/KYB documents as well as their status. Service endpoints There are two endpoints (base UR"
icon: file-lines
---

# KYC - Request Status

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/kyc-request-status](https://developer.hipay.com/marketplace/api-integration/kyc-request-status)
{% endhint %}

This web service enables you to request the list of sent KYC/KYB documents as well as their status.

## Service endpoints

There are two endpoints (base URLs) to which you can make your API calls.

Stage : https://test-professional.hipay.com/api/identification {format} (POST)

Production : https://professional.hipay.com/api/identification {format} (POST)

## Format

JSON | XML

The format is not mandatory, but you can choose the format of the received response. By default, the response is in JSON format.

## Authentication

This web service requires a basic HTTP authentication, with the HiPay technical account wsLogin and wsPassword.

## Request header

You may use the Account ID or the Account email login to select an account different from the authenticated one.

Field name

Format

Length

Req

Description

php-auth-subaccount-id

N

12

C

Account ID of the HiPay account for which to request the list of sent KYC/KYB documents and their status

php-auth-subaccount-login

AN

255

C

Email login of the HiPay account for which to request the list of sent KYC/KYB documents and their status

Bash
PHP

Bash

```
curl -v -X GET
https://professional.hipay.com/api/identification.json
-u "XX12xxab000b00ab0101010abcd0a0xx:abc0abcd1ee1ff6789abc2345fff0000"
-H "php-auth-subaccount-id: 543210"
```

PHP

```
define('API_ENDPOINT', 'https://professional.hipay.com/api/identification.json');
define('API_USERNAME', 'XX12xxab000b00ab0101010abcd0a0xx');
define('API_PASSWORD', 'abc0abcd1ee1ff6789abc2345fff0000');
$credentials = API_USERNAME . ':' . API_PASSWORD;

$reso
);urce = API_ENDPOINT;

// create a new cURL resource
$curl = curl_init();

// header parameters
$header = array(
'Accept: application/json',
'php-auth-subaccount-id: 543210
);

// set appropriate options
$options = array(
CURLOPT_URL => $resource,
CURLOPT_HTTPHEADER => $header,
CURLOPT_USERPWD => $credentials,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_FAILONERROR => false,
CURLOPT_HEADER => false,
CURLOPT_POST => false,

foreach ($options as $option => $value) {
curl_setopt($curl, $option, $value);
}

// execute the given cURL session
if (false === ($result = curl_exec($curl))) {
throw new RuntimeException(curl_error($curl), curl_errno($curl));
}

$status = (int)curl_getinfo($curl, CURLINFO_HTTP_CODE);
$response = json_decode($result);

var_dump($response);

curl_close($curl);
```

## Response fields

Field name

Description

code

Indicates if the API call has been done without errors (0 = success)

message

Displays the message related to the code

user_space

ID of the user space being verified

- Deprecated: will be removed soon

identification_status

User space identification status

- Unidentified: the user space is not identified, documents are missing

- Identified

- Identification in progress: a manual review is being performed to identify the user space

documents

All the required KYC/KYB documents for this user space:

- type: please see here for a detailed description

- label: please see here for a detailed description

- status_code: please see table 15 for a detailed description

- status_label: please see table 15 for a detailed description

## Status codes and status labels

status_code

status_label

Description

-1

NA

No document has been uploaded

1

Waiting

The document has been sent to HiPay

2

Validated

The document has been validated for identification

3

Refused

The document has been refused because it is falsified, expired or inconsistent

5

Waiting

The document is being reviewed

8

Refused

The document has been refused

## Response examples

Example of an ok response

JSON
XML

JSON

```
{
"code": 0,
"message": "Identification documents list succeeded",
"user_space": 012345,
"identification_status": "Identified",
"documents": [
{
"type": 1,
"label": "ID proof",
"status_code": 2,
"status_label": "Validated"
},
{
"type": 4,
"label": "Company Registration",
"status_code": 2,
"status_label": "Validated"
},
{
"type": 5,
"label": "Distribution of power",
"status_code": 2,
"status_label": "Validated"
},
]
}
```

XML

```

0

012345

1

9

2

9

```

Example of an authentication error response

JSON
XML

JSON

```
{
"code": 401,
"message": "Authentication Failed."
}
```

XML

```

401
Authentication Failed.

```
