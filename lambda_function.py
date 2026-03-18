import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("InventoryChecks")

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, default=decimal_default)
    }

def lambda_handler(event, context):
    http_method = event.get("requestContext", {}).get("http", {}).get("method", "")
    raw_path = event.get("rawPath", "")

    # POST /inventory-checks
    if http_method == "POST" and raw_path == "/inventory-checks":
        try:
            body = json.loads(event.get("body") or "{}")

            item = {
                "check_id": str(uuid.uuid4()),
                "item_id": body.get("item_id", ""),
                "location": body.get("location", ""),
                "counted_qty": body.get("counted_qty", 0),
                "note": body.get("note", ""),
                "counted_by": body.get("counted_by", ""),
                "created_at": datetime.utcnow().isoformat()
            }

            table.put_item(Item=item)
            return response(200, item)

        except Exception as e:
            return response(500, {"error": str(e)})

    # GET /inventory-checks/{check_id}
    if http_method == "GET" and raw_path.startswith("/inventory-checks/"):
        try:
            check_id = raw_path.split("/inventory-checks/")[1]

            result = table.get_item(Key={"check_id": check_id})
            item = result.get("Item")

            if not item:
                return response(404, {"message": "Record not found"})

            return response(200, item)

        except Exception as e:
            return response(500, {"error": str(e)})

    return response(404, {"message": "Route not found"})
