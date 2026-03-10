import allure

from config import BASE_URL
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def is_register_page_opened(self) -> bool:
        return self.is_visible(RegisterPageLocators.PAGE_TITLE)

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, user_data: dict):
        self.type(RegisterPageLocators.FIRST_NAME_INPUT, user_data["first_name"])
        self.type(RegisterPageLocators.LAST_NAME_INPUT, user_data["last_name"])
        self.type(RegisterPageLocators.USERNAME_INPUT, user_data["username"])
        self.type(RegisterPageLocators.EMAIL_INPUT, user_data["email"])
        self.type(RegisterPageLocators.PASSWORD_INPUT, user_data["password"])

    @allure.step("Отправить форму регистрации")
    def submit_registration(self):
        self.click(RegisterPageLocators.SUBMIT_BUTTON)
