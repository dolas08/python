class MyZeroDivisionError(Exception):
    pass


def ans_check(_str):
    """
    :return: возвращает int(arg) полученное с input
    """
    while True:
        try:
            arg = int(input(f"{_str}: "))
            return arg
        except ValueError:
            print(f"Вы ввели не число")


a = ans_check("Введите делимое")
b = ans_check("Введите делитель")
try:
    if b == 0:
        raise MyZeroDivisionError
except MyZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"{a}/{b} = {a / b}")
