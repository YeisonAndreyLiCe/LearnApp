from flask_app.config.mysqlconnection import connectToMySQL


class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Metodo para guardar categorias
    @classmethod
    def save(cls, data):
        query = "INSERT INTO categories (name, description) VALUES (%(name)s, %(descrition)s);"
        return connectToMySQL('learn_app').query_db(query, data)

    # Metodo para traer todas las categorias
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ctaegories"
        return connectToMySQL('learn_app').query_db(query)

    # Metodo para traer la información de una sola categoria
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM categories WHERE id = %(id)s"
        result = connectToMySQL('learn_app').query_db(query, data)
        return result

    # Metodo para editar una categoria
    @classmethod
    def update(cls, data):
        query = "UPDATE categories SET name = %(name)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)

    # Metodo para eliminar una categoria
    @classmethod
    def delete(cls, data):
        id = {'id': data}
        query = "DELETE FROM categories WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)

    # Metodo para validar la información que se está enviando a la base de datos
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['name']) < 2:
            errors['name'] = 'The field name should have at least 2 characters'
        if len(data['description']) < 2:
            errors['description'] = 'The field description should have at least 2 characters'
        return errors
