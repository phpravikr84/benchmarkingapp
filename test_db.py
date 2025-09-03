from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text  # Import text construct
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

with app.app_context():
    db.session.execute(text('SELECT 1'))  # Wrap query in text()
    print("MySQL connection successful!")