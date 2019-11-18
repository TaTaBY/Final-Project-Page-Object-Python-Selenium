from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def test_on_empty_basket(self):
    	self.should_not_be_element_present()
    	self.should_be_text_present()

    def should_not_be_element_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"
    
    def should_be_text_present(self):
    	assert self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY).text == "Your basket is empty. Continue shopping", "Message not present"

   