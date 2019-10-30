from .base_page import BasePage
from .locators import ProductPageLocatiors

import time


class ProductPage(BasePage):

    def get_product_name_message(self):
        time.sleep(0.5)
        product_name_message = self.browser.find_element(*ProductPageLocatiors.PRODUCT_NAME_IN_MESSAGE)
        try:
            product_name_message.is_displayed()
            return product_name_message.text
        except:
            print("PNM is empty")

    def get_product_name_header(self):
        time.sleep(0.5)
        product_name_header = self.browser.find_element(*ProductPageLocatiors.PRODUCT_NAME_IN_PRODUCT_HEADER)
        try:
            product_name_header.is_displayed()
            return product_name_header.text
        except:
            print("PNH is empty")

    def get_product_price_message(self):
        time.sleep(0.5)
        product_price_message = self.browser.find_element(*ProductPageLocatiors.PRICE_MESSAGE)
        try:
            product_price_message.is_displayed()
            return product_price_message.text
        except:
            print("elementPPM is empty")

    def get_product_price_header(self):
        time.sleep(0.5)
        product_price_header = self.browser.find_element(*ProductPageLocatiors.PRICE_HEADER)
        try:
            product_price_header.is_displayed()
            return product_price_header.text
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


