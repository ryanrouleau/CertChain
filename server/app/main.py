from flask import Flask

app = Flask(__name__)

DATABASE = 'temp.db'

@app.route("/")
def index():
    return "<h1>You shouldn't be here</h1>"

@app.route("/get")
def get_certificate():
    """
    Retrieve certificate from the blockchain.
    """
    domain = request.args.get('domain')
    return 0

@app.route("/put", methods=['POST'])
def put_certificate():
    """
    Put certificate into the blockchain.
    """
    # DB connections
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    # Extract field values
    domain = request.args.get('domain')
    file_contents = request.args.get('filecontents')
    # Enter into database
    cur.execute("INSERT INTO blockchain (domain, filecontents) VALUES (?,?);", \
            (domain, file_contents))

    conn.commit()
    conn.close()

    return 0

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
