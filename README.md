# Phishing Email Analyzer

A web application that detects potential phishing attempts in emails by analyzing their content for common warning signs. Users can paste suspicious email text, and the app provides a risk score, highlights suspicious elements, and explains its reasoning—making it a valuable educational and security awareness tool.

---

## Table of Contents

- [What is Phishing Email Analyzer?](#what-is-phishing-email-analyzer)
- [How Does It Work?](#how-does-it-work)
- [Features](#features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Installation & Running](#installation--running)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage Guide](#usage-guide)
- [How the Detection Works](#how-the-detection-works)
- [Customization](#customization)
- [Limitations](#limitations)
- [License](#license)

---

## What is Phishing Email Analyzer?

Phishing Email Analyzer is a full-stack web application that helps users identify potential phishing emails. It uses simple natural language processing and pattern matching to flag suspicious language, requests for sensitive information, and risky links.

This project is designed for:

- **Security Awareness & Training**: Demonstrate phishing tactics to users and employees.
- **Education**: Show how basic email analysis works and how phishing can be detected.
- **Personal Use**: Quickly check emails for red flags before acting on them.

---

## How Does It Work?

1. **User Interface**:  
   - Paste the content of a suspicious email into a text box.
   - Click "Analyze Email".
2. **Backend Analysis**:  
   - The backend scans the email for common phishing signs:
     - Urgent or manipulative language
     - Requests for sensitive info (passwords, SSN, credit card)
     - Suspicious or obfuscated links
     - Free webmail sender addresses
   - Each finding increases a "risk score".
3. **Results**:  
   - The app returns a risk score (0–100), a risk level (Low, Medium, High), and highlights all detected issues with explanations.

---

## Features

- **Paste Email Content**: Analyze any email body text (no attachments or headers needed).
- **Risk Scoring**: Get a clear numerical and categorical risk rating.
- **Highlighted Findings**: See which phrases, links, or addresses are suspicious.
- **Explanations**: Learn why each element is considered a red flag.
- **Simple & Fast**: No login or setup required for users.
- **Educational**: Great for classroom demonstrations and security training.

---

## Screenshots

*You can add screenshots here to visually demonstrate the UI and results.*

---

## Project Structure

```
phishing-email-analyzer/
│
├── backend/
│   ├── app.py              # Flask backend for email analysis
│   └── requirements.txt    # Backend dependencies
│
├── frontend/
│   └── src/
│       ├── App.js
│       ├── EmailInput.js
│       └── ResultDisplay.js
│   └── package.json        # Frontend dependencies
│
└── README.md               # This file
```

---

## Installation & Running

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Start the backend server:**
   ```bash
   python app.py
   ```
   The backend will run on [http://localhost:5000](http://localhost:5000).

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the frontend app:**
   ```bash
   npm start
   ```
   The frontend will run on [http://localhost:3000](http://localhost:3000).

---

## Usage Guide

1. **Open the app** in your browser at [http://localhost:3000](http://localhost:3000).
2. **Paste** the content of any suspicious email into the text area.
3. **Click** the "Analyze Email" button.
4. **View Results**:
    - See the overall risk score and risk level.
    - Review a bullet-point list of flagged items, each with a category (e.g., "Suspicious Link", "Urgency/Phishing Language") and the exact text found.

---

## How the Detection Works

The backend uses several simple but effective heuristics:

- **Urgency and Manipulation**: Looks for words like "urgent", "immediately", "verify", "click here", "update your account", etc.
- **Sensitive Info Requests**: Detects phrases such as "password", "SSN", "credit card", "bank account", etc.
- **Suspicious Links**: Finds links in the email and checks for obfuscation (e.g., hexadecimal encoding, "@" in the URL) or mismatched domains.
- **Sender Email**: Flags emails from common free webmail providers (e.g., Gmail, Yahoo) when appearing in "From:" lines.
- **Risk Scoring**: Each finding increases the risk score. The risk level (Low/Medium/High) is based on the total score.

**Note:**  
This is a demonstration project and does not use advanced AI or external blacklists. It's intended for educational use, not as a replacement for enterprise security solutions.

---

## Customization

- **Add More Heuristics**:  
  Edit `backend/app.py` to add new keywords or more complex detection rules.
- **Change Scoring**:  
  Adjust the score increments for each finding in `analyze_email()` to fine-tune the risk level.
- **UI Enhancements**:  
  Modify `frontend/src/ResultDisplay.js` to improve how findings are displayed or to add colors/icons.

---

## Limitations

- Does not parse email headers or attachments.
- Does not check real sender domains or validate link destinations.
- Cannot detect very sophisticated phishing attempts.
- No multi-language support (English only).
- Not intended for production or enterprise use.

---

## License

This project is provided for educational and research purposes only.  
**Do not use for malicious purposes.**

---

**Star this repo if you find it helpful for learning or teaching about phishing awareness!**
