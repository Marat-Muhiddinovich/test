#get all products test
import pytest # type: ignore
from api.products_api import ProductsAPI
from api.products_api import ProductByIDAPI
from api.products_api import SearchProductsAPI
from api.products_api import LimitProductsAPI
from api.products_api import SortProductsAPI
from api.products_api import CategoriesAPI
from api.products_api import AddProductAPI
from api.products_api import UpdateProductAPI

#get all products test
@pytest.mark.api
def test_get_all_products(api_context):
    products_api = ProductsAPI(api_context)
    response = products_api.get_all_products()
    assert response.status == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0
    assert "total" in data
    print(f"Total products: {data['total']}")

# search products test
@pytest.mark.api
def test_search_products(api_context):
    search_item = "Essence"  
    search_api = SearchProductsAPI(api_context)
    response = search_api.search_products(search_item)
    assert response.status == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0
    for product in data["products"]:
        assert search_item.lower() in product["title"].lower() or search_item.lower() in product.get("description", "").lower()
    print(f"Found {len(data['products'])} products matching '{search_item}'")

# limit products test
def test_limit_products(api_context):
    limit = 5
    skip = 5
    select = "title,price, category"
    limit_api = LimitProductsAPI(api_context)
    response = limit_api.limit_products(limit, skip, select)
    assert response.status == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) == limit
    for product in data["products"]:
        assert "title" in product
        assert "price" in product
        assert len(product) == len(data["products"][0])  
    print(f"Retrieved {len(data['products'])} products with fields: {select}")

# sort products test
def test_sort_products(api_context):
    sort_by = "-price"
    sort_api = SortProductsAPI(api_context)
    response = sort_api.sort_products(sort_by)
    assert response.status == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0
    print(f"Products sorted by {sort_by} in ascending order.")
    prices = [product["price"] for product in data["products"] if "price" in product]
    print("Prices in ascending order:", prices)

categories = [
     "beauty",
  "fragrances",
  "furniture",
  "groceries",
  "home-decoration",
  "kitchen-accessories",
  "laptops",
  "mens-shirts",
  "mens-shoes",
  "mens-watches",
  "mobile-accessories",
  "motorcycle",
  "skin-care",
  "smartphones",
  "sports-accessories",
  "sunglasses",
  "tablets",
  "tops",
  "vehicle",
  "womens-bags",
  "womens-dresses",
  "womens-jewellery",
  "womens-shoes",
  "womens-watches"
]

# categories of products test
@pytest.mark.parametrize("category_name", categories)
def test_get_single_category(api_context, category_name):
    categories_api = CategoriesAPI(api_context)
    response = categories_api.get_single_category(category_name)
    assert response.status == 200
    data = response.json()
    assert isinstance(data["products"], list)
    assert len(data) > 0
    for product in data["products"]:
        assert product["category"] == category_name
    print(f"Found {len(data['products'])} products in category '{category_name}'")
    print("titles:", [product["title"] for product in data["products"]])

# add new product test
def test_add_product(api_context):
    new_product = {
        "title": "macbook pro",
        "description": "Apple MacBook Pro 2021 with M1 Pro chip",
        "price": 1999,
        "discountPercentage": 10.0,
        "rating": 4.8,
        "stock": 50,
        "brand": "Apple",
        "category": "laptops",
        "thumbnail": "https://example.com/macbookpro.jpg",
        "images": [ 
            "https://example.com/macbookpro1.jpg",
            "https://example.com/macbookpro2.jpg"
        ],
    }

    product = AddProductAPI(api_context)
    response = product.add_product(new_product)
    assert response.status == 200 or response.status == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_product["title"]
    assert data["price"] == new_product["price"]
    assert data["category"] == new_product["category"]
    print(f"Added new product with ID: {data['id']}, Title: {data['title']}, Price: {data['price']}")

# update product test
def test_update_product(api_context):
    product_id = 194,
    update_data = {
        "price": 1799,
        "stock": 30
    }
    update_api = UpdateProductAPI(api_context)
    response = update_api.update_product(product_id, update_data)
    assert response.status == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["price"] == update_data["price"]
    assert data["stock"] == update_data["stock"]
    print(f"Updated product ID: {data['id']}, New Price: {data['price']}, New Stock: {data['stock']}")