from selenium.webdriver.common.by import By


class LoginPageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Войти на сайт']")
    LOGIN_FORM = (By.TAG_NAME, "form")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
