import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Foodgram")
@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Пользователь может авторизоваться")
    def test_user_can_login(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_main_page()
        main_page.click_login_button()

        login_page.fill_login_form(
            registered_user["email"],
            registered_user["password"],
        )
        login_page.submit_login()

        main_page.wait_url_contains("/recipes")

        assert main_page.is_logout_button_visible(), "Кнопка 'Выход' не отображается"
