from flask import (
    Flask,
    request,
)
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.data.decode("ascii")

    url = "https://car-damage-detection1.herokuapp.com/v1/models/car_model:predict"

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
    }

    response = requests.request("POST", url, headers=headers, data=data)

    res_json = response.json()

    return res_json


@app.route("/")
def home():
    return "Running Home at default route."


if __name__ == "__main__":
    app.run()
