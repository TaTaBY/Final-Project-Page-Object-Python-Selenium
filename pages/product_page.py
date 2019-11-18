from .base_page import BasePage
from .locators import ProductPageLocators


import time

class ProductPage(BasePage):
    #def should_be_product_page(self):
        #self.should_not_be_success_message()
        #self.add_to_basket()
        #self.solve_quiz_and_get_code()
        #self.should_be_right_name_of_book()
        #self.should_be_correct_price_in_basket()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_disappear()

    def add_to_basket(self):
        button1 = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button1.click()
        time.sleep(1)

    def should_be_correct_price_in_basket(self):
        text1 = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        text2 = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert text1 == text2, "Incorrect price"

    def should_be_right_name_of_book(self):
        #time.sleep(20)
        text3 = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        text4 = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_MESSAGE).text
        assert text3 == text4, "Name of book is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
    
    def test_user_cant_see_success_message(self):
        self.should_not_be_success_message()