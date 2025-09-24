import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.settings import BASE_URL, USERNAME, PASSWORD, EXPIRES_IN
from api.login_api import LoginAPI
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
    context = playwright.request.new_context(
        base_url = BASE_URL,
        extra_http_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"  
        }
    )
    yield context
    context.dispose()

@pytest.fixture(scope="session")
def auth_token(api_context):
    login_api = LoginAPI(api_context)
    response = login_api.login(USERNAME, PASSWORD, EXPIRES_IN)
    token = response.json()["accessToken"]
    return token