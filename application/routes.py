#from turtle import title
from flask.helpers import url_for
from application import app,db,mail
from flask import render_template, request,Response, json, redirect, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from application.forms import LoginForm, RegisterForm, IndexEditForm, ProjectAddForm,EmailForm
from flask_mail import Message

#for mongo atlas
from flask_pymongo import pymongo

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    form = EmailForm()
    one_user = db.db.biography.find_one({"email": "johnkang03@gmail.com"})
    list_of_projects = list(db.db.projects.find({"user":"johnkang03@gmail.com"}))
    return render_template("index.html", current_user = one_user,list_of_projects=list_of_projects, form = form)

@app.route("/register",  methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #email will already be validated with validate_email function in forms obj
        #increment user id 
        post = {"name": form.first_name.data+" "+form.last_name.data, 
        "password": generate_password_hash(form.password.data), 
        "email": form.email.data}
        post_id = db.db.biography.insert_one(post).inserted_id

        flash("You are successfully registered!", "success")
        return redirect(url_for("index"))
    return render_template("register.html", form=form, title="Register", register = True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        #this is from the request, same as request.form.get('')
        email = form.email.data
        password = form.password.data
        #from database
        user = db.db.biography.find_one({"email": email}) #gets emails with the email from the form, kinda like a query filter
        if user and check_password_hash(user['password'], password):
            flash(f"{user['name']}, Your are successfully logged in!", category="success") #this is sent to request class
            session['user_id'] = str(user['_id'])
            session['username'] = user['name']
            session['email'] = user['email']
            return redirect("/index")
        else:
            flash("Sorry something went wrong.", category="danger") #this is sent to request class
    return render_template("login.html", title = "Login" , form = form, login = True)

@app.route("/logout")
def logout():
    session["user_id"] = False
    session.pop('email',None)
    session.pop('username',None)
    return redirect(url_for("index"))

@app.route("/index/edit", methods=['GET', 'POST'])
def index_edit():
    if session.get('email') != 'johnkang03@gmail.com':
        flash("You are not the owner of this page!",category= "danger")
        redirect(url_for("index"))
    form = IndexEditForm()
    if form.validate_on_submit():
        #this is from the request, same as request.form.get('')
        name = form.name.data
        age = form.age.data
        location = form.location.data
        education = form.education.data
        interests = form.interests.data
        skills = form.skills.data
        #from database
        #collection.update_one(filter, newvalues)
        user = db.db.biography.update_one(
            {"email": "johnkang03@gmail.com"}, 
            {
                "$set": {
                    "name": name,
                    "age": age,
                    "location": location,
                    "education": education,
                    "interests": interests,
                    "skills": skills,
                }
            }
        ) 
        return redirect("/index")

    one_user = db.db.biography.find_one({"email": "johnkang03@gmail.com"})
    form.interests.data = one_user['interests']
    form.skills.data = one_user['skills']
    return render_template("index_edit.html",title="Edit Index Page", current_user = one_user,form=form)

@app.route("/index/project_add", methods=['GET', 'POST'])
def project_add():
    if session.get('email') != 'johnkang03@gmail.com':
        flash("You are not the owner of this page!", category="danger")
        redirect(url_for("index"))
    form = ProjectAddForm()
    if form.validate_on_submit():
        #this is from the request, same as request.form.get('')
        user = form.user.data
        title = form.title.data
        description = form.description.data
        image_url = form.image_url.data
        github_url = form.github_url.data
        index = len(list(db.db.projects.find()))
        db.db.projects.insert_one({
            "user": user,
            "title": title,
            "description": description,
            "image_url": image_url,
            "github_url": github_url,
            "index": index
        })
        return redirect("/index")

    #one_user = db.db.projects.find({"email": "johnkang03@gmail.com"})
    #form.interests.data = one_user['interests']
    #form.skills.data = one_user['skills']
    return render_template("project_add.html",title="Add Project",form=form)

@app.route("/index/project_delete", methods=['GET', 'POST'])
def project_delete():
    if session.get('email') != 'johnkang03@gmail.com':
        flash("You are not the owner of this page!",category= "danger")
        redirect(url_for("index"))
    #could use request.args['index'] if using url_for arguments
    #to use /<int:id? can't use url_for on the html page
    if request.args['index']:
        db.db.projects.delete_one({'index': int(request.args['index'])})
        flash("Project deleted!", category="danger")
    else: 
        flash("No Project Index Found!", category="danger")
    return redirect("/index") #flash doesnt pesist if using url_for (not sure need to double check this claim)

@app.route("/index/email", methods=['GET', 'POST'])
def email():
    print("i hit the email route")
    form = EmailForm()
    if form.validate_on_submit():
        print("submitted email")
        contacter = form.contacter.data
        message = form.message.data
        try:
            msg = Message('email from johnkang.dev', sender = contacter, recipients = ['johnkang03@gmail.com'])
            msg.body = message + ' ' + contacter
            mail.send(msg)
            print(contacter, message, msg)
            return redirect("/index")
        except:
            flash("email did not work!",category= "danger")
    return redirect("/index")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)