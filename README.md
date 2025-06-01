```markdown
# 🧠 Multi-Agent AI Classification System

A local, open-source-powered AI system that accepts input in **Email**, **JSON**, or **plain text** format, classifies its **format** and **intent**, routes it to the appropriate agent, and logs results in a shared memory database.

Built with **Flask**, **SQLite**, and **open-source LLMs (Ollama + Mistral)** — no OpenAI API key required!

---

## 🚀 Features

✅ Classifies input format: `Email`, `JSON`, or `Text`  
✅ Determines intent: `Invoice`, `RFQ`, `Complaint`, etc.  
✅ Routes input to the correct agent:
- **JSON Agent**: Reformat + validate structured JSON
- **Email Agent**: Extract sender, urgency, intent  
✅ Logs everything in **SQLite** (thread ID, timestamp, source)  
✅ View logs at: `http://localhost:5000/logs`

---

## 🧱 Tech Stack

- 🔹 Python 3.8+
- 🔹 Flask
- 🔹 SQLite (lightweight memory)
- 🔹 Ollama + Mistral LLM (runs locally)
- 🔹 Bootstrap (web UI)
- 🔹 `llama-cpp-python` optional alternative

---

## 🗂️ Folder Structure

```

multi\_agent\_ai/
├── app.py                 # Flask app
├── classifier\_agent.py    # Uses LLM to detect format and intent
├── json\_agent.py          # Processes and validates JSON
├── email\_agent.py         # Extracts info from emails
├── memory.py              # Shared memory (SQLite)
├── templates/
│   └── index.html         # Web interface
├── .env                   # For local secrets
├── requirements.txt
└── README.md

````

---

## 📦 Setup Instructions

### 1. ✅ Install Dependencies

```bash
pip install -r requirements.txt
````

### 2. ✅ Install Ollama & Mistral LLM (Local)

* Download Ollama: [https://ollama.com/download](https://ollama.com/download)
* In terminal:

```bash
ollama run mistral
```

This downloads and runs the `mistral` model locally.

---

### 3. ✅ Run the Flask App

```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Example Inputs

### 📧 Email Input:

```
From: user@company.com
Please send a quote for 200 units. Urgent.
```

### 🧾 JSON Input:

```json
{"intent": "Invoice", "name": "ACME Corp", "amount": 1499.99}
```

---

## 📄 View Logs

Visit: [http://localhost:5000/logs](http://localhost:5000/logs)
All memory logs are stored in `memory.db`

---

## 📌 Future Improvements

* [ ] Add PDF parser and PDF Agent
* [ ] Export logs to CSV/JSON
* [ ] Deploy via Docker or Replit
* [ ] Role-based agent chaining
* [ ] Fine-tune LLM on internal classification needs

---

## 🤝 Contributing

Feel free to fork and submit PRs to improve routing logic, add agent types, or suggest better local models.

---

## 📜 License

MIT License — free for personal and commercial use.

---

## 🙌 Acknowledgments

* [Ollama](https://ollama.com) for local LLM runtime
* [Flask](https://flask.palletsprojects.com/)
* [Mistral](https://huggingface.co/mistralai) for fast open-source LLM

```

---

