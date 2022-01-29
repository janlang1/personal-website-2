from flask import Flask
from flask_pymongo import pymongo
#from application import app
from bson.json_util import dumps
import ssl
import certifi
from secret import PASSWORD


CONNECTION_STRING = "mongodb+srv://johnkang54:"+PASSWORD+"@cluster0.dmkth.mongodb.net/flask_personal_website?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())
db = client['flask_personal_website']
print('db connected')