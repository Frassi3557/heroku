import os
import json
import urllib.request
from flask import Flask, render_template
from datetime import datetime
from jinja2 import Template

app = Flask(__name__)

with urllib.request.urlopen('https://apis.is/petrol') as url:
    gogn = json.loads(url.read().decode())

@app.route('/')
def homepage():

    return render_template('index.tpl', gogn=gogn)
    

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)