from flask_app.models.category import Category
from flask_app.models.course import Course
from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.record import Record

@app.route('/admin')
def admin():
    if 'user_id' not in session:
        return redirect('/')
    if session['user_id'] != 1:
        return redirect('/')
    return render_template('admin.html')

@app.route('/admin/users')
def admin_users():
    if 'user_id' not in session:
        return redirect('/')
    if session['user_id'] != 1:
        return redirect('/')
    users = User.get_all()
    return render_template('admin_users.html', users=users)