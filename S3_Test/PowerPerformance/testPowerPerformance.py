import os
import json

def testGeneral():

    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.json")

    with open(filePath) as fileStream:
        data = json.load(fileStream)