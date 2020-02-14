from app import app, db
from app.models import User
from config import Config
from flask_api import status
import jwt
import unittest


class UserModelCase(unittest.TestCase):

    def setUp(self):
        self.good_user = User(username=Config.good_test_user, password=Config.good_test_password)
        db.session.add(self.good_user)
        db.session.commit()
        pass

    def tearDown(self):
        User.query.delete()
        db.session.commit()
        pass

    # Login Tests
    def test_login_success(self):
        test_credentials = {'username': Config.good_test_user, 'password': Config.good_test_password}
        with app.test_client() as client:
            response = client.post('/login', json=test_credentials)
            self.assertTrue(status.is_success(response.status_code))
            json_response = response.get_json(force=True)
            decoded_token = jwt.decode(bytes(json_response['token'], "utf-8"), Config.jwt_secret, algorithms=['HS256'])
            self.assertTrue(decoded_token['username'] == Config.good_test_user)

    def test_login_bad_json_fields(self):
        test_credentials = {'Kasikil': 'Pope'}
        with app.test_client() as client:
            response = client.post('/login', json=test_credentials)
            self.assertTrue(status.is_server_error(response.status_code))

    def test_login_no_json(self):
        with app.test_client() as client:
            response = client.post('/login')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_login_failure_bad_username(self):
        test_credentials = {'username': Config.bad_test_user, 'password': Config.bad_test_password}
        with app.test_client() as client:
            response = client.post('/login', json=test_credentials)
            self.assertTrue(status.is_client_error(response.status_code))

    def test_login_failure_bad_password(self):
        test_credentials = {'username': Config.good_test_user, 'password': Config.bad_test_password}
        with app.test_client() as client:
            response = client.post('/login', json=test_credentials)
            self.assertTrue(status.is_client_error(response.status_code))

    def test_login_authenticated_request(self):
        pass

    # Register Tests
    def test_register_success(self):
        test_credentials = {'username': Config.new_user, 'password': Config.new_password}
        with app.test_client() as client:
            response = client.post('/register', json=test_credentials)
            self.assertTrue(status.is_success(response.status_code))
            json_response = response.get_json(force=True)
            decoded_token = jwt.decode(bytes(json_response['token'], "utf-8"), Config.jwt_secret, algorithms=['HS256'])
            self.assertTrue(decoded_token['username'] == Config.new_user)

    def test_register_no_json(self):
        with app.test_client() as client:
            response = client.post('/registers')
            self.assertTrue(status.is_client_error(response.status_code))

    def test_register_bad_json(self):
        test_credentials = {'Kasikil': 'Pope'}
        with app.test_client() as client:
            response = client.post('/register', json=test_credentials)
            self.assertTrue(status.is_server_error(response.status_code))

    def test_register_existing_user(self):
        test_credentials = {'username': Config.good_test_user, 'password': Config.good_test_password}
        with app.test_client() as client:
            response = client.post('/register', json=test_credentials)
            self.assertTrue(status.is_client_error(response.status_code))



if __name__ == '__main__':
    unittest.main(verbosity=2)
