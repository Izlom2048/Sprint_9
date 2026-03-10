import allure

from data.test_data import RECIPE_DATA
from pages.create_recipe_page import CreateRecipePage
from pages.main_page import MainPage
from pages.recipe_page import RecipePage


@allure.epic("Foodgram")
@allure.feature("Создание рецепта")
class TestCreateRecipe:
    @allure.title("Авторизованный пользователь может создать рецепт")
    def test_authorized_user_can_create_recipe(self, driver, authorized_user):
        main_page = MainPage(driver)
        create_recipe_page = CreateRecipePage(driver)
        recipe_page = RecipePage(driver)

        main_page.open_main_page()
        assert main_page.is_logout_button_visible(), "Пользователь не авторизован"

        main_page.click_create_recipe_tab()
        assert create_recipe_page.is_create_recipe_page_opened(), "Страница создания рецепта не открылась"

        create_recipe_page.fill_recipe_form(RECIPE_DATA)
        create_recipe_page.submit_recipe()

        recipe_page.wait_url_contains("/recipes/")

        assert recipe_page.is_description_section_visible(), "Карточка рецепта не открылась"
        assert recipe_page.get_recipe_title() == RECIPE_DATA["name"], "Название рецепта не совпадает"
