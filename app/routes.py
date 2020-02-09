from app import app
from config import Config
from flask import request
from flask_api import status
import requests


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    try:
        json_pack = {'username': data['username']}
    except KeyError as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    # Query the database here for the username and its associated password
    try:
        response = requests.post(Config.database_url + 'login', json=json_pack)
    except Exception as e:
        return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    json_response = response.json()
    # If the username does not exist, return 400 {with username error message}
    if 'username' not in json_response:
        return {'error': 'No matched user found'}, status.HTTP_400_BAD_REQUEST
    # If the username does exist, check if the passwords match
    if 'password' in json_response:
        try:
            if json_response['password'] == data['password']:
                # TODO: Make a login cookie, whatever that is
                return {'': ''}, status.HTTP_200_OK
            else:
                return {'error': 'Password entered does not match the record'}, status.HTTP_400_BAD_REQUEST
        except KeyError as e:
            return {'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR
    return {'error': 'Something went wrong. You shouldn\'t be here'}, status.HTTP_500_INTERNAL_SERVER_ERROR


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    try:
        json_pack = {'username': data['username'], 'password': data['password'], 'email': data['email']}
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
