from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.course import Course


class User_has_Courses:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.course_id = data['course_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_enrolled_courses(cls, data):
        id = {'id': data}
        query = "SELECT courses.* FROM courses LEFT JOIN users_has_courses ON courses.id = users_has_courses.course_id WHERE users_has_courses.user_id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, id)
        if results:
            return [Course(course) for course in results]
        return False
    @classmethod
    def enroll_course(cls, data):
        query = "INSERT INTO users_has_courses (user_id, course_id) VALUES (%(user_id)s, %(course_id)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @staticmethod
    def validate(data):
        errors={}
        query='SELECT * FROM users_has_courses WHERE course_id=%(course_id)s and user_id=%(user_id)s'
        result=connectToMySQL('learn_app').query_db(query,data)
        if result :
            errors['enroll_course']='You have already enroll this course'
        return errors