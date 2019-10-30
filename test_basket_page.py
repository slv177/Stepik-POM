from pages.basket_page import BasketPage


def test_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_empty_basket()
    page.should_be_message_about_emptyness()
