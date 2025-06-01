from classifier_agent import classify_input
from json_agent import process_json
from email_agent import process_email
from memory import log_to_memory
import uuid

def route_input(content):
    classification = classify_input(content)
    if 'error' in classification:
        return classification

    format_ = classification["format"]
    intent = classification["intent"]
    thread_id = str(uuid.uuid4())

    if format_.lower() == "json":
        try:
            json_payload = eval(content)  # For testing only. Use `json.loads` in production!
            result = process_json(json_payload)
        except:
            result = {"error": "Invalid JSON format"}
    elif format_.lower() == "email":
        result = process_email(content)
    else:
        result = {"message": "Unsupported format"}

    log_to_memory(source="user", format_=format_, intent=intent, values=result, thread_id=thread_id)
    return {
        "classification": classification,
        "result": result,
        "thread_id": thread_id
    }
