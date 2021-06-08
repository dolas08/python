from random import randint


def my_func(args):
    i = 1
    temp_list = []
    while i < len(args):
        if args[i] > args[i - 1]:
            temp_list.append(args[i])
        i += 1
    return temp_list


my_list = [el+randint(0, 980) for el in range(0, 20)]
print(f"my list is:\n{my_list}\nresult is:\n{my_func(my_list)}")
