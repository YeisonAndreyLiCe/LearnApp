from flask_app.config.mysqlconnection import connectToMySQL


class Records:
    def __init__(self, data):
        self.name = data['id']
        self.name = data['name']
        self.course_id = data['course_id']
        self.description = data['description']
        self.record = data['record']
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO records (name,course_id,description,record) VALUES (%(name)s,%(course_id)s,%(descrition)s,%(record)s);"
        return connectToMySQL('learn_app').query_db(query, data)
        

