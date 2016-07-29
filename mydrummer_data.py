import json
import requests
from flask import Flask, make_response, request, jsonify, Response

#Phase 3

app = Flask(__name__)
data_dir = "./"
data_file = "drummer.txt"


@app.route("/options", methods=["GET"])
def options_route():
    if request.method == "GET":
        options = {"options":option_list()}
        status = 200
    resp = Response(
        json.dumps(options, sort_keys=True, indent = 4, separators = (',', ': ')),
        content_type='application/json',
        status=status)
    return resp


def option_list():
    options = []
    with open(data_file) as f:
        for line in f:
            line = line.rstrip()
            options.append(line)
    return options


@app.route("/lookupdrummer", methods=["POST"])
def messit():
    drummer = request.data
    resp = readdrummer(drummer)
    return resp


def readdrummer(drummer):
    s = ""
    with open('drummers/'+ drummer + ".html") as f:
        for l in f:
            l = l.rstrip()
            s += l
    return s


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')




