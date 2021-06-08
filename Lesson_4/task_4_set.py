from random import randint


def find_unique(arg_1):
    set_unique = set()
    list_unique = []
    for el in my_list:
        if el not in set_unique:
            set_unique.add(el)
            list_unique.append(el)
    return list_unique


my_list = [el + randint(0, 10) for el in range(0, 20)]
print(f"my list is:\n{my_list}\nunique elements is:\n{find_unique(my_list)}")
