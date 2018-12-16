import json
import re
from board import *
import os

def create_board(name, about):
    id = create_id()
    b = Board(name, id, [], about)

    with open('data/data_'+id+'.json', mode='w', encoding='utf-8') as f:
        ser = b.serialize()
        json.dump(ser, f)
    return b

def insert_data(data, s):
    with open(s, 'r') as f:
        feeds = json.loads(f.read())
    with open(s, mode='w', encoding='utf-8') as f:
        feeds['data'] = feeds['data'] + [data]
        json.dump(feeds, f)

def is_secure(s):
    if re.match(r'^.*(script|link).*', s):
        return False
    else:
        return True

def get_data_from_id(id):
    files = os.listdir('./data')
    
    for f in files:
        if f == 'data_'+id+'.json':
            return create_board_from_file('data/'+f)
    
    return None

def get_all_data():
    files = os.listdir('./data')
    data = []

    for f in files:
        if re.match(r'^.*\.json', f):
            data.append(create_board_from_file('data/'+f))
    
    return data


def create_board_from_file(s):
    with open(s, 'r') as f:
        data = json.loads(f.read())

        name = data['name']
        id = data['id']
        content = data['data']
        about = data['about']

        return Board(name, id, content, about)