from typing import Text
from flask.signals import message_flashed
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, TextField, TextAreaField
from wtforms.validators import AnyOf, InputRequired, URL, Optional, NumberRange, Length


class AddPet(FlaskForm):
    name = StringField(
        'Pet Name',
        validators=[InputRequired()],
    )
    species = SelectField(
        'Species',
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('cow', 'Cow')
        ],
    )
    photo_url = StringField(
        'Photo URL',
        validators=[
            Optional(),
            URL()
        ],
    )
    age = IntegerField(
        'Age',
        validators=[
            Optional(),
            NumberRange(min=0, max=30)
        ],
    )
    notes = TextAreaField(
        'Notes',
        validators=[Optional(), Length(min=10)],
    )


class EditPet(FlaskForm):
    photo_url = StringField('Photo URL', [
        URL(require_tld=False),
        Optional()
    ])
    notes = StringField('Notes')
    available = BooleanField('Available')
