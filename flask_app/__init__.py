from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'super secret key'

app.config['UPLOAD_FOLDER'] = 'flask_app/static/records/'