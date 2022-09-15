from flask_app.config.mysqlconnection import connectToMySQL
class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image = data['image']
    # Method to create a new category
    @classmethod
    def save(cls, data):
        query = "INSERT INTO categories (name, description, image) VALUES (%(name)s, %(description)s, %(image)s);"
        return connectToMySQL('learn_app').query_db(query, data)
    # Method to get all categories
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM categories"
        results = connectToMySQL('learn_app').query_db(query)
        if results:
            return [cls(result) for result in results]
        return False
    @classmethod
    def get_all_as_dic(cls):
        query = "SELECT name, id FROM categories"
        return connectToMySQL('learn_app').query_db(query)
    
    # Method to get one category
    @classmethod
    def get_by_id(cls, data):
        id = {'id': data}
        query = "SELECT * FROM categories WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        if result:
            return cls(result[0])
        return False
    # Method to update a category
    @classmethod
    def update(cls, data):
        query = "UPDATE categories SET name = %(name)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)
    # Method to delete a category
    @classmethod
    def delete(cls, data):
        id = {'id': data}
        query = "DELETE FROM categories WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)
    # Method to validate category data
    @staticmethod
    def validate(data):
        errors = {}
        if len(data['name']) < 2:
            errors['name'] = 'The field name should have at least 2 characters long'
        if len(data['description']) < 10:
            errors['description'] = 'The field description should have at least 10 characters long'
        return errors
