from flask import Flask, render_template, request, redirect, send_file, session
import sqlite3
import os
import subprocess
import sys

app = Flask(__name__)

app.secret_key = "ticket_triage_secret_key"

# =========================
# Create Database & Tables
# =========================

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/tickets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    mobile TEXT,
    username TEXT UNIQUE,
    password TEXT
)
""")

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
conn.close()

# =========================
# Login
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database/tickets.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user"] = username

            return redirect("/")

        return "Invalid Username or Password"

    return render_template("login.html")

# =========================
# Register
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        try:

            name = request.form["name"]
            email = request.form["email"]
            mobile = request.form["mobile"]
            username = request.form["username"]
            password = request.form["password"]

            print("===== REGISTER DATA =====")
            print(name)
            print(email)
            print(mobile)
            print(username)
            print(password)

            conn = sqlite3.connect("database/tickets.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (
                    name,
                    email,
                    mobile,
                    username,
                    password
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    mobile,
                    username,
                    password
                )
            )

            conn.commit()

            print("USER INSERTED SUCCESSFULLY")

            conn.close()

            return redirect("/login")

        except Exception as e:

            print("REGISTER ERROR:", e)

            return str(e)

    return render_template("register.html")

# =========================
# Logout
# =========================

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")

# =========================
# Home Page
# =========================

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database/tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM tickets")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Bug'"
    )
    bug_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Feature'"
    )
    feature_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Billing'"
    )
    billing_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Other'"
    )
    other_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        tickets=tickets,
        total=total,
        bug_count=bug_count,
        feature_count=feature_count,
        billing_count=billing_count,
        other_count=other_count
    )

# =========================
# Analyze Uploaded Tickets
# =========================

@app.route("/analyze", methods=["POST"])
def analyze():

    if "user" not in session:
        return redirect("/login")

    files = request.files.getlist("tickets")

    if not files or files[0].filename == "":
        return redirect("/")

    os.makedirs("tickets", exist_ok=True)

    uploaded_files = []

    for file in files:

        if file and file.filename.endswith(".json"):

            filepath = os.path.join(
                "tickets",
                file.filename
            )

            file.save(filepath)

            uploaded_files.append(filepath)

    try:

        for filepath in uploaded_files:

            result = subprocess.run(
                [
                    sys.executable,
                    "agent.py",
                    filepath
                ],
                capture_output=True,
                text=True,
                timeout=180
            )

            print("\n========== AGENT OUTPUT ==========")
            print(result.stdout)

            if result.stderr:
                print("\n========== AGENT ERRORS ==========")
                print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Agent execution timed out")

    except FileNotFoundError:
        print("agent.py not found")

    except Exception as e:
        print(f"Error running agent: {e}")

    return redirect("/")

# =========================
# Download CSV
# =========================

@app.route("/download")
def download():

    if "user" not in session:
        return redirect("/login")

    csv_path = "outputs/results.csv"

    if os.path.exists(csv_path):

        return send_file(
            csv_path,
            as_attachment=True,
            download_name="ticket_analysis_results.csv",
            mimetype="text/csv"
        )

    return "CSV file not found", 404

# =========================
# Clear All Data
# =========================

@app.route("/clear", methods=["POST"])
def clear_tickets():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database/tickets.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tickets")

    conn.commit()
    conn.close()

    if os.path.exists("tickets"):

        for file in os.listdir("tickets"):

            if file.endswith(".json"):

                os.remove(
                    os.path.join(
                        "tickets",
                        file
                    )
                )

    csv_file = "outputs/results.csv"

    if os.path.exists(csv_file):
        os.remove(csv_file)

    return redirect("/")

# =========================
# Run App
# =========================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )

