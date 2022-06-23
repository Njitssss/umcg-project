from umcg import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

##################################
#      Gebruikers Database       #
##################################

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String(128))
    
#                                         #
# Begrijpen van de verschillende gegevens #
#                                         #

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

##################################
#       Dagboek Database         #
##################################

class Dagboek(db.Model, UserMixin):
    __tablename__ = "Dagboek"
    dagboek_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, ForeignKey(User.username))
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    dag = db.Column(db.String)
    input = db.Column(db.String)

#                                         #
# Begrijpen van de verschillende gegevens #
#                                         #

    def __init__(self, username, user_id, dag, input):
        self.username = username
        self.user_id = user_id
        self.dag = dag
        self.input = input

##################################
#     Persoonlijke Database      #
##################################

class Persoonlijk(db.Model):
    __tablename__ = "Persoonlijk"
    persoonlijk_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, ForeignKey(User.username))
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    voornaam = db.Column(db.String)
    achternaam = db.Column(db.String)
    leeftijd = db.Column(db.String)

#                                         #
# Begrijpen van de verschillende gegevens #
#                                         #

    def __init__(self, username, user_id, voornaam, achternaam, leeftijd):
        self.username = username
        self.user_id = user_id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd

##################################
#       Lichaam Database         #
##################################

class Lichaam(db.Model):
    __tablename__ = "Lichaam"
    Lichaam_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, ForeignKey(User.username))
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    input = db.Column(db.String)

    #                                         #
    # Begrijpen van de verschillende gegevens #
    #                                         #

    def __init__(self, username, user_id, input):
        self.username = username
        self.user_id = user_id
        self.input = input

db.create_all()