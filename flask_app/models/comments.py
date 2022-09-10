from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.course_id = data['course_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        results = connectToMySQL('learn_app').query_db(query)
        comments = []
        for comment in results:
            comments.append(cls(comment))
        return comments
    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (comment, user_id, message_id) VALUES (%(title)s, %(comment)s, %(user_id)s, %(course_id)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def get_by_id(cls, data):
        id = { 'id': data }
        query = "SELECT * FROM comments WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        return cls(result[0])
    @classmethod
    def update(cls, data):
        query = "UPDATE comments SET title = %(title)s, comment = %(comment)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    @classmethod
    def delete(cls, data):
        id = { 'id': data }
        query = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['title']) < 2:
            errors['title'] = 'The field title should have at least 2 characters'
        if len(data['comment']) < 10:
            errors['comment'] = 'The field comment should have at least 10 characters'
        return errors