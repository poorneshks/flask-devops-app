from flask import Flask
import logging
import os

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def home():
    return "✅ Flask App deployed using GitHub Actions + OIDC!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/log")
def log():
    logger.info("This is a test log message from /log route")
    return "Log generated", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
