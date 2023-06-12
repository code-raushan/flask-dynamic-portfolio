import os
import json
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .models import Message, Project, Comment
from . import db, create_app

main = Blueprint('main', __name__)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/skills')
@login_required
def skills():
    return render_template('skills.html')

@main.route('/project')
@login_required
def project():
    projects = Project.query.all()
    if current_user.adminRole==True:
       return render_template('project.html', role=current_user.adminRole, projects=projects)
    return render_template('project.html', role=current_user.adminRole, projects=projects)

@main.route('/experience')
@login_required
def experience():
    return render_template('experience.html')

@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@main.route('/profile')
@login_required
def profile():
    if current_user.adminRole==True:
        allMessage=Message.query.all()
        return render_template('profile.html',name=current_user.name, email=current_user.email, role=current_user.adminRole, allMessage=allMessage)
    return render_template('profile.html', name=current_user.name, email=current_user.email, role=current_user.adminRole)

@main.route('/contact', methods=['POST'])
def contact_post():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        
        messageAllDetails=Message(name=name, email=email, phone=phone, message=message)
        db.session.add(messageAllDetails)
        db.session.commit()
    return render_template('dashboard.html')

@main.route('/projectupload', methods=['POST'])
def project_upload():
    if request.method=='POST':
        title=request.form.get('title') 
        sourcecode = request.form.get('sourcecode')
        link = request.form.get('link')
        new_project = Project(title=title, sourcecode=sourcecode, link=link)
        db.session.add(new_project)
        db.session.commit()
        
    return redirect(url_for('main.project'))

@main.route('/project/<int:project_id>/like')
def project_like(project_id):
    project = Project.query.get(project_id)
    userid = current_user.id
    liked_by_list = json.loads(project.liked_by) if project.liked_by else []
    if project is None:
        return 'Post not found', 404
    if userid in liked_by_list:
        return redirect(url_for('main.project'))
    project.likes+=1
    liked_by_list.append(userid)
    project.liked_by = json.dumps(liked_by_list)
    db.session.commit()
    
    return redirect(url_for('main.project'))

@main.route('/project/<int:project_id>/comment', methods=['POST'])
def project_comment(project_id):
    project=Project.query.get(project_id)
    user_id=current_user.id 
    username=current_user.name
    if project is None:
        return 'Post not found', 404
    
    commenttext=request.form.get('comment')
    if commenttext=='':
        return redirect(url_for('main.project'))
    comment = Comment(content=commenttext, project_id=project_id, user_id=user_id, username=username)
    
    db.session.add(comment)
    db.session.commit()
    
    return redirect(url_for('main.project'))
    
@main.route('/project/<int:project_id>/allcomments')
def allcomments(project_id):
    project=Project.query.get(project_id)
    comments = Comment.query.filter_by(project_id=project_id).all()
    
    comments_list = []
    for comment in comments:
        comments_list.append({
            'id': comment.id,
            'content': comment.content,
            'author': comment.username
        })
    return render_template('projectdetails.html', comments_list=comments_list, project=project)