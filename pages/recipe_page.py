from config import BASE_URL
from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class RecipePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def get_recipe_title(self) -> str:
        return self.get_text(RecipePageLocators.RECIPE_TITLE)

    def get_recipe_description(self) -> str:
        return self.get_text(RecipePageLocators.DESCRIPTION_TEXT)

    def is_description_section_visible(self) -> bool:
        return self.is_visible(RecipePageLocators.DESCRIPTION_TITLE)
