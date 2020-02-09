from app import app
from flask import request
from flask_api import status


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    data['username']
    data['password']
    # Sanitize the username and password at this step to prevent SQL INJECTION ATTACKS
    # Query the database here for the username and its associated password
    # If the username does not exist, return 400 {with username error message}
    # If the username does exist, check if the passwords match
    # If the passwords do not match, return 400 {with password error message}
    # If the passwords do match, return 200 {with a login cookie to bind to the client}
    # return {'username': data['username'], 'password': data['password']}, status.HTTP_200_OK
    pass


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
    # Sanitize all inputs to prevent SQL INJECTION ATTACKS
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