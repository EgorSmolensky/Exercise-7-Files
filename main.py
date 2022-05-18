from pprint import pprint
import os

# Задачи 1, 2

def get_shop_list_by_dishes(dishes, person_count):
    shoplist = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shoplist:
                shoplist[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shoplist[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                           'quantity': ingredient['quantity'] * person_count}
    return shoplist


cook_book = dict()
with open('text.txt', 'r', encoding='utf-8') as file:
    while True:
        dish = file.readline().strip()
        cook_book[dish] = []
        number = int(file.readline().strip())
        for _ in range(number):
            ingredient = file.readline().strip().split(' | ')
            cook_book[dish].append(
                {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
        line = file.readline()
        if not line:
            break
pprint(cook_book)
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

# Задача 3

CURRENT_PATH = os.getcwd()
FOLDER = 'files'
FULL_PATH = os.path.join(CURRENT_PATH, FOLDER)
files = os.listdir(FULL_PATH)

lens = dict()
for file in files:
    file_path = os.path.join(FULL_PATH, file)
    lines_quantity = sum(1 for line in open(file_path, 'r', encoding='utf-8'))
    if lines_quantity in lens:
        lens[lines_quantity] += [file]
    else:
        lens[lines_quantity] = [file]

write_path = os.path.join(CURRENT_PATH, 'result.txt')
with open(write_path, 'w', encoding='utf-8') as file:
    for number in sorted(lens):
        for filename in lens[number]:
            file.write(filename + '\n')
            file.write(str(number) + '\n')
            current_file = open(os.path.join(FULL_PATH, filename), 'r', encoding='utf-8')
            text = current_file.read()
            current_file.close()
            file.write(text + '\n')
