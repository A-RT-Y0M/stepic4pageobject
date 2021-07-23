from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def successful_addition_to_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE)
        self.true_expectation(product_price, product_basket_price)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_NAME)
        self.true_expectation(product_name, product_basket_name)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
    def disappeared(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_MESSAGE), "Element is not disappeared"