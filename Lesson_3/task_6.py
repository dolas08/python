def int_func(arg_1):
    """
    :param arg_1: lowercase string
    :return: 1st symbol is uppercase, other is lowercase
    """
    temp_A = arg_1[0:1]
    temp_a = arg_1[1:]
    temp_A = chr(ord(temp_A) + (ord("A") - (ord("a"))))
    return temp_A + temp_a


def check(arg_1):
    """
    creating check sets:
    control_set_a is for lowercase
    control_set_A is for uppercase
    :param arg_1: string
    :return: true if no errors and all symbols of string is lowercase
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


temp = input("Введите слово из маленьких латинских букв: ")
if check(temp):
    print(int_func(temp))
