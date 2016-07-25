import json
import requests
from flask import Flask, make_response, request, jsonify, Response
import paho.mqtt.client as mqtt


app = Flask(__name__)
data_dir = "./"
data_file = "drummer.txt"

'''
def on_connect(client, userdata, flags, rc):
    client.subscribe("q_list")

def on_message(client, userdata, msg):
        sys.stderr.write("topic: ", msg.topic + '\nMessage: ' + str(msg.payload))
'''

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
    #app.run(debug=True, host='0.0.0.0', port=int('5003'))
    app.run(debug=True, host='0.0.0.0')

'''
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.99.100", 32775, 32774)
    client.loop_forever()
'''




