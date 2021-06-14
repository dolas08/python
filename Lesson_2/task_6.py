my_database = []
my_list = []
my_dict = dict()
check = False
while check is False:
    try:
        products = int(input("Введите количество товаров, которые вы хотите добавить: "))
        check = True
    except ValueError:
        print(f"Вы ввели не число")
        check = False
index = 1
while index <= products:
    type_items = input(f"Укажите тип техники: ")
    check = False
    while check is False:
        try:
            price_items = int(input(f"Укажите цену {type_items}: "))
            check = True
        except ValueError:
            print(f"Вы ввели не число")
            check = False
    check = False
    while check is False:
        try:
            amount_items = int(input(f"Укажите количество {type_items} на складке: "))
            check = True
        except ValueError:
            print(f"Вы ввели не число")
            check = False
    check = False
    while check is False:
        type_amount_items = input("Введите тип количества (шт/л): ")
        if (type_amount_items == "шт") | (type_amount_items == "л"):
            check = True
    my_dict = {"название": type_items, "Цена": price_items, "Количество": amount_items, "ед": type_amount_items}
    my_list = [index, my_dict]
    my_tuple = tuple(my_list)
    my_database.append(my_tuple)
    index = index + 1
print("[")
print(*my_database, sep='\n')
print("]")
my_db_analytics = dict()
my_db_keys = list(my_database[0][1].keys())
amount_keys = len(my_db_keys)
i = 0
j = 0
while i < amount_keys:
    temp_list = []
    key = my_db_keys[i]
    j = 0
    while j < products:
        temp_list.append(my_database[j][1].get(key))
        j += 1
    i += 1
    my_db_analytics.setdefault(key, temp_list)
my_db_analytics.setdefault("ед", list(set(my_db_analytics.pop('ед'))))
print("{")
for key in my_db_keys:
    print(f'"{key}" : {my_db_analytics.get(key)}')
print("}")
