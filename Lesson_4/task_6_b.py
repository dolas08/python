from itertools import cycle


def testing_int(description, iterable):
    for _ in cycle([1]):
        try:
            iterable = int(iterable)
            return iterable
        except ValueError:
            print(f"Вы ввели не число")
            iterable = input(description)


my_list = ['a', 1, 'False', True, (3, 4), {1, 'a', 3.4}, [1, 2, 3], None]

n = testing_int(s := "Сколько раз вывести по одному элементу из списка?: ", input(s))
check = 0
for el in cycle(my_list):
    check += 1
    print(el)
    if check == n:
        break
