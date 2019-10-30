from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > button")


class BasketPageLocators():
    BASKET_IS_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner")
    BASKET_CONTENT = (By.CLASS_NAME, ".basket-items")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    REGISTER_PASS_1 = (By.CSS_SELECTOR,"#id_registration-password1")
    REGISTER_PASS_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocatiors():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    OK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME_IN_PRODUCT_HEADER = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")

    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_HEADER = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")