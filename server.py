from flask_app import app
from flask import session
from flask_app.controllers import users_controller
from flask_app.controllers import courses_controller
from flask_app.controllers import categories_controller
from flask_app.controllers import records_controller
from flask_app.controllers import admin_controller

if __name__ == '__main__':
    app.run(debug=True)
