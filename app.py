import os
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import DateField
from forms import NewEvent
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_DBNAMEs")
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEYs")


mongo = PyMongo(app)


@app.route('/new_record', methods=['GET', 'POST'])
def new_record():
    formX = NewEvent()
    return render_template('newrecord.html', formX=formX)


@app.route('/add_record', methods=['POST'])
def add_record():
    newrecord = mongo.db.Player_Records
    formdata = [{
        'player_name': request.form.get('player_name'),
        'mtgformat': request.form.get('mtgformat'),
        'deck_name': request.form.get('deck_name'),
        'event_date': request.form.get('event_date'),
        'event_rounds': [
            {
                'round': 1,
                'opp_name': request.form.get('first_oppname'),
                'opp_deck': request.form.get('first_oppdeck'),
                'games_won': request.form.get('first_w'),
                'games_drawn': request.form.get('first_d'),
                'games_lost': request.form.get('first_l')
            },
            {
                'round': 2,
                'opp_name': request.form.get('second_oppname'),
                'opp_deck': request.form.get('second_oppdeck'),
                'games_won': request.form.get('second_w'),
                'games_drawn': request.form.get('second_d'),
                'games_lost': request.form.get('second_l')
            },
            {
                'round': 3,
                'opp_name': request.form.get('third_oppname'),
                'opp_deck': request.form.get('third_oppdeck'),
                'games_won': request.form.get('third_w'),
                'games_drawn': request.form.get('third_d'),
                'games_lost': request.form.get('third_l')
            },
            {
                'round': 4,
                'opp_name': request.form.get('fourth_oppname'),
                'opp_deck': request.form.get('fourth_oppdeck'),
                'games_won': request.form.get('fourth_w'),
                'games_drawn': request.form.get('fourth_d'),
                'games_lost': request.form.get('fourth_l')
            },
            {
                'round': 5,
                'opp_name': request.form.get('fifth_oppname'),
                'opp_deck': request.form.get('fifth_oppdeck'),
                'games_won': request.form.get('fifth_w'),
                'games_drawn': request.form.get('fifth_d'),
                'games_lost': request.form.get('fifth_l')
            }
        ],
        'final_record': request.form.get('eventrecordinput'),
        'gamewin_perc': request.form.get('eventgamewin'),
        'event_status': request.form.get('eventstatusinput')
    }]
    newrecord.insert_many(formdata)
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
