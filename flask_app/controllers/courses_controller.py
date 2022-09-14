from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.comment import Comment
from flask_app.models.record import Record


@app.route('/categories/<int:id>')
def course_by_category(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {'id':id}
    data_user = {'id':session['user_id']}
    context = {
        'courses':Course.get_by_category_id(data),
        'category' : Category.get_by_id(data),
        'user':User.get_by_id(data_user),
        'categories':Category.get_all(),
    }
    
    return render_template('category_desc.html', **context)

@app.route('/courses/<int:id>')
def course(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data={'id':id}
    data_user = {'id':session['user_id']}
    context = {
        'course':Course.get_by_id(data),
        'user':User.get_by_id(data_user),
        'comments':Comment.get_by_course_id(data),
        'records': Record.get_by_course_id(data),
        'categories':Category.get_all(),
    }
    return render_template('course.html', **context)

@app.route('/create_comment', methods=['POST'])
def create_comment():
    Comment.save(request.form)
    return redirect('courses/'+request.form['course_id'])

@app.route('/enroll', methods=['POST'])
def enroll_course():
    User.enroll_course(request.form)
    return redirect('/courses') 


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
            #revisar a donde se va a redireccionar
            return jsonify({'route':'/courses'})
    return redirect('/register_login')


