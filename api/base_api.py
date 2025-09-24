class APIClient:
    def __init__(self, context):
        self.context = context

    def get(self, endpoint: str, headers: dict = None):
        return self.context.get(endpoint, headers=headers)
    
    def post(self, endpoint: str, data: dict, headers: dict = None):
        return self.context.post(endpoint, data=data, headers=headers)
        
    def put(self, endpoint: str, data: dict):
        return self.context.put(endpoint, data=data)
    
    def delete(self, endpoint: str):
        return self.context.delete(endpoint)