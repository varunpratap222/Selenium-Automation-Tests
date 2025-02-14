import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

# Pytest fixture to initialize and later clean up the WebDriver
@pytest.fixture
def driver():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    # Open the base URL (the SauceDemo website)
    driver.get(BASE_URL)
    # Yield the driver to the test functions so they can use it
    yield driver
    # After the test is finished, close the browser
    driver.quit()

# Test case for a valid login
def test_valid_login(driver):
    # Create an instance of the LoginPage using the driver
    login_page = LoginPage(driver)
    # Call the login method with valid credentials
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    # Verify that the current URL contains '/inventory.html'
    # which indicates a successful login and redirection to the inventory page
    assert "/inventory.html" in driver.current_url

# Test case for an invalid login
def test_invalid_login(driver):
    # Create an instance of the LoginPage using the driver
    login_page = LoginPage(driver)
    # Attempt to login with invalid credentials
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    # Verify that the error message contains "Epic sadface"
    # This confirms that the application displays the correct error for invalid logins
    assert "Epic sadface" in login_page.get_error_message()
