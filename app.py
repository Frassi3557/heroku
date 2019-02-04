import os
import requests
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    resp = requests.get('https://apis.is/petrol')
    print(resp.content)
    

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)