from api.base_api import APIClient

# users API client
class UsersAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"   

    def get_all_users(self):
        return self.get(self.base_endpoint) 

# search users API client
class UserSearchAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users/search"

    def search_users(self, query):
        return self.get(f"{self.base_endpoint}/?q={query}")

# filter users API client
class UserFilterAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users/filter"

    def filter_users(self, key=str, value=str, type=str):
        return self.get(f"{self.base_endpoint}/?key={key}.color&value={value}&type={type}")
    
# limit, skip, filter users API client
class LimitSkipFilterUsersAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"

    def limit_skip_filter_users(self, limit=int, skip=int, ):
        return self.get(f"{self.base_endpoint}?limit={limit}&skip={skip}&select=firstName,lastName,age")
    
# sort users API client
class UserSortAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"

    def sort_users(self, sort_by=str):
        return self.get(f"{self.base_endpoint}?sortBy={sort_by}&order=asc")
    
# get user by ID API client
class UserGetByIDAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"

    def get_user_by_id(self, user_id=int):
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        return self.get(f"{self.base_endpoint}/{user_id}/carts")
    
class GetUserPostsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"

    def get_user_posts(self, user_id=int):
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        return self.get(f"{self.base_endpoint}/{user_id}/posts")    
    
class AddUserAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/users"
        
    def add_user(self, user_data: dict):
        return self.post(f"{self.base_endpoint}/add", data=user_data)
    