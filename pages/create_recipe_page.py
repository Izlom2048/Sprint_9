import allure

from config import BASE_URL, RECIPE_IMAGE_PATH
from locators.create_recipe_locators import CreateRecipeLocators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def is_create_recipe_page_opened(self) -> bool:
        return self.is_visible(CreateRecipeLocators.PAGE_TITLE)

    @allure.step("Заполнить форму создания рецепта")
    def fill_recipe_form(self, recipe_data: dict):
        self.type(CreateRecipeLocators.RECIPE_NAME_INPUT, recipe_data["name"])
        self.click(CreateRecipeLocators.BREAKFAST_TAG_BUTTON)

        self.type(CreateRecipeLocators.INGREDIENT_INPUT, recipe_data["ingredient_search"])
        ingredient_locator = self.build_xpath_locator(
            CreateRecipeLocators.INGREDIENT_DROPDOWN_ITEM_PATTERN,
            ingredient_name=recipe_data["ingredient_name"],
        )
        self.click(ingredient_locator)
        self.type(CreateRecipeLocators.INGREDIENT_AMOUNT_INPUT, recipe_data["ingredient_amount"])
        self.click(CreateRecipeLocators.ADD_INGREDIENT_BUTTON)

        self.type(CreateRecipeLocators.COOKING_TIME_INPUT, recipe_data["cooking_time"])
        self.type(CreateRecipeLocators.DESCRIPTION_TEXTAREA, recipe_data["description"])
        self.upload_file(CreateRecipeLocators.FILE_INPUT, RECIPE_IMAGE_PATH)

    @allure.step("Создать рецепт")
    def submit_recipe(self):
        self.scroll_to(CreateRecipeLocators.CREATE_BUTTON)
        self.click(CreateRecipeLocators.CREATE_BUTTON)
