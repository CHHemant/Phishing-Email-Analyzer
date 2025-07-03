import React, { useState } from "react";
import EmailInput from "./EmailInput";
import ResultDisplay from "./ResultDisplay";

function App() {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: 30, maxWidth: 700 }}>
      <h1>Phishing Email Analyzer</h1>
      <EmailInput email={email} setEmail={setEmail} setResult={setResult} />
      <ResultDisplay result={result} />
    </div>
  );
}

export default App;
