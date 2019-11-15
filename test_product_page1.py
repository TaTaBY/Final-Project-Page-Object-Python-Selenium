
from selenium.common.exceptions import NoSuchElementException
from pages.product_page import ProductPage
from pages.main_page import MainPage
import pytest

@pytest.mark.parametrize('mark', ["0","1","2","3","4","5","6",
    ["7", pytest.param("7", marks=pytest.mark.xfail),
                                  "okay_link"],
                                  "8","9"])
def test_guest_can_add_product_to_basket(browser,mark):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{mark}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()





