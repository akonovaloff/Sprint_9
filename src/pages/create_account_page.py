from src.helpers.user_data import UserData
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from src.helpers.urls import Urls


class CreateAccountPage(BasePage):
    SIGNUP_BTN = (By.XPATH, "//a[text()='Создать аккаунт']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")

    @allure.step("Открыть страницу «Регистрация»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.get_current_url() not in [Urls.SIGNIN, Urls.SIGNUP]:
            self.goto_page(Urls.SIGNIN)
        self.wait_for_element_to_be_clickable(self.SIGNUP_BTN)

    @allure.step("Клик по кнопке «Создать аккаунт» в шапке страницы")
    def click_on_signup_btn(self):
        self.click_on(self.SIGNUP_BTN)
        self.wait_for_url_to_be(Urls.SIGNUP)

    @allure.step("Заполнить поле «Имя»")
    def fill_the_first_name_field(self, text: str):
        self.send_keys(self.FIRST_NAME_FIELD, text=text)

    @allure.step("Заполнить поле «Фамилия»")
    def fill_the_last_name_field(self, text: str):
        self.send_keys(self.LAST_NAME_FIELD, text=text)

    @allure.step("Заполнить поле «Имя пользователя»")
    def fill_the_username_field(self, text: str):
        self.send_keys(self.USERNAME_FIELD, text=text)

    @allure.step("Заполнить поле «Адрес электронной почты»")
    def fill_the_email_field(self, text: str):
        self.send_keys(self.EMAIL_FIELD, text=text)

    @allure.step("Заполнить поле «Пароль»")
    def fill_the_password_field(self, text: str):
        self.send_keys(self.PASSWORD_FIELD, text=text)

    @allure.step("Клик по кнопке «Создать аккаунт»")
    def click_on_the_register_account_button(self):
        self.click_on(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»")
    def fill_registration_form_and_click_register_account_btn(self, user: UserData):
        self.fill_the_first_name_field(user.first_name)
        self.fill_the_last_name_field(user.last_name)
        self.fill_the_username_field(user.username)
        self.fill_the_email_field(user.email)
        self.fill_the_password_field(user.password)
        self.click_on_the_register_account_button()
        self.wait_for_url_to_be(Urls.SIGNIN)

    @allure.step("Клик по кнопке «Войти»")
    def click_on_login_to_account_btn(self):
        self.click_on(self.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Вход в аккаунт")
    def login_to_account(self, user: UserData):
        self.fill_the_email_field(user.email)
        self.fill_the_password_field(user.password)
        self.click_on_login_to_account_btn()