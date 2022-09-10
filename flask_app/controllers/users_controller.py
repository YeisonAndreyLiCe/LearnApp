import json
from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.users import User
from flask_bcrypt import Bcrypt 
#import bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return redirect('/register_login')

@app.route('/register_login')
def index():
    return render_template('register_prov.html') #nombre primer html

@app.route('/register', methods=['POST'])
def register():
    if request.method=='POST':
        errors = User.validate(request.form)
        #data = {}
        if errors:
            #for key, value in errors:
                #data[key]=value
            return jsonify(errors)
        else:
            pwd = bcrypt.generate_password_hash(request.form['password'])
        
            form = {
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'birth_date':request.form['birth_date'],
                'rol_id':request.form['rol_id'],
                #rol
                'email':request.form['email'],
                'password':pwd,
            }
            id=User.save(form)
            session['user_id']=id
            return jsonify({'route':'/home'})
    return redirect('/register_login')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: 
        return jsonify({'message':'Wrong email'})
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return jsonify({'message':'Wrong password'})
    session['user_id']=user.id
    return jsonify({'route':'/home'})

@app.route('/home')
def home_reviews():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    users = User.get_all()
    return render_template('home.html', user=user, users=users)

# @app.route('/view_user')
# def view_user():
#     if not 'user_id' in session:
#         return redirect('/register_login')
#     data = {
#         'id': session['user_id']
#     }
#     user = User.user_by_id(data)
#     return render_template('view_user.html', user=user)

@app.route('/edit_user')
def edit_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('edit_user.html', user=user)

@app.route('/update_user', methods=['POST'])
def update_user():
    if not User.valid_edit(request.form):
            return redirect('/edit_user')
    User.update(request.form)
    return redirect('/view_user')

@app.route('/delete/<int:id>')
def delete_user(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {'id':id}
    User.delete(data)
    return redirect('/home')

@app.route('/update_password', methods=['POST'])
def update_password():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    if not bcrypt.check_password_hash(user.password, request.form['old_password']):
        flash('Wrong current password', 'password')
        return redirect('/edit_user')
    if not User.valid_password(request.form):
        return redirect('/edit_user')
    pwd1 = bcrypt.generate_password_hash(request.form['password'])
    form = {
        'id':request.form['id'],
        'password':pwd1
    }
    User.update_password(form)
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')