import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@allure.epic("Foodgram")
@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("Пользователь может создать аккаунт")
    def test_user_can_register(self, driver, user_data):
        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)

        main_page.open_main_page()
        main_page.click_create_account_button()

        assert register_page.is_register_page_opened(), "Страница регистрации не открылась"

        register_page.fill_registration_form(user_data)
        register_page.submit_registration()

        login_page.wait_url_contains("/signin")

        assert login_page.is_login_page_opened(), "Не произошел переход на страницу авторизации"
        assert login_page.is_login_form_visible(), "Форма авторизации не отображается"
