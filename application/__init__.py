from flask import Flask
from config import Config
#from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config) #this calls config.py and sets the attributes 

from application import routes