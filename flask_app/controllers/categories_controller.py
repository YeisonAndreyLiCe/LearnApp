from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.record import Record

@app.route('/create_category', methods=['POST'])
def create_category():
    if request.method=='POST':
        print('*'*100,request.form)
        errors = Category.validate(request.form)
        if errors:
            data = {}
            for key, value in errors.items():
                data[key] = value
            return jsonify(data)
        if 'category_id' in request.form:
            user = User.get_by_email({'email': request.form['instructor_email']})
            if not user:
                return jsonify({'instructor_email': 'No instructor with that email'})
            data = {
                'name': request.form['name'],
                'description': request.form['description'],
                'instructor_id': user.id,
                'category_id': request.form['category_id'],
            }
            Course.save(data)
            return jsonify({'route':'/courses'})
        elif 'record' in request.form:
            Record.save(request.form)
            return jsonify({'route':'/courses'})
        Category.save(request.form)  
        return jsonify({'route':'/courses'})    
    return redirect('/register_login')