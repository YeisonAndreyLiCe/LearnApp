from flask_app.config.mysqlconnection import connectToMySQL


class Rol:
    def __init__(self, data):
        self.id = data['id']
        self.rol = data['rol']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def get_roles(cls):
        query = "SELECT * FROM roles;"
        results = connectToMySQL('learn_app').query_db(query)
        roles = []
        for rol in results:
            roles.append(cls(rol))
            print(roles)
        return roles
