from umcg import app, db 
from flask import render_template, redirect, request, url_for, flash, send_from_directory
from flask_login import login_user, login_required, logout_user, current_user
from umcg.models import User, Dagboek, Persoonlijk, Lichaam
from umcg.forms import LichaamForm, LoginForm, RegistrationForm, DagboekForm, PersoonlijkForm, LichaamForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import time
import os

###########################
#       Home Route        #
###########################

@app.route('/')
def home():
    time.sleep(1)
    return render_template("home.html")
    
###########################
# Login & Register Routes #
###########################

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            # Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0] == '/':
                next = url_for('home')
                time.sleep(1)
            return redirect(next)
    time.sleep(1)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        flash('Dank voor de registratie. Er kan nu ingelogd worden!')
        time.sleep(1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    time.sleep(1)
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    time.sleep(1)
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home'))

###########################
#  Persoonlijke Gegevens  #
###########################

@app.route('/gegevens', methods=['GET', 'POST'])
@login_required
def gegevens():
    form = PersoonlijkForm()
    if form.validate_on_submit():
        Persoonlijk.query.filter(Persoonlijk.user_id).delete()
        username = current_user.username
        user_id = current_user.id
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        leeftijd = form.leeftijd.data
        db.session.add(Persoonlijk(username, user_id, voornaam, achternaam, leeftijd))
        db.session.commit()
        flash("Opslaan gelukt")
        time.sleep(1)
        return render_template('home.html', form=form)
    user_id = Persoonlijk.user_id
    persoonlijk = Persoonlijk.query.filter_by(user_id=user_id)
    voornaam = form.voornaam.data
    achternaam = form.achternaam.data
    leeftijd = form.leeftijd.data
    time.sleep(1)
    return render_template('gegevens.html', form=form, persoonlijk=persoonlijk)

###########################
#     Dagboek Functie     #
###########################

@app.route('/dagboek', methods=['GET', 'POST'])
@login_required
def dagboek():
    form = DagboekForm()
    if form.validate_on_submit():
        username = current_user.username
        user_id = current_user.id
        dag = datetime.now().strftime("%d-%m-%Y")
        input = form.input.data
        db.session.add(Dagboek(username, user_id, dag, input))
        db.session.commit()
        flash("Opslaan gelukt")
        time.sleep(1)
        return render_template('home.html', form=form)
    time.sleep(1)
    return render_template('dagboek.html', form=form)

@app.route('/mijn-dagboek')
def mijn_dagboek():
    user_id = current_user.username
    dagboek = Dagboek.query.filter_by(username=user_id)
    time.sleep(1)
    return render_template('mijn_dagboek.html', dagboek=dagboek)

###########################
#    Gevoelens Functie    #
###########################

@app.route('/gevoelens')
def gevoelens():
    time.sleep(1)
    return render_template('gevoelens.html')

###########################
#   Schematisch Lichaam   #
###########################

@app.route('/lichaam', methods=['GET', 'POST'])
@login_required
def lichaam():
    form = LichaamForm()
    if form.validate_on_submit():
        username = current_user.username
        user_id = current_user.id
        input = form.input.data
        db.session.add(Lichaam(username, user_id, input))
        db.session.commit()
        flash("Opslaan gelukt")
        time.sleep(1)
        return render_template('home.html', form=form)
    time.sleep(1)
    return render_template('lichaam.html', form=form)

@app.route('/mijn_hoofd')
@login_required
def hoofd():
    time.sleep(1)
    return render_template('lichaam_hoofd.html')

@app.route('/mijn_torso')
@login_required
def torso():
    time.sleep(1)
    return render_template('lichaam_torso.html')

@app.route('/mijn_ledematen')
@login_required
def ledematen():
    time.sleep(1)
    return render_template('lichaam_ledematen.html')

###########################
#      Error Functie      #
###########################

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

###########################
#     App Run Functie     #
###########################

if __name__ == '__main__':
    app.run(debug=True)
