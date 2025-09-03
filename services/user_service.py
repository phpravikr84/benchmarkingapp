from models.user_model import User
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

class UserService:
    @staticmethod
    def register_user(username, password, firstname, lastname, email):
        # Check if username or email already exists
        if User.find_by_username_or_email(username):
            raise ValueError('Username already exists')
        if User.find_by_username_or_email(email):
            raise ValueError('Email already exists')
        
        # Create user (password is hashed in the model)
        user = User.create_user(
            username=username,
            password=password,  # Pass plain password, model will hash it
            firstname=firstname,
            lastname=lastname,
            email=email
        )
        return user

    @staticmethod
    def login_user(identifier, password):
        user = User.find_by_username_or_email(identifier)
        
        if user:
            # Directly use check_password_hash instead of the method
            if check_password_hash(user.password, password):
                return user
        return None