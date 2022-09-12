from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category

@app.route('/create_category', methods=['POST'])
def create_category():
    if request.method=='POST':
        errors = Category.validate(request.form)
        if errors:
            data = {}
            for key, value in errors.items():
                data[key] = value
            return jsonify(data)
        else:
            Category.save(request.form)
            return jsonify({'route':'/courses'})
    return redirect('/register_login')