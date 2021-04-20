from __main__ import *
from flask import current_app, Flask, Blueprint, render_template,url_for,redirect, request, flash, session
import os, dotenv, re
from flask_pymongo import PyMongo

home_blueprint = Blueprint("home_blueprint", __name__, static_folder="static", template_folder="templates")

app = Flask(__name__)

@home_blueprint.route("/")
def home():
    return render_template("home.html")