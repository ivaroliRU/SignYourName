import json

def get_data(s):
    data = {}

    with open(s, 'r') as f:
        data = json.loads(f.read())
    return data

def insert_data(data, s):
    with open(s, 'r') as f:
        feeds = json.loads(f.read())
    with open(s, mode='w', encoding='utf-8') as f:
        feeds = feeds + [data]
        print(feeds)
        json.dump(feeds, f)
