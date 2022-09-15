import json
from flask_app.models.category import Category
from flask_app.models.course import Course
from flask_app.models.role import Role
from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.record import Record
from werkzeug.utils import secure_filename
import os

@app.route('/admin')
def admin():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id(session['user_id'])
    if user.role_id!=1:
        return redirect('/logout')
    categories = Category.get_all_as_dic()
    courses = Course.get_all_as_dic()
    context = {
        'categories': categories,
        'categories_json':json.dumps(categories),
        'courses': json.dumps(courses),
        'users': User.get_all(),
        'roles': Role.get_all(),
        'user': User.get_by_id( session['user_id']),
    }
    print(Role.get_all())
    return render_template('admin.html', **context)

@app.route('/admin_actions', methods=['POST'])
def admin_actions():
    if request.method=='POST':
        errors = Category.validate(request.form)
        if errors:
            data = {}
            for key, value in errors.items():
                data[key] = value
            return jsonify(data)
        if 'instructor_email' in request.form:
            user = User.get_by_email({'email': request.form['instructor_email']})
            if not user:
                return jsonify({'instructor_email': 'No instructor with that email'})
            file = request.files['image']
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            data = {
                'name': request.form['name'],
                'description': request.form['description'],
                'instructor_id': user.id,
                'category_id': request.form['category_id'],
                'image': file_name
            }
            Course.save(data)
            return jsonify({'route':'/courses'})
        elif 'record' in request.files:
            if request.files['record'].filename=="":
                return jsonify({'record': 'Please upload a file'})
            file = request.files['record']
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            form = {
                'name': request.form['name'],
                'course_id': request.form['course_id'],
                'description': request.form['description'],
                'record': file_name
            }
            Record.save(form)
            return jsonify({'route': '/courses'})
        file = request.files['image']
        file_name = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'image': file_name,
        }
        Category.save(data)  
        return jsonify({'route':'/courses'})    
    return redirect('/register_login')

@app.route('/update_role', methods=['POST'])
def update_role():
    if request.method=='POST':
        User.update_role(request.form)
        return redirect('/admin')
    return redirect('/register_login')
