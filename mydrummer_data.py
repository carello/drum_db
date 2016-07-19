from flask import Flask, make_response, request, jsonify, Response
#import datetime, json, sys, os
#from collections import Counter

app = Flask(__name__)
data_dir = "./"
data_file = "drummer.txt"

@app.route("/")
def hero_list():
    drummer_list = []
    with open("drummer.txt") as f:
        for line in f:
            line = line.rstrip()
            drummer_list.append(line)
    resp = make_response(jsonify(drummers=drummer_list))
    return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
