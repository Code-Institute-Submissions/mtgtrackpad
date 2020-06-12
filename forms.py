from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class NewEvent(FlaskForm):
    player_name = StringField('Your Name')
    mtgformat = StringField('Format')
    deck_name = StringField('Deck Name')
    event_date = DateField("Date", format='%d-%m-%Y')


class NewRound(FlaskForm):
    event_rounds = IntegerField('Round')
    oppname = StringField('Opponent Name')
    oppdeck = StringField('Deck Name')
    roundwins = IntegerField("Games Won")
    rounddraws = IntegerField("Games Drawn")
    roundloss = IntegerField("Games Lost")
