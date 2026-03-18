# inventory-checks-api

## Project Overview
This project is a simple serverless API for logging inventory checks (cycle counts) and retrieving them later by ID.

In many businesses, inventory checks are often tracked in spreadsheets, paper notes, or chat messages. This can lead to missing records, inconsistent formats, and difficulty finding past checks. This API provides a simple centralized way to store and retrieve inventory check records.

## Real Use Case
This project models an **inventory check log** for business operations.

A team member can create a new inventory check record with:
- item ID
- location
- counted quantity
- note
- counted by

Later, the same record can be retrieved by its unique `check_id`.

## Why It Matters to Business
This matters because a centralized inventory check log can help:
- reduce inventory discrepancies
- save time during audits and re-checks
- improve inventory visibility
- support better replenishment decisions

## AWS Services Used
This project uses 3 core AWS services:

1. **API Gateway**
   - provides the public API endpoint

2. **AWS Lambda**
   - runs the backend logic for POST and GET requests

3. **Amazon DynamoDB**
   - stores inventory check records in a table

## Additional AWS Service Used for Debugging
- **CloudWatch Logs**
  - used to view Lambda execution logs and troubleshoot errors

## API Endpoints

### 1. Create an inventory check
**POST** `/inventory-checks`

Example request body:
```json
{
  "item_id": "SKU-1001",
  "location": "Warehouse A",
  "counted_qty": 25,
  "note": "Initial test count",
  "counted_by": "Shiqi"
}
