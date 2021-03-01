from flask import json
from datetime import datetime


def format_date_now():
    return datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")


def write_ips(client_ip):
    file = open('list_client_ip.csv', 'a+')
    captured_at = format_date_now()
    file.write("{}\n".format({"ip": client_ip, "captured_at": captured_at}))
    file.close()


def list_ips():
    with open('list_client_ip.csv', 'r') as file:
        data = file.readlines()
        return json.dumps({"list_ips": data})
