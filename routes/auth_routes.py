from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services.user_service import UserService
from flask_cors import cross_origin

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        
        user = UserService.register_user(username, password, firstname, lastname, email)
        access_token = create_access_token(identity=user.username)
        
        return jsonify({
            'message': 'User registered successfully',
            'access_token': access_token,
            'user': user.to_dict()
        }), 201
        
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 409
    except Exception as e:
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    try:
        identifier = data['identifier']  # Username or email
        password = data['password']

        user = UserService.login_user(identifier, password)
        if user:
            access_token = create_access_token(identity=user.username)
            return jsonify({
                'message': 'Login successful', 
                'access_token': access_token, 
                'user': user.to_dict()
            }), 200
        
        #return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'error': f'Invalid credential'}), 401
        
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'Login failed', 'details': str(e)}), 500

@auth_bp.route('/dashboard', methods=['GET'])
@cross_origin()
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Welcome to the dashboard, {current_user}!'}), 200