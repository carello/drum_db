import json
import requests
from flask import Flask, make_response, request, jsonify, Response


def stevegadd():
    sg = {'stevegadd': readsteve()}
    print type(sg)
    for k,v in sg.items():
        print v
    resp = Response(json.dumps(sg))
    print resp
    return resp



def readsteve():
    s = ""
    with open("drummers/stevegadd.html") as f:
            for l in f:
                l = l.rstrip()
                s += l
    return s

r = stevegadd()
print r

