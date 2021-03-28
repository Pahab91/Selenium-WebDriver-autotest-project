from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"] h2')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"] h2')


class ProductPageLocators():
    CHART_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_PAGE_LINK = (By.CSS_SELECTOR, '[id="write_review"]')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, 'div h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '[class="price_color"]')
    SHOULD_BE_ADDED_TO_THE_CART = (By.CSS_SELECTOR, 'div :nth-last-of-type(3) div strong')
    CORRECT_PRICE_HAS_BEEN_ADDED = (By.CSS_SELECTOR, '[class="alertinner "] :nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[class="alertinner "]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")