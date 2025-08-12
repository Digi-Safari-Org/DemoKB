from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    total = data["a"] + data["b"]
    return jsonify({"result": total})


if __name__ == "__main__":
    app.run()
