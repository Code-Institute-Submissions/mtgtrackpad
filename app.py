import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_DBNAMEs")
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")
mongo = PyMongo(app)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html")


@app.route('/new_record')
def new_record():
    return render_template("newrecord.html")


@app.route('/player_history')
def player_history():
    return render_template("playerhistory.html")


@app.route('/edit_formats')
def edit_formats():
    return render_template("editformats.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
