from random import randint

import allure

from src.pages.base_page import BasePage, By
from src.helpers.urls import Urls
from random import choice
from pathlib import Path


class RecipesPage(BasePage):
    CREATE_RECIPE_TAB = (By.XPATH, "//a[text()='Создать рецепт']")
    RECIPES_TAB = (By.XPATH, "//a[text()='Рецепты']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/../input")
    INGREDIENTS_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/../input")
    INGREDIENTS_POPUP_LIST = (By.XPATH, "//div[@class='styles_container__3ukwm']/div")
    INGREDIENTS_QUANTITY_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    RECIPE_IMAGE_INPUT = (By.XPATH, "//label[text()='Загрузить фото']/../input")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/../input")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/../textarea")
    RECIPE_TITLE = (By.XPATH, "//h1")

    @allure.step("Открыть страницу «Создать рецепт»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.get_current_url() not in [Urls.RECIPES]:
            self.goto_page(Urls.RECIPES)
        self.wait_for_element_to_be_visible(self.RECIPES_TAB)

    @allure.step("Клик по вкладке «Создать рецепт»")
    def click_on_the_create_recipe_tab(self):
        self.click_on(self.CREATE_RECIPE_TAB)
        self.wait_for_element_to_be_visible(self.CREATE_RECIPE_BUTTON)

    @allure.step("Клик по кнопке «Создать рецепт»")
    def click_on_the_create_recipe_button(self):
        self.click_on(self.CREATE_RECIPE_BUTTON)
        self.wait_for_element_to_be_visible(self.CREATE_RECIPE_BUTTON)

    @allure.step("Ввести текст в поле «Название рецепта»")
    def fill_the_recipe_name_input(self, text: str):
        self.send_keys(self.RECIPE_NAME_INPUT, text=text)

    @allure.step("Ввести текст в поле «Ингредиенты»")
    def fill_the_ingredients_input(self, text: str):
        self.send_keys(self.INGREDIENTS_INPUT, text=text)

    @allure.step("Выбрать случайный ингредиент из списка ингредиентов")
    def click_on_random_ingredient_from_the_popup_list(self):
        list_len = len(self.find_elements(self.INGREDIENTS_POPUP_LIST))
        self.click_on_locator_by_index(locator=self.INGREDIENTS_POPUP_LIST, index=randint(0, list_len-1))

    @allure.step("Ввести количество ингредиента")
    def fill_the_ingredients_quantity(self, text: str):
        self.send_keys(self.INGREDIENTS_QUANTITY_INPUT, text=text)

    @allure.step("Клик по кнопке «Добавить ингредиент»")
    def click_on_add_ingredient_btn(self):
        self.click_on(self.ADD_INGREDIENT_BUTTON)

    @allure.step("Добавить случайный ингредиент")
    def add_a_random_ingredient(self):
        valid_russian_letters = (
            'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
            'щ', 'э', 'я'
        )
        self.fill_the_ingredients_input(choice(valid_russian_letters))
        self.click_on_random_ingredient_from_the_popup_list()
        self.fill_the_ingredients_quantity(str(randint(1, 999)))
        self.click_on_add_ingredient_btn()

    @allure.step("Загрузить тестовую картинку рецепта")
    def upload_the_picture_to_a_recipe(self):
        file_path = str(Path("tests/test_data/images/test_recipe_picture.webp").absolute())
        self.make_element_to_be_visible_by_java_script(self.RECIPE_IMAGE_INPUT)
        self.send_keys(self.RECIPE_IMAGE_INPUT, file_path)

    @allure.step("Указать время приготовления")
    def set_cooking_time(self, text: str):
        self.send_keys(self.COOKING_TIME_INPUT, text=text)

    @allure.step("Добавить описание рецепта")
    def set_recipe_description(self, text: str):
        self.send_keys(self.RECIPE_DESCRIPTION_INPUT, text=text)

    def get_recipe_title(self) -> str:
        return self.get_element_text(self.RECIPE_TITLE)