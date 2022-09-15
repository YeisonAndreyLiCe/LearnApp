from flask_app.models.user import User
from flask_app.models.course import Course
from flask_app.models.category import Category
from flask_app.models.record import Record
from flask_bcrypt import Bcrypt 
from flask_app import app

bcrypt = Bcrypt(app)

users = [{'first_name': 'Mariana', 'last_name': 'Mesa', 'birth_date': '2000-10-04', 'role_id': '1'},
        {'first_name': 'Juan', 'last_name': 'Camilo', 'birth_date': '1990-01-01', 'role_id': '1'},
        {'first_name': 'Marcelo', 'last_name': 'coding', 'birth_date': '1995-01-01', 'role_id': '1'},
        {'first_name': 'Yeison', 'last_name': 'Liscano', 'birth_date': '2001-01-01', 'role_id': '1'},
        {'first_name': 'Vanessa', 'last_name': 'Bedoya', 'birth_date': '2000-01-01', 'role_id': '2'},
        {'first_name': 'John', 'last_name': 'coding', 'birth_date': '1990-01-01', 'role_id': '3'},
        ]

categories = [{"name":"English", "description":"In this category you'll learn to love the English!!", "image":"english_learnapp.png"},
            {"name":"Français", "description":"Dans cette catégorie, vous apprendrez la belle langue du français. !!","image":"français_learnapp.png"},
            {"name":"Web Development", "description":"Here you'll become full-stack developer using Python and JavaScript frameworks","image":"webdev_learnapp.png"},
            {"name":"Data Science", "description":"In this category you'll develope the thinking process to analyze data, and likely you'd create algorithms that would simplify our lives!","image":"data_science.png"},]

courses = [
        {"name":"Python", "description":"Python is a programming language that lets you work quickly and integrate systems more effectively." ,"category_id":"3","instructor_id":"1","image":"python.png"},
        {"name":"JavaScript", "description":"JavaScript is a programming language that adds interactivity to your website.", "category_id":"3","instructor_id":"2","image":"js.png"},
        {"name":"Machine Learning", "description":"Machine learning is the study of computer algorithms that improve automatically through experience.", "category_id":"4","instructor_id":"4","image":"machine_learning.png"},
        {"name":"Data Analysis", "description":"Data analysis is a process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, suggesting conclusions, and supporting decision-making.", "category_id":"4","instructor_id":"4","instructor_id":"4","image":"data-science.png"},
        {"name":"Data Visualization", "description":"Data visualization is the presentation of data in a pictorial or graphical format. It enables decision makers to see analytics presented visually, so they can grasp difficult concepts or identify new patterns.", "category_id":"4","instructor_id":"3","image":"datascience.jpg"},
        {"name":"Data Science", "description":"Data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from many structural and unstructured data.", "category_id":"4","instructor_id":"3","image":"datascience.jpg"},
        {"name":"Data Mining", "description":"Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.", "category_id":"4","instructor_id":"3","image":"datascience.jpg"},
        {"name":"Data Engineering", "description":"Data engineering is the practice of collecting, storing, processing, and analyzing data to extract useful information.", "category_id":"4","instructor_id":"3","image":"datascience.jpg"}]

""" records = [{"user_id":"1","course_id":"1"},
        {"user_id":"1","course_id":"2"},
        {"user_id":"1","course_id":"3"},] """

records_info = [
                {"name":"PythonI", "description":"Python is a programming language that lets you work    quickly and integrate systems more effectively." ,"course_id":"1","record":"calculo_de_pi_py.png"},
                {"name":"Python2", "description":"In this class you'll learn the logic we can implement to calculate pi using Python", "course_id":"1","record":"calculo_de_pi.webm"},
                {"name":"JavaScript", "description":"JavaScript is a programming language that adds interactivity to your website.", "course_id":"2","record":"switch_js.png"},
                {"name":"Machine Learning", "description":"Machine learning is the study of computer algorithms that improve automatically through experience.", "course_id":"3","record":"machine_learning.png"},]

if __name__ == '__main__':
    for user in users:
        user['email'] = user['first_name'][0].lower() + user['last_name'].lower()+ '@learnapp.com'
        user['password'] = user['first_name'][0].upper() + user['last_name'].lower() + '123'
        user['password'] = bcrypt.generate_password_hash(user['password']) 
        User.save(user)
    for category in categories:
        Category.save(category)
    for course in courses:
        Course.save(course)
    for record in records_info:
        Record.save(record)    