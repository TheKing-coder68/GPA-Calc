from __main__ import *
from flask import current_app, Flask,Blueprint, render_template,url_for,redirect, request, flash, session
from argon2 import PasswordHasher
import os, dotenv, re
from flask_pymongo import PyMongo

login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

app = Flask(__name__)
dotenv.load_dotenv()
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', None)
mongo = PyMongo(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)


@login.route('/signup', methods=["POST","GET"])
def signup():
    if request.method=="POST":
        user=mongo.db.User

        first_name=request.form.get("firstName")
        last_name=request.form.get("lastName")
        username= request.form.get("username")
        password= request.form.get("password")
        email= request.form.get("email")

        if not re.search('^[^@ ]+@[^@ ]+\.[^@ .]{2,}$', email):
                flash("That is not a valid email entry, please try again.")  

        user.insert_one({"FirstName":first_name, "LastName":last_name, "Username":username, "Password":password, "Email":email})
        flash("You have signed in.")
        return render_template("signup.html")
    return render_template("signup.html")


