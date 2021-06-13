from itertools import count


def testing_int(description, iterable):
    for _ in count(1, 1):
        try:
            iterable = int(iterable)
            return iterable
        except ValueError:
            print(f"Вы ввели не число")
            iterable = input(description)


m = testing_int(s := "Введите начало цикла: ", input(s))
n = testing_int(s := "Введите конец цикла: ", input(s))
for el in count(m, 1):
    print(el)
    if el == n:
        break
