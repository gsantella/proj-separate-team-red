from flask import Flask
from flask_cors import CORS
from flask import json
from flask import request
app = Flask('app')
cors = CORS(app)
defaultValue = -999

@app.route('/')
def convert():
    # Get Values from get
    IF = request.args.get('F', doNoInputError = defaultValue, type = float)
    IC = request.args.get('C', doNoInputError = defaultValue, type = float)

    #Filler json data
    data = json.jsonify({"return": "Methods Failed to load"})

    #Error checking and method selection
    if (IF == defaultValue and IC == defaultValue): # No inputs
      data = doNoInputError()
    elif (IF == defaultValue and IC != defaultValue): # F inputed
      data = covertCtoF(IC)
    elif (IF != defaultValue and IC == defaultValue): # C inputed
      data = convertFtoC(IF)
    else: # Too many inputs
      data = doTooManyInputError()
    return data

# Not enough Input Error
def doNoInputError():
    return json.jsonify({"return": "No input"})

# Farenheit to Celcius
def convertFtoC(F1):
    C1 = (F1 - 32) * (5 / 9)
    return json.jsonify({"return": C1})

# Celcius to Farenheit
def covertCtoF(C2):
    F2 = (C2 * 9 / 5) + 32
    return json.jsonify({"return": F2})

# Too Many Input Error
def doTooManyInputError():
  return json.jsonify({"return": "Too many input"})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
