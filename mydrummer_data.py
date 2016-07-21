from flask import Flask, make_response, request, jsonify, Response
import datetime, json, sys, os
from collections import Counter

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

    
@app.route("/options", methods=["GET", "PUT", "POST"])
def options_route():
    '''
    Methods used to view options, add new option, and replace options.
    '''
    if request.method == "GET":
        options = {"options":option_list()}
        status = 200
    
    resp = Response(
        json.dumps(options, sort_keys=True, indent = 4, separators = (',', ': ')),
        content_type='application/json',
        status=status)
    return resp


def option_list():
    '''
    Get a list of possible options.
    '''
    options = []
    with open(data_file) as f:
        for line in f:
            line = line.rstrip()
            options.append(line)
    return options


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
