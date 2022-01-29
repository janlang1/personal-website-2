import flask
from application import db #db from init.py
from werkzeug.security import generate_password_hash, check_password_hash
#from {file} import {object/var}

class User(db.Document): #this becomes the collection name lower cap
    user_id = db.IntField(unique = True)
    first_name = db.StringField(max_length = 50)
    last_name = db.StringField(max_length = 50)
    email = db.StringField(max_length = 30, unique = True)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)

class Course(db.Document):
    courseID = db.StringField(max_length = 10, unique = True)
    title = db.StringField(max_length = 100)
    description = db.StringField(max_length = 255)
    credits = db.IntField()
    term = db.StringField(max_length = 25)


class Enrollment(db.Document): #many to many relationship
    user_id = db.IntField() #or can use ObjectIdField from mongo that gets created
    courseID = db.StringField(max_length = 10)