"""
project
    app.py
    templates
        index.html
    static
        style.css
"""

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

"""
> $env:FLASK_APP = "app.py"
> $env:FLASK_DEBUG = 1
> flask run
> CTRL + C
"""