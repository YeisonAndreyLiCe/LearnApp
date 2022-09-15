from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.comment import Comment
from flask_app.models.record import Record
from flask_app.models.users_has_courses import User_has_Courses


@app.route('/categories/<int:id>')
def course_by_category(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    context = {
        'courses':Course.get_by_category_id(id),
        'category' : Category.get_by_id(id),
        'user':User.get_by_id(session['user_id']),
        'categories':Category.get_all(),
    }
    return render_template('category_desc.html', **context)

@app.route('/courses/<int:id>')
def course(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    context = {
        'course':Course.get_by_id(id),
        'user':User.get_by_id(session['user_id']),
        'comments':Comment.get_by_course_id({'id':id}),
        'records': Record.get_by_course_id({'id':id}),
        'categories':Category.get_all(),
    }
    return render_template('course.html', **context)

@app.route('/create_comment', methods=['POST'])
def create_comment():
    if request.method=='POST':
        errors = Comment.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            Comment.save(request.form)
            return jsonify({'route':'/courses/'+request.form['course_id']})
    return redirect('/register_login')


@app.route('/enroll', methods=['POST'])
def enroll_course():
    if request.method=='POST':
        errors=User_has_Courses.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            User_has_Courses.enroll_course(request.form)
            return jsonify({'route':'/courses'})
    return redirect('/register_login')

@app.route('/create_course', methods=['POST'])
def create_course():
    if request.method=='POST':
        errors = Course.validate(request.form)
        if errors:
            data = {}
            for key, value in errors.items():
                data[key] = value
            return jsonify(data)
        else:
            email = {'email':request.form['instructor_email']}
            user=User.get_by_email(email)
            data = {'name': request.form['name'],
                'description':request.form['description'],
                'instructor_id':user.id,
                'category_id':request.form['category_id']}
            Course.save(data)
            return jsonify({'route':'/courses'})
    return redirect('/register_login')