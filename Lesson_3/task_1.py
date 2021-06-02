def my_division(arg_1, arg_2):
    """
    :param arg_1: first int
    :param arg_2: second int
    :return: result arg_1 / arg_2
    """
    if arg_2 == 0:
        return print(f"на ноль делить нельзя", end=' ')
    else:
        return print(f"{arg_1} / {arg_2} is {arg_1 / arg_2}")


check = False
while check is False:
    try:
        number_1 = int(input("введите делимое: "))
        check = True
    except ValueError:
        print(f"Вы ввели не число")
        check = False

check = False
while check is False:
    try:
        number_2 = int(input("введите делитель: "))
        check = True
    except ValueError:
        print(f"Вы ввели не число")
        check = False

my_division(number_1, number_2)
