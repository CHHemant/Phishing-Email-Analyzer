from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Heuristics for phishing detection
PHISHING_KEYWORDS = [
    "urgent", "immediately", "verify", "click here", "update your account",
    "password", "login", "confirm", "security alert", "limited time", "reset"
]

SENSITIVE_REQUESTS = [
    "password", "ssn", "social security", "credit card", "bank account", "login", "verify your identity"
]

def detect_links(text):
    # Simple regex for URLs
    url_regex = r'(https?://[^\s]+)'
    return re.findall(url_regex, text)

def suspicious_link(link):
    # Checks for hex or decimal obfuscation, or mismatched TLDs (very simple)
    if re.search(r'%[0-9a-fA-F]{2}', link):
        return True
    if "@" in link:
        return True
    # Check for known mismatched domains (example)
    if "secure" in link and not link.startswith("https"):
        return True
    return False

def analyze_email(text):
    findings = []
    score = 0

    # Keyword analysis
    for kw in PHISHING_KEYWORDS:
        if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE):
            findings.append({"type": "Urgency/Phishing Language", "text": kw})
            score += 10

    # Sensitive requests
    for kw in SENSITIVE_REQUESTS:
        if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE):
            findings.append({"type": "Sensitive Info Request", "text": kw})
            score += 15

    # Link analysis
    links = detect_links(text)
    for link in links:
        if suspicious_link(link):
            findings.append({"type": "Suspicious Link", "text": link})
            score += 20
        else:
            findings.append({"type": "Link", "text": link})

    # Spoofed sender (very basic, checks for 'From:' with free mailers)
    from_match = re.search(r'from:\s*([^\s]+)', text, re.IGNORECASE)
    if from_match:
        sender = from_match.group(1)
        if any(free in sender for free in ["gmail.com", "yahoo.com", "hotmail.com"]):
            findings.append({"type": "Free Email Sender", "text": sender})
            score += 10

    # Overall
    risk = min(score, 100)
    level = "Low"
    if risk > 70:
        level = "High"
    elif risk > 40:
        level = "Medium"

    return {
        "risk_score": risk,
        "risk_level": level,
        "findings": findings
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    email_text = data.get("email", "")
    result = analyze_email(email_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)
