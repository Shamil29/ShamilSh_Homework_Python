import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ProductsPage import ProductsPage
from pages.YourCartPage import YourCartPage
from pages.YourInfoPage import YourInfoPage
from pages.OverviewPage import OverviewPage


user_name = 'standard_user'
password = 'secret_sauce'

first_name = 'Shamil'
last_name = 'Shamsudinov'
zip_postal_code = '171381'


@allure.feature("Магазин 'Swag Labs'")
@allure.suite("Тест магазина 'Swag Labs'")
@allure.title("Тест на отображение стоимости добавленных товаров в корзину")
@allure.severity("blocker")
def test_swag_labs():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    with allure.step("Авторизация"):
        main_page.username(user_name)
        main_page.password(password)
        main_page.login_button()

    products_page = ProductsPage(browser)
    with allure.step("Добавление товаров"):
        products_page.sauce_labs_backpack()
        products_page.sauce_labs_bolt_t_shirt()
        products_page.sauce_labs_onesie()
        products_page.shopping_cart()

    your_cart_page = YourCartPage(browser)
    your_cart_page.button_checkout()

    your_info_page = YourInfoPage(browser)
    with allure.step("Заполнение информации"):
        your_info_page.first_name(first_name)
        your_info_page.last_name(last_name)
        your_info_page.zip_postal_code(zip_postal_code)
        your_info_page.button_continue()

    overview_page = OverviewPage(browser)
    with allure.step(
            "Проверить, что стоимость добавленных товаров равно '$58.29'"):
        result = overview_page.total_price()
        assert "$58.29" in result

    browser.quit()
