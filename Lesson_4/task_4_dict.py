from random import randint


def find_unique(arg_1):
    return [el for el in dict.fromkeys(arg_1, 1).keys()]


my_list = [el + randint(0, 10) for el in range(0, 20)]
print(f"my list is:\n{my_list}\nunique elements is:\n{find_unique(my_list)}")

