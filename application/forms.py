from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
#from application.models import User
from application import db

#class name(INHERITENCE!!!)
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    password_confirm = PasswordField("Password Confirm", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password') ])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        #cahnged from using mongoengine to using pymongo
        user = db.db.biography.find_one({"email": email.data})
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

class IndexEditForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(),Length(min=2,max=55)])
    age = IntegerField("Age", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired(),Length(min=2)])
    education = StringField("Education", validators=[DataRequired(),Length(min=2)])
    interests = TextAreaField("Interests", validators=[DataRequired(),Length(min=2)])
    skills = TextAreaField("Skills", validators=[DataRequired(),Length(min=2)])
    submit = SubmitField("Update")

class ProjectAddForm(FlaskForm):
    user = StringField("User", default='johnkang03@gmail.com')
    title = StringField("Title", validators=[DataRequired(),Length(min=2)])
    description = StringField("Description", validators=[DataRequired(),Length(min=2)])
    image_url = StringField("Image URL", validators=[DataRequired(),Length(min=2)])
    github_url = StringField("Github URL", validators=[DataRequired(),Length(min=2)])
    #index = IntegerField("Index", validators=[DataRequired(),Length(min=2)]) dont need this use .count() and +1 
    submit = SubmitField("Add")

class EmailForm(FlaskForm):
    contacter = StringField("My Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired(),Length(min=2)])
    submit = SubmitField("Send Email")

