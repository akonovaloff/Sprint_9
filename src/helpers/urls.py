from re import compile
class Urls:
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
    SIGNIN = f"{BASE_URL}/signin"
    SIGNUP = f"{BASE_URL}/signup"
    RECIPES = f"{BASE_URL}/recipes"
    READY_RECIPE_URL_PATTERN = compile(
        r'^https://foodgram-frontend-1\.prakticum-team\.ru/recipes/\d+$'
    )
