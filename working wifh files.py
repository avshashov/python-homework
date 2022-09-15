# Задача №1

with open('recipes.txt', encoding='utf-8') as recipes_list:
    cook_book = {}
    for dish in recipes_list:
        cook_book[dish.rstrip()] = []
        for i in range(int(recipes_list.readline())):
            ingredient_name, quantity, measure = recipes_list.readline().rstrip().split(' | ')
            cook_book.get(dish.rstrip()).append(
                {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        recipes_list.readline()

print(cook_book)


# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = []
    for dish in dishes:
        ingredients.extend(cook_book[dish])

    shop_dict = {}
    for el in ingredients:
        if el['ingredient_name'] not in shop_dict:
            shop_dict[el['ingredient_name']] = {'measure': el['measure'], 'quantity': el['quantity'] * person_count}
        else:
            shop_dict[el['ingredient_name']]['quantity'] += el['quantity'] * person_count

    print(shop_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача №3

file_list = ['1.txt', '2.txt', '3.txt']
content_list = []
for file in file_list:
    with open(file, encoding='utf-8') as f:
        content_list.append([file, f.read().rstrip().split('\n')])

content_list = sorted(content_list, key=lambda x: len(x[1]))

with open('result.txt', 'w', encoding='utf-8') as res:
    for el in content_list:
        print(el[0], len(el[1]), *el[1], sep='\n', file=res)
