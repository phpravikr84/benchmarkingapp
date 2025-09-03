from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.user_model import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")