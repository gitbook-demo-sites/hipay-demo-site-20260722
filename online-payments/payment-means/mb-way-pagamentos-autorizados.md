---
description: "This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by MB Way Pagament"
icon: file-lines
---

# MB Way Pagamentos Autorizados

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/payment-means/mb-way-pagamentos-autorizados](https://developer.hipay.com/online-payments/payment-means/mb-way-pagamentos-autorizados)
{% endhint %}

This payment method is currently on a supervised rollout phase. Please contact your Technical Account Manager if you are interested by MB Way Pagamentos Autorizados.

MB Way Mandates Payment Method - HiPay

* This payment method is exclusively dedicated to transactions in Portugal. MB Way allows customers to create a mandate for recurring and one-click payments directly from their mobile phone in a simple and secure way. ## PRESENTATION Brand MB WAY Payment Flow Synchronous & Asynchronous (In-App Approval for Mandate Creation) Integration Debit Agreement API & Order API Product Code mbway Country Portugal (PT) Currency EUR Recurring / One-click Yes Refunds Yes User Timeout 4 minutes (Standard time for the user to approve in the app) MB Way provides a seamless and secure mobile payment experience. For mandates, customers authorize future payments by approving a request in their MB Way app, linking their phone number to the mandate creation. ## ESSENTIAL INFORMATION ### POPULARITY AND AVAILABILITY MB Way is the leading mobile payment solution in Portugal, widely adopted and trusted by Portuguese consumers for both one-off and recurring payments. ### PROCESS The mandate creation process is initiated by the customer entering their phone number. They then receive a notification in the MB Way app to approve the mandate, which authorizes the merchant to initiate future payments. The mandate creation is done regardless of a transaction. ### SECURITY Transactions are highly secure, as the approval happens within the customer's personal MB Way app using their PIN or biometric authentication. The merchant only handles the phone number, not sensitive bank details. ### COMPATIBILITY MB Way is compatible with all major browsers. The customer must have the MB Way app installed on their smartphone. ### CONFIGURATION AND COMPLIANCE Before integration, ensure your HiPay account is configured for Portugal. This method only supports transactions in EUR. The customer's phone number is a mandatory field for this payment method. Minimum and maximum amount for a subsequent transaction are configured at merchant level. These settings are applied to all customers. ### USE CASES Ideal for subscription models, recurring billing, and one-click services targeting a Portuguese customer base. ## INTEGRATION (Mandate Creation) ### INTEGRATION METHODS Method Description Order API Enables direct creation and management of transactions. ### USER EXPERIENCE (Mandate Creation) The customer selects MB Way on the merchant site.

* The customer enters their phone number associated with their MB Way account.

* The customer receives a push notification on their smartphone.

* The customer opens the MB Way app, reviews the mandate details, and authorizes it with their PIN or biometrics.

* The mandate is successfully created. The merchant receives a confirmation via an asynchronous notification (webhook) (see section "Mandate Status Notifications (Webhooks)" below).

* The customer is redirected to the merchant's confirmation page.

* Once the mandate is activated, for all subsequent transactions using this mandate, the customer will not need to confirm the transaction on their app.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS

Parameter
Description / Example

currency
ISO 4217 code. The only accepted currency is the euro. (e.g., EUR)

payment_product_parameters
An object containing specific details required for the MB WAY Mandate cretion.

firstname
Customer's first name associated with their MB WAY account

lastname
Customer's last name associated with their MB WAY account

phone
The mobile phone number linked to the MB WAY account. It must include the country code prefix (e.g., 351# for Portugal) followed by the number

cof_type
Indicates the Mandate type. Use RECURRING to establish a mandate for subsequent recurring payments. Otherwise, use ONE_CLICK

#### ENDPOINTS

Environment
URL

Stage
https://stage-api-gateway.hipay.com/v3/debit-agreement/mbway

Production
https://api-gateway.hipay.com/v3/debit-agreement/mbway

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### MB Way Mandates Sample request

```
curl --location 'https://stage-api-gateway.hipay.com/v3/debit-agreement/mbway' \
--header 'Content-Type: application/json' \
--header 'Authorization:***** \
--data '{
"currency": "EUR",
"payment_product_parameters": {
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678",
"cof_type": "RECURRING"
}
}'
```

## INTEGRATION (Mandate Usage)

### INTEGRATION METHODS

Method
Description

Order API
Enables direct creation and management of transactions.

### USER EXPERIENCE (Mandate Usage - One-click)

* The customer selects MB Way on the merchant site.

* The customer enters their phone number associated with their MB Way mandate.

* The transaction is done without the need for the customer to open their MB Way app. They receive a notification on their phone to attest the success of the transaction.

### USER EXPERIENCE (Mandate Usage - Recurring)

* The merchant initiate the transaction.

* The transaction is done without the need for the customer to open their MB Way app. They receive a notification on their phone to attest the success of the transaction.

### ORDER API INTEGRATION

#### MANDATORY PARAMETERS to create an order

General Parameters
Description / Example

payment_product
mbway

phone
Customer's phone number for MB Way (e.g., 351#912345678)

description
Description of your order. (e.g., Summer sales)

orderid
Unique order ID. (e.g., Order_1232)

currency
ISO 4217 code. The only accepted currency is the euro. (e.g., EUR)

amount
Total order amount. (e.g., 9.99)

Specific Parameters
Description / Example

debit_agreement_id
Unique identifier for the debit agreement

One-click Transaction
eci: 7

one_click: 1

Recurring Transaction

eci: 9

recurring_payment: 1

#### ENDPOINTS

Environment
URL

Stage
https://stage-secure-gateway.hipay-tpp.com/rest/v1/order

Production
https://secure-gateway.hipay-tpp.com/rest/v1/order

NOTE: Ensure that your HiPay account and redirection URLs are correctly configured to guarantee proper integration.

#### MB Way Mandates Sample request - One-click

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencode' \
--header 'Authorization:******' \
--form 'payment_product="mbway"' \
--form 'orderid="1742305004"' \
--form 'description="your description"' \
--form 'amount="55.50"' \
--form 'currency="EUR"' \
--form 'phone="351#912345678"' \
--form 'debit_agreement_id="12182120"' \
--form 'eci="7"' \
--form 'one_click="1"' \
```

#### MB Way Mandates Sample request - Recurring

```
curl --location 'https://stage-secure-gateway.hipay-tpp.com/rest/v1/order' \
--header 'Content-Type: application/x-www-form-urlencode' \
--header 'Authorization:******' \
--form 'payment_product="mbway"' \
--form 'orderid="1742305004"' \
--form 'description="your description"' \
--form 'amount="55.50"' \
--form 'currency="EUR"' \
--form 'phone="351#912345678"' \
--form 'debit_agreement_id="12182120"' \
--form 'eci="9"' \
--form 'recurring="1"' \
```

## INTEGRATION (Actions on mandate)

### Actions by the merchant

#### Cancel a mandate

A merchant can cancel a mandate, for example, when a subscription ends. To do so, they need to call the endpoint DELETE /v3/debit-agreement/{debit_agreement_id}

#### Consult a mandate

A merchant can view a specific mandate. To do so, they need to call the endpoint GET /v3/debit-agreement/{debit_agreement_id}

#### List the mandates

A merchant can view the list of their mandates. To do so, they need to call the endpoint GET /v3/debit-agreements/list

### Actions by the customer

From their application, a customer can suspend, reactivate, modify, or cancel a mandate. To understand how you, as a merchant, can track these changes, please refer to the following section.

## Mandate Status Notifications (Webhooks)

To monitor the status of your Debit Agreements (mandates) in real-time, you must configure your system to receive asynchronous notifications (webhooks). These are essential to know when a mandate is successfully created, suspended, or deleted.

### 1. Configuration

You must provide a callback URL in your HiPay back-office in the svnotif.url field. Our system will send an HTTP POST request to this URL for each event.

Your server must reply with an HTTP 200 OK status code to acknowledge receipt of the notification. Any other response (4xx, 5xx, or a timeout of 3 seconds) will be considered a failure, and HiPay will attempt to send the notification again.

Note: In case of doubt, or to reconcile the status of a mandate after receiving a notification, you can consult its information at any time using the GET /v3/debit-agreement/{debit_agreement_id} endpoint

### 2. Notification Format

You will receive a JSON payload in the body of the POST request.

#### Structure:

```
{
"event_key": "string",
"data": { ... Debit Agreement object ... },
"sent_date": "timestamp:1761734585891"
}
```

* event_key (string): The event identifier ( object.status ).

* data (json): The full Debit Agreement object, identical to a GET API call.

* sent_date (timestamp): The timestamp (UTC) of when the notification was sent.

#### data Object structure

Field
Type
Description

id

Integer

The unique identifier debit_agreement_id of the mandate

status

String

The current status of the mandate. Possible values: pending, available, suspended, terminated

properties

Object

A JSON object containing payment method-specific properties (e.g., phone, firstname, lastname, currency)

cof_type

String

The type of mandate (Context of Use).
Possible values: RECURRING (for subscriptions) or ONE_CLICK (for one-click payments)

date_created

Timestamp ISO 8601

The mandate's creation date (corresponds to creation_date in the database)

date_updated

Timestamp ISO 8601

The mandate's last update date (corresponds to updated_date in the database)

### 3. Events to Listen For ( event_key )

These are the event_key values your system should monitor. Events are triggered by a status change , except for debit_agreement.updated .

* debit_agreement.pending : Sent when the mandate has been authorized by the customer, but is awaiting final processing or bank confirmation before becoming active.

* debit_agreement.available : Sent when the mandate becomes fully active and ready to be used for payments. This can occur directly at creation or after a pending status.

* debit_agreement.suspended : Sent if the mandate is suspended (e.g., by the customer from their bank app).

* debit_agreement.terminated : Sent if the mandate is permanently terminated or deleted.

* debit_agreement.updated : Sent only if a mandate's properties (like phone number) are modified without a change in its status (e.g., status remains available ).

### 4. Notification Examples

#### Example 1: Mandate created as Pending ( debit_agreement.pending )

This is sent just after the customer approves the mandate. The mandate exists but is not yet active.

```
{
"event_key": "debit_agreement.pending",
"data": {
"id": 12182120,
"status": "pending",
"properties": {
"currency": "EUR",
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678"
},
"cof_type": "RECURRING",
"date_created": "2025-10-27T11:05:50+01:00"
},
"sent_date": "1761734585891"
}
```

#### Example 2: Mandate created or becomes Available ( debit_agreement.available )

This is sent when the mandate status changes from pending to available . (Note: For some flows, a mandate might be created directly as available , triggering this notification immediately).

```
{
"event_key": "debit_agreement.available",
"data": {
"id": 12182120,
"status": "available",
"properties": {
"currency": "EUR",
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678"
},
"cof_type": "RECURRING",
"date_created": "2025-10-27T11:05:50+01:00"
},
"sent_date": "1761734585891"
}
```

#### Example 3: Mandate Suspended ( debit_agreement.suspended )

Sent if the customer revokes the mandate from their app. You should stop initiating payments for this mandate

```
{
"event_key": "debit_agreement.suspended",
"data": {
"id": 12182120,
"status": "suspended",
"properties": {
"currency": "EUR",
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678"
},
"cof_type": "RECURRING",
"date_created": "2025-10-27T11:05:50+01:00"
},
"sent_date": "1761734585891"
}
```

#### Example 4: Mandate Terminated ( debit_agreement.terminated )

Sent when the mandate is permanently deactivated.

```
{
"event_key": "debit_agreement.terminated",
"data": {
"id": 12182120,
"status": "terminated",
"properties": {
"currency": "EUR",
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678"
},
"cof_type": "RECURRING",
"date_created": "2025-10-27T11:05:50+01:00"
},
"sent_date": "1761734585891"
}
```

#### Example 5: Mandate Updates - Property Change ( debit_agreement.updated )

This event is sent only if properties change, but the status does not. Here, the phone number is updated while the status remains available .

```
{
"event_key": "debit_agreement.updated",
"data": {
"id": 12182120,
"status": "available",
"properties": {
"currency": "EUR",
"firstname": "Sofia",
"lastname": "COSTA",
"phone": "351#912345678"
},
"cof_type": "RECURRING",
"date_created": "2025-10-27T11:05:50+01:00"
},
"sent_date": "1761734585891"
}
```

### 5. Retry Mechanism

WIP the mechanism may change when implemented.

If our system does not receive an HTTP 200 OK from your server:

* Initial Retries: We will automatically retry 3 times (at 1 minute, 3 minutes, and 5 minutes).

* Delayed Retries: If all 3 attempts fail, a robust delayed-retry mechanism (using a 15-minute Time-To-Live) will re-queue the message for several additional attempts over the next hour before flagging the notification as undeliverable.
