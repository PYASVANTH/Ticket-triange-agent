import os
import sys
import json
import sqlite3
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

# =========================
# Load API Key
# =========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================
# Check Uploaded File
# =========================

if len(sys.argv) < 2:
    print("No ticket file provided")
    sys.exit(1)

ticket_file = sys.argv[1]

if not os.path.exists(ticket_file):
    print(f"File not found: {ticket_file}")
    sys.exit(1)

# =========================
# Database Connection
# =========================

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/tickets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
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

results = []

# =========================
# Read Ticket
# =========================

with open(ticket_file, "r", encoding="utf-8") as f:
    ticket = json.load(f)

print(f"\nProcessing {ticket['ticket_id']}")

prompt = f"""
You are a Ticket Triage Agent.

Use ReAct reasoning.

Allowed Categories:
* Bug
* Feature
* Billing
* Other

Allowed Priorities:
* P1 (Critical - system down, data loss)
* P2 (High - major feature broken)
* P3 (Medium - minor issue, workaround exists)
* P4 (Low - cosmetic, documentation)

Example:

Ticket:
Website unavailable for all users

Output:
{{
"thought":"Website is unavailable affecting all users",
"action":"Analyze impact and scope",
"observation":"Complete outage affecting 100% of users",
"category":"Bug",
"priority":"P1",
"reason":"Production outage affecting all users"
}}

Classify this ticket.

Title:
{ticket['title']}

Description:
{ticket['description']}

Return ONLY valid JSON.

Format:
{{
"thought":"",
"action":"",
"observation":"",
"category":"",
"priority":"",
"reason":""
}}
"""

try:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response.choices[0].message.content.strip()

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    if start == -1 or end == 0:
        raise Exception("JSON not found")

    response_text = response_text[start:end]

    result = json.loads(response_text)

    print(f"Category : {result.get('category')}")
    print(f"Priority : {result.get('priority')}")

    cursor.execute(
        """
        INSERT OR REPLACE INTO tickets
        (
            ticket_id,
            thought,
            action,
            observation,
            category,
            priority,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ticket["ticket_id"],
            result.get("thought", ""),
            result.get("action", ""),
            result.get("observation", ""),
            result.get("category", ""),
            result.get("priority", ""),
            result.get("reason", "")
        )
    )

    conn.commit()

    results.append({
        "ticket_id": ticket["ticket_id"],
        "thought": result.get("thought", ""),
        "action": result.get("action", ""),
        "observation": result.get("observation", ""),
        "category": result.get("category", ""),
        "priority": result.get("priority", ""),
        "reason": result.get("reason", "")
    })

except Exception as e:

    print(f"Error processing ticket")
    print(str(e))

# =========================
# CSV Export
# =========================

if results:

    os.makedirs("outputs", exist_ok=True)

    df = pd.DataFrame(results)

    csv_file = "outputs/results.csv"

    try:

        if os.path.exists(csv_file):

            df.to_csv(
                csv_file,
                mode="a",
                header=False,
                index=False,
                encoding="utf-8"
            )

        else:

            df.to_csv(
                csv_file,
                index=False,
                encoding="utf-8"
            )

        print("CSV Updated Successfully")

    except PermissionError:
        print("Close results.csv and run again")

    except Exception as e:
        print(e)

conn.close()

print("Project Completed")

