from flask import Flask,

app = Flask(__name__)


@app.route("/get")
def get_certificate():

    # Retrieve certificate from the blockchain
    domain = request.args.get('domain')

    return 0

@app.route("/put", methods=['POST'])
def put_certificate():

    # Put certificate into the blockchain
    domain = request.args.get('domain')
    file_contents = request.args.get('filecontents')

    return 0

if __name__ == "__main__":

    # Only for debugging while developing

    app.run(host='0.0.0.0', debug=True, port=80)
