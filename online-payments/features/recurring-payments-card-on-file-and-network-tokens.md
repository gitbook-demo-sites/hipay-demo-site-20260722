---
description: "Recurring, One-Click, and Network Tokens - HiPay This functionality is currently being implemented on HiPay's side. Please be aware that we can still "
icon: file-lines
---

# Recurring Payments, Card-on-File, and Network Tokens

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/online-payments/features/recurring-payments-card-on-file-and-network-tokens](https://developer.hipay.com/online-payments/features/recurring-payments-card-on-file-and-network-tokens)
{% endhint %}

Recurring, One-Click, and Network Tokens - HiPay

* This functionality is currently being implemented on HiPay's side. Please be aware that we can still change anything that is presented on this page. This documentation describes the methods for processing Card-on-File (COF) payments: RECURRING (MIT - Merchant Initiated Transactions) and ONE_CLICK (CIT - Customer Initiated Transactions). ## OVERVIEW & CONCEPTS This guide covers the following use cases: Unified Flow (Recommended): How a single CIT can initiate mandates for both RECURRING and ONE_CLICK flows.

* External Recurring Flow: Migrating subscriptions (MIT) initiated by a Payment Service Provider different from HiPay.

* Optimization (Network Tokens): HiPay's automatic optimization of these flows using scheme tokenization.
This feature is still a work in progress. It will be available soon, and the mechanism may change once implemented.

### KEY CONCEPTS & DEFINITIONS

Before implementing these flows, specifically the External Recurring Flow , it is essential to understand the identifiers used to link transactions across the payment network:

Identifier
Definition & Purpose

SRD
(Scheme Reference Data)

The unique identifier assigned by the Card Scheme (e.g., Visa, Mastercard) to the initial transaction.

It serves as a proof of the original cardholder consent and is required to authorize subsequent recurring payments (MIT).

TLID
(Transaction Link IDentifier)

A unique trace identifier generated during the initial transaction.

It ensures the traceability of the transaction chain, linking a subsequent Merchant-Initiated Transaction (MIT) back to the original Customer-Initiated Transaction (CIT) for risk and authentication analysis.

## CASE 1: UNIFIED FLOW (RECURRING + ONE-CLICK)

HiPay simplifies mandate management. Initiating a recurring payment now automatically creates the necessary mandates for both recurring and one-click payments, thereby avoiding a second strong customer authentication.

### PHASE 1: INITIAL TRANSACTION (CIT) - MANDATE CREATION

This is the first payment where the customer provides consent.

* The merchant calls the POST /rest/v1/order endpoint.

* The customer is redirected for Strong Customer Authentication (SCA / 3DS).

* After success, HiPay automatically creates two debit_agreement objects (RECURRING and ONE_CLICK).

* Result: The CVC is deleted for security, and the token is ready for both use cases.

#### REQUIRED PARAMETERS (REQUEST)

The request must contain the parameters for a recurring payment:

Parameter
Value / Description

cardtoken
Token containing the CVC.

eci
7

recurring_payment
1

recurring_info
PSD2 object containing expiration_date and frequency .

### PHASE 2: SUBSEQUENT TRANSACTIONS (MIT & ONE-CLICK)

Thanks to automatic duplication, the merchant can now use the same token for either flow.

#### OPTION A: RECURRING (MIT) PAYMENT

Endpoint: POST /rest/v1/order

Parameter
Value

eci
9

recurring_payment
1

cardtoken
The token generated in Phase 1 (e.g., 28270dc0b... )

#### OPTION B: ONE-CLICK PAYMENT

Endpoint: POST /rest/v1/order

Parameter
Value

eci
7

one_click
1

cardtoken
The token generated in Phase 1 (e.g., 28270dc0b... )

## CASE 2: EXTERNAL RECURRING FLOW (THIRD-PARTY SRD)

This flow allows you to migrate subscriptions (MIT) initiated at another PSP to HiPay.

### STEP 0: OBTAIN A HIPAY TOKEN

You must first tokenize the card data via the POST /rest/v2/token endpoint (ensure you send multi_use: 1 ).

### STEP 1: CREATE THE DEBIT AGREEMENT

Register the external mandate with HiPay using the identifiers retrieved from the previous PSP.

Endpoint: POST /v3/debit-agreement/{payment_product}

Key Parameter
Description

token
The HiPay token generated in Step 0.

cof_type
Must be set to RECURRING .

provider_agreement_ref
Insert the SRD from the initial transaction here.

transaction_link_identifier
Insert the TLID value here.

The API returns a debit_agreement object containing an ID.

### STEP 2: PROCESS THE MIT PAYMENT

Endpoint: POST /rest/v1/order

Key Parameter
Value / Description

debit_agreement_id
The ID returned in Step 1.

recurring_payment
1

eci
9

cardtoken
The payment method token.

## CASE 3: OPTIMIZATION (NETWORK TOKENS)

This feature is still a work in progress. It will be available soon, and the mechanism may change once implemented.

Regardless of the method used (Unified or External), HiPay optimizes your Card-on-File transactions using Network Tokens (NT) .

### BENEFITS

* Higher Authorization Rates: Network Tokens enhance security and trust with issuers.

* Lifecycle Management: Tokens are automatically updated by the banks (e.g., upon card expiration), ensuring subscription continuity without merchant or user intervention.

* Security: Limits the circulation of the actual PAN (Primary Account Number).

### HOW IT WORKS

When you enable the "Network Token" option and initiate a first payment (Case 1 or 2) with multi_use: 1 , HiPay processes the payment with the standard token but asynchronously triggers the generation of a Network Token in the background.

### CONDITIONS FOR USAGE

Using a Network Token for a payment is not automatic and depends on two cumulative conditions:

Condition
Details

1. Merchant Option
You must subscribe to the "Network Token" option.

2. Routing Eligibility
The routing system must be eligible to process Network Tokens.

### PROCESSING LOGIC

For future transactions (MIT or One-Click), if both conditions are met, HiPay will automatically prioritize the Network Token instead of the PAN to process the transaction seamlessly.

This functionality is currently being implemented on HiPay's side. Please be aware that we can still change anything that is presented on this page.
