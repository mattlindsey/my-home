import { useState } from "react";

export default function App() {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function sayHi() {
    setError("");
    try {
      const res = await fetch("/api/hi");
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      const data = await res.json();
      setMessage(data.message);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <main style={{ fontFamily: "system-ui, sans-serif", padding: "2rem" }}>
      <button onClick={sayHi}>Hi</button>
      {message && <p>{message}</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}
    </main>
  );
}
