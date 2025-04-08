import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from src.helpers.user_data import UserData
from src.pages.create_account_page import CreateAccountPage, Urls

@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture()
def registered_user(driver) -> UserData:
    page = CreateAccountPage(driver)
    page.click_on_signup_btn()
    user = UserData()
    page.fill_registration_form_and_click_register_account_btn(user)
    return user

@pytest.fixture()
def login_user(driver, registered_user) -> None:
    page = CreateAccountPage(driver)
    page.login_to_account(registered_user)
    page.wait_for_url_to_be(Urls.RECIPES)