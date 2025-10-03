#get all products
from api.base_api import APIClient

class ProductsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def get_all_products(self):
        return self.get(f"{self.base_endpoint}")
    
class ProductByIDAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def get_product_by_id(self, product_id=int):
        if not isinstance(product_id, int) or product_id < 0:
            raise ValueError("product_id must be a positive integer")
        return self.get(f"{self.base_endpoint}/{product_id}")