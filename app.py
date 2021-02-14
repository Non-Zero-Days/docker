from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/motd')
def basic_endpoint():
    with open("motd.txt", 'r') as file:
        return file.read()

@app.route("/setmotd", methods=['POST'])
def setmessageoftheday():
    with open("motd.txt", 'w') as file:
        data = request.json
        file.write(data['motd'])
    return 'Success!'

app.run(host="0.0.0.0")
