from app import app
from datetime import datetime, timedelta
from flask_api import status
import unittest


class UserModelCase(unittest.TestCase):
    # Special method
    def setUp(self):
        pass

    # Special method
    def tearDown(self):
        pass
    
    # Standard method
    def test_feature_example_pass_or_fail(self):
        pass

    def test_login_success(self):
        good_creds = {'username': 'Psweet', 'password': 'dollas'}
        with app.test_client() as client:
            response = client.post('/login', data=good_creds)
            self.assertTrue(status.is_success(response.status_code))

    # Test several of these methods for different failure cases
    def test_login_failure(self):
        bad_creds = {}
        with app.test_client() as client:
            response = client.post('/login', data=bad_creds)
            self.assertTrue(status.is_client_error(response.status_code))

    def test_logout_success(self):
        with app.test_client() as client:
            response = client.post('/logout')


if __name__ == '__main__':
    unittest.main(verbosity=2)
