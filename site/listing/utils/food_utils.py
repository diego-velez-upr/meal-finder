from typing import List
from ..models import Food


def search_food(foods: List[Food], keyword: str, delimiter=' ') -> List[Food]:
    """
    Searches for all the foods in a food list that match the keyword, where the keyword is split using the delimiter
    passed.
    """
    foods_found = set()

    for food in foods:
        for word in keyword.split(delimiter):
            if word.lower() in food.tags or word.lower() in food.name.lower() or word.lower() in food.description:
                foods_found.add(food)

    return list(foods_found)
