# 🚀 Ticket Triangle Agent

An AI-powered Support Ticket Classification and Prioritization System built using Python, Flask, React, SQLite, and LLM-based reasoning.

---

# 👥 Team Information

## Team Name

Team 31

## Team Number

31

## Team Members

* YASVANTH P
* YAMUNA SHRI T
* VOMKAR BS

* ## Team Members Resume

* YASVANTH P - [resume](<resumes/yasvanth resume - 23IT062.pdf (1).pdf>)
* YAMUNA SHRI T - [resume](<resumes/Yamuna Shri resume category B.pdf>)
* VOMKAR BS - [resume](<resumes/RESUME (3)  vomkar.pdf>)

---

# 🌐 Deliverable Links

## Live Deployment Link

Currently not deployed.

---

## Demo Video

Demo Link:
https://www.loom.com/share/99d3ccdc5a5a46beabf18580d7b8dc32

---

## GitHub Repository

(https://github.com/PYASVANTH/Ticket-triange-agent/tree/main)
---

# 📌 Project Overview

Ticket Triangle Agent is an AI-powered support ticket automation system that helps organizations automatically classify and prioritize customer support tickets.

The system reduces manual effort by using LLM reasoning and prompt engineering to analyze support tickets and generate intelligent classifications.

The application performs:

* Support Ticket Classification
* Priority Prediction
* AI-Based Reasoning
* JSON Ticket Processing
* CSV Report Generation
* SQLite Database Storage
* Automated Ticket Analysis

---

# ✨ Features

## 🔐 User-Friendly Interface

* Modern React Frontend
* JSON File Upload Support
* Real-Time Classification Results

---

## 📂 Ticket Upload

* Upload Support Ticket JSON Files
* Preview Uploaded Ticket Information
* Automatic Processing

---

## 🤖 AI-Powered Ticket Classification

The system automatically classifies tickets into:

* Bug
* Feature Request
* Billing
* Other

---

## 🚨 Priority Prediction

The system assigns priorities such as:

* P1 – Critical
* P2 – High
* P3 – Medium
* P4 – Low

---

## 🧠 LLM-Based Reasoning

The AI model performs reasoning to:

* Understand issue context
* Analyze business impact
* Determine urgency
* Generate classification explanations

---

## 📜 Structured Output Generation

The application generates structured JSON outputs for reliable automation and storage.

---

## 💾 Data Storage

Stores:

* Ticket Information
* Classification Results
* Priority Details
* AI Reasoning Outputs

using:

* CSV Files
* SQLite Database

---

# 🛠 Technology Stack

| Category             | Technology   |
| -------------------- | ------------ |
| Frontend             | React + Vite |
| Backend              | Flask        |
| Database             | SQLite       |
| AI Model             | LLM API      |
| Programming Language | Python       |
| Styling              | CSS          |
| API Communication    | Axios        |
| Version Control      | GitHub       |

---

# 📁 Project Structure

Ticket-Triangle-Agent/

├── frontend/

│ ├── src/

│ ├── public/

│ └── package.json

│

├── backend/

│ ├── app.py

│ ├── output/

│ ├── database/

│ └── requirements.txt

│

├── tickets/

│

├── .gitignore

└── README.md

---

# 🏗 Architecture Diagram

Frontend (React)

↓

Flask Backend API

↓

LLM Processing Engine

↓

Classification & Reasoning

↓

CSV + SQLite Storage

↓

Results Displayed to User

---

# 🔄 System Workflow

1. User uploads a support ticket JSON file.
2. Frontend sends ticket data to Flask backend.
3. Backend extracts ticket details.
4. LLM processes the ticket using prompt engineering.
5. AI analyzes issue category and urgency.
6. Structured classification output is generated.
7. Results are stored in CSV and SQLite.
8. Classification results are displayed to the user.

---

# 🚀 Setup Instructions

## Clone Repository

(https://github.com/PYASVANTH/Ticket-triange-agent/tree/main)
---

## Navigate to Project Folder

cd Ticket-Triangle-Agent

---

## Frontend Setup

cd frontend

npm install

npm run dev

---

## Backend Setup

cd backend

python -m venv venv

---

## Activate Virtual Environment

### Windows

venv\Scripts\activate

---

## Install Dependencies

pip install flask flask-cors openai python-dotenv pandas

---

## Run Backend

python app.py

---

## Frontend URL

http://localhost:5173

---

## Backend URL

http://127.0.0.1:5000

---

# 📋 Ticket Categories Supported

* Bug
* Feature
* Billing
* Other

---

# 📋 Priority Levels Supported

* P1 – Critical
* P2 – High
* P3 – Medium
* P4 – Low

---

# 🧪 Sample Input Ticket

{
"ticket_id": "T101",
"title": "Refund not received",
"description": "Money deducted but refund still pending."
}

---

# 🧪 Expected Output

{
"category": "Billing",
"priority": "P1",
"reason": "Financial issue affecting customer payment."
}

---

# 🧠 AI Concepts Used

* LLM Reasoning
* Prompt Engineering
* Few-Shot Prompting
* Structured JSON Output
* AI-Based Classification
* Agentic AI Workflow

---

# ⚠ Limitations

* Supports JSON ticket files only
* Uses SQLite for local storage
* Requires internet connection for AI API
* Classification depends on prompt quality

---

# 🔮 Future Enhancements

* Real-Time Ticket Monitoring
* Dashboard Analytics
* Multi-Agent Architecture
* Sentiment Analysis
* Email Integration
* Automatic Ticket Routing
* Cloud Deployment
* Admin Dashboard

---

# 🤖 AI Usage Note

## AI Tools Used

* ChatGPT
* Claude AI
* GitHub Copilot

---

## What AI Helped With

* Frontend Development
* Backend API Development
* Prompt Engineering
* SQLite Integration
* JSON Processing
* Debugging
* UI Improvements
* Documentation

---

## What AI Got Wrong

* Initial UI Alignment Issues
* JSON Parsing Errors
* API Response Formatting Issues
* Frontend Integration Bugs

---

## Human Corrections

* Improved User Interface
* Fixed API Integration
* Refined Prompt Structure
* Added Better Error Handling
* Improved Result Display

---

# 🎥 Project Demonstration Video

Demo Link:

https://www.loom.com/share/99d3ccdc5a5a46beabf18580d7b8dc32

The demonstration video includes:

* Project Overview
* Frontend Demonstration
* JSON Upload
* AI Classification
* Priority Prediction
* CSV Output
* SQLite Database
* Architecture Explanation

---

# ✅ Project Outcome

Ticket Triangle Agent successfully automates support ticket classification and prioritization using AI-powered reasoning, helping organizations reduce manual effort and improve support efficiency.

---

# 👨‍💻 Developed By

Team Number – 31

Project: Ticket Triangle Agent
