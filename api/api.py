import flask
from flask import jsonify, request

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

books = [
            {
                'id' : 2,
                'title' : 'Twenty Thousands Leagues'
            },
            {
                'id' : 1,
                'title' : 'Mobby Dick'
            }
        ]
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading</h1><p>First API</p>"

@app.route('/api/v1/resources/books', methods=['GET'])
def api_all():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        #return 'Error'
        return jsonify(books)

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()