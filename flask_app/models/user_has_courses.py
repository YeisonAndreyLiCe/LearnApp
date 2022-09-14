from flask_app.config.mysqlconnection import connectToMySQL


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