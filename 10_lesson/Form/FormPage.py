from selenium.webdriver.common.by import By
import allure

class FormPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.browser.maximize_window()

    @allure.step("Заполнение полей данными")
    def data_types(self, input_data):
        for k in input_data:
            selector = f'[name={k}]'
            value = input_data[k]
            self.browser.find_element(
                By.CSS_SELECTOR, selector).send_keys(value)

    @allure.step("Нажатие на кнопку 'Submit'")
    def click_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        self.browser.execute_script("arguments[0].click();", button)

    @allure.step("Красный цвет поля 'Zip code'")
    def danger_color(self):
        danger = self.browser.find_element(
            By.ID, 'zip-code').value_of_css_property("background-color")
        return danger

    @allure.step("Зеленый цвет остальных полей")
    def success_color(self, other_fields):
        for field in other_fields:
            success = (self.browser.find_element(By.CSS_SELECTOR, field)
                       .value_of_css_property("background-color"))
            return success
