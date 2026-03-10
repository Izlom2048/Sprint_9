from selenium.webdriver.common.by import By


class RecipePageLocators:
    RECIPE_TITLE = (By.TAG_NAME, "h1")
    DESCRIPTION_TITLE = (By.XPATH, "//h3[normalize-space()='Описание:']")
    DESCRIPTION_TEXT = (By.XPATH, "//h3[normalize-space()='Описание:']/following-sibling::div")
