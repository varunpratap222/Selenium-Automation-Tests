import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.logout_page import LogoutPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver

def test_logout(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)
    
    # Open the menu and perform logout.
    inventory_page.open_menu()
    logout_page = LogoutPage(driver)
    logout_page.logout()
    
    # After logout, you might verify the URL if your app changes it,
    # but a more robust check is to verify that the login form is displayed.
    login_page = LoginPage(driver)
    assert login_page.is_login_form_displayed()
