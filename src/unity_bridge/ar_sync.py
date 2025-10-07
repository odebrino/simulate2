"""
SIMULATE 2 – ar_sync.py
Handles communication between Python (AI) and Unity (AR).
Currently placeholder logic for message passing.
"""

import time
import requests  # Example for HTTP bridge (future use)

def send_to_unity(data):
    """
    Placeholder to simulate sending AI data to Unity.
    """
    print(f"📡 Sending to Unity: {data}")
    time.sleep(0.5)  # simulate latency
    return {"status": "ok", "received": data}
