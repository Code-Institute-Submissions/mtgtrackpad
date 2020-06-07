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
    return render_template("homepage.html",
    records=mongo.db.Player_Records.find().sort("event_date", -1))


@app.route('/new_record')
def new_record():
    return render_template("newrecord.html")


@app.route('/player_history')
def player_history():
    return render_template("playerhistory.html")


@app.route('/add_events')
def add_events():
    return render_template("addevents.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
