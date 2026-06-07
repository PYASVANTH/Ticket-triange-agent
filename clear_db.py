import sqlite3

conn = sqlite3.connect("database/tickets.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM tickets")

conn.commit()

conn.close()

print("Database Cleared Successfully")