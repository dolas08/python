def int_func(arg_1):
    """
    :param arg_1: lowercase string
    :return: 1st symbol is uppercase, other is lowercase
    """
    temp_A = arg_1[0:1]
    temp_a = arg_1[1:]
    temp_A = chr(ord(temp_A) + (ord("A") - (ord("a"))))
    return temp_A + temp_a


def int_func_list(arg_1):
    """
    :param arg_1: list of strings
    :return: string with all first char is uppercase
    """
    index = 0
    while index < len(arg_1):
        arg_1[index] = int_func(arg_1[index])
        index = index + 1
    str_temp = ""
    for el in arg_1:
        str_temp += el + ' '
    str_temp = str_temp[0:len(str_temp) - 1]
    return str_temp


def check(arg_1):
    """
    creating check sets:
    control_set_a is for lowercase
    control_set_A is for uppercase
    :param arg_1: string
    :return: true if no errors and 1 symbol of string is lowercase
    """
    control_set_a = set()
    control_set_A = set()

    i = ord("a")
    j = ord("z")
    while i <= j:
        control_set_a.add(chr(i))
        i += 1

    i = ord("A")
    j = ord("Z")
    while i <= j:
        control_set_A.add(chr(i))
        i += 1

    temp_bool = True
    for el in arg_1:
        if (el in control_set_a) or (el == ' ') or (el in control_set_A):
            temp_bool = True
        else:
            print(f"обнаружен как минимукм один не-латинский символ")
            temp_bool = False
            break
        if el in control_set_A:
            print(f"обнаружена как минимум одна заглавная буква")
            temp_bool = False
            break
    return temp_bool


temp = input("Введите строку строчными латинскими символами: ")

if check(temp):
    temp = temp.split()
    print(f"{int_func_list(temp)}")
