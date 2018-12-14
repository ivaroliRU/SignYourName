import json

def get_data(s):
    data = {}

    with open(s, 'r') as f:
        data = json.loads(f.read())
    return data