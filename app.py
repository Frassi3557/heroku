import os
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    response = requests.get("https://apis.is/petrol.json")
    print(response.content)



#@app.errorhandler(404)
#def page_not_found(error):
    #return render_template('page_not_found.tpl'), 404

#if __name__ == '__main__':
    #app.run()
    #app.run(debug=True, use_reloader=True)