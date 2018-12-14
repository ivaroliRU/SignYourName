from flask import Flask, render_template, request
from data_storage import get_data, insert_data

app = Flask(__name__)
app.debug = True

@app.route('/')
def front_page():
    data = get_data('data.json')
    print(data)
    return render_template("index.html", content=data)

@app.route('/add_msg', methods=['POST'])
def add_msg():
    data = request.get_json()
    insert_data(data, 'data.json')

    return "success!"

if __name__ == '__main__':
    app.run(port=3000)