from random import randint


def find_unique(arg_1):
    set_unique = set()
    list_unique = []
    skip_list = []
    for el in arg_1:
        if el in skip_list:
            continue
        elif el not in set_unique:
            set_unique.add(el)
            list_unique.append(el)
        elif el in set_unique:
            skip_list.append(el)
            list_unique.remove(el)

    return list_unique


# my_list = [el + randint(0, 5) for el in range(0, 10)]
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"my list is:\n{my_list}\nunique elements is:\n{find_unique(my_list)}")
