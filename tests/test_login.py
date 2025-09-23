import pytest
from api.users_api import LoginAPI
import json

@pytest.mark.api
def test_login(api_context):
    login_api = LoginAPI(api_context)
    response = login_api.login(
        username="emilys", 
        password="emilyspass",
        expiresInMins=30
    )

    assert response.status == 200
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))
    assert "accessToken" in data
    assert data["accessToken"] is not None
    print(f"Login successful, accessToken: {data['accessToken']}")
   
    assert data["username"] == "emilys"
    assert data["email"] == "emily.johnson@x.dummyjson.com"
