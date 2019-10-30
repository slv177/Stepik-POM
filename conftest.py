import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', default="en", help="Choose language.")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print(user_language)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser (10)..")
    time.sleep(12)
    browser.quit()
