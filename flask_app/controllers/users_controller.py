from flask import render_template, request, redirect, session, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register_login')
def index():
    return render_template('register.html') #nombre primer html

@app.route('/register', methods=['POST'])
def register():

    #messages = User.validation(request.form)
    #print(messages)
    #if len(messages)>0:
        #return jsonify(message=messages)
    
    pwd = bcrypt.generate_password_hash(request.form['password'])
    
    form = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'birth_date':request.form['birth_date'],
        #rol
        'email':request.form['email'],
        'password':pwd,
    }
    
    id=User.create_user(form)
    session['user_id']=id
    
    return jsonify(message='Correct')

@app.route('/login', methods=['POST'])
def login():
    user = User.user_by_email(request.form)
    if not user: 
        return jsonify(message='Wrong email')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return jsonify(message='Wrong password')
    session['user_id']=user.id
    return jsonify(message='Correct')

@app.route('/home')
def home_reviews():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.user_by_id(data)
    users = User.get_all()
    return render_template('home.html', user=user, users=users)

@app.route('/view_user')
def view_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.user_by_id(data)
    return render_template('view_user.html', user=user)

@app.route('/edit_user')
def edit_user():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.user_by_id(data)
    return render_template('edit_user.html', user=user)

@app.route('/update_user', methods=['POST'])
def update_user():
    if not User.valid_edit(request.form):
            return redirect('/edit_user')
    User.edit_user(request.form)
    return redirect('/view_user')

@app.route('/delete/<int:id>')
def delete_user(id):
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {'id':id}
    User.delete_user(data)
    return redirect('/home')

@app.route('/change_password', methods=['POST'])
def change_password():
    if not 'user_id' in session:
        return redirect('/register_login')
    data = {
        'id': session['user_id']
    }
    user = User.user_by_id(data)
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
    User.change_password(form)
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')