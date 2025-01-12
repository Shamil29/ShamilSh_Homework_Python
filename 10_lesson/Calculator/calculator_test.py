import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


@allure.epic("Калькулятор")
@allure.title("Тест на отображение результата в окне")
def test_data_types():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)
    calculator_page.field_waits()
    calculator_page.click_button_1()
    calculator_page.click_button_2()
    calculator_page.click_button_3()
    calculator_page.click_button_4()
    result = calculator_page.find_result()

    with allure.step(
            "Проверить, что в окне отобразится результат '15' через 45 сек"):
        assert result == '15'

    browser.quit()
