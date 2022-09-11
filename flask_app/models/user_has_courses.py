from flask_app.config.mysqlconnection import connectToMySQL


class User_has_Courses:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.course_id = data['course_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_user_id(cls, data):
        query = "FROM learn_app.users_has_courses LEFT JOIN users as user_courses ON users_has_courses.user_id = %(id)s JOIN courses ON user_courses.id = %(id)s;"
        results = connectToMySQL('learn_app').query_db(query, data)
        if results:
            courses = [cls(course) for course in results]
            return courses
        return False