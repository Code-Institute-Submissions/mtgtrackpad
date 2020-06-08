from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import InputRequired, Length, Email


...


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(),
        Email("This field requires a valid email address")])
    body = TextField('Message',
        validators=[InputRequired(),
                    Length(min=10,
                    message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
