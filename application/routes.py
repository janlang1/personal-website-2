from flask.helpers import url_for
from application import app
from flask import render_template, request,Response, json, redirect, flash, url_for, session

#for mongo atlas
from flask_pymongo import pymongo
#from pymongo.errors import DuplicateKeyError, OperationFailure
import bson
from bson.objectid import ObjectId
from bson.errors import InvalidId

from application import db

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    one_user = db.db.biography.find_one()
    return render_template("index.html", index = True, current_user = one_user)

#test to insert data to the data base
@app.route("/test")
def test():
    return db

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)