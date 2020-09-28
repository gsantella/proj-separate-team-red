from flask import Flask, json
app = Flask(__name__)

@app.route('/api2/howdy')
def howdy():
    return json.jsonify({"Howdy": "World"})

#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def catch_all(path):
#    return json.jsonify({"Hello": "World"})