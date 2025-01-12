import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage


input_data = {
    'first-name': 'Иван',
    'last-name': 'Петров',
    'address': 'Ленина, 55-3',
    'e-mail': 'test@skypro.com',
    'zip-code': '',
    'phone': '+7985899998787',
    'city': 'Москва',
    'country': 'Россия',
    'job-position': "QA",
    'company': 'SkyPro'
}

other_fields = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company",
        ]

alert_danger_color = "rgba(248, 215, 218, 1)"
alert_success_color = "rgba(209, 231, 221, 1)"


@allure.feature("Форма")
@allure.suite("Тест формы")
@allure.title("Тест на заполнение полей 'Типы данных'")
@allure.severity("blocker")
def test_data_types():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    form_page = FormPage(browser)
    form_page.data_types(input_data)
    form_page.click_button()

    with allure.step("Проверить, что поле 'Zip code' подсвечено красным"):
        danger = form_page.danger_color()
        assert danger == alert_danger_color

    with allure.step("Проверить, остальные поля подсвечены зеленым"):
        success = form_page.success_color(other_fields)
        assert success == alert_success_color

        browser.quit()
