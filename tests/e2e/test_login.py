import re
pytestmark = pytest.mark.e2e
from playwright.sync_api import Page, expect
from framework.config import UI_BASE_URL, SAUCE_USER, SAUCE_PASSWORD

@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page):
    page.goto(UI_BASE_URL)
    page.get_by_placeholder("Username").fill(SAUCE_USER)
    page.get_by_placeholder("Password").fill(SAUCE_PASSWORD)
    page.get_by_test_id("login-button").click()
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator("[data-test='title']")).to_have_text("Products")

def test_login_with_invalid_password_shows_error_message(page: Page):
    page.goto(UI_BASE_URL)
    page.get_by_test_id("username").fill(SAUCE_USER)
    page.get_by_test_id("password").fill("whatever")
    page.get_by_test_id("login-button").click()
    error = page.get_by_test_id("error")
    expect(error).to_be_visible()
    expect(error).to_contain_text("do not match")
    expect(page).to_have_url(UI_BASE_URL + "/")
