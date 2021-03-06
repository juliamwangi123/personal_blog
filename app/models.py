from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Blog(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30))
    sub_title=db.Column(db.String(20))
    content=db.Column(db.String(300))
    time_posted=db.Column(db.DateTime,index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='article', lazy=True)
    

    def __repr__(self):
        return '<User {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')
    comments=db.relationship('Comment' ,backref='writer', lazy='dynamic')



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False) 
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)
    author=db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

    def __repr__(self):
        return f"Comment('{self.body}', '{self.blog_id}')"