from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
	LOGIN_FORM = (By.ID, "login_form")
	REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators ():
	ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
	PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
	NAME_OF_BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	NAME_OF_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")