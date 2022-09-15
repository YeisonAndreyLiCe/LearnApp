from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime, timedelta
import re
from flask_app.models.role import Role
from flask_app.models.users_has_courses import User_has_Courses

re_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
re_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.birth_date = data['birth_date']
        self.role_id = data['role_id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.role = Role.get_by_id(self.role_id)
        #self.courses = User_has_Courses.get_enrolled_courses(self.id)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('learn_app').query_db(query)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, birth_date, email, password, role_id) VALUES (%(first_name)s, %(last_name)s, %(birth_date)s, %(email)s, %(password)s, %(role_id)s);"
        result = connectToMySQL('learn_app').query_db(query, data)
        return result
    @classmethod
    def get_by_email(cls,data):
        query='SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL('learn_app').query_db(query, data)
        if result:
            return cls(result[0])
        return False
    @classmethod
    def get_by_id(cls, data):
        id = { 'id': data }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        if result:
            return cls(result[0])
        return False
    @classmethod
    def update_without_password(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, birth_date = %(birth_date)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def update_password(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, birth_date = %(birth_date)s, password = %(password)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def update_role(cls, data):
        data = {'role_id':data['role_id'],'id': data['id']}
        query = "UPDATE users SET role_id = %(role_id)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = { 'id': data }
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    @staticmethod
    def validate(data):
        errors={}
        if len(data['first_name'])<2:
            errors['first_name']='First name should have at least 2 characters'
        if len(data['last_name'])<2:
            errors['last_name']='Last name should have at least 2 characters'
        if data['birth_date'] == '':
            errors['birth_date']='Birth date is required'
        else:
            now = datetime.now().year
            date = datetime.strptime((data['birth_date']),'%Y-%m-%d').year
            if now-date < 14:
                errors['birth_date']='You should are at least 14 years old'
        if not re_email.match(data['email']):
            errors['email']='Please enter a valid email'
        query='SELECT * FROM users WHERE email = %(email)s'
        result=connectToMySQL('learn_app').query_db(query,data)
        if result:
            errors['emailExist']='Email already exists'
        if not re_password.match(data['password']):
            errors['password']= "Password must be at least 8 characters, contain at least one number, one uppercase and one lowercase letter"
        return errors
    
    @staticmethod
    def validate_update(data):
        errors={}
        if len(data['first_name'])<2:
            errors['first_name']='First name should have at least 2 characters'
        if len(data['last_name'])<2:
            errors['last_name']='Last name should have at least 2 characters'
        if data['birth_date'] == '':
            errors['birth_date']='Birth date is required'
        else:
            now = datetime.now().year
            date = datetime.strptime((data['birth_date']),'%Y-%m-%d').year
            if now-date < 14:
                errors['birth_date']='You should are at least 14 years old'
        if not re_email.match(data['email']):
            errors['email']='Please enter a valid email'
        query='SELECT * FROM users WHERE email = %(email)s AND id != %(id)s;'
        result=connectToMySQL('learn_app').query_db(query,data)
        if result:
            errors['emailExist']='Email already exists' 
        return errors
    @staticmethod
    def validate_password(data):
        errors={}
        if not re_password.match(data['password']):
            errors['password']= "Password must be at least 8 characters, contain at least one number, one uppercase and one lowercase letter"
        return errors