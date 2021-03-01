import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    site_language = request.config.getoption("language")
    browser = None
    if site_language == "ru":
        print("\nstart Russian version site for test..")
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
    elif site_language == "es":
        print("\nstart Spanish version site for test..")
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
        browser.get(link)
    elif site_language == "fr":
        print("\nstart France version site for test..")
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
        browser.get(link)
    elif site_language == "en":
        print("\nstart English version site for test..")
        browser = webdriver.Chrome()
        link = "http://selenium1py.pythonanywhere.com/en/catalogue/coders-at-work_207/"
        browser.get(link)
    else:
        raise pytest.UsageError("--language should be ru, fr, en or es")
    yield browser
    print("\nquit browser..")
    browser.quit()
