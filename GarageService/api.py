from flask import Flask, jsonify, request, json
from datetime import datetime

app = Flask(__name__)

@app.route("/getStatus", methods = ["GET"])
def getStatus():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route("/postStatus", methods = ["POST"])
def postStatus():
    stat = request.json["status"]
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %I:%M:%S %p")
    status = {"status": stat, "time": time}

    with open('data.txt', 'w') as outfile:
        json.dump(status, outfile)

    return jsonify(status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)

