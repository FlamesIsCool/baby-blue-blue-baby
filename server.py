from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1444450056282570783/bi3f5VmBUYlOUtxqAtjDpjwIiSOs2qpDQZbhqOwOq9c-oglW3-5YMZ2FWISOBN7pBHd8"

@app.post("/send")
def send():
    data = request.json
    if not data:
        return {"error": "no data"}, 400

    r = requests.post(WEBHOOK_URL, json=data)

    return {"success": r.status_code in (200, 204)}
