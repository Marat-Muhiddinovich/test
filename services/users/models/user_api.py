# services/auth/models/api.py
from api.base_api import APIClient
from services.users.models import endpoints, payloads
from config.headers import get_default_headers

class AuthAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)

    def login(self, username, password, expires_in=30):
        data = payloads.login_payload(username, password, expires_in)
        return self.post(endpoints.LOGIN, data=data)

    def get_profile(self, token):
        headers = get_default_headers(token)
        return self.get(endpoints.PROFILE, headers=headers)
