from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.login
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemaila.org"
        link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link_login)
        page.open()
        page.register_new_user(email, "100Vostok$$Zapad")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_added_to_basket()

        browser.implicitly_wait(5)
        product_name_in_header = page.get_product_name_header()
        product_name_in_message = page.get_product_name_message()
        page.should_be_correct_name(product_name_in_header, product_name_in_message)

        product_price_in_header = page.get_product_price_header()
        product_price_in_message = page.get_product_price_message()
        page.should_be_correct_price(product_price_in_header, product_price_in_message)


@pytest.mark.xfail(reason="lesson4-3-6")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5","offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link_promo = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    page = ProductPage(browser, link_promo)
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()

    browser.implicitly_wait(5)
    product_name_in_header = page.get_product_name_header()
    product_name_in_message = page.get_product_name_message()
    page.should_be_correct_name(product_name_in_header, product_name_in_message)

    product_price_in_header = page.get_product_price_header()
    product_price_in_message = page.get_product_price_message()
    page.should_be_correct_price(product_price_in_header, product_price_in_message)


@pytest.mark.xfail(reason="lesson4-3-6")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_about_emptyness()
