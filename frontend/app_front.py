from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5001"


@app.route("/", methods=["GET"])
def index():
    response = requests.get(BACKEND_URL + "/api/message")
    raw_msg = response.json().get("message", "")

    # Extract timestamp part from backend
    if "(updated at" in raw_msg:
        parts = raw_msg.split("(updated at")
        message_text = parts[0].strip()
        timestamp = parts[1].replace(")", "").strip()
    else:
        message_text = raw_msg
        timestamp = "No updates yet"

    return render_template("index.html",
                           current_message=message_text,
                           timestamp=timestamp)


@app.route("/update", methods=["POST"])
def update():
    new_message = request.form.get("new_message")
    requests.post(BACKEND_URL + "/api/message", json={"message": new_message})
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)