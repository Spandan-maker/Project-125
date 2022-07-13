from flask import Flask, jsonify, request
from classifier import prediction

app = Flask(__name__)

@app.route("/test", methods = ["POST"])

def alphabets():
    image = request.files.get("Alphabet")
    predict = prediction(image)

    return jsonify({
        "Prediction": predict
    }), 200

if (__name__ == "__main__"):
    app.run(debug = True)