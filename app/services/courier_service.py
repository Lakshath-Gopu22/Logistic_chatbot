import json
from pathlib import Path

DB = Path(__file__).parent.parent / "data" / "courier_db.json"

def get_tracking(tracking_id):
    return json.load(open(DB)).get(tracking_id)
