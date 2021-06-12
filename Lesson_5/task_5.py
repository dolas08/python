def list_into_float(arg_1):
    """
    transform char numbers into int
    this func cant work with non-numbers
    delete it before
    :param arg_1: list with str numbers
    :return: list with int numbers
    """
    count = 0
    while count < len(arg_1):
        arg_1[count] = float(arg_1[count])
        count += 1
    return arg_1


def not_int_check(arg_1):
    """
    :param arg_1: any list
    :return: result False if wrong symbols not found
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.'}
    int_check = False
    j = 0
    while j < len(arg_1):
        if arg_1[j] in set_of_true:
            int_check = False
        else:
            int_check = True
            break
        j += 1
    if int_check:
        print(f"Был введён символ не являющийся числом или пробелом\n"
              f"Строка не будет засчитана, введите заново\n"
              f"Для ввода дробных чисел используйте точку. Например: 123.456")
        return True
    else:
        return False


f = open('text_5.txt', 'w', encoding='utf-8')
input_check = True
while input_check:
    temp = input("Введите строку чисел через пробел: ")
    input_check = not_int_check(temp)
    if input_check is False:
        print(temp, file=f)
f.close()
with open('text_5.txt', 'r', encoding='utf-8') as f:
    temp = list_into_float(f.readline().split())
    i = 0
    for el in temp:
        i += el
    print(f"Сумма введённых элементов = {i}")
