from .base_page import BasePage
from .locators import ProductPageLocatiors

import time

class ProductPage(BasePage):

    def get_product_name_message(self):
        time.sleep(0.5)
        elementPNM = self.browser.find_element(*ProductPageLocatiors.PRODUCT_NAME_IN_MESSAGE)
        try:
            elementPNM.is_displayed()
            return elementPNM.text
        except:
            print("PNM is empty")

    def get_product_name_header(self):
        time.sleep(0.5)
        elementPNH = self.browser.find_element(*ProductPageLocatiors.PRODUCT_NAME_IN_PRODUCT_HEADER)
        try:
            elementPNH.is_displayed()
            return elementPNH.text
        except:
            print("PNH is empty")

    def get_product_price_message(self):
        time.sleep(0.5)
        elementPPM = self.browser.find_element(*ProductPageLocatiors.PRICE_MESSAGE)
        try:
            elementPPM.is_displayed()
            return elementPPM.text
        except:
            print("elementPPM is empty")

    def get_product_price_header(self):
        time.sleep(0.5)
        elementPPH = self.browser.find_element(*ProductPageLocatiors.PRICE_HEADER)
        try:
            elementPPH.is_displayed()
            return elementPPH.text
        except:
            print("elementPPH is empty")

    def should_be_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocatiors.ADD_BUTTON), "Add to basket button is not here."
        btn_add_to_basket = self.browser.find_element(*ProductPageLocatiors.ADD_BUTTON)
        btn_add_to_basket.click()

    def should_be_correct_name(self, product_name_header, product_name_message):
        assert product_name_message == product_name_header, "Product names are  not equal"

    def should_be_correct_price(self, product_price_header, product_price_message):
        assert product_price_message == product_price_header, "Product prices are  not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocatiors.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocatiors.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


