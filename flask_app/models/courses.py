from flask_app.config.mysqlconnection import connectToMySQL

class Course:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['name']
        self.description = data['description']
        self.description = data['instructor_id']
        self.description = data['category_id']
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
        query = "INSERT INTO courses (name, description, instructor_id, category_id) VALUES (%(name)s, %(description)s, %(instructor_id)s,%(category_id)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
        id = {'id': data}
        query = "SELECT * FROM courses WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        return cls(result[0])
    @classmethod
    def update(cls, data):
        query = "UPDATE courses SET name = %(name)s, description = %(description)s, instructor_id=%(instructor_id)s, category_id=%(categoryy_id)s  WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = { 'id': data }
        query = "DELETE FROM courses WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)