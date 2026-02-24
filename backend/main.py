from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import ChatBot
from app.services.order_service import get_order

app = FastAPI()

bot = ChatBot()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):

    reply = bot.handle_message(req.message)

    order_id = None

    for word in req.message.split():
        if word.upper().startswith("ORD"):
            order_id = word.upper()

    order_data = None

    if order_id:
        order = get_order(order_id)

        if order:
            order_data = {
                "order_id": order_id,
                "status": order.get("status"),
                "eta": order.get("eta"),
                "refund": order.get("refund_amount"),
                "payment": order.get("payment_mode"),
                "city": order.get("customer_city")
            }

    return {
        "reply": reply,
        "order": order_data
    }