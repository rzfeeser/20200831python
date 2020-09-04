#!/usr/bin/python3

import json

def jsonreader():
    with open("cmdstoissue.json", "r") as myfile:
        decodeme = myfile.read()
    return json.loads(decodeme)


def test_jsonreader():
    assert len(jsonreader()) == 3


