from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return "DevSecOps Pipeline is Working!"

@app.route("/health")
def health():
	return jsonify(status="UP", service="devsecops-app")

@app.route("/version")
def version():
	return jsonify(version="1.0.0", environment="local")

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000)
