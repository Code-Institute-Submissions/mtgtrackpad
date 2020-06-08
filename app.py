import os
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextField, SubmitField, IntegerField
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import InputRequired, Email, Length
from wtforms.fields.html5 import DateField
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_DBNAMEs")
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEYs")

mongo = PyMongo(app)


class NewEvent(FlaskForm):
    username = StringField('Your Name')
    mtgformat = StringField('Format')
    deckname = StringField('Deck Name')
    date = DateField("Date", format='%Y-%m-%d')


class NewRound(FlaskForm):
    oppname = StringField('Opponent Name')
    oppdeck = StringField('Deck Name')
    roundwins = IntegerField("Games Won")
    rounddraws = IntegerField("Games Drawn")
    roundloss = IntegerField("Games Lost")


@app.route('/new_record', methods=('GET', 'POST'))
def new_record():
    formX = NewEvent()
    formY = NewRound()

    if formX.validate_on_submit():
        return '<h1>The username is {}. The password is {}. Games Won were {}</h1>'.format(formX.username.data, formX.mtgformat.data, formY.roundwins.data)
    return render_template('newrecord.html', formX=formX, formY=formY)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html",
                           records=mongo.db.Player_Records.find().sort("event_date", -1))


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
