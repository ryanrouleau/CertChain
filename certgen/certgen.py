from flask import Flask, render_template, request, redirect, url_for, send_file
import ssllib
from zipfile import ZipFile
import json
import urllib2

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
    req = urllib2.urlopen('http://localhost/put?domain=' + result.get('commonname') +
            '&filecontents=' + ca_cert.as_pem()).read()

    return send_file(cert_name, as_attachment=True)
