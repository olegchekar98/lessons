from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    file = '/index.html'
    return render_template(file)


@app.route('/contact/<username>', methods=['GET', 'POST'])
@app.route('/contact/', methods=['GET', 'POST'])
def contact(username = None):
    file = '/contact.html'
    if request.method == 'POST':
        data_dict = {}
        name = request.form['name']
        email = request.form['email']
        text = request.form['text']

        data_dict['name'] = name
        data_dict['email'] = email
        data_dict['text'] = text
        with open('data.json', 'w') as f:
            json.dump(data_dict, f)

    return render_template(file, username = username)

