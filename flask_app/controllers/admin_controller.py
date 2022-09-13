import json
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
    if session['user_id'] ==2 or session['user_id']==1:
        return redirect('/')
    categories = Category.get_all()
    courses = Course.get_all_as_dic()
    categories = json.dumps(categories)
    print(categories)
    courses = json.dumps(courses)
    users = User.get_all()
    return render_template('admin.html', categories=categories, courses=courses, users=users) 

