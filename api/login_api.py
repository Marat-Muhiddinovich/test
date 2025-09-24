from api.base_api import APIClient

class LoginAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/auth"

    def login(self, username: str, password: str, expiresInMins: int = 60):
        payload = {
            "username": username,
            "password": password,
            "expiresInMins": expiresInMins
        }   
        return self.post(f"{self.base_endpoint}/login", data=payload)
    
    def get_profile(self, token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        return self.get(f"{self.base_endpoint}/me", headers=headers)