import allure
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")
        self.browser.maximize_window()

    @allure.step("Заполнение поля 'Username' {user_name}")
    def username(self, user_name):
        user_name_field = self.browser.find_element(By.ID, 'user-name')
        user_name_field.clear()
        login = user_name
        user_name_field.send_keys(login)

    @allure.step("Заполнение поля 'Password' {password}")
    def password(self, password):
        password_field = self.browser.find_element(By.ID, 'password')
        password_field.clear()
        my_password = password
        password_field.send_keys(my_password)

    @allure.step("Нажатие на кнопку 'Login'")
    def login_button(self):
        self.browser.find_element(By.ID, 'login-button').click()
