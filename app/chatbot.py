from app.intent import detect_intent
from app.utils import extract_order_id
from app.services.order_service import get_order
from app.services.courier_service import get_tracking
from app.ai_response import *

class ChatBot:

    def __init__(self):
        self.order_id = None

    def handle_message(self, message: str):

        order_id = extract_order_id(message)

        if order_id:
            self.order_id = order_id

        intent = detect_intent(message)

        # HELP
        if intent == "HELP":
            return (
                "I can help you with:\n"
                "• Track order\n"
                "• Refund status\n"
                "• Cancel order\n"
                "• Delivery ETA\n"
                "• Delay explanation\n"
                "• Order summary\n\n"
                "Please provide your Order ID (example: ORD1002)"
            )

        # ORDER ID required for most things
        if not self.order_id:

            if intent == "REFUND_STATUS":
                return (
                    "Please provide your Order ID to check refund status.\n"
                    "Example: Refund for ORD1002"
                )

            return (
                "Please provide your Order ID so I can help.\n"
                "Example: Where is ORD1002?"
            )

        order = get_order(self.order_id)

        if not order:
            return "Order not found. Please check your Order ID."

        tracking = get_tracking(order["tracking_id"])

        status = tracking.get("status")

        if status == "Lost in Transit":
            return lost_reply(self.order_id, order)

        if status == "Return Initiated":
            return return_reply(self.order_id, order)

        if intent == "TRACK_ORDER":
            return tracking_reply(self.order_id, tracking, order)

        if intent == "REFUND_STATUS":
            return refund_reply(self.order_id, order)

        if intent == "CANCEL_ORDER":
            return cancel_reply(self.order_id, order)

        if intent == "DELIVERY_ETA":
            return eta_reply(order)

        if intent == "DELAY":
            return delay_reply(tracking)

        if intent == "ORDER_SUMMARY":
            return summary_reply(self.order_id, order)

        return (
            "I'm not sure. Try asking:\n"
            "• Where is ORD1002?\n"
            "• Refund for ORD1002\n"
            "• Cancel ORD1002"
        )