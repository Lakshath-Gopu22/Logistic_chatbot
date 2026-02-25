from app.ai_intent import classify_intent_llm

def detect_intent(msg: str):

    text = msg.lower()

    if any(w in text for w in ["track", "where", "status", "location"]):
        return "TRACK_ORDER"

    if any(w in text for w in ["cancel", "cancellation"]):
        return "CANCEL_ORDER"

    if any(w in text for w in ["refund", "money back"]):
        return "REFUND_STATUS"

    if any(w in text for w in ["eta", "when arrive", "delivery time"]):
        return "DELIVERY_ETA"

    if any(w in text for w in ["delay", "late"]):
        return "DELAY"

    if any(w in text for w in ["summary", "details", "info"]):
        return "ORDER_SUMMARY"

    if any(w in text for w in ["help", "what can you do"]):
        return "HELP"

    return classify_intent_llm(msg)