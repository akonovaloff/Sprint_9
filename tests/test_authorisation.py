import allure

from src.pages.create_account_page import CreateAccountPage, Urls


class TestAuthorisation:
    @allure.title("Авторизация пользователя ")
    def test_authorisation(self, driver, registered_user):
        page = CreateAccountPage(driver)
        page.login_to_account(registered_user)
        page.wait_for_url_to_be(Urls.RECIPES)
        assert page.get_current_url() == Urls.RECIPES
        assert page.element_is_visible(page.LOGOUT_BUTTON)