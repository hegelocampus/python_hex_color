from flask import Flask
from config import Config
import re

app = Flask(__name__)
app.config.from_object(Config)

toots = 'This worked?'

n_file_value = open('value.txt', 'r+')

n = n_file_value.read() if n_file_value.read() else 2

def plus():
    global n
    n = n * 2
    print(f"{n}")
    n_file_value.write(f"{n}")
    return n

def valid_hex(code):
    return re.match(r"^[a-f1-9]{6,6}$", code, re.I) is not None

@app.route('/color/<string:code>')
def basics(code):
    valid = valid_hex(code)
    styling = "" if not valid else f' style="color:#{code}"'
    color = f'<span{styling}>#{code}</span>'
    return f'<h1>{color} is {"a" if valid else "not a"} valid hex color"</h1>'

