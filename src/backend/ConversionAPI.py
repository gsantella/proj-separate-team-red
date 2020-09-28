from flask import Flask
from flask_cors import CORS
from flask import json
from flask import request
app = Flask('app')
cors = CORS(app)
defaultValue = -999

@app.route('/')
def convert():
    IF = request.args.get('F', default = defaultValue, type = float)
    IC = request.args.get('C', default = defaultValue, type = float)
    data = json.jsonify({"return": "Methods Failed to load"})
    #Error checking and mthod selection
    if (IF == defaultValue and IC == defaultValue):
      data = default()
    elif (IF == defaultValue and IC != defaultValue):
      data = CtoF(IC)
    elif (IF != defaultValue and IC == defaultValue):
      data = FtoC(IF)
    else:
      data = error()
    return data

def default():
    return json.jsonify({"return": "No input"})

def FtoC(F1):
    C1 = (F1 - 32) * (5 / 9)
    return json.jsonify({"return": C1})

def CtoF(C2):
    F2 = (C2 * 9 / 5) + 32
    return json.jsonify({"return": F2})

def error():
  return json.jsonify({"return": "Too many input"})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
