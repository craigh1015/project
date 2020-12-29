from flask import Flask
from flask.helpers import make_response
# from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response('{"msg": "Hello, World!"}')
    response.mimetype = 'application/json'
    return response

@app.route('/ping')
def ping():
    response = make_response('{"msg": "pong"}')
    response.mimetype = 'application/json'
    return response

@app.route('/test')
def test():
    response = make_response('{"msg": "passed"}')
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
   app.run(host = '0.0.0.0')

