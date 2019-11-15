from selenium.common.exceptions import NoSuchElementException
from pages.product_page import ProductPage
from pages.main_page import MainPage

def test_guest_can_buy_at_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    login_page = ProductPage(browser, browser.current_url)
    login_page.should_be_product_page()    

