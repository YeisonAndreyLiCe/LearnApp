from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.record import Record
#Para subir imagenes
from werkzeug.utils import secure_filename
import os


@app.route('/create_record')
def create_record():
    if not 'user_id' in session:
        return redirect('/register_login')
    return render_template('create_record.html')

@app.route('/insert', methods=['POST'])
def insert_record():
    if request.method == 'POST':
        # vamos a validar?
        errors = Record.validate_record(request.form)
        if errors:
            return jsonify(errors)
        else:
            # Almaceno el archivo en una variable
            file = request.files['course_record']
            # extraigo el nombre de ese archivo
            file_name = secure_filename(file.filename)
            # guardo el archivo en la carpeta del servidor
            file.save(os.path.join(app.config['UPLOAD_FOLDER']), file_name)
            # creo un nuevo formulario para enviar a la base de datos
            form = {
                'name': request.form['name'],
                'course_id': request.form['course_id'],
                'description': request.form['description'],
                'record': file_name
            }
            Record.save(form)
            # revisar a donde se va a redireccionar
            return jsonify({'route': '/courses'})
    return redirect('/register_login')
