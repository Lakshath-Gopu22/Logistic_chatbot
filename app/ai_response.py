import ollama

MODEL = "mistral:7b"

def ai_reply(prompt: str) -> str:
    res = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return res["message"]["content"].strip()


def tracking_reply(order_id, tracking, order):
    return ai_reply(f"""
You are a logistics support agent.

Order ID: {order_id}
Current Location: {tracking.get('current_location')}
Status: {tracking.get('status')}
Last Scan: {tracking.get('last_scan')}
Next Hub: {tracking.get('next_hub')}
ETA: {order.get('eta')}

Explain clearly where the order is and what happens next.
""")


def eta_reply(order):
    return ai_reply(f"""
Order ETA: {order.get('eta')}
Customer City: {order.get('customer_city')}

Explain expected delivery time politely.
""")


def delay_reply(tracking):
    return ai_reply(f"""
Order Status: {tracking.get('status')}
Current Location: {tracking.get('current_location')}
Delay Reason: {tracking.get('delay_reason', 'Operational delay')}

Apologize and explain delay. Reassure the customer.
""")


def lost_reply(order_id, order):
    return ai_reply(f"""
Order ID: {order_id}
Order Status: Lost in Transit
Refund Amount: ₹{order.get('refund_amount')}
Payment Mode: {order.get('payment_mode')}

Explain the lost shipment situation and refund process.
""")


def return_reply(order_id, order):
    return ai_reply(f"""
Order ID: {order_id}
Return Status: Initiated
Refund Amount: ₹{order.get('refund_amount')}
Payment Mode: {order.get('payment_mode')}

Explain return handling and refund timeline.
""")


def cancel_reply(order_id, order):
    if not order.get("eligible_for_cancellation"):
        return (
            f"❌ Order {order_id} cannot be cancelled because it is already "
            f"'{order.get('status')}'."
        )

    return ai_reply(f"""
Order ID: {order_id}
Refund Amount: ₹{order.get('refund_amount')}
Cancellation Fee: ₹{order.get('cancellation_fee')}
Payment Mode: {order.get('payment_mode')}

Confirm cancellation and explain refund timeline.
""")


def summary_reply(order_id, order):
    return ai_reply(f"""
Order ID: {order_id}
Status: {order.get('status')}
ETA: {order.get('eta')}
City: {order.get('customer_city')}
Payment Mode: {order.get('payment_mode')}
Order Value: ₹{order.get('order_value')}

Give a short, clear order summary.
""")
def refund_reply(order_id, order):

    refund = order.get("refund_amount", 0)
    payment = order.get("payment_mode")

    if refund == 0:
        return f"No refund is pending for order {order_id}."

    return (
        f"Refund of ₹{refund} for order {order_id} "
        f"will be credited to your {payment} within 3-5 business days."
    )