from pprint import pprint
import os

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_data.append(
                {'ingredient_name': ingredient_name.strip(), "quantity": int(quantity.strip()),
                 'measure': measure.strip()}
            )
        cook_book[dish_name] = temp_data
        file.readline()
    # print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for name_of_dish in dishes:
        for ingredient in cook_book[name_of_dish]:
            if ingredient['ingredient_name'] in result.keys():
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
            else:
                result[ingredient['ingredient_name']] = {}
                result[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                result[ingredient['ingredient_name']]['quantity'] = ingredient['quantity'] * person_count
    return result


data = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
pprint(data)
print()
data = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(data)