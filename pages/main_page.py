import allure

from config import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open("recipes")

    @allure.step("Перейти на страницу регистрации")
    def click_create_account_button(self):
        self.click(MainPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Перейти на страницу авторизации")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Перейти на страницу создания рецепта")
    def click_create_recipe_tab(self):
        self.click(MainPageLocators.CREATE_RECIPE_TAB)

    def is_logout_button_visible(self) -> bool:
        return self.is_visible(MainPageLocators.LOGOUT_BUTTON)
