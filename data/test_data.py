from uuid import uuid4


def generate_user_data() -> dict:
    token = uuid4().hex[:10]
    return {
        "first_name": "Anna",
        "last_name": "Tester",
        "username": f"anna_{token}",
        "email": f"anna_{token}@mail.com",
        "password": "StrongPass123!",
    }


RECIPE_DATA = {
    "name": f"Авторецепт {uuid4().hex[:6]}",
    "ingredient_search": "лук",
    "ingredient_name": "лук белый",
    "ingredient_amount": "100",
    "cooking_time": "15",
    "description": "Описание рецепта",
}
