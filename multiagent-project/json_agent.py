# import json

# def process_json(payload):
#     required_fields = ["name", "amount"]
#     issues = []

#     for field in required_fields:
#         if field not in payload:
#             issues.append(f"Missing field: {field}")

#     reformatted = {
#         "customer_name": payload.get("name"),
#         "total_amount": payload.get("amount")
#     }

#     return {
#         "cleaned_data": reformatted,
#         "anomalies": issues
#     }


import json

def process_json(payload):
    intent = payload.get("intent")  
    issues = []
    reformatted = {}

    intent_schemas = {
        "Invoice": {
            "required": ["name", "amount"],
            "mapping": {"name": "customer_name", "amount": "total_amount"}
        },
        "RFQ": {
            "required": ["name", "item", "quantity"],
            "mapping": {"name": "requester", "item": "requested_item", "quantity": "requested_quantity"}
        },
        "Complaint": {
            "required": ["name", "issue_description"],
            "mapping": {"name": "complainant", "issue_description": "description"}
        }
    }

    if intent not in intent_schemas:
        return {
            "cleaned_data": {},
            "anomalies": [f"Unsupported or missing intent: {intent}"]
        }

    schema = intent_schemas[intent]

    for field in schema["required"]:
        if field not in payload:
            issues.append(f"Missing field: {field}")

    for original_field, new_field in schema["mapping"].items():
        reformatted[new_field] = payload.get(original_field)

    return {
        "cleaned_data": reformatted,
        "anomalies": issues
    }

