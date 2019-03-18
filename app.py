import os
import json
import urllib.request
from flask import Flask, render_template, request, session, redirect, url_for, escape
from jinja2 import Template
#from . import app
#from wtforms import EmailPasswordForm

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def student():
   return render_template('student.tpl')

#Verkefni 6
@app.route('/6')
def login():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/6/login' , methods = ['GET', 'POST'])
def user():
    return render_template('session.tpl')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)  

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True) 