from flask_app.config.mysqlconnection import connectToMySQL

class Role:
    def __init__(self, data):
        self.id = data['id']
        self.role = data['role']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM roles;"
        results = connectToMySQL('learn_app').query_db(query)
        print(results)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def get_by_id(cls, data):
        data = {'id': data}
        query = "SELECT role FROM roles WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, data)
        return result[0]['role']