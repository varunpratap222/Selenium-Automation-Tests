import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert "/inventory.html" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    assert "Epic sadface" in login_page.get_error_message()
