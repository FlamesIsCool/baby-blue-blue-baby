from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1444450056282570783/bi3f5VmBUYlOUtxqAtjDpjwIiSOs2qpDQZbhqOwOq9c-oglW3-5YMZ2FWISOBN7pBHd8"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    r = requests.post(WEBHOOK_URL, json=data)

    return jsonify({"success": r.status_code in (200, 204)}), r.status_code


# REQUIRED FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5004))
    app.run(host="0.0.0.0", port=port)
