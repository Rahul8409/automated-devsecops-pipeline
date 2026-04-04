from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/health")
def health():
	return jsonify(status="healthy")

@app.route("/version")
def version():
	return jsonify(version="1.0.0", environment="local")

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000)
 