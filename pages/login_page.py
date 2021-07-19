from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        cur_url = self.browser.current_url
        cur_url.index("login"), "Loginis not in url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email input field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password input field is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email input field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), "Register password input field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), "Register re password input field is not presented"
        assert True