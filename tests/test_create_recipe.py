import time

import allure

from src.helpers.urls import Urls
from src.pages.recipes_page import RecipesPage
from random import randint

class TestCreateRecipe:
    @allure.title("Создание рецепта")
    def test_create_recipe(self, driver, login_user):
        recipe_name = 'Тестовый рецепт'
        recipe_description = 'Это тестовое описание тестового рецепта'
        page = RecipesPage(driver)
        page.click_on_the_create_recipe_tab()
        page.fill_the_recipe_name_input(recipe_name)
        for _ in range(0, randint(2,6)):
            page.add_a_random_ingredient()
        page.set_cooking_time(str(randint(2, 180)))
        page.upload_the_picture_to_a_recipe()
        page.set_recipe_description(recipe_description)
        page.click_on_the_create_recipe_button()
        page.wait_for_url_matches(Urls.READY_RECIPE_URL_PATTERN)
        assert page.get_recipe_title() == recipe_name