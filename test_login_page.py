from pages.login_page import LoginPage


def test_guest_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/sk/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
