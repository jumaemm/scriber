from scriber.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean)