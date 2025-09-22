from playwright.sync_api import sync_playwright, Page

def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/python/docs/intro")
    assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"  
    assert "playwright" in page.url
    page.screenshot(path="example.png")