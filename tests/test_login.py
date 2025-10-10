import pytest # type: ignore
# from api.login_api import LoginAPI
from services.users.models.user_api import AuthAPI
import json
from config.settings import USERNAME, PASSWORD, EXPIRES_IN, FakeUserName, FakePassword

#positive test
@pytest.mark.api
def test_login_valid(api_context):
    login_api = AuthAPI(api_context)
    response = login_api.login(USERNAME, PASSWORD, EXPIRES_IN)
    assert response.status == 200 or response.status == 201
    login_data = response.json()
    print(json.dumps(login_data, indent=4, ensure_ascii=False))
    assert "accessToken" in login_data

def test_get_profile(api_context, auth_token):
    login_api = AuthAPI(api_context)
    response = login_api.get_profile(auth_token)
    assert response.status == 200
    profile_data = response.json()
    assert profile_data["username"] == USERNAME
    assert profile_data["password"] == PASSWORD

#negative test
@pytest.mark.api
def test_login_invalid_credentials(api_context):
    login_api = AuthAPI(api_context)
    response = login_api.login(FakeUserName, FakePassword, EXPIRES_IN)
    assert response.status == 400 or response.status == 401
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))
    assert "message" in data
    print(f"Login failed as expected, message: {data['message']}")
