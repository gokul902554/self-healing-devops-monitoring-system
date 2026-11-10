from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Self Healing DevOps Platform",
        "status": "Running",
        "message": "Welcome to DevOps Monitoring Platform"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/info")
def info():
    return jsonify({
        "application": "DevOps Monitoring Platform",
        "version": "1.0",
        "environment": "Development"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)