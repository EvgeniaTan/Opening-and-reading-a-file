from pprint import pprint

cook_book_dict = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}
    ],
    'Фахитос': [
        {'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'},
        {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'},
        {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'},
        {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'},
        {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}
    ]
}
def get_shop_list_by_dishes(dishes_list, person_count=1):
    ingredient_dict_all = {}

    for dish in dishes_list:
        for el in cook_book_dict.get(dish, []):
            ingredient_name = el['ingredient_name'].strip()
            quantity = int(el['quantity'].strip()) * person_count

            if ingredient_name in ingredient_dict_all:
                ingredient_dict_all[ingredient_name]['quantity'] += quantity
            else:
                ingredient_dict_all[ingredient_name] = {
                    'measure': el['measure'].strip(),
                    'quantity': quantity
                }

    pprint(ingredient_dict_all)

# Пример использования
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)