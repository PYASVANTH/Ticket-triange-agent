import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/tickets.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS tickets")

cursor.execute("""
CREATE TABLE tickets(
    ticket_id TEXT PRIMARY KEY,
    thought TEXT,
    action TEXT,
    observation TEXT,
    category TEXT,
    priority TEXT,
    reason TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")