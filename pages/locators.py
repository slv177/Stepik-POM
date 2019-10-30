from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocatiors():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    OK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "# messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")
    PRICE_TOTAL = (By.CSS_SELECTOR, "# messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_ITEM = (By.CSS_SELECTOR, "# content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")