import re

def process_email(content):
    sender = re.search(r'From:\s*(.*)', content)
    urgency = "high" if "urgent" in content.lower() else "normal"
    intent = "RFQ" if "quote" in content.lower() else "Unknown"

    return {
        "sender": sender.group(1) if sender else "unknown@example.com",
        "intent": intent,
        "urgency": urgency
    }
 