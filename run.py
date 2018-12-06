#!/usr/bin/python3

from flask import Flask, jsonify
from pymongo import MongoClient
from recursos.users import usuarios

app = Flask(__name__)
app.register_blueprint(usuarios)

@app.route('/')
def index():
    return jsonify({"mensagem": "TDC-POÁ 2018"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
