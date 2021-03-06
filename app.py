import os
import psycopg2 
import sqlite3
import json
import urllib.request
from flask import Flask, render_template, request, session, redirect, url_for, escape
from jinja2 import Template
#from . import app
#from wtforms import EmailPasswordForm

app = Flask(__name__)

#DATABASE_URL = os.environ['DATABASE_URL']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def student():
   return render_template('student.tpl')

#Verkefni 6
@app.route('/6')
def index():
    if 'username' in session:
        return render_template('session.tpl')
    return 'You are not logged in'

@app.route('/6/login' , methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/6/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

#Verkefni 7
@app.route('/7')
def index7():
    if 'username' in session:
        return render_template('session.tpl')
    return 'You are not logged in'

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)  

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True) 