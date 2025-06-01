from flask import Flask, request, render_template, jsonify, render_template_string
from classifier_agent import classify_input
from json_agent import process_json
from email_agent import process_email
from memory import init_db, log_to_memory
import uuid

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        content = request.form.get("content")

        if content:
            classification = classify_input(content)

            if "error" in classification:
                result = classification
            else:
                format_ = classification["format"]
                intent = classification["intent"]
                thread_id = str(uuid.uuid4())

                # Route to correct agent
                if format_.lower() == "json":
                    try:
                        json_payload = eval(content)  # For testing
                        agent_result = process_json(json_payload)
                    except Exception as e:
                        agent_result = {"error": "Invalid JSON format", "details": str(e)}

                elif format_.lower() == "email":
                    agent_result = process_email(content)
                else:
                    agent_result = {"message": "Unsupported format"}

                log_to_memory("user", format_, intent, agent_result, thread_id)

                result = {
                    "classification": classification,
                    "result": agent_result,
                    "thread_id": thread_id
                }

    return render_template("index.html", result=result)
    
    from flask import render_template_string
import sqlite3
import json

@app.route("/logs")
def view_logs():
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    rows = c.execute("SELECT * FROM logs ORDER BY timestamp DESC").fetchall()
    conn.close()

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Logs</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
        body { background: #f8f9fa; padding: 30px; }
        pre { background: #f1f1f1; padding: 10px; border-radius: 5px; }
      </style>
    </head>
    <body>
      <div class="container">
        <h2>📄 Memory Logs</h2>
        {% for row in rows %}
          <div class="card my-3">
            <div class="card-body">
              <strong>ID:</strong> {{ row[0] }}<br>
              <strong>Source:</strong> {{ row[1] }}<br>
              <strong>Format:</strong> {{ row[2] }}<br>
              <strong>Intent:</strong> {{ row[3] }}<br>
              <strong>Timestamp:</strong> {{ row[4] }}<br>
              <strong>Thread ID:</strong> {{ row[6] }}<br>
              <strong>Values:</strong>
              <pre>{{ row[5] | tojson(indent=2) }}</pre>
            </div>
          </div>
        {% endfor %}
      </div>
    </body>
    </html>
    """
    return render_template_string(html_template, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
