from flask_app.config.mysqlconnection import connectToMySQL


class Record:
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

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM records;"
        results = connectToMySQL('learn_app').query_db(query)
        records = []
        for record in results:
            records.append(cls(record))
        return records


    @classmethod
    def get_by_id(cls, data):
        id = {'id': data}
        query = "SELECT * FROM records WHERE id = %(id)s;"
        result = connectToMySQL('learn_app').query_db(query, id)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE records SET name = %(name)s, course_id = %(course_id)s, description = %(description)s, record = %(record)s WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, data)

    @classmethod
    def delete(cls, data):
        id = {'id': data}
        query = "DELETE FROM records WHERE id = %(id)s;"
        return connectToMySQL('learn_app').query_db(query, id)

    @staticmethod
    def validate_record(data):
        errors = {}
        if len(data['name']) < 5:
            errors['name'] = 'The field title should have at least 5 characters'
        if len(data['description']) < 15:
            errors['description'] = 'The field description should have at least 15 characters'
        if 'course_record' not in data.files:
            errors['course_record'] = 'The record info field must not be empty'
        record = data.file['course_record']

        if record.filename == '':
            errors['filename'] = 'The file name must not be empty'
        return errors