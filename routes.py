from flask import request, jsonify
from __main__ import app
from modules.database import db

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'