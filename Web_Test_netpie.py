from flask import Flask, request, abort

import requests # pip install requests
import urllib3

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()

#-------------------------------------------------

