from pages.product_page import ProductPage
from pages.locators import ProductPageLocatiors

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_price()
