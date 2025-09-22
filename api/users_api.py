from api.api_client import APIClient

class UsersAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"   

    def get_all_users(self):
        return self.get(self.base_endpoint)    