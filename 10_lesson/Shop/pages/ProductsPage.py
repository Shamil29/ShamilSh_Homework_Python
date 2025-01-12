from selenium.webdriver.common.by import By
import allure

class ProductsPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/inventory.html")
        self.browser.maximize_window()

    @allure.step("Добавление товара 'Sauce Labs Backpack'")
    def sauce_labs_backpack(self):
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()

    @allure.step("Добавление товара 'Sauce Labs Bolt T-Shirt'")
    def sauce_labs_bolt_t_shirt(self):
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    @allure.step("Добавление товара 'Sauce Labs Onesie'")
    def sauce_labs_onesie(self):
        self.browser.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переход в корзину")
    def shopping_cart(self):
        self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
