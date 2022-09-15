from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import category
class Course:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructor_id = data['instructor_id']
        self.category_id = data['category_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.instructor = user.User.get_by_id(self.instructor_id)
        self.category = category.Category.get_by_id(self.category_id)
        self.image = data['image']

    @classmethod
    def get_all(cls):
        query = "SELECT users.first_name AS instructor_name ,courses.* FROM courses LEFT JOIN users ON courses.instructor_id = users.id;"
        results = connectToMySQL('learn_app').query_db(query)
        print(results)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def get_all_as_dic(cls):
        query = "SELECT name, id FROM courses;"
        results = connectToMySQL('learn_app').query_db(query)
        return results
    @classmethod
    def save(cls, data):
        query = "INSERT INTO courses (name, description, instructor_id, category_id, image) VALUES (%(name)s, %(description)s, %(instructor_id)s,%(category_id)s, %(image)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
        id = {'id': data}
        query = "SELECT users.first_name AS instructor_name, courses.* FROM courses LEFT JOIN users ON courses.instructor_id = users.id WHERE courses.id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        print(result)
        if result:
            return cls(result[0])
        return False
    @classmethod
    def update(cls, data):
        query = "UPDATE courses SET name = %(name)s, description = %(description)s, instructor_id=%(instructor_id)s, category_id=%(category_id)s  WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = {'id': data}
        query = "DELETE FROM courses WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    @classmethod
    def get_by_category_id(cls, data):
        data = {'id': data}
        query = "SELECT users.first_name AS instructor_name, courses.* FROM courses LEFT JOIN users ON courses.instructor_id = users.id WHERE category_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def get_by_user_id(cls, data):
        query = "SELECT users.first_name AS instructor_name, courses.* FROM courses LEFT JOIN users ON courses.instructor_id = users.id WHERE courses.instructor_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            return [cls(course) for course in results]
        return False
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['name']) < 5:
            errors['name'] = 'The field title should have at least 5 characters'
        if len(data['description']) < 15:
            errors['description'] = 'The field description should have at least 15 characters'
        if len(data['category_id']) < 1:
            errors['category_id'] = 'The course should have at least a category'
        return errors