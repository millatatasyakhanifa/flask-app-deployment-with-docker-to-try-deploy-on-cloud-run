import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
from flask import Flask, request, jsonify
import urllib.request
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = request.args.get('NAME', "World")
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
