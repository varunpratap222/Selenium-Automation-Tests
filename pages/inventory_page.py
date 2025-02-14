from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    CART_ICON = (By.ID, "shopping_cart_container")
    # Add the locator for the menu button (hamburger button)
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    def add_item_to_cart(self, item_name):
        add_button_locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button[contains(.,'Add to cart')]")
        self.click_element(add_button_locator)

    def get_cart_item_count(self):
        badge_locator = (By.CLASS_NAME, "shopping_cart_badge")
        try:
            return int(self.find_element(badge_locator, timeout=5).text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.click_element(self.CART_ICON)

    def click_product(self, product_name):
        product_locator = (By.XPATH, f"//div[text()='{product_name}']")
        self.click_element(product_locator)
        
    def open_menu(self):
        # Wait until the menu button is clickable and then click it.
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        element.click()
