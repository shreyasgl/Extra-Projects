import sqlite3
import json
from datetime import datetime

DB = "memory.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
    "CREATE TABLE IF NOT EXISTS logs ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "source TEXT, "
    "format TEXT, "
    "intent TEXT, "
    "timestamp TEXT, "
    "log_values TEXT, "   # <-- Renamed here
    "thread_id TEXT)"
    )
    conn.commit()
    conn.close()

def log_to_memory(source, format_, intent, values=None, thread_id=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
    'INSERT INTO logs (source, format, intent, timestamp, log_values, thread_id) VALUES (?, ?, ?, ?, ?, ?)',
    (source, format_, intent, datetime.utcnow().isoformat(), json.dumps(values or {}), thread_id)
    )

    conn.commit()
    conn.close()



