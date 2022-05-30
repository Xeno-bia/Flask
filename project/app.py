"""
project
├ app.py
├ templates
│　└ index.html
└ static
    └ style.css
"""

from flask import *

app = Flask(__name__)

@app.route("URL末尾")
def メソッド():
    return render_template("HTMLファイル", 変数 = 値)

"""
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = 0 or 1
$ flask run
CTRL + C
"""