from datetime import datetime
import email
from tokenize import StringPrefix
from app import db 



#user table

class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    email=db.Column(db.String(200))
    password=db.Column(db.String())
    blogs=db.relationship('Blog' ,backref='author', lazy='dynamic')
    def __repr__(self):
        
        return f"User('{self.email}','{self.password}')"
#blog table

class Blog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(120), index=True)
    sub_title=db.Column(db.String(120))
    image=db.Column(db.String )
    date_posted=db.Column(db.DateTime, default=datetime.now)
    content=db.Column(db.Text)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        
        return f"Blog('{self.title}','{self.sub_title}','{self.date_posted}')"


