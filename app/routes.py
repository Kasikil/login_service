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
        if json_response['password'] == data['password']:
            # TODO: Make a login cookie, whatever that is
            return {'': ''}, status.HTTP_200_OK
        else:
            return {'error': 'Password entered does not match the record'}, status.HTTP_400_BAD_REQUEST
    return {'error': 'Something went wrong. You shouldn\'t be here'}, status.HTTP_500_INTERNAL_SERVER_ERROR


@app.route('/logout', methods=['POST'])
def logout():
    # Lookup what logging out means. Probably something with returning 
    # a new expired cookie or a null cookie or who knows what they want here
    pass


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    data['username']
    data['password']
    data['email']
    # Query the database to check if username exists
    # If username exists, return 400 {with username taken error message}
    # If username does not exist, attempt to save data to the database
    # If saving to the database succeeds, return 200
    # If saving to the database fails, return 500 {something on our end went wrong}
    pass


@app.route('/reset', methods=['POST'])
def reset():
    # Implementation TBD
    pass
