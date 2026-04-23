from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Testing Project 2 🚀"

@app.route("/health")
def health():
    return {"status": "ok", "app": "testingapp"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)