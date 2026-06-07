import sqlite3

conn = sqlite3.connect("database/tickets.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tickets")

rows = cursor.fetchall()

print("\n===== DATABASE RECORDS =====\n")

for row in rows:
    print(row)

print("\nTotal Records:", len(rows))

conn.close()