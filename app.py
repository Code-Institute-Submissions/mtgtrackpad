import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import DateField
from forms import new_event_form
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_DBNAMEs")
app.config["MONGO_URI"] = os.environ.get("MONGODB_URIs")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEYs")
app.config['WTF_CSRF_ENABLED'] = True


mongo = PyMongo(app)


# HomePage
@app.route('/player_history')
@app.route('/player_history/')
@app.route('/')
@app.route('/homepage')
def homepage():
    records = mongo.db.Player_Records.find().sort('_id', -1).limit(5)
    return render_template("homepage.html", records=records)


# Player History search, value invoked by JQuery function via input field
@app.route('/player_history/<player_name>', methods=['GET', 'POST'])
def player_history(player_name):
    records = mongo.db.Player_Records.find(
        {"player_name": player_name}).sort('_id', -1)
    # redirect for if input value returns no data
    if records.count() == 0:
        flash('This player does not exist in our data. Please try again.')
        return redirect(url_for('homepage'))
    # if data is found, return to playerhistory page with player's data
    return render_template("playerhistory.html", records=records)


# New record route to record new data
@app.route('/new_record', methods=['GET', 'POST'])
def new_record():
    form = new_event_form()
    newrecord = mongo.db.Player_Records
    if request.method == 'POST':
        if form.validate_on_submit():
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
                # Inputs are JQuery generated. A function is called to calc them into uneditable input fields
                'final_record': request.form.get('eventrecordinput'),
                'gamewin_perc': request.form.get('eventgamewin'),
                'event_status': request.form.get('eventstatusinput')
            }]
            newrecord.insert_many(formdata)
            flash('Event record added!')
            return redirect(url_for('homepage'))
        return render_template('newrecord.html', form=form)

    return render_template('newrecord.html', form=form)


# Edit a record based on _id
@app.route('/edit_record/<record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    form = new_event_form()
    records = mongo.db.Player_Records
    record = mongo.db.Player_Records.find_one({'_id': ObjectId(record_id)})
    if request.method == 'POST':
        if form.validate_on_submit():
            records.update_one({'_id': ObjectId(record_id)},
                               {"$set": {
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
                                   # Jquery function calcs these inputs as uneditable fields
                                   'final_record': request.form.get('eventrecordinput'),
                                   'gamewin_perc': request.form.get('eventgamewin'),
                                   'event_status': request.form.get('eventstatusinput')}})
            flash('Event record has been updated!')
            return redirect(url_for('homepage'))
        return render_template('editrecord.html', record=record, form=form)

    try:
        record = mongo.db.Player_Records.find_one({'_id': ObjectId(record_id)})
        return render_template('editrecord.html', record=record, form=form)
    except Exception:
        flash("Record was not found!", "error")
        return redirect(url_for('homepage'))
    return render_template('editrecord.html', record=record, form=form)


# Deletes a record from the data base
@app.route('/remove_record/<record_id>')
def remove_record(record_id):
    mongo.db.Player_Records.remove({'_id': ObjectId(record_id)})
    flash('Event record has been deleted!')
    return redirect(url_for('homepage'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
