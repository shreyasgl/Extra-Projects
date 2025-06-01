import openai
import json
import os
from dotenv import load_dotenv
import requests

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def classify_input(content):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a classifier. Identify format (PDF, Email, JSON) and intent (Invoice, RFQ, Complaint, Regulation, etc.)"},
#                 {"role": "user", "content": content}
#             ],
#             functions=[
#                 {
#                     "name": "classify_document",
#                     "parameters": {
#                         "type": "object",
#                         "properties": {
#                             "format": {"type": "string"},
#                             "intent": {"type": "string"}
#                         },
#                         "required": ["format", "intent"]
#                     }
#                 }
#             ],
#             function_call={"name": "classify_document"}
#         )
#         args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
#         return args
#     except Exception as e:
#         return {"error": str(e)}
    

#     import requests
# import json

def classify_input(content):
    try:
        # Ask Ollama to classify the text
        prompt = f"""
You are a classifier AI. The user provides input that may be an email, a JSON string, or text. Your job is to classify the FORMAT and the INTENT.

Respond with JSON like this:
{{
  "format": "Email or JSON or Text",
  "intent": "RFQ, Invoice, Complaint, or Regulation"
}}

Input:
{content}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        raw = response.json()["response"]

        # Try to extract a JSON dict from the text
        try:
            result = json.loads(raw)
        except:
            # Try to extract the first JSON-looking block
            start = raw.find("{")
            end = raw.rfind("}")
            result = json.loads(raw[start:end+1])

        return result

    except Exception as e:
        return {"error": str(e)}

