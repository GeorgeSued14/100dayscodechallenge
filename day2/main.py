from datetime import datetime
from flask import Flask, request, render_template
from flask_cors import CORS
import handleFile

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    ip = request.remote_addr
    handleFile.write_ips(ip)
    return render_template('index.html', ip=ip, date=handleFile.format_date_now())


@app.route('/access_clients_ip')
def access_clients_ip():
    return handleFile.list_ips()
