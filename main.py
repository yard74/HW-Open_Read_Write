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


# data = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
# pprint(data)
# print()
# data = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# pprint(data)


task_3_path = os.path.join(os.getcwd(), 'task_3_data')


def get_files_dict(path_line):
    files_list = os.listdir(task_3_path)
    data = {}
    for file_name in files_list:
        with open(os.path.join(path_line, file_name), encoding='utf-8') as f:
            lines_quantity = 0
            data_in_file = ''
            for line in f:
                data_in_file += line
                lines_quantity += 1
        data[file_name] = (lines_quantity, data_in_file)
    return data


def get_sorted_files_dict(files_dict):
    sorted_values = sorted(files_dict.values())
    sorted_files_dict = {}
    for value in sorted_values:
        for key in files_dict.keys():
            if files_dict[key] == value:
                sorted_files_dict[key] = files_dict[key]
                break
    return sorted_files_dict


def get_sorted_data_into_file(new_dict):
    with open('task_3_result.txt', 'x', encoding='utf-8') as f:
        for key in new_dict:
            f.write(f'{key}\n')
            f.write(f'{new_dict[key][0]}\n')
            f.write(f'{new_dict[key][1]}\n')
    return print('Запись данных в файл прошла успешно.')


dict_of_files_data = get_files_dict(task_3_path)
sorted_dict = get_sorted_files_dict(dict_of_files_data)
get_sorted_data_into_file(sorted_dict)

