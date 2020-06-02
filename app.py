import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Project3'
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")

mongo = PyMongo(app)

@app.route('/')
@app.route('/homepage')
def get_hompage():
    return render_template("homepage.html",formats=mongo.db.MtG_Formats.find())

