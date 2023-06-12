from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User, Message
from . import db


auth = Blueprint('auth', __name__)

#   #ADMIN CREDENTIALS

#     db.session.add(admin_user)
#     db.session.commit()

@auth.route('/admin')
def auth_login():
    ADMIN_NAME='Admin'
    ADMIN_EMAIL='admin@example.com'
    ADMIN_PASSWORD='password'

    check_user=User.query.filter_by(email=ADMIN_EMAIL).first()
    if not check_user:
        admin_user = User(email=ADMIN_EMAIL, password=generate_password_hash(ADMIN_PASSWORD, method='sha256'), name=ADMIN_NAME, adminRole=True)
        db.session.add(admin_user)
        db.session.commit()
    
    return render_template('admin_login.html')

@auth.route('/admin', methods=['POST'])
def admin_login_post():
    email=request.form.get('email')
    password=request.form.get('password')
    
    admin_user=User.query.filter_by(email=email).first()
    if not admin_user or not check_password_hash(admin_user.password, password) or admin_user.adminRole!=True:
        flash('Your credentials do not match the crediantials of the Admin')
        return redirect(url_for('auth.login'))
    
    login_user(admin_user)
    return redirect(url_for('main.dashboard'))

@auth.route('/')
def login():
    return render_template('login.html')

@auth.route('/', methods=['POST'])
def login_post():
    ADMIN_NAME='Admin'
    ADMIN_EMAIL='admin@example.com'
    ADMIN_PASSWORD='password'

    check_user=User.query.filter_by(email=ADMIN_EMAIL).first()
    if not check_user:
        admin_user = User(email=ADMIN_EMAIL, password=generate_password_hash(ADMIN_PASSWORD, method='sha256'), name=ADMIN_NAME, adminRole=True)
        db.session.add(admin_user)
        db.session.commit()
    #code
    email=request.form.get('email')
    password=request.form.get('password')
    
    user=User.query.filter_by(email=email).first()
    
    #chekcing if the user exist or not
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    
    login_user(user)
    return redirect(url_for('main.dashboard'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #code
    email=request.form.get('email')
    name=request.form.get('name')
    password=request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    #if already exist with same email
    if user:
        flash('Email Already Exists. Log In please:-)')
        return redirect(url_for('auth.signup'))
    
    #creating a new user
    new_user=User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    #adding the new user to the database
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))