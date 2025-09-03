from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.user_model import db, User
from services.user_service import UserService

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    # Test registration
    try:
        user = UserService.register_user(
            username='testuser',
            password='testpassword',
            firstname='John',
            lastname='Doe',
            email='john.doe@example.com'
        )
        print(f"Registered user: {user.username}, Email: {user.email}")
    except ValueError as e:
        print(f"Registration error: {e}")

    # Test login with username
    user = UserService.login_user('testuser', 'testpassword')
    if user:
        print(f"Login successful with username: {user.username}")
    else:
        print("Login failed with username")
