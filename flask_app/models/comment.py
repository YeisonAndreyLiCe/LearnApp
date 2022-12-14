from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.comment = data['comment']
        self.rate = data['rate']
        self.user_id = data['user_id']
        self.course_id = data['course_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.author = User.get_by_id(self.user_id)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        results = connectToMySQL('learn_app').query_db(query)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (title, comment, rate, user_id, course_id) VALUES (%(title)s, %(comment)s, %(rate)s, %(user_id)s, %(course_id)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
        id = { 'id': data }
        query = "SELECT * FROM comments WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        return cls(result[0])
    @classmethod
    def update(cls, data):
        query = "UPDATE comments SET title = %(title)s, comment = %(comment)s, rate = %(rate)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = {'id': data }
        query = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    @classmethod
    def get_by_course_id(cls, data):
        id = { 'id': data }
        query = "SELECT comments.*,users.first_name AS first_name FROM comments LEFT JOIN users ON users.id=comments.user_id WHERE course_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def get_by_user_id(cls, data):
        id = { 'id': data }
        query = "SELECT * FROM comments WHERE user_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, id)
        comments = [cls(comment) for comment in results]
        return comments
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['title']) < 5:
            errors['title'] = 'The field title should have at least 5 characters'
        if len(data['comment']) < 10:
            errors['comment'] = 'The field comment should have at least 10 characters'
        if len(data['rate']) < 1:
            errors['rate'] = 'The course should be rated'
        if int(data['rate'])<1 or int(data['rate'])>5:
            errors['rate_range'] = 'Rate should be from 1 to 5'
        query='SELECT * FROM comments WHERE course_id=%(course_id)s and user_id=%(user_id)s'
        result=connectToMySQL('learn_app').query_db(query,data)
        if result :
            errors['comment_exist']='You have already comment this course'
        return errors