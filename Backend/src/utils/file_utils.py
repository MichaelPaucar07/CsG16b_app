import json

def leer_json(path):
    with open(path, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)