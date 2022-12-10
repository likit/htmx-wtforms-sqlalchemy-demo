from app import db


class User(db.Model):
    __tablename__ = 'users'
    email = db.Column('email', db.String(255), primary_key=True)
    password = db.Column('password', db.String())  # storing a plain password is ok for now
