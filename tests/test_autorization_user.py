import requests


class TestUserAuth:
    def test_auth_user(self):
        data = {'email': 'vinkotov@example.com',
                'password': '1234'}

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is no auth cookies in the response"
        assert "x-crsf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json()

