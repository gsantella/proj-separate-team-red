from flask import Flask
from flask_cors import CORS
from flask import json
app = Flask('app')
cors = CORS(app)

def FtoC(F)
  C = (F - 32) × 5/9
  return C
  
def CtoF(C)
  F = (C × 9/5) + 32
  return F

@app.route('/')
def get_data():
  #Test Data
  data = {
    "value": 99,
    "type": "F"
  }
  return json.jsonify(data)