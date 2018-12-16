from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from data_storage import *

app = Flask(__name__)
Bootstrap(app)

@app.route('/create_board', methods=['POST'])
def c_board():
    board_data = request.get_json()

    b = create_board(board_data['name'], board_data['about'])
    print("createing a board")
    return json.dumps({'success':True, 'id':b.board_id}), 200, {'ContentType':'application/json'}

@app.route('/')
def front_page():
    data = []
    temp = []
    boards = get_all_data() 
    n = 0
    index = 0

    while index <= len(boards):
        if index < len(boards):
            temp.append(boards[index])
        else:
            temp.append(None)
        index = index + 1
        n = n + 1

        if(n >= 3):
            data.append(temp)
            temp = []
            n = 0
    data.append(temp)

    print(data)
    return render_template("index.html", content=data)

@app.route('/board/<id>')
def board(id):
    board_data = get_data_from_id(id)

    if(board_data == None):
        return redirect("/", code=302)

    data = board_data.board_content

    return render_template("board.html", content=data)

@app.route('/board/<id>/add_msg', methods=['POST'])
def add_msg(id):
    data = request.get_json()
    insert_data(data, 'data/data_'+id+'.json')

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(port=3000, debug = True)