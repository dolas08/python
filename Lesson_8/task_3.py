class NotIntError(Exception):
    pass


def not_int_check(arg_1):
    """
    :param arg_1: string
    :return: result False if wrong symbols not found
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '}
    if arg_1.lower() == "stop":
        return False
    j = 0
    while j < len(arg_1):
        try:
            if arg_1[j] not in set_of_true:
                raise NotIntError
        except NotIntError:
            print(f"Был введён символ не являющийся числом, пробелом или словом Stop.\n"
                  f"Ввод не будет засчитан, введите заново")
            return True
        j += 1
    return False


my_list = []
temp_check = True
print("Ввод чисел по одному, для остановки введите STOP")
while True:
    input_check = True
    while input_check:
        temp = input("Введите число : ")
        try:
            if temp.lower() == "stop":
                temp_check = False
        except AttributeError:
            continue
        input_check = not_int_check(temp)
    if temp_check:
        my_list.append(temp)
    else:
        break
print(my_list)
