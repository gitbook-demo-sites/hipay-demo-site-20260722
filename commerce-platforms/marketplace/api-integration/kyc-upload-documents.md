---
description: "This web service enables you to upload KYC/KYB documents to a HiPay user account. Sent KYC/KYB documents are automatically processed in real time if t"
icon: file-lines
---

# KYC - Upload Documents

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/marketplace/api-integration/kyc-upload-documents](https://developer.hipay.com/marketplace/api-integration/kyc-upload-documents)
{% endhint %}

This web service enables you to upload KYC/KYB documents to a HiPay user account.

Sent KYC/KYB documents are automatically processed in real time if the documents provided are usable. Otherwise, a manual review is performed within 72 hours (working days). If a document is uploaded and sent by mistake, please wait until it is refused to re-submit the right document.

Please note that all the information collected will be kept confidential and will not be disclosed to third parties, except as provided by the law.

## Document constraints

* Accepted formats: JPG, GIF, PDF, PNG
* Maximum file size: 15 MB
* A certified translation is required for documents in a non-Latin language

## Service endpoints

There are two endpoints (base URLs) to which you can make your API calls.

Stage : https://test-professional.hipay.com/api/identification {format} (POST)

Production : https://professional.hipay.com/api/identification {format} (POST)

## Format

JSON | XML

The format is not mandatory, but you can choose the format of the received response. By default, the response is in JSON format.

## Authentication

This web service requires a basic HTTP authentication, with the HiPay technical account wsLogin and wsPassword.

## Types of KYC/KYB

### Individual accounts

Type

Label

Description

1

ID proof

A copy of front and back sides of a valid identification document

(ID card or passport) of the account holder (person)

2

Proof of address

Proof of address issued within the last 3 months

(e.g.: utility/phone bill, rent receipt)

### Professional accounts (corporations)

Type

Label

Description

1

ID proof

A copy of front and back sides of a valid identification document

(ID card or passport) of the legal representative

4

Company Registration

Certificate of incorporation (document certifying Company registration) issued within the last 3 months (Kbis extract or any equivalent document)

5

Distribution of power

Signed Articles of Association with the division of powers (featuring the address of the head office, the name of the company and the name of the legal representative)

### Professional accounts (persons)

Type

Label

Description

1

ID proof

A copy of front and back sides of a valid identification document

(ID card or passport) of the individual

8

Company Registration

Registration number with the Registry of Companies (SIREN number or its equivalent)

### Association accounts

Type

Label

Description

1

ID proof

A copy of front and back sides of a valid identification document

(ID card or passport) of the legal representative

11

President of association

Document certifying the function and the name of the legal representative of the association

12

Official Journal

Publication in the dedicated register (or equivalent) or a receipt of the registration of the association issued by public authorities

13

Association status

A copy of the association statutes

Please note: Professional (corporations) and association accounts also require a document entitled Identification of Ultimate Beneficial Owners, duly completed, signed and accompanied by supporting identification documents of beneficial owners (to be sent through https://professional.hipay.com/login : to access this platform, please contact your HiPay account manager).

## Request header

You may use the Account ID or the Account email login to select an account different from the authenticated one.

Field name

Format

Length

Req.

Description

php-auth-subaccount-id

N

12

C

Account ID of the HiPay account for which to upload the KYC/KYB documents

php-auth-subaccount-login

AN

255

C

Email login of the HiPay account for which to upload the KYC/KYB documents

## Request parameters

Field name

Format

Length

Req.

Description

type

N

12

M

Type of KYC/KYB document (please see here for a detailed description)

file

AN

255

M

KYC/KYB document to upload

- Accepted formats:

JPG, GIF, PDF, PNG

- Maximum file size: 15 MB

back

AN

255

C

Back side of the identification document to upload

- Accepted formats:

JPG, GIF, PDF, PNG

- Maximum file size: 15 MB

validity_date

D

10

C

Document expiry date

(YYYY-MM-DD format)

- Mandatory for identification documents (type 1)

- Optional for other KYC/KYB documents

Bash
PHP

Bash

```
curl -v -X POST
https://professional.hipay.com/api/identification.json
-u "XX12xxab000b00ab0101010abcd0a0xx:abc0abcd1ee1ff6789abc2345fff0000"
-H "php-auth-subaccount-id: 543210"
-F "file=@/home/johndoe/Desktop/Projects/uploads/DSCF1131.jpg"
-F "type=1"
-F "validity_date=2025-05-17"
```

PHP

```
define('API_ENDPOINT', 'https://professional.hipay.com/api/identification');
define('API_USERNAME', 'XX12xxab000b00ab0101010abcd0a0xx');
define('API_PASSWORD', 'abc0abcd1ee1ff6789abc2345fff0000');
$credentials = API_USERNAME . ':' . API_PASSWORD;

$resource = API_ENDPOINT;

// create a new cURL resource
$curl = curl_init();

// request headers
$header = array(
'Accept: application/json',
'php-auth-subaccount-id: 543210
);
// request parameters
$data = array(
'type' => 1,
'validity_date' => '2025-05-17',
'file' => '@/home/johndoe/desktop/Projects/uploads/DSCF1131.jpg'
);

// set appropriate options
$options = array(
CURLOPT_URL => $resource,
CURLOPT_HTTPHEADER => $header,
CURLOPT_USERPWD => $credentials,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_FAILONERROR => false,
CURLOPT_HEADER => false,
CURLOPT_POST => true,
CURLOPT_POSTFIELDS => $data
);

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

## Response examples

Example of an ok response

JSON
XML

JSON

```
When the document upload is successful:
{
"code":0,
"message":"Document uploaded",
"user_space":012345,
"type":1
}

When validation failed:
{
"code": 400,
"message": "Validation Failed",
"errors": [
{
"field": "type",
"message": "This value should not be blank."
},
{
"field": "file",
"message": "This value should not be blank."
}
]
}

When the account is not allowed (identity theft):
{
"code": 403,
"message": "This account is not allowed to use this webservice for the user space 012345"
}

When the user space has already been identified:
{
"code": 414,
"message": "User space 012345 already identified"
}

When the document has already been validated or is pending validation:
{
"code": 415,
"message": "A document of this type is already validated or waiting for validation. Please contact [email protected]."
}
```

XML

```

0

012345
1

```

Example of an authentication error response

JSON
XML

JSON

```
{
"code": 401
"message": "Authentication Failed."
}
```

XML

```

401
Authentication Failed.

```

Example of a parameter error response

JSON
XML

JSON

```
{
"code":400,
"message":"Validation Failed",
"errors":[
{
"field":"validity_date",
"message":"This value should not be blank"
}
]
}
```

XML

```

400

```
