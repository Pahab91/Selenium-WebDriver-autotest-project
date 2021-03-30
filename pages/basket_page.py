from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_NOT_EMPTY), \
            "Success message is presented, but should not be"

    def basket_should_be_empty(self):
        assert self.is_element_present(
            *BasePageLocators.BASKET_EMPTY_TEXT), 'не прошла проверка на текст "коризина пуста"'


