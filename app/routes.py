from app import app, db
from config import Config
from datetime import datetime, timedelta
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
        return {'error': '{} is an invalid key'.format(str(e))}, status.HTTP_500_INTERNAL_SERVER_ERROR
    login_user = User.query.filter_by(username=json_pack['username']).first()
    if login_user is None:
        return {'error': 'No matched user found'}, status.HTTP_400_BAD_REQUEST
    if login_user.check_password(json_pack['password']):
        expire_time = datetime.timestamp(datetime.now() + timedelta(Config.cookie_expiration_time))
        jwt_content = {'id': login_user.id, 'username': login_user.username, 'expires': expire_time}
        token_bytes = jwt.encode(jwt_content, Config.jwt_secret, algorithm='HS256')
        token = token_bytes.decode("utf-8")
        return {'token': token}, status.HTTP_200_OK
    else:
        return {'error': 'Password entered does not match the record'}, status.HTTP_400_BAD_REQUEST


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    try:
        json_pack = {'username': data['username'], 'password': data['password']}
    except KeyError as e:
        return {'error': '{} is an invalid key'.format(str(e))}, status.HTTP_500_INTERNAL_SERVER_ERROR
    existing_user = User.query.filter_by(username=json_pack['username']).first()
    if existing_user is not None:
        return {'error': 'Username already taken: {}'.format(json_pack['username'])}, status.HTTP_406_NOT_ACCEPTABLE
    new_user = User(username=json_pack['username'], password=json_pack['password'])
    db.session.add(new_user)
    db.session.commit()
    expire_time = datetime.timestamp(datetime.now() + timedelta(Config.cookie_expiration_time))
    jwt_content = {'id': new_user.id, 'username': new_user.username, 'expires': expire_time}
    token_bytes = jwt.encode(jwt_content, Config.jwt_secret, algorithm='HS256')
    token = token_bytes.decode("utf-8")
    return {'token': token}, status.HTTP_200_OK


@app.route('/logout', methods=['POST'])
def logout():
    # Lookup what logging out means. Probably something with returning
    # a new expired cookie or a null cookie or who knows what they want here
    pass


@app.route('/reset', methods=['POST'])
def reset():
    return {'error': 'Route not implemented'}, status.HTTP_501_NOT_IMPLEMENTED
