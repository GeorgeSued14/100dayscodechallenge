from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    x = "Ip access {}, url: {}".format(request.remote_addr, request.url)
    return x
