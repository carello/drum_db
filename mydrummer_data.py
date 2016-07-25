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
    sg = {'stevegadd': readsteve()}
    resp = Response(json.dumps(sg))
    return resp

def readsteve():
    s = ""
    with open("drummers/stevegadd.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s


@app.route("/buddyrich")
def buddyrich():
    sg = {'buddyrich': readbuddy()}
    resp = Response(json.dumps(sg))
    return resp

def readbuddy():
    s = ""
    with open("drummers/buddyrich.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s

@app.route("/carterbeauford")
def carterbeauford():
    sg = {'carterbeauford': readcarter()}
    resp = Response(json.dumps(sg))
    return resp

def readcarter():
    s = ""
    with open("drummers/carterbeauford.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s

@app.route("/chetcarello")
def chetcarello():
    sg = {'chetcarello': readchet()}
    resp = Response(json.dumps(sg))
    return resp

def readchet():
    s = ""
    with open("drummers/chetcarello.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s

@app.route("/neipeart")
def neilpeart():
    sg = {'neilpeart': readneil()}
    resp = Response(json.dumps(sg))
    return resp

def readneil():
    s = ""
    with open("drummers/neilpeart.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s


@app.route("/vinniecolaiutra")
def vinniecolaiutra():
    sg = {'vinniecolaiuta': readvinnie()}
    resp = Response(json.dumps(sg))
    return resp

def readvinnie():
    s = ""
    with open("drummers/vinniecolaiutra.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s



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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



