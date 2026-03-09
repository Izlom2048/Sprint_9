from selenium.webdriver.common.by import By


class MainPageLocators:
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes' and normalize-space()='Рецепты']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/signup' and normalize-space()='Создать аккаунт']")
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/signin' and normalize-space()='Войти']")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[@href='/recipes/create' and normalize-space()='Создать рецепт']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Выход']")
