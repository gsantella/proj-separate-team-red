from flask import Flask
from flask_cors import CORS
from flask import json
app = Flask('app')
cors = CORS(app)

@app.route('/')
def default():
  data = {
    "return": "No input was given"
  }
  return json.jsonify(data)

@app.route('/FtoC')
def FtoC():
  C1 = (70 - 32) * 5/9
  data1 = {
    "return": C1
  }
  return json.jsonify(data1)

@app.route('/CtoF')
def CtoF():
  F2 = (70 * 9/5) + 32
  data2 = {
    "return": F2
  }
  return json.jsonify(data2)

app.run(host='0.0.0.0', port=8080)