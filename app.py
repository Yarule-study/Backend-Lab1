from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"<p>Check my health!</p>", 200

@app.route("/healthcheck")
def healthcheck():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {
        "date": current_time,
        "status": "running"
    }
    return jsonify(response), 200