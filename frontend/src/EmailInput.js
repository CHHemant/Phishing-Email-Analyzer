import React, { useState } from "react";

function EmailInput({ email, setEmail, setResult }) {
  const [loading, setLoading] = useState(false);

  const analyzeEmail = async () => {
    setLoading(true);
    setResult(null);
    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const data = await res.json();
      setResult(data);
    } catch (e) {
      setResult({ error: "Failed to analyze email." });
    }
    setLoading(false);
  };

  return (
    <div>
      <textarea
        rows={10}
        cols={70}
        style={{ width: "100%" }}
        value={email}
        onChange={e => setEmail(e.target.value)}
        placeholder="Paste your email content here..."
        disabled={loading}
      />
      <br />
      <button onClick={analyzeEmail} disabled={loading || !email.trim()}>
        Analyze Email
      </button>
      {loading && <span> Analyzing...</span>}
    </div>
  );
}

export default EmailInput;
