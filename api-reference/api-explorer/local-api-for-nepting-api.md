---
description: "Description The Local API for Nepting allows you to trigger in-store payments via the Nepting payment gateway simply by sending a payment request to a"
icon: file-lines
---

# Local API for Nepting - API

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/api-explorer/local-api-for-nepting-api](https://developer.hipay.com/api-explorer/local-api-for-nepting-api)
{% endhint %}

## Description

The Local API for Nepting allows you to trigger in-store payments via the Nepting payment gateway simply by sending a payment request to a specific POS payment terminal located in the same LAN (Local Area Network) .

It has been designed to deal with dead zone scenarios: situations where the POS payment terminal has no or bad Internet access, but a LAN connection shared by the payment initiator (a cash register system installed on a tablet or smartphone).

When the Local API receives a payment request, it then:
- awakes the payment terminal
- waits for the payment processing
- responds to the payment request initiator with the payment information

Please note this documentation introduces the Local API by presenting its requirements and how to implement it (endpoints, request parameters, response parameters, error codes, etc.)
If you are looking for a presentation overview, please check the dedicated page .

## Requirements

Please find below the list of all prerequisites you need to fulfill to be able to use the Local API for Nepting:

REQUIREMENT
DESCRIPTION

POS payment terminal
An Android POS payment terminal (please consult this page to get the list of all the devices that are officially supported) with:
- A working and stable Internet (Wi-Fi) connection
- A fixed IP address
- The last version of the Nepting Android app installed
- The last version of the HiPay POS Android app installed
- The Local API service enabled

## How does it work?

The communication between the request initiator and the POS payment terminal relies on a socket connection. Thus, the payment request initiator need to know the following information to be able to join the POS payment terminal:
- Its IP address
- Its listening port (set in the HiPay app preferences / the default value is 8888)

This API is based on a TLV (Type-Length-Value) notation .
It means all the request and response attributes are sent in the form of one text frame, describing these attributes thanks to:

DESCRIPTION
SIZE
FORMAT

Type
The type (also called tag) of information composing the frame.
ex. the amount, the operation type, the payment result, etc.
2 bytes
Alphabetic (A..Z)

Length
The number of characters used to define the information value.
ex. 012 for an information value of 12 characters
3 bytes
Numeric (0..9)

Value
The value of the information.
ex. ORDER_123456
Variant
Alphanumeric

Notes:
- The length must be > 0
- Except for the protocol information*, which must be the first one in a frame, a tag can be sent in any order
- An information (tag) should appear only once in a frame

* Please check the next sections to discover the available tags .

## Payment request

### Parameters

INFORMATION
DESCRIPTION
M/O
TAG
LENGTH
EXPECTED VALUE
EXAMPLES

Protocol

Protocol version used to send the payment to the POS payment terminal.

/!\ This tag must be the first one

M
CZ
4
CZ0040320
N/A

Cash register identifier
Identifier of the cash register.
M
CJ
12
CJ012999999999999
N/A

Cash register number
Number of the cash register
M
CA
2
CA00201
N/A

Amount
Amount of the transaction to be paid by the customer.
The amount is expressed in the smallest unit of the currency (100 for 1).
M
CB
2-12
N/A
- 0.01: CB0011
- 1.50: CB003150
- 235.70: CB00523570

Operation

Type of transaction to be performed.

Possible values:
0 = Debit
1 = Credit
2 = Debit reversal*

* Debit reversal is not implemented yet

M
CD
1
N/A
- Debit: CD0010
- Credit: CD0011
- Debit reversal*: CD0012

Currency

Base currency used for the transaction.
This three-character currency code must comply with ISO 4217 format .

Possible values:
- 978 = EURO

M
CE
3
N/A
- EUR: CE003978

Force authorization request

Whether the authorization request should be forced or not.

Possible values:
- 0 = Do not force auth request
- 1 = Force auth request

O
BB
1
N/A
- Do not force auth request: BB0010
- Force auth request: BB0011

Merchant transaction identifier
Merchant transaction identifier used to uniquely identify each transaction from every merchant transaction.
O
CF
1-99
N/A
- ORD_20221015_123: CF019ORD_20221015_123456

Customer receipt

Whether the customer receipt should be returned or not.

Possible values:
- 000 = customer ticket NOT returned by the POS payment terminal
- 100 = customer ticket returned by the POS payment terminal

O
CK
3
N/A
- Returned by the POS payment terminal: CK003100
- Not returned by the POS payment terminal: CK003000

Phone number

Customer's phone number.

This information can be used by the HiPay app to prefill the phone number to which the customer receipt will be sent.

O
BH
8-20
N/A
- 0606060606: BH0100606060606

Email address

Customer's email address.

This information can be used by the HiPay app to prefill the email address to which the customer receipt will be sent.

O
BI
6-256
N/A
- [email protected] : [email protected]

Notes:
- M/O means Mandatory / Optional
- Expected value means this exact value must be sent
- If you want to send additional data, you can exploit the CF tag (Merchant transaction identifier), by using the character as a value separator

For example, if you want to send 123456 in addition to ORD_20221015_123 (the merchant transaction identifier), you should send: CF026ORD_20221015_123456123456
Please make sure the merchant transaction identifier is always placed at the left part of the separation character.
Be careful not exceeding the max length of the CF tag.

### Examples

Only mandatory fields

Payment request information

INFORMATION
VALUE

Operation
Debit

Currency
EURO

Amount
123.45

Frame to send

```
CZ0040300CJ012247300123456CA00201CB00512345CD0010CE003978
```

All existing fields

Payment request information

INFORMATION
VALUE

Operation
Credit

Currency
EURO

Amount
67.00

Force authorization request
YES

merchant transaction identifier
2023-05-04-010

Additional data
custom data

Customer receipt
should be returned by the POS payment terminal

Customer's phone number
0606060606

Customer's email address
[email protected]

Frame to send

```
CZ0040300CJ012247300123456CA00201CB0046700CD0011CE003978BB0011CF0262023-05-04-010custom [email protected]
```

## Payment response

### Parameters

INFORMATION
DESCRIPTION
M/O
TAG
LENGTH
EXPECTED VALUE
EXAMPLES

Protocol

Protocol version set in the payment request.

This tag is the first sent by the POS payment terminal

M
CZ
4
CZ0040320
N/A

Cash register identifier
Identifier of the cash register set in the payment request.
M
CJ
12
CJ012999999999999
N/A

Authorization number
Authorization number, in case an authorization was requested before performing the payment.
O
AC
1-10
N/A
- 123456: AC006123456

Operation result

Payment result after the processing of the operation by the POS payment terminal.

Possible values:
- 01 = operation NOT performed
- 10 = operation performed

M
AE
2
N/A
- Success: AE00210
- Failure: AE00201

Operation result - Additional info

Additional information to understand the operation result, only in case the operation was NOT performed.

Possible values:
- 00 = Unknown
- 01 = Authorized transaction
- 02 = Phone call
- 03 = Forcing
- 04 = Refused
- 05 = Forbidden
- 06 = Abandonment
- 07 = Not ended
- 08 = Operation not performed: user input timeout
- 09 = Operation not performed: bad message format
- 10 = Operation not performed: bad selection
- 11 = Operation not performed: acquirer abandonment
- 12 = Operation not performed: unknown operation type
- 13 = Currency not supported

For CB/EMV applications, this field can be supplemented with:
- 2 bytes for the CB2A's field 39 (authorization response)
- 21 bytes for the CB2A's field 44 - BC (message to the transaction initiator)
- 2 bytes for the CB2A's field 55 - DF70 (CB check results performed by the acceptance system)
- 2 bytes for the CB2A's field 58 - FF50 (reason to be not ended)
If some of these fields are not fulfilled, they are filled in with spaces.

O
AF
2-50
N/A
- Refused: AF00207

Cash register number
Number of the cash register set in the payment request.
M
CA
2
CA00201
N/A

Amount

Amount really paid by the customer (authorized amount).
It can be lower than the requested amount.

The amount is expressed in the smallest unit of the currency (100 for 1).

M
CB
2-12
N/A
- 0.01: CB0011
- 1.50: CB003150
- 235.70: CB00523570

Application

Payment application used to process the operation.

Possible values:
- 000 = Indifferent
- 001 = CB (VISA/MASTERCARD) with contact mode
- 002 = American Express with contact mode
- 003 = CB ENSEIGNE (CETELEM instalment payment)
- 004 = CETELEM
- 005 = COFINOGA
- 006 = DINNER'S CLUB
- 007 = PASS
- 008 = FRANFINANCE
- 009 = JCB
- 101 = CB VAD (Payment by entering the CB card numbers)
- 201 = quasi-Cash
- 301 = PLBS (Product Location Goods and Services)
- 401 = OPTALION (Credit Lyonnais instalment payment)
- 501 = Cash-Agence
- 601 = PNF (Credit Mutuel instalment payment)
- 602 = P3F
- 603 = OPTALION
- 604 = Preauto-CM
- 605 = PRCME
- 607 = Paiement-QR (Payment by QR-Code)
- 608 = TOP3-3XCB
- 609 = PNF-HPS
- 701 = PPFCA (Credit Agricole)
- 00A = Banque Accord EMV
- 00B = CB (VISA/MASTERCARD) contactless
- 00C = CHEQUE
- 00D = American Express contactless
- 00E = CONECS with contact mode
- 00F = DCC (Dynamic Currency Conversion)
- 00G = QuickPass
- 00I = CPEI-EMV
- 00S = SOFINCO (private card)
- 00U = UPI (China Union Pay)
- 10E = CONECS contactless
- 30F = PLBS-DCC-GB

M
CC
3
N/A
- CB (VISA/MASTERCARD) with contact mode: CC003001
- CB (VISA/MASTERCARD) contactless: CC00300B

Operation

Type of transaction set in the payment request.

Possible values:
0 = Debit
1 = Credit
2 = Debit reversal*

* Debit reversal is not implemented yet

M
CD
1
N/A
- Debit: CD0010
- Credit: CD0011
- Debit reversal*: CD0012

Currency

Base currency set in the payment request.
This three-character currency code must comply with ISO 4217 format.

Possible values:
- 978 = EURO

M
CE
3
N/A
- EUR: CE003978

Merchant transaction identifier
Merchant transaction identifier set in the payment request.
O
CF
1-32
N/A
- ORD_20221015_123: CF019ORD_20221015_123456

Merchant contract
Merchant contract used to process the payment request.
O
CG
7
N/A
- 1234567: CG0071234567

Customer receipt

The customer receipt, base64 encoded.

It is sent only if both assertions are true:
- The payment succeeded (AE00210) or failed (AE00210)
- The customer receipt was set to be returned by the POS payment terminal in the payment request (CK003100)

It is made up of:
- CK tag: set in the payment request
- AK tag: the customer receipt encoded in base64

O
CK
3
N/A
- Returned by the POS payment terminal: CK003100
- Not returned by the POS payment terminal: CK003000

Notes:
- M/O means Mandatory / Optional.
- Expected value means this exact value will be sent.
- Except for the protocol information, which will be the first one sent in the response frame, the information can be sent in any order
- Additional tags could be sent by the POS payment terminal in the response frame

### Response types

Payment success

Response frame

```
CZ0040320CJ012999999999999CA00201CB00512345CC00300BCD0010CE003978AC006184117AE00210CF0262023-05-04-010custom dataCG0071234567ZT374CK003100AK361ICBDQVJURSBCQU5DQUlSRQogICAgICBTQU5TIENPTlRBQ1QKQTAwMDAwMDAwNDEwMTAKTWFzdGVyQ2FyZApMZSAxOS8xMi8yMDIyIGEgMTM6NTc6MjIKSElQQVkKOTJMRVZBTExPSVMKMTIzNDU2NyAzOTAzMzQyMjUwMDA5NiAzMDAwNAojIyMjIyMjIyMjIyM2MzY4CkQ2QzY5MUUxMkI3MEFDNDAKMDA1IDAwMSAwMDAwMTAgQyBAIApOVU0gQVVUTyA6IDE4NDExNwpNT05UQU5UIDoKICAgICAgICAgMTIzLDQ1IEVVUgpERUJJVAoKVElDS0VUIENMSUVOVApBIENPTlNFUlZFUgo=
```

Description

FRAME ATTRIBUTE
INFORMATION
VALUE

CD0010
Operation
Debit

CE003978
Currency
EURO

CB00512345
Amount
123,45

AE00210
Payment result
success

CG0071234567
Merchant contract
1234567

CC00300B
Payment application
CB (VISA/MASTERCARD) contactless

AC006184117
Authorization number
184117

CF0262023-05-04-010custom data
Merchant transaction identifier
- Merchant transaction identifier: 2023-05-04-010
- Additional data: custom data

AK361ICBDQVJURSBCQU5DQUlSRQogICAgICBTQU5TIENPTlRBQ1QKQTAwMDAwMDAwNDEwMTAKTWFzdGVyQ2FyZApMZSAxOS8xMi8yMDIyIGEgMTM6NTc6MjIKSElQQVkKOTJMRVZBTExPSVMKMTIzNDU2NyAzOTAzMzQyMjUwMDA5NiAzMDAwNAojIyMjIyMjIyMjIyM2MzY4CkQ2QzY5MUUxMkI3MEFDNDAKMDA1IDAwMSAwMDAwMTAgQyBAIApOVU0gQVVUTyA6IDE4NDExNwpNT05UQU5UIDoKICAgICAgICAgMTIzLDQ1IEVVUgpERUJJVAoKVElDS0VUIENMSUVOVApBIENPTlNFUlZFUgo=
Customer receipt

CARTE BANCAIRE
SANS CONTACT
A0000000041010
MasterCard
Le 19/12/2022 a 13:57:22
HIPAY
92LEVALLOIS
1234567 39033422500096 30004
############6368
D6C691E12B70AC40
005 001 000010 C @
NUM AUTO : 184117
MONTANT :
123,45 EUR
DEBIT

TICKET CLIENT
A CONSERVER

Payment failure

Response frame

```
CZ0040320CJ012999999999999CA00201CB00512345CD0010CE003978AC006184118AE00201AF00204CF0262023-05-04-011custom dataZT323CK003100AK309ICBDQVJURSBCQU5DQUlSRQpBMDAwMDAwMDAzMTAxMApWSVNBCkxlIDI2LzA1LzIwMjMgYSAxMjo0ODozMApISVBBWQo5MkxFVkFMTE9JUwpBQkFORE9OIERFQklUCjEyMzQ1NjggMzkwMzM0MjI1MDAwOTYgMzAwMDQKIyMjIyMjIyMjIyMjNjM2OAowMDUgMDAxIDAwMDAxOCBDIApOVU0gQVVUTyA6IDE4NDExOApNT05UQU5UIDoKICAgICAgICAxMjMsNDUgRVVSClRJQ0tFVCBDTElFTlQKQSBDT05TRVJWRVIK
```

Description

FRAME ATTRIBUTE
INFORMATION
VALUE

CD0010
Operation
Debit

CE003978
Currency
EURO

CB00512345
Amount
123,45

AE00201Payment resultfailure

AF00204
Failure reason
payment refused

AC006184118
Authorization number
184118

CF0262023-05-04-011custom data
Merchant transaction identifier
- Merchant transaction identifier: 2023-05-04-011
- Additional data: custom data

AK309ICBDQVJURSBCQU5DQUlSRQpBMDAwMDAwMDAzMTAxMApWSVNBCkxlIDI2LzA1LzIwMjMgYSAxMjo0ODozMApISVBBWQo5MkxFVkFMTE9JUwpBQkFORE9OIERFQklUCjEyMzQ1NjggMzkwMzM0MjI1MDAwOTYgMzAwMDQKIyMjIyMjIyMjIyMjNjM2OAowMDUgMDAxIDAwMDAxOCBDIApOVU0gQVVUTyA6IDE4NDExOApNT05UQU5UIDoKICAgICAgICAxMjMsNDUgRVVSClRJQ0tFVCBDTElFTlQKQSBDT05TRVJWRVIK
Customer receipt

CARTE BANCAIRE
A0000000031010
VISA
Le 26/05/2023 a 12:48:30
HIPAY
92LEVALLOIS
ABANDON DEBIT
1234568 39033422500096 30004
############6368
005 001 000018 C
NUM AUTO : 184118
MONTANT :
123,45 EUR
TICKET CLIENT
A CONSERVER

Rejected request (bad frame format)

Response frame

```
CZ0040320CJ012999999999999AE00201AF00209CA00201CB00512345CD0010CE003978
```

Description

FRAME ATTRIBUTE
INFORMATION
VALUE

CD0010
Operation
Debit

CE003978
Currency
EURO

CB00512345
Amount
123,45

AE00201
Payment result
failure

AF00209
Failure reason
operation not performed: bad message format

## Troubleshooting

I never receive the payment result from the payment terminal

Please make sure you are not waiting for any CR/LF data to be received

The payment terminal always reject my payment requests

Please make sure CR/LF data are sent after the payment request
