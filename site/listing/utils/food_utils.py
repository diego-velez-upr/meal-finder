from typing import List, Set
from ..models import Food


def search_food(foods: List[Food], keyword: str) -> Set[Food]:
    """
    Searches for all the foods in a food list that match the keyword.
    """
    foods_found = set()

    for food in foods:
        if keyword.lower() in food.tags or keyword.lower() in food.name.lower():
            foods_found.add(food)

    return foods_found
