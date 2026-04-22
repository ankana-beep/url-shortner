"use client";
import { useState } from "react";
import axios from "axios";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

export default function Home() {
  const [url, setUrl] = useState("");
  const [short, setShort] = useState("");

  const handleSubmit = async () => {
    const res = await axios.post(`${API_BASE_URL}/shorten`, { url });
    setShort(res.data.shortUrl);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>URL Shortener</h1>
      <input value={url} onChange={(e) => setUrl(e.target.value)} />
      <button onClick={handleSubmit}>Shorten</button>
      {short && <p>{short}</p>}
    </div>
  );
}
