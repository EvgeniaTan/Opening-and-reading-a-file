
from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        number_ingredients = int(file.readline().strip())
        ingredients_list = []
        for _ in range(number_ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            ingredients_list.append({
                'ingredient_name': ingredient_name.strip(),
                'quantity': int(quantity.strip()),  # Преобразуем в int
                'measure': measure.strip()
            })
        if file.readline().strip() == "":
            pass
        cook_book[dish] = ingredients_list

pprint(cook_book, sort_dicts=False)
