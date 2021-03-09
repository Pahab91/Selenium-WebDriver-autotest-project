from selenium.common.exceptions import NoSuchFrameException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)  # how как искать (css, id, xpath и тд)
        except "NoSuchElementException":     # what что искать (строку-селектор)
            return False
        return True
