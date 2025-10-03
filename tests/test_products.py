#get all products test
import pytest # type: ignore
from api.products_api import ProductsAPI

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