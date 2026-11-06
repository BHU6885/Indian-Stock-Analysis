import json
import urllib.request

payload = json.dumps({"stock": "Reliance Industries"}).encode("utf-8")
req = urllib.request.Request(
    "http://127.0.0.1:5000/get_stock_data",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=20) as response:
    data = json.loads(response.read().decode("utf-8"))
    print(response.status)
    print(data["ticker"])
    print(len(data["dates"]), len(data["prices"]))
