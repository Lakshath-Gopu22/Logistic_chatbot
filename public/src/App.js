import { useState, useEffect } from "react";

import ChatWindow from "./components/ChatWindow";
import InputBox from "./components/InputBox";
import OrderHistory from "./components/OrderHistory";
import OrderCard from "./components/OrderCard";

import { sendMessage, getOrders } from "./services/api";

import "./App.css";

function App() {

  const [messages, setMessages] = useState([]);

  const [orders, setOrders] = useState([]);

  const [selectedOrder, setSelectedOrder] = useState(null);

  useEffect(() => {

    async function loadOrders() {

      const data = await getOrders();

      setOrders(data.orders);
    }

    loadOrders();

  }, []);

  async function handleSend(text) {

    const userMsg = { role: "user", text };

    setMessages(prev => [...prev, userMsg]);

    const res = await sendMessage(text);

    const botMsg = { role: "bot", text: res.reply };

    setMessages(prev => [...prev, botMsg]);

    if (res.order)
      setSelectedOrder(res.order);
  }

  function handleOrderSelect(orderId) {

    handleSend(`Summary ${orderId}`);
  }

  return (
    <div className="app">

      <OrderHistory
        orders={orders}
        onSelect={handleOrderSelect}
      />

      <div className="main">

        <OrderCard order={selectedOrder} />

        <ChatWindow messages={messages} />

        <InputBox onSend={handleSend} />

      </div>

    </div>
  );
}

export default App;