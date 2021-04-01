import json


def escreverJSON(arquivo, data):
    with open(f'{arquivo}', 'w') as json_file:
        json.dump(data, json_file)


def lerJSON(arquivo):
    with open(f'{arquivo}', 'r') as json_file:
        return json.load(json_file)
