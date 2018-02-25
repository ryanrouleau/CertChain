from flask import Flask, render_template, request, redirect, url_for, send_file
import ssllib
from zipfile import ZipFile
import json
import requests
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def cert_gen():
    return render_template('certgen.html')

@app.route('/insert', methods=['POST'])
def insertCerts():
    result = request.form

    ca_cert, server_cert, server_private_key = ssllib.generate_certs_and_keys(result.get('country'), result.get('state'), result.get('city'), result.get('commonname'), result.get('org'), result.get('orgunit'))

    cert_name = result.get('commonname') + '.crt'
    with open(cert_name, 'w') as f:
        f.write(server_cert.as_pem())
        f.write(server_private_key.as_pem(None))

    # insert ca_cert into blockchain here
    #  with open("temp.crt", "w") as f:
    #      f.write(ca_cert.as_pem())
    #  with open("temp.crt", "r") as f:
    #      f.read(ca_
    URL = 'http://localhost:30333/'


    curl_url = "curl http://localhost:30333 -H \"Content-Type: application/json\" -X POST -d '{\"jsonrpc\":\"2.0\", \"method\":\"invokefunction\",\"params\":[\"0xa7e87c17332d3e34d43d9ac87340f445c17167a5\", \"put_cert\",[\"" + result.get('commonname') + "\",\"" + ca_cert.as_pem() + "\"]]}'"

    # content = {"jsonrpc":"2.0", "method":"invokefunction","params":["0xa7e87c17332d3e34d43d9ac87340f445c17167a5", "put_cert",[result.get('commonname'), ca_cert.as_pem()]]}

    # r = requests.posts(url = URL, headers="Content-Type: application/json", json=content)

    subprocess.call(curl_url, shell = True)

    return send_file(cert_name, as_attachment=True)
