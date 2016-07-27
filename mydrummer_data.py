import json
import requests
from flask import Flask, make_response, request, jsonify, Response

app = Flask(__name__)
data_dir = "./"
data_file = "drummer.txt"


@app.route("/drummer_list")
def drummer_list():
    drummer_list = []
    with open("drummer.txt") as f:
        for line in f:
            line = line.rstrip()
            drummer_list.append(line)
    resp = make_response(jsonify(drummers=drummer_list))
    return resp

@app.route("/stevegadd")
def stevegadd():
    sg = {'stevegadd': readdrummer("stevegadd")}
    resp = Response(json.dumps(sg))
    return resp


@app.route("/buddyrich")
def buddyrich():
    sg = {'buddyrich': readdrummer("buddyrich")}
    resp = Response(json.dumps(sg))
    return resp


@app.route("/carterbeauford")
def carterbeauford():
    sg = {'carterbeauford': readdrummer("carterbeauford")}
    resp = Response(json.dumps(sg))
    return resp


@app.route("/chetcarello")
def chetcarello():
    sg = {'chetcarello': readdrummer("chetcarello")}
    resp = Response(json.dumps(sg))
    return resp


@app.route("/neilpeart")
def neilpeart():
    sg = {'neilpeart': readdrummer("neilpeart")}
    resp = Response(json.dumps(sg))
    return resp


@app.route("/vinniecolaiuta")
def vinniecolaiutra():
    sg = {'vinniecolaiuta': readdrummer("vinniecolaiuta")}
    resp = Response(json.dumps(sg))
    return resp


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


def readdrummer(drummer):
    s = ""
    with open('drummers/'+ drummer + ".html") as f:
        for l in f:
            l = l.rstrip()
            s += l
    return s




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("5003"))




