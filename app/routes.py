from app import app
from config import Config
from flask import request
from flask_api import status
import jwt
from app.models import User
import requests


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    try:
        json_pack = {'username': data['username'], 'password': data['password']}
    except KeyError as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    try:
        login_user = User.query.filter_by(username=json_pack['username']).first()
    except Exception as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    if login_user is None:
        return {'error': 'No matched user found'}, status.HTTP_400_BAD_REQUEST
    if login_user.check_password(json_pack['password']):
        jwt_content = {'id': login_user.id, 'username': login_user.username}
        token = jwt.encode(jwt_content, Config.jwt_secret, algorithm='HS256')
        return {'token': token}, status.HTTP_200_OK
    else:
        return {'error': 'Password entered does not match the record'}, status.HTTP_400_BAD_REQUEST


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    try:
        json_pack = {'username': data['username'], 'password': data['password']}
    except KeyError as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    # Query the database to check if username exists
    # TODO: Talk to Strum. Single database call or multiple database call to validate username, email, etc?
    try:
        response = requests.post(Config.database_url + 'register', json=json_pack)
    except Exception as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    if status.is_server_error(response.status_code):
        return {'error': 'Error in saving data to the database'}, status.HTTP_500_INTERNAL_SERVER_ERROR
    json_response = response.json()
    if 'error' in json_response:
        return {'error': json_response['error']}, status.HTTP_400_BAD_REQUEST
    else:
        return {'': ''}, status.HTTP_200_OK


@app.route('/logout', methods=['POST'])
def logout():
    # Lookup what logging out means. Probably something with returning
    # a new expired cookie or a null cookie or who knows what they want here
    pass


@app.route('/reset', methods=['POST'])
def reset():
    # Implementation TBD
    pass
