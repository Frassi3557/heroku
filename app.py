import os
import json
import urllib.request
from flask import Flask, render_template, request
from jinja2 import Template
#from . import app
#from wtforms import EmailPasswordForm

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.tpl')

#Verkefni 6
@app.route('/6')
def login():
    return render_template('login.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)  

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True) 