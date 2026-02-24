import re

def extract_order_id(text):
    match = re.search(r"(ORD\d+)", text.upper())
    return match.group(1) if match else None
