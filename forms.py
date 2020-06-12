from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class NewEvent(FlaskForm):
    player_name = StringField('Your Name')
    mtgformat = StringField('Format')
    deck_name = StringField('Deck Name')
    event_date = DateField('Date', format='%d-%m-%Y')
    event_rounds = StringField('Round')
    first_oppname = StringField('Opponent Name')
    first_oppdeck = StringField('Deck Name')
    first_w = IntegerField('Games Won')
    first_d = IntegerField('Games Drawn')
    first_l = IntegerField('Games Lost')
    second_oppname = StringField('Opponent Name')
    second_oppdeck = StringField('Deck Name')
    second_w = IntegerField('Games Won')
    second_d = IntegerField('Games Drawn')
    second_l = IntegerField('Games Lost')
    third_oppname = StringField('Opponent Name')
    third_oppdeck = StringField('Deck Name')
    third_w = IntegerField('Games Won')
    third_d = IntegerField('Games Drawn')
    third_l = IntegerField('Games Lost')
    fourth_oppname = StringField('Opponent Name')
    fourth_oppdeck = StringField('Deck Name')
    fourth_w = IntegerField('Games Won')
    fourth_d = IntegerField('Games Drawn')
    fourth_l = IntegerField('Games Lost')
    fifth_oppname = StringField('Opponent Name')
    fifth_oppdeck = StringField('Deck Name')
    fifth_w = IntegerField('Games Won')
    fifth_d = IntegerField('Games Drawn')
    fifth_l = IntegerField('Games Lost')
