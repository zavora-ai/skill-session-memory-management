#!/usr/bin/env python3
"""Check if stored memory is still fresh enough to use."""
import json, sys
from datetime import datetime

def check(data):
    stored_at = data.get("stored_at", "")
    max_age_hours = data.get("max_age_hours", 24)
    if not stored_at:
        return {"fresh": False, "reason": "No timestamp"}
    stored = datetime.fromisoformat(stored_at.replace("Z", "+00:00")).replace(tzinfo=None)
    age_hours = (datetime.now() - stored).total_seconds() / 3600
    return {"fresh": age_hours < max_age_hours, "age_hours": round(age_hours, 1), "max_age_hours": max_age_hours}

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
