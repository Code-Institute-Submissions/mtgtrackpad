import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextField, SubmitField
from wtforms.validators import InputRequired, Email, Length
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

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email(message=("This field requires a valid email address"))])
    body = StringField('Message', validators=[InputRequired(), Length(min=10, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


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


@app.route('/contact_us', methods=('GET', 'POST'))
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return "<p>Got it!</p>"
    return render_template('contactus.html', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
