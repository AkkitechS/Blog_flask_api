from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required
from app.models.users import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/signup', methods=['POST', 'PUT'])
def signup_update_user():
    try:
        if request.method == 'POST':
            username = request.json.get('username')
            password = request.json.get('password')
            email = request.json.get('email')
            print(username, password, email)
            return jsonify({'username': username, 'password': password, 'email': email})
        else:
            return jsonify({'username': '', 'password': '', 'email': ''})
    except Exception as e:
        return jsonify({'username': '', 'password': '', 'email': ''})

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(user.to_dict() for user in users)