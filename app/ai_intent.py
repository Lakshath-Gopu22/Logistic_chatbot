import ollama

SYSTEM_PROMPT = """
Classify the intent strictly as:
TRACK_ORDER, CANCEL_ORDER, DELIVERY_ETA,
DELAY, ORDER_SUMMARY, HELP, UNKNOWN.
Reply ONLY with intent name.
"""

def classify_intent_llm(msg):
    res = ollama.chat(
        model="mistral:7b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg}
        ]
    )
    return res["message"]["content"].strip()
