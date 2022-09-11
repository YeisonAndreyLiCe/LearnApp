from flask_app import app
from flask import session
from flask_app.controllers import pruebasestilo
from flask_app.controllers import users_controller

if __name__ == '__main__':
    app.run(debug=True)
