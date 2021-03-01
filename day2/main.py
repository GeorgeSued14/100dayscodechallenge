from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    x = "Ip access {}, url: {}".format(request.remote_addr, request.url)
    return x
