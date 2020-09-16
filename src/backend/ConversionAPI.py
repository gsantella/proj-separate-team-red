from flask import Flask
from flask_cors import CORS
from flask import json
app = Flask('app')
cors = CORS(app)

@app.route('/FtoC')
def FtoC(F):
  C = (F - 32) * 5/9
  data = {
    "return": C
  }
  return json.jsonify(data)

@app.route('/CtoF')
def CtoF(C):
  F = (C * 9/5) + 32
  data = {
    "return": F
  }
  return json.jsonify(data)