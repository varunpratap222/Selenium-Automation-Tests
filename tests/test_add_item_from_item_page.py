import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

# Fixture to initialize the WebDriver and open the base URL.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

# Fixture to perform login.
@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver

def test_add_item_from_item_page(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)
    
    # For this test, we first add two items to simulate a pre-existing cart count of 2.
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bike Light")
    
    # Verify that the cart count is 2.
    assert inventory_page.get_cart_item_count() == 2
    
    # Click on the product name to navigate to the product details page.
    inventory_page.click_product("Sauce Labs Onesie")
    
    # On the product details page, use InventoryItemPage to add the item.
    from pages.inventory_item_page import InventoryItemPage
    item_page = InventoryItemPage(driver)
    item_page.add_to_cart()
    
    # Verify that the cart count has increased to 3.
    assert inventory_page.get_cart_item_count() == 3
