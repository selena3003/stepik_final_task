from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN)
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN).click()

    def should_be_correct_product_name(self):

        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGE), "Success message is not present"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_SUCCESS_NAME).text, "Wrong name of te book in the cart"

    def should_be_correct_price(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO_MESSAGE), "Message with the price is not present"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_SUCCESS_PRICE).text, "The prices on the product page and in the message do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"




