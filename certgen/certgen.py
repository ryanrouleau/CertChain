from flask import Flask, render_template, request, redirect, url_for
import ssllib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def cert_gen():
    return render_template('certgen.html')

@app.route('/insert', methods=['POST'])
def insertCerts():
    result = request.form 
    print result
    ca_cert, server_cert, server_private_key = ssllib.generate_certs_and_keys(result.get('country'), result.get('state'), result.get('city'), result.get('commonname'), result.get('org'), result.get('orgunit'))

    with open('cacert.crt', 'w') as f:
        f.write(ca_cert.as_pem())
    with open('cert.crt', 'w') as f:
        f.write(server_cert.as_pem())
        f.write(server_private_key.as_pem(None))

    return redirect(url_for('cert_gen')) 
