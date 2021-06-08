from itertools import count


def fact(arg):
    i = 1
    for each in range(1, arg + 1):
        i *= each
        yield i


def testing_int(description, iterable):
    for _ in count(1, 1):
        try:
            iterable = int(iterable)
            return iterable
        except ValueError:
            print(f"Вы ввели не число")
            iterable = input(description)


n = testing_int(s := "Введите n: ", input(s))
for el in fact(n):
    print(f"{el}")
