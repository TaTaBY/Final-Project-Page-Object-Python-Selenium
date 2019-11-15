from .base_page import BasePage
from .locators import ProductPageLocators


import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_right_name_of_book()
        self.should_be_correct_price_in_basket()

    def add_to_basket(self):
        button1 = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button1.click()
        time.sleep(1)

    def should_be_correct_price_in_basket(self):
        text1 = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        text2 = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert text1 == text2, "Incorrect price"

    def should_be_right_name_of_book(self):
        text3 = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        text4 = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_MESSAGE).text
        assert text3 == text4, "Name of book is wrong"


    #def should_be_login_form(self):
     #   assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    #def should_be_register_form(self):
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"