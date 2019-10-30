from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Success message is presented, but should not be"

    def should_be_message_about_emptyness(self):
        try:
            element_pnm = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MSG)
        except:
            print("PNM is empty")
        message = element_pnm.text
        assert "empty" in message
