import { useState } from "react";

export default function InputBox({ onSend }) {

  const [input, setInput] = useState("");

  function handleSend() {

    if (!input) return;

    onSend(input);

    setInput("");
  }

  return (
    <div className="input-box">

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about your order..."
      />

      <button onClick={handleSend}>
        Send
      </button>

    </div>
  );
}