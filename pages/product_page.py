from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_link(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PAGE_LINK), 'не прошла проверка на страницу продукта'

    def add_to_chart(self):
        chart = self.browser.find_element(*ProductPageLocators.CHART_BUTTON)  # нужно использовать .browser.find_element
        # иначе будет ошибка bool' object has no attribute 'click'
        chart.click()
        self.solve_quiz_and_get_code()

    def should_be_added_to_the_cart(self):
        book1 = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        self.add_to_chart()
        price = self.browser.find_element(*ProductPageLocators.CORRECT_PRICE_HAS_BEEN_ADDED).text
        book = self.browser.find_element(*ProductPageLocators.SHOULD_BE_ADDED_TO_THE_CART).text
        assert book == book1 or price1 == price, "не добавилась нужная книга или цена не соответствует"

    def should_be_added_to_the_cart_without_capcha(self):
        book1 = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        self.add_to_chart_without_capcha()
        price = self.browser.find_element(*ProductPageLocators.CORRECT_PRICE_HAS_BEEN_ADDED).text
        book = self.browser.find_element(*ProductPageLocators.SHOULD_BE_ADDED_TO_THE_CART).text
        assert book == book1, "не добавилась нужная книга или цена не соответствует"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def add_to_chart_without_capcha(self):
        chart = self.browser.find_element(*ProductPageLocators.CHART_BUTTON)  # нужно использовать .browser.find_element
        # иначе будет ошибка bool' object has no attribute 'click'
        chart.click()
