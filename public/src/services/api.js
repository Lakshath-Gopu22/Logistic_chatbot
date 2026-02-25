const API_BASE = "http://127.0.0.1:8000";

export async function sendMessage(message) {

  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message})
  });

  return await res.json();
}

export async function getOrders() {

  const res = await fetch(`${API_BASE}/orders`);

  return await res.json();
}