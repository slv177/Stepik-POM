from .base_page import BasePage
from .locators import ProductPageLocatiors
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_added_to_basket()
        self.should_be_correct_price()

    def should_be_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocatiors.ADD_BUTTON), "Add to basket button is not here."
        btn_add_to_basket = self.browser.find_element(*ProductPageLocatiors.ADD_BUTTON)
        btn_add_to_basket.click()


    def should_be_correct_price(self):
        assert "has been added to your basket." in self.browser.find_element(*ProductPageLocatiors.OK_MESSAGE).text, \
            "-has been added to your basket- message is not here."
        assert self.is_element_present(*ProductPageLocatiors.PRICE_ITEM) == \
            self.is_element_present(*ProductPageLocatiors.PRICE_TOTAL), "Prices are  not equal"

