import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

empdb = [
            {
                'id' : 1,
                'Name' : 'Sarvanan S',
                'Designation' : 'Project Manager'
            },
            {
                'id' : 2,
                'Name' : 'Kriss Lobb',
                'Designation': 'Developer'
            }
        ]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Employee Service</h1><p>Welcome</p>"

app.run()
