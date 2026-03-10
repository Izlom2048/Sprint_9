from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Создание рецепта']")
    RECIPE_NAME_INPUT = (
        By.XPATH,
        "//div[normalize-space()='Название рецепта']/following::input[1]",
    )
    BREAKFAST_TAG_BUTTON = (
        By.XPATH,
        "//span[normalize-space()='Завтрак']/preceding-sibling::button",
    )
    INGREDIENT_INPUT = (
        By.XPATH,
        "//div[normalize-space()='Ингредиенты']/following::input[1]",
    )
    INGREDIENT_AMOUNT_INPUT = (
        By.XPATH,
        "//div[normalize-space()='Ингредиенты']/following::input[2]",
    )
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[normalize-space()='Добавить ингредиент']")
    COOKING_TIME_INPUT = (
        By.XPATH,
        "//div[normalize-space()='Время приготовления']/following::input[1]",
    )
    DESCRIPTION_TEXTAREA = (
        By.XPATH,
        "//div[normalize-space()='Описание рецепта']/following::textarea[1]",
    )
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space()='Создать рецепт']")
    INGREDIENT_DROPDOWN_ITEM_PATTERN = (
        "//div[normalize-space()='Ингредиенты']/following::div[normalize-space()='{ingredient_name}'][1]"
    )
