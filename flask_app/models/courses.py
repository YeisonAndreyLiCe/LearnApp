from flask_app.config.mysqlconnection import connectToMySQL

class Course:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM courses;"
        results = connectToMySQL('learn_app').query_db(query)
        courses = []
        for course in results:
            courses.append(cls(course))
        return courses
    @classmethod
    def save(cls, data):
        query = "INSERT INTO courses (title, description) VALUES (%(title)s, %(description)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
        id = { 'id': data }
        query = "SELECT * FROM courses WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        return cls(result[0])
    @classmethod
    def update(cls, data):
        query = "UPDATE courses SET title = %(title)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = { 'id': data }
        query = "DELETE FROM courses WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['title']) < 5:
            errors['title'] = 'The field title should have at least 5 characters'
        if len(data['description']) < 15:
            errors['description'] = 'The field description should have at least 15 characters'
        return errors