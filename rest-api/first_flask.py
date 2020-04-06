#!flask/bin/python
from flask import Flask

app = Flask(__name__)
@app.route("/ziyotek", methods=['GET'])
def index():
    return "Hey what's up?!"
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")