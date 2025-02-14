from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryItemPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    
    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
