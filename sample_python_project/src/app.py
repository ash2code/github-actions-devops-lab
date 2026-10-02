from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "Hello from Flask!"}


@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/add")
def add_numbers():
    a = request.args.get("a")
    b = request.args.get("b")

    try:
        result = int(a) + int(b)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
