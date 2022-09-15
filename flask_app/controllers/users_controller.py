import json
from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_bcrypt import Bcrypt 
from flask_app.models.users_has_courses import User_has_Courses
#import bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return redirect('/register_login')

@app.route('/register_login')
def index():
    if 'user_id' in session:
        return redirect('/courses')
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method=='POST':
        errors = User.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            pwd = bcrypt.generate_password_hash(request.form['password'])
            form = {
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'birth_date':request.form['birth_date'],
                'role_id':'1',
                'email':request.form['email'],
                'password':pwd,
            }
            id=User.save(form)
            session['user_id']=id
            return jsonify({'route':'/courses'})
    return redirect('/register_login')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: 
        return jsonify({'message':'Wrong email'})
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return jsonify({'message':'Wrong password'})
    session['user_id']=user.id
    return jsonify({'route':'/courses'})

@app.route('/courses')
def courses():
    if not 'user_id' in session:
        return redirect('/register_login')
    user = User.get_by_id(session['user_id'])
    context = {
        'user' : user,
        'courses_user' : User_has_Courses.get_enrolled_courses(user.id),
        'categories' : Category.get_all(),
    }
    return render_template('courses.html', **context)

@app.route('/view_user')
def view_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    user = User.get_by_id(session['user_id'])
    return render_template('view_user.html', user=user)

@app.route('/edit_user')
def edit_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    user = User.get_by_id(session['user_id'])
    return render_template('edit_user.html', user = user)

@app.route('/update_user_info', methods=['POST'])
def update_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    errors = User.validate_update(request.form)
    if errors:
        return jsonify(errors)
    if 'password' in request.form:
        error = User.validate_password(request.form)
        if error:
            return jsonify(error)
        pwd = bcrypt.generate_password_hash(request.form['password'])
        form = {
            'id':request.form['id'],
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'birth_date':request.form['birth_date'],
            'role_id':'1',
            'email':request.form['email'],
            'password':pwd,
        }
        User.update_password(form)
        return jsonify({'route':'/view_user'})
    User.update_without_password(request.form)
    return jsonify({'route':'/view_user'})

@app.route('/delete/<int:id>')
def delete_user(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    User.delete(id)
    return redirect('/courses')

@app.route('/update_password', methods=['POST'])
def update_password():
    if not 'user_id' in session:
        return redirect('/register_login')
    user = User.get_by_id(session['user_id'])
    if not bcrypt.check_password_hash(user.password, request.form['old_password']):
        return jsonify({'message':'Wrong password'})
    if User.valid_password(request.form):
        return jsonify({'message':'Password must be at least 8 characters'})
    pwd1 = bcrypt.generate_password_hash(request.form['password'])
    form = {
        'id':request.form['id'],
        'password':pwd1
    }
    User.update_password(form)
    return redirect('/logout')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')