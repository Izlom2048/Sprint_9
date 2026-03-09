import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

from config import BROWSER_NAME, BROWSER_VERSION, SELENOID_URL
from data.test_data import generate_user_data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if SELENOID_URL:
        options.set_capability("browserName", BROWSER_NAME)
        options.set_capability("browserVersion", BROWSER_VERSION)
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
                "sessionTimeout": "3m",
            },
        )
        browser = webdriver.Remote(
            command_executor=SELENOID_URL,
            options=options,
        )
        browser.file_detector = LocalFileDetector()
    else:
        browser = webdriver.Chrome(options=options)

    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def registered_user(driver, user_data):
    main_page = MainPage(driver)
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)

    main_page.open_main_page()
    main_page.click_create_account_button()
    assert register_page.is_register_page_opened(), "Страница регистрации не открылась"

    register_page.fill_registration_form(user_data)
    register_page.submit_registration()
    login_page.wait_url_contains("/signin")

    return user_data


@pytest.fixture
def authorized_user(driver, registered_user):
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

    return registered_user


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                browser.page_source,
                name="page_source",
                attachment_type=allure.attachment_type.HTML,
            )
