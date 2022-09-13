from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL


class Course:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructor_id = data['instructor_id']
        self.category_id = data['category_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.instructor_name = data['instructor_name']

    @classmethod
    def get_all(cls):
        query = "SELECT u.first_name as instructor_name ,c.* FROM courses as c left join users as u on c.instructor_id = u.id;"
        results = connectToMySQL('learn_app').query_db(query)
        courses = []
        for course in results:
            courses.append(cls(course))
        return courses

    @classmethod
    def get_all_as_dic(cls):
        query = "SELECT name, id FROM courses;"
        results = connectToMySQL('learn_app').query_db(query)
        print(results)
        return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO courses (name, description, instructor_id, category_id) VALUES (%(name)s, %(description)s, %(instructor_id)s,%(category_id)s);"
        return connectToMySQL('learn_app').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        #id = {'id': data}
        query = "SELECT u.first_name as instructor_name, c.* FROM courses as c left join users as u on c.instructor_id = u.id WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, data)
        print(f" resultados mostrados:{result}")
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE courses SET name = %(name)s, description = %(description)s, instructor_id=%(instructor_id)s, category_id=%(categoryy_id)s  WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)

    @classmethod
    def delete(cls, data):
        id = {'id': data}
        query = "DELETE FROM courses WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)

    @classmethod
    def get_by_category_id(cls, data):
        query = "SELECT u.first_name as instructor_name, c.* FROM courses as c left join users as u on c.instructor_id = u.id WHERE category_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        #print(results)
        courses = [cls(course) for course in results]
        return courses

    @classmethod
    def get_by_user_id(cls, data):
        query = "SELECT u.first_name as instructor_name, c.* FROM courses as c left join users as u on c.instructor_id = u.id WHERE c.instructor_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            courses = [cls(course) for course in results]
            return courses
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