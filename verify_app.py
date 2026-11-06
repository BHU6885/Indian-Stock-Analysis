import urllib.request

url = "http://127.0.0.1:5000/"
with urllib.request.urlopen(url, timeout=10) as response:
    body = response.read(200).decode("utf-8", errors="ignore")
    print(response.status)
    print(body)
