#!/usr/bin/python3

import json

def jsonreader():
    with open("cmdstoissue.json", "r") as myfile:
        decodeme = myfile.read()
    return json.loads(decodeme)
