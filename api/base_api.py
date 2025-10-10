import allure # type: ignore
from config.headers import get_default_headers
from core.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    def __init__(self, context):
        self.context = context

    @allure.step("Get request to endpoint")
    def get(self, endpoint: str, token: str=None):
        headers = get_default_headers(token)
        logger.info(f"Get {endpoint}")
        response = self.context.get(endpoint, headers=headers)
        logger.info(f"Response: {response.status} - {response.text()}")
        return response
    
    def post(self, endpoint: str, data: dict, headers: dict = None):
        return self.context.post(endpoint, data=data, headers=headers)
        
    def put(self, endpoint: str, data: dict):
        return self.context.put(endpoint, data=data)
    
    def delete(self, endpoint: str):
        return self.context.delete(endpoint)