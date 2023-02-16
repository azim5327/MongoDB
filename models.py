from . import db
from flask_login import UserMixin
from flask_sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(150), unique=True)
     username = db.Column(db.String(150), unique=True)
     password = db.Column(db.String(150), unique=True)
     date_created = db.Column(db.Date(timezone=True), default=func.now())
     posts = db.relationships('Post', backref='user,' passive_deletes=True)
     comments = db.relationships('Comment', backref='user,' passive_deletes=True)
     likes = db.relationships('Like', backref='user,' passive_deletes=True)   


class Post(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    text = db.Column(db.Text, nullable=False)
     date_created = db.Column(db.Date(timezone=True), default=func.now())
     author = db.Column(db.Integer, db.ForeignKey(
         'user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationships('Comment', backref='post,' passive_deletes=True) 
    likes = db.relationships('Like', backref='post,' passive_deletes=True)   

class Comment(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
     date_created = db.Column(db.Date(timezone=True), default=func.now())
     author = db.Column(db.Integer, db.ForeignKey(
         'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
         'post.id', ondelete="CASCADE"), nullable=False)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date(timezone=True), default=func.now())
     author = db.Column(db.Integer, db.ForeignKey(
         'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
         'post.id', ondelete="CASCADE"), nullable=False)