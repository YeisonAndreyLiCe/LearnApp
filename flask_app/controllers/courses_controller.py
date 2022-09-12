from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category

@app.route('/categories/<int:id>')
def course_by_category(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {'id':id}
    data_user = {'id':session['user_id']}
    courses=Course.get_by_category_id(data)
    category = Category.get_by_id(data)
    user=User.get_by_id(data_user)
    return render_template('category_desc.html', courses=courses, category=category, user=user)

@app.route('/courses/<int:id>')
def course(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data={'id':id}
    data_user = {'id':session['user_id']}
    course=Course.get_by_id(data)
    user=User.get_by_id(data_user)
    return render_template('course.html', course=course, user=user)

@app.route('/enroll', methods=['POST'])
def enroll_course():
    User.enroll_course(request.form)
    return('/courses') 

@app.route('/create_course')
def create_course():
    if not 'user_id' in session:
        return redirect('/register_login')
    return render_template('create_course.html')

@app.route('/insert', methods=['POST'])
def insert_course():
    if request.method=='POST':
        errors = Course.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            Course.save(request.form)
            #revisar a donde se va a redireccionar
            return jsonify({'route':'/courses'})
    return redirect('/register_login')


