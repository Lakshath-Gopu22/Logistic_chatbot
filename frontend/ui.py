import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000/chat"

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Logistics AI Support",
    page_icon="📦",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_order" not in st.session_state:
    st.session_state.selected_order = None

if "order_card" not in st.session_state:
    st.session_state.order_card = None


# ---------- SIDEBAR ----------
st.sidebar.title("📦 Logistics AI Dashboard")

st.sidebar.subheader("Order History")

# Demo orders (replace later with backend call)
order_list = [
    "ORD1001",
    "ORD1002",
    "ORD1003",
    "ORD1004",
    "ORD1005",
    "ORD2001",
    "ORD2002",
    "ORD2003"
]

selected = st.sidebar.selectbox(
    "Select Order",
    order_list,
    index=0
)

st.session_state.selected_order = selected

st.sidebar.subheader("Quick Actions")

col1, col2 = st.sidebar.columns(2)

track_btn = col1.button("Track")
refund_btn = col2.button("Refund")

cancel_btn = col1.button("Cancel")
summary_btn = col2.button("Summary")

clear_btn = st.sidebar.button("Clear Chat")


# ---------- HANDLE BUTTON ACTIONS ----------
def send_message_to_backend(message):

    response = requests.post(
        BACKEND_URL,
        json={"message": message},
        timeout=30
    )

    data = response.json()

    reply = data["reply"]

    if data.get("order"):
        st.session_state.order_card = data["order"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "time": datetime.now().strftime("%H:%M")
    })


if track_btn:
    send_message_to_backend(f"Track {selected}")

if refund_btn:
    send_message_to_backend(f"Refund for {selected}")

if cancel_btn:
    send_message_to_backend(f"Cancel {selected}")

if summary_btn:
    send_message_to_backend(f"Summary {selected}")

if clear_btn:
    st.session_state.messages = []
    st.session_state.order_card = None
    st.rerun()


# ---------- HEADER ----------
st.title("💬 Logistics Customer Support")


# ---------- ORDER CARD ----------
if st.session_state.order_card:

    order = st.session_state.order_card

    status = order.get("status", "Unknown")

    status_color = {
        "Packed": "🟢",
        "In Transit": "🟡",
        "Out for Delivery": "🟠",
        "Delivered": "🔵",
        "Delayed": "🔴",
        "Lost in Transit": "❌",
        "Return Initiated": "🟣"
    }.get(status, "⚪")

    st.markdown(
        f"""
        <div style="
            padding:15px;
            border-radius:10px;
            border:1px solid #ccc;
            background-color:#111;
            margin-bottom:15px;
        ">
        <h4>📦 Order {order.get("order_id")}</h4>
        <p>Status: {status_color} {status}</p>
        <p>ETA: {order.get("eta")}</p>
        <p>City: {order.get("city")}</p>
        <p>Refund: ₹{order.get("refund")}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- CHAT DISPLAY ----------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        st.caption(msg["time"])


# ---------- CHAT INPUT ----------
user_input = st.chat_input("Ask about your order...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": datetime.now().strftime("%H:%M")
    })

    send_message_to_backend(user_input)

    st.rerun()