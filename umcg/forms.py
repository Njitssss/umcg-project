from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from wtforms import ValidationError
from umcg.models import User

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={"placeholder": "           email-adres"})
    username = StringField('Gebruikersnaam', validators=[DataRequired()], render_kw={"placeholder": "        gebruikersnaam"})
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden komen niet overeen!'), Length(min=5, max=50)], render_kw={"placeholder": "          wachtwoord"})
    pass_confirm = PasswordField('Wachtwoord bevestigen', validators=[DataRequired()], render_kw={"placeholder": "   wachtwoord herhalen"})
    submit = SubmitField('Registreer')

    def check_email(self, field):
        # Check of het e-mailadres al in de database voorkomt!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')

    def check_username(self, field):
        # Check of de gebruikersnaam nog niet vergeven is!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al vergeven, kies een andere naam!')

class DagboekForm(FlaskForm):
    input = TextAreaField('Hoe was je dag?', validators=[DataRequired()], render_kw={"placeholder": "      Hoe was jouw dag vandaag?"})
    submit = SubmitField('Verstuur')

class PersoonlijkForm(FlaskForm):
    voornaam = StringField('Wat is je voornaam?', validators=[DataRequired()], render_kw={"placeholder": "   Voornaam"})
    achternaam = StringField('Wat is je achternaam?', validators=[DataRequired()], render_kw={"placeholder": "   Achternaam"})
    leeftijd = IntegerField('Wat is je leeftijd', validators=[DataRequired()], render_kw={"placeholder": "Leeftijd"})
    submit = SubmitField('Verstuur')

class LichaamForm(FlaskForm):
    input = SelectField('Naam van de plek?', choices=[('Hoofd-Nek', 'Nek'), ('Hoofd-Kaak', 'Kaak'), ('Hoofd-Oren', 'Oren'), ('Hoofd-Ogen', 'Ogen')], coerce=str)
    submit = SubmitField('Verstuur')

