import React from "react";

function ResultDisplay({ result }) {
  if (!result) return null;
  if (result.error) return <div style={{ color: "red" }}>{result.error}</div>;

  return (
    <div style={{ marginTop: 24 }}>
      <h2>Analysis Result</h2>
      <p>
        <b>Risk Score:</b> {result.risk_score}/100 <br />
        <b>Risk Level:</b> {result.risk_level}
      </p>
      <h3>Findings:</h3>
      <ul>
        {result.findings.map((f, i) => (
          <li key={i}>
            <b>{f.type}:</b> <span style={{ color: "#b00" }}>{f.text}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ResultDisplay;
