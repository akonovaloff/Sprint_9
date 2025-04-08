from src.pages.create_account_page import CreateAccountPage, Urls, UserData
import allure

class TestCreateAccount:

    @allure.title("Создание аккаунта")
    def test_create_account(self, driver):
        page = CreateAccountPage(driver)
        page.click_on_signup_btn()
        user = UserData()
        page.fill_registration_form_and_click_register_account_btn(user)
        assert page.get_current_url() == Urls.SIGNIN
