from flask_login import UserMixin
from . import db

#UserMixin: This provides default implementations for the methods that Flask-Login expects user objects to have.

class User(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(100), nullable=False)
    name=db.Column(db.String(200), nullable=False) 
    adminRole = db.Column(db.Boolean, default=False)   
    
    
class Message(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(200), nullable=False)
    phone=db.Column(db.Integer)
    message=db.Column(db.String(1000), nullable=False)
    
class Project(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    link=db.Column(db.String(200), nullable=False)
    sourcecode = db.Column(db.String(200), nullable=False)
    likes=db.Column(db.Integer, default=0)
    liked_by = db.Column(db.String)
    comments=db.relationship('Comment', backref='project', lazy=True)

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.Text, nullable=False)
    project_id=db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    username=db.Column(db.String)



#for creating db, in Python REPL:
#>>> from project import db, create_app, models
#>>> app = create_app()
#>>> app.app_context().push()
#>>> db.create_all()
