from app import app
from config import Config
from datetime import datetime, timedelta
from flask_api import status
import json
import unittest
from tests.mock_database_service import mocked_requests_database_post
from unittest import mock


class UserModelCase(unittest.TestCase):
    # Standard method
    def test_feature_example_pass_or_fail(self):
        pass

    @mock.patch('app.routes.requests.post', side_effect=mocked_requests_database_post)
    def test_login_success(self, mock_post):
        test_creds = {'username': Config.good_test_user, 'password': Config.good_test_password}
        with app.test_client() as client:
            response = client.post('/login', json=test_creds)
            # TODO: Verify cookie for successful login - self.assertEqual() or such
            self.assertTrue(status.is_success(response.status_code))

    @mock.patch('app.routes.requests.post', side_effect=mocked_requests_database_post)
    def test_login_failure_bad_username(self, mock_post):
        bad_creds = {'username': Config.bad_test_user, 'password': Config.bad_test_password}
        with app.test_client() as client:
            response = client.post('/login', data=bad_creds)
            self.assertTrue(status.is_client_error(response.status_code))

    @mock.patch('app.routes.requests.post', side_effect=mocked_requests_database_post)
    def test_login_failure_bad_password(self, mock_post):
        bad_creds = {'username': Config.good_test_user, 'password': Config.bad_test_password}
        with app.test_client() as client:
            response = client.post('/login', data=bad_creds)
            self.assertTrue(status.is_client_error(response.status_code))

    # TODO: Test authentication of the requester on login route


"""
    # Test several of these methods for different failure cases
    def test_login_failure(self):
        bad_creds = {}
        with app.test_client() as client:
            response = client.post('/login', data=bad_creds)
            self.assertTrue(status.is_client_error(response.status_code))


    def test_logout_success(self):
        with app.test_client() as client:
            response = client.post('/logout')
"""


if __name__ == '__main__':
    unittest.main(verbosity=2)
