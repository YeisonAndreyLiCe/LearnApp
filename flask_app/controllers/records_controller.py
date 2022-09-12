from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.record import Record

@app.route('/create_record')
def create_record():
    if not 'user_id' in session:
        return redirect('/register_login')
    return render_template('create_record.html')

@app.route('/insert', methods=['POST'])
def insert_record():
    if request.method=='POST':
        #vamos a validar?
        errors = Record.validate(request.form)
        if errors:
            return jsonify(errors)
        else:
            Record.save(request.form)
            #revisar a donde se va a redireccionar
            return jsonify({'route':'/courses'})
    return redirect('/register_login')
