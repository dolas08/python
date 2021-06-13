from random import randint


def find_unique(arg_1):
    f = dict.fromkeys(arg_1, 0)
    for el in arg_1:
        if el in f:
            f[el] += 1
    return [el for el in f if f[el] == 1]


#my_list = [el + randint(0, 5) for el in range(0, 10)]
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"my list is:\n{my_list}\nunique elements is:\n{find_unique(my_list)}")

