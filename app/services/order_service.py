import json
from pathlib import Path

DB = Path(__file__).parent.parent / "data" / "orders_db.json"

def get_order(order_id):
    return json.load(open(DB)).get(order_id)
