from pathlib import Path

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step("Открыть страницу: {path}")
    def open(self, path: str = ""):
        self.driver.get(f"{self.base_url}{path}")

    def find(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_visible(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Клик по элементу")
    def click(self, locator: tuple, timeout: int = 10):
        self.wait_clickable(locator, timeout).click()

    @allure.step("Заполнить поле значением: {text}")
    def type(self, locator: tuple, text: str, timeout: int = 10, clear: bool = True):
        element = self.wait_visible(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple, timeout: int = 10) -> str:
        return self.wait_visible(locator, timeout).text

    def is_visible(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to(self, locator: tuple, timeout: int = 10):
        element = self.find(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Загрузить файл: {file_path}")
    def upload_file(self, locator: tuple, file_path: Path, timeout: int = 10):
        element = self.find(locator, timeout)
        self.driver.execute_script(
            "arguments[0].style.display='block'; arguments[0].style.visibility='visible';",
            element,
        )
        element.send_keys(str(Path(file_path).resolve()))

    def wait_url_contains(self, value: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(value))

    def current_url_contains(self, value: str) -> bool:
        return value in self.driver.current_url

    def build_xpath_locator(self, template: str, **kwargs):
        return By.XPATH, template.format(**kwargs)
