from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

DATA_PATH = "/data/message.txt"


def read_message():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            return f.read()
    return ""


def write_message(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"{msg} (updated at {timestamp})"
    with open(DATA_PATH, "w") as f:
        f.write(formatted)


@app.route("/api/message", methods=["GET"])
def get_message():
    message = read_message()
    return jsonify({"message": message})


@app.route("/api/message", methods=["POST"])
def update_message():
    data = request.get_json()
    new_message = data.get("message")
    write_message(new_message)
    return jsonify({"status": "ok"})


# New endpoint for v2
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)