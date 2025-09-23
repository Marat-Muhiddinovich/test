from api.api_client import APIClient

class UsersAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"   

    def get_all_users(self):
        return self.get(self.base_endpoint) 

class LoginAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/auth/login"

    def login(self, username: str, password: str, expiresInMins: int = 60):
        payload = {
            "username": username,
            "password": password,
            "expiresInMins": expiresInMins
        }   
        return self.post(self.base_endpoint, data=payload)