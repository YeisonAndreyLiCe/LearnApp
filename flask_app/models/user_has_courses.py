from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.course import Course


class User_has_Courses:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.course_id = data['course_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.name_course = data['name_course']

    @classmethod
    def get_by_user_id(cls, data):
        query = "SELECT c.name as name_course, u.* FROM users_has_courses as u LEFT JOIN courses as c on u.course_id = c.id where u.user_id = %(id)s"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            courses = [cls(course) for course in results]
            return courses
        return False
    
    @classmethod
    def get_enrolled_courses(cls, data):
        data = {'user_id': data} 
        query = "SELECT * FROM users_has_courses WHERE user_id = %(user_id)s;"
        #results = connectToMySQL('learn_app').query_db(query, self.__dict__)
        results = connectToMySQL('learn_app').query_db(query, data)
        print('*'*100)
        print(results)
        courses = [Course(result) for result in results]
        return courses

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