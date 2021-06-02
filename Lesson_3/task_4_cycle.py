def my_func(arg_1, arg_2):
    """
    function for a^(-n) with cycle
    :param arg_1: a
    :param arg_2: -n
    :return: a^(-n)
    """
    index = -1
    temp = arg_1
    while index > arg_2:
        arg_1 = arg_1 * temp
        index -= 1
    return 1 / arg_1


check = False
while check is False:
    try:
        number = float(input("Введите действительное положительное число: "))
        if number > 0:
            check = True
        else:
            "вы ввели отрицательное число или ноль"
    except ValueError:
        print(f"Вы ввели не число")
        check = False
check = False
while check is False:
    try:
        number_1 = int(input("Введите целое отрицательное число: "))
        if number_1 < 0:
            check = True
        else:
            "вы ввели ное число или ноль"
    except ValueError:
        print(f"Вы ввели не целое число или не число совсем")
        check = False
print(f"{number} в степени {number_1} это {my_func(number, number_1)}")
