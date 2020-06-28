from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Optional, length, AnyOf


class new_event_form(FlaskForm):

    player_name = StringField('Your Name', validators=[InputRequired(),
                              length(max=20,
                              message='Please enter a player name with 20 or fewer characters.'
                              )])
    mtgformat = StringField('Format', validators=[InputRequired()])
    deck_name = StringField('Deck Name', validators=[InputRequired(),
                            length(max=20,
                            message='Please enter a deck name with 20 or fewer characters.'
                            )])
    event_date = DateField('Date', validators=[InputRequired()])
    event_rounds = IntegerField('Round')
    first_oppname = StringField('Opponent Name',
                                validators=[InputRequired(),
                                length(max=20,
                                message='Please enter a player name with 20 or fewer characters.'
                                )])
    first_oppdeck = StringField('Deck Name',
                                validators=[InputRequired()])
    first_w = IntegerField('Games Won', validators=[InputRequired(),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    first_d = IntegerField('Games Drawn',
                           validators=[Optional(strip_whitespace=True)])
    first_l = IntegerField('Games Lost', validators=[InputRequired(),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    second_oppname = StringField('Opponent Name',
                                 validators=[length(max=20,
                                 message='Please enter a player name with 20 or fewer characters.'
                                 )])
    second_oppdeck = StringField('Deck Name',
                                 validators=[length(max=20,
                                 message='Please enter a deck name with 20 or fewer characters.'
                                 )])
    second_w = IntegerField('Games Won',
                            validators=[Optional(strip_whitespace=True),
                            AnyOf(values=[0, 1, 2],
                            message='Please input number 0, 1 or 2')])
    second_d = IntegerField('Games Drawn',
                            validators=[Optional(strip_whitespace=True)])
    second_l = IntegerField('Games Lost',
                            validators=[Optional(strip_whitespace=True),
                            AnyOf(values=[0, 1, 2],
                            message='Please input number 0, 1 or 2')])
    third_oppname = StringField('Opponent Name',
                                validators=[length(max=20,
                                message='Please enter a player name with 20 or fewer characters.'
                                )])
    third_oppdeck = StringField('Deck Name', validators=[length(max=20,
                                message='Please enter a deck name with 20 or fewer characters.'
                                )])
    third_w = IntegerField('Games Won',
                           validators=[Optional(strip_whitespace=True),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    third_d = IntegerField('Games Drawn',
                           validators=[Optional(strip_whitespace=True)])
    third_l = IntegerField('Games Lost',
                           validators=[Optional(strip_whitespace=True),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    fourth_oppname = StringField('Opponent Name',
                                 validators=[length(max=20,
                                 message='Please enter a player name with 20 or fewer characters.'
                                 )])
    fourth_oppdeck = StringField('Deck Name',
                                 validators=[length(max=20,
                                 message='Please enter a deck name with 20 or fewer characters.'
                                 )])
    fourth_w = IntegerField('Games Won',
                            validators=[Optional(strip_whitespace=True),
                            AnyOf(values=[0, 1, 2],
                            message='Please input number 0, 1 or 2')])
    fourth_d = IntegerField('Games Drawn',
                            validators=[Optional(strip_whitespace=True)])
    fourth_l = IntegerField('Games Lost',
                            validators=[Optional(strip_whitespace=True),
                            AnyOf(values=[0, 1, 2],
                            message='Please input number 0, 1 or 2')])
    fifth_oppname = StringField('Opponent Name',
                                validators=[length(max=20,
                                message='Please enter a player name with 20 or fewer characters.'
                                )])
    fifth_oppdeck = StringField('Deck Name', validators=[length(max=20,
                                message='Please enter a deck name with 20 or fewer characters.'
                                )])
    fifth_w = IntegerField('Games Won',
                           validators=[Optional(strip_whitespace=True),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    fifth_d = IntegerField('Games Drawn',
                           validators=[Optional(strip_whitespace=True)])
    fifth_l = IntegerField('Games Lost',
                           validators=[Optional(strip_whitespace=True),
                           AnyOf(values=[0, 1, 2],
                           message='Please input number 0, 1 or 2')])
    eventstatusinput = StringField('Event Status:')
    eventrecordinput = StringField('Event Record (Win/Draw/Loss):')
    eventgamewin = StringField('Event Game Win %:')
