import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
    context = playwright.request.new_context(
        base_url = "https://dummyjson.com",
        extra_http_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"  
        }
    )
    yield context
    context.dispose()
    return context