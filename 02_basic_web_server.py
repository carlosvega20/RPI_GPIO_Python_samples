#!/usr/bin/python
# Basic Web python server using Flask Framework
# Written in Python 2.7.3 by Carlos Vega

# How to:
# pip install Flask
# python 02_basic_web_server.py

from flask import Flask #Flask framework http://flask.pocoo.org/
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0') #Running on http://localhost:5000
