from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)  # Changed from String to Text
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def find_by_username_or_email(identifier):
        # Search by username OR email
        return User.query.filter(
            (User.username == identifier) | (User.email == identifier)
        ).first()

    @staticmethod
    def create_user(username, password, firstname, lastname, email, status='active'):
        # Hash the password before storing
        hashed_password = generate_password_hash(password)
        user = User(
            username=username,
            password=hashed_password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            status=status
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'status': self.status
        }