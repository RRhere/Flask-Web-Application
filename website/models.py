from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"Note('{self.title}', '{self.created}')"    

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    last_name=db.Column(db.String(150))
    notes=db.relationship('Note')
    