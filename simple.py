from flask import Flask, render_template, redirect
from config import Config
import re

from simple_form import SampleForm

app = Flask(__name__)
app.config.from_object(Config)

n_file_value = open('value.txt', 'r+')

n = n_file_value.read() if n_file_value.read() else ""

def plus():
    global n
    n = n * 2
    print(f"{n}")
    n_file_value.write(f"{n}")
    return n

def valid_hex(code):
    return re.match(r"^[a-f\d]{6,6}|[a-f\d]{3,3}$", code, re.I) is not None

@app.route('/')
def root():
    return f'<h1>Root</h1>'

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('form.html', form=form)


@app.route('/<string:color>')
def root_color(color):
    return redirect(f'/color/{color}')

@app.route('/color/<string:code>')
def basics(code):
    if not valid_hex(code):
        return f'<div><h1>{code} is not a valid hex color</h1></div>'

    color_code = '#' + code
    return render_template('index.html', color=color_code)

