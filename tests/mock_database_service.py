from config import Config


def mocked_requests_database_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == str(Config['database_url'] + 'login'):
        return MockResponse({'username': 'Psweet', 'password': 'dollas'}, 200)
    elif args[1] == str(Config['database_url'] + 'register'):
        pass

    return MockResponse(None, 404)
