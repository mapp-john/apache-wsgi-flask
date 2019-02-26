import yaml
import json
import cgi
import urllib.parse
import sys, os
sys.path.insert(0, "/home/user/flask")
from flask import Flask, request, Response, Request, render_template
from imp import reload


vars_dict={}
vars_dict.update({'name1':'joe', 'name2':'bob'})

app = Flask(__name__)

import hello
# Simple Get/Post page
@app.route('/', methods=['GET','POST'])
def hello_world():
   print(request.method)
   print(request.data)
   print(request.json)
   if request.method == "POST":
       JSON= (str(request.data))
       reload (hello)
       hello.script(JSON)
       #print (request.data)
       response = Response()
       response.status_code= (201)
       response.data = 'TestPost1\nPython3.5\nInstance 1'
       return response
   else:
       return render_template('hello.j2', **vars_dict) #name='joe')


# Start Flask Process
# Not required for WSGI
# but allows you to natively test your app.py
if __name__ == '__main__':
   app.run(debug=True)
#
# Rename App to Application for WSGI
application = app
