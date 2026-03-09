import allure

from config import BASE_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def is_login_page_opened(self) -> bool:
        return self.is_visible(LoginPageLocators.PAGE_TITLE)

    def is_login_form_visible(self) -> bool:
        return self.is_visible(LoginPageLocators.LOGIN_FORM)

    @allure.step("Заполнить форму авторизации")
    def fill_login_form(self, username: str, password: str):
        self.type(LoginPageLocators.EMAIL_INPUT, username)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Отправить форму авторизации")
    def submit_login(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)
