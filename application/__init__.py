from flask import Flask
from config import Config
#from flask_mongoengine import MongoEngine
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object(Config) #this calls config.py and sets the attributes 
mail = Mail(app)

from application import routes