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
    print(cook_book)