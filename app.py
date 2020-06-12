import os
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import DateField
from forms import NewEvent, NewRound
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAMEs")
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEYs")


mongo = PyMongo(app)


@app.route('/new_record', methods=['GET', 'POST'])
def new_record():
    formX = NewEvent()
    formY = NewRound()
    return render_template('newrecord.html', formX=formX, formY=formY)


@app.route('/add_record', methods=['POST'])
def add_record():
    records = mongo.db.Player_Records
    formdata = [{
        'player_name': request.form.get('player_name'),
        'mtgformat': request.form.get('mtgformat'),
        'deck_name': request.form.get('deck_name'),
        'event_date': request.form.get('event_date'),
        'event_rounds': [
            {
                'round': 1,
                'opp_name': request.form.get('oppname'),
                'opp_deck': request.form.get('oppdeck'),
                'game_wins': request.form.get('roundwins'),
                'game_draws': request.form.get('rounddraws'),
                'game_loss': request.form.get('roundloss')
            }
        ]
    }]
    records.insert_many(formdata)
    return redirect(url_for('homepage'))


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html",
                           records=mongo.db.Player_Records.find())


@app.route('/player_history')
def player_history():
    return render_template("playerhistory.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
