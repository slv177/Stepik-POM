from pages.product_page import ProductPage
import pytest

# @pytest.mark.parametrize('promo',["offer0","offer1",\
#                                   "offer2","offer3","offer4","offer5","offer6",\
#                                   pytest.param("offer7", marks=pytest.mark.xfail),"offer8","offer9"])
# def test_guest_can_add_product_to_basket(browser, promo):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_added_to_basket()
#     page.solve_quiz_and_get_code()
#
#     browser.implicitly_wait(5)
#     print(link)
#     product_name_in_header = page.get_product_name_header()
#     product_name_in_message = page.get_product_name_message()
#     page.should_be_correct_name(product_name_in_header, product_name_in_message)
#
#     product_price_in_header = page.get_product_price_header()
#     product_price_in_message = page.get_product_price_message()
#     page.should_be_correct_price(product_price_in_header, product_price_in_message)

@pytest.mark.xfail(reason="lesson4-3-6")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_messag(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="lesson4-3-6")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_disappeared_success_message()
