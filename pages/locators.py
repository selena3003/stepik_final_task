from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini a.btn")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    ALERT_INFO_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")
    PRODUCT_SUCCESS_NAME = (By.CSS_SELECTOR, ".alert-success  .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_SUCCESS_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
