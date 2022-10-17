import json

class jsonFile:
    def read_json(filename):
        with open(filename) as file:
            data = json.load(file)
            return data[0]['text']

class config:
    timeout = 10