#get all products
from api.base_api import APIClient

class ProductsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def get_all_products(self):
        return self.get(f"{self.base_endpoint}")
    
# get product by ID
class ProductByIDAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def get_product_by_id(self, product_id=int):
        if not isinstance(product_id, int) or product_id < 0:
            raise ValueError("product_id must be a positive integer")
        return self.get(f"{self.base_endpoint}/{product_id}")
# search products
class SearchProductsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"
    
    def search_products(self, search_item=str):
        if not isinstance(search_item, str) or not search_item.strip():
            raise ValueError("search_item must be a non-empty string")
        return self.get(f"{self.base_endpoint}/search?q={search_item}")
    
# limit products
class LimitProductsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def limit_products(self, limit=int, skip=int, select=str):
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("limit must be a positive integer")
        if not isinstance(skip, int) or skip <= 0:
            raise ValueError("skip must be a positive integer")
        if not isinstance(select, str) or not select.strip():
            raise ValueError("select must be a non-empty string")
        return self.get(f"{self.base_endpoint}?limit={limit}&skip={skip}&select={select}")
    
# sort products
class SortProductsAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"
    
    def sort_products(self, sort_by=str):
        if not isinstance(sort_by, str) or not sort_by.strip():
            raise ValueError("sort_by must be a non-empty string")
        return self.get(f"{self.base_endpoint}?ordering={sort_by}")
    
#categories of products
class CategoriesAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products/category"

    def get_single_category(self, category_name=str):
        if not isinstance(category_name, str) or not category_name.strip():
            raise ValueError("category_name must be a non-empty string")
        return self.get(f"{self.base_endpoint}/{category_name}")
    
# add new product
class AddProductAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products/add"

    def add_product(self, product_data=dict):
        if not isinstance(product_data, dict) or not product_data:
            raise ValueError("product_data must be a non-empty dictionary")
        return self.post(self.base_endpoint, data=product_data)
    
# update product
class UpdateProductAPI(APIClient):
    def __init__(self, context):
        super().__init__(context)
        self.base_endpoint = "/products"

    def update_product(self, product_id=int, update_data=dict):
        if not isinstance(product_id, int) or product_id > 0:
            raise ValueError("product_id must be a positive integer")
        if not isinstance(update_data, dict) or not update_data:
            raise ValueError("update_data must be a non-empty dictionary")
        return self.put(f"{self.base_endpoint}/{product_id}", data=update_data)