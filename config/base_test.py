# config/base_test.py
import pytest # type: ignore
import os
from playwright.sync_api import Playwright # type: ignore
from config.settings import BASE_URL

class BaseTest:
    """Base class for API tests."""

    @pytest.fixture(autouse=True)
    def setup(self, playwright: Playwright):
        base_url = BASE_URL
        self.api_context = playwright.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        yield
        self.api_context.dispose()
