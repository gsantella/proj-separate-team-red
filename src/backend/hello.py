from flask import Flask
from flask import json
from flask import request
app = Flask('app')

@app.route('/')
def hello():
    return json.jsonify({"return": "Hello"})

@app.route('/howdy')
def world():
    return json.jsonify({"return": "World"})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)