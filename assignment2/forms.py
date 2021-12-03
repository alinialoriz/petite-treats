from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    name = TextField("Name")
    email = EmailField("Email")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
