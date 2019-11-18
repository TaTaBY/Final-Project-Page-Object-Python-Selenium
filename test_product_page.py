
from selenium.common.exceptions import NoSuchElementException
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest
from pages.basket_page import BasketPage
import faker
from pages.login_page import LoginPage

#@pytest.mark.parametrize('mark', ["0","1","2","3","4","5","6",
#    ["7", pytest.param("7", marks=pytest.mark.xfail),
#                                  "okay_link"],
#                                  "8","9"])
#def test_guest_can_add_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #page = BasePage(browser, link)
    #page.open()
    #product_page = ProductPage(browser, browser.current_url)
   
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #page = BasePage(browser, link)
    #page.open()
    #product_page = ProductPage(browser, browser.current_url)
    #product_page.test_guest_cant_see_success_message_after_adding_product_to_basket()

#def test_guest_cant_see_success_message(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #page = BasePage(browser, link)
    #page.open()
    #product_page = ProductPage(browser, browser.current_url)
    #product_page.test_guest_cant_see_success_message()

#def test_message_disappeared_after_adding_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #page = BasePage(browser, link)
    #page.open()
    #product_page = ProductPage(browser, browser.current_url)
    #product_page.test_message_disappeared_after_adding_product_to_basket()

#def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.go_to_login_page()

#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.go_to_basket_page()
    #basket_page = BasketPage(browser, browser.current_url)
    #basket_page.test_on_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password = f.password()
        page = LoginPage(browser, link)
        print (email)
        print (password)
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = BasePage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)

    def test_guest_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.test_guest_cant_see_success_message()
    


        