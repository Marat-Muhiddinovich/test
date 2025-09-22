import pytest
from api.users_api import UsersAPI

@pytest.mark.api
def test_get_all_users(api_context):
    users_api = UsersAPI(api_context)
    response = users_api.get_all_users()
    assert response.status == 200 
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0
    assert "total" in data

    print(f"Total users: {data['total']}")
