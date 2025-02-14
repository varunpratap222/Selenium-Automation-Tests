from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_FIELD, last_name)

    def enter_postal_code(self, postal_code):
        self.enter_text(self.POSTAL_CODE_FIELD, postal_code)

    def continue_checkout(self):
        self.click_element(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click_element(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_confirmation_message(self):
        return self.get_success_message()
