from flask import Flask
from config import Config
import re

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

@app.route('/color/<string:code>')
def basics(code):
    if not valid_hex(code):
        return f'<div><h1>{color} is not a valid hex color"</h1></div>'

    styling = (
        """<style>
        body, html {
            margin: 0 0 0 0;
            height: 100%;
            width: 100%;
        }
        .color-h1 {
            text-shadow: 0 1px 1px #111111;
            color: #fff;
        }
        .background-div {
        """
        + "background-color: #" + code + ";"
        + """
          height: 100%;
          width: 100%;
        }
        </style>
        """
    )
    color = f'<h1 class="color-h1"><span>#{code}</span></h1>'
    return ("<html>\n"
           + styling
           + "<body\n>"
           f'<div class="background-div">{color}</div>\n'
           "</body\n>"
           "</html>\n"
           )
