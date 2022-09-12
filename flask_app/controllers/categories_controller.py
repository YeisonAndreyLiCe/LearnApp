from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category

@app.route('/create_category')
def create_category():
    if not 'user_id' in session:
        return redirect('/register_login')
    return render_template('create_category.html')

@app.route('/insert', methods=['POST'])
def insert_category():
    if request.method=='POST':
        errors = Category.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            Category.save(request.form)
            #revisar a donde se va a redireccionar
            return jsonify({'route':'/courses'})
    return redirect('/register_login')