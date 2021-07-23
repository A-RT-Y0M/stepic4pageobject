from selenium.webdriver.common.by import By

#class MainPageLocaters():

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators():
    PRODUCT_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")

    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 > h1")
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "div.alert div.alertinner")