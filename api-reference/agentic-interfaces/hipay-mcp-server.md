---
description: "The HiPay MCP Server is a Model Context Protocol (MCP) implementation that bridges HiPay's Enterprise APIs with conversational or agentic interfaces. "
icon: file-lines
---

# HiPay MCP Server

{% hint style="info" %}
Imported from the current HiPay WordPress developer portal for the demo migration. Source: [https://developer.hipay.com/agentic-interfaces/hipay-mcp-server](https://developer.hipay.com/agentic-interfaces/hipay-mcp-server)
{% endhint %}

The HiPay MCP Server is a Model Context Protocol (MCP) implementation that bridges HiPay's Enterprise APIs with conversational or agentic interfaces.

It currently enables secure, standardized access to HiPay's transaction management/consultation and payment page creation - all through a single MCP endpoint.

It's available on Github here .

## Features

* Transaction Management - Retrieve, update, or create transactions via HiPay's V1 and V3 APIs

* Payment Processing - Generate hosted payment pages

* Order Management - Fetch all transactions linked to a specific order

* Multi-Environment Support - Compatible with both staging and production

* Secure Authentication - Uses Basic Auth with username/password credentials

* MCP-Compliant - Fully aligned with the Model Context Protocol standard

## Usage

### Command Line

Bash

Bash

```
# Using environment variables

export HIPAY_USERNAME="your_username"

export HIPAY_PASSWORD="your_password"

export HIPAY_ENVIRONMENT="stage"

npx @hipay/mcp-server --tools=transactions.get,transactions.update

# Using command-line arguments

npx @hipay/mcp-server --tools=all --username=your_username --password=your_password --environment=production

# Enable only specific tools

npx @hipay/mcp-server --tools=transactions.get,transactions.update --username=your_username --password=your_password
```

## Available Tools

### Transactions

* transactions.get - Retrieve transaction details by ID (V3 API)

* transactions.getV1 - Retrieve transaction details by ID (V1 API)

* transactions.getByOrder - Retrieve all transactions linked to an order

* transactions.update - Update a transaction (capture, refund, accept, etc.)

### Hosted Payment Pages

* hostedPaymentPages.create - Create a hosted payment page

## Tool Selection

You can enable all or a subset of tools:

Option
Description

-tools=all
Enable every available tool

-tools=transactions.get,transactions.update
Enable specific tools (comma-separated)

(omit -tools)
All tools are enabled by default

## Environment Options

Value
Description

stage
HiPay staging environment (default)

production
HiPay production environment

## Configuration

### Environment Variables

Variable
Description
Required

HIPAY_USERNAME
HiPay API username

HIPAY_PASSWORD
HiPay API password

HIPAY_ENVIRONMENT
stage or production (default: stage )

### Command-Line Arguments

Argument
Description

-tools
Comma-separated list of tools or all

-username
API username (overrides env var)

-password
API password (overrides env var)

-environment
stage or production (default: stage)

## Prerequisites

* Node.js v18+

* npm
