from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from routes.auth_routes import auth_bp
from models.user_model import db  # Import db from your model
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)

# Initialize extensions with app
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def hello():
    return jsonify({'message': 'API is working!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)