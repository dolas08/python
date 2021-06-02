def list_into_int(arg_1):
    """
    transform char numbers into int
    this func cant work with non-numbers
    delete it before
    :param arg_1: list with str numbers
    :return: list with int numbers
    """
    count = 0
    while count < len(arg_1):
        arg_1[count] = int(arg_1[count])
        count += 1
    return arg_1


def not_int_check(arg_1):
    """
    :param arg_1: any list
    :return: result False if wrong symbols not found
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', ' '}
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
        print(f"Был введён символ не являющийся числом, пробелом или *.\n"
              f"Строка не будет засчитана, введите заново")
        return True
    else:
        return False


check = True
check_el = False
temp_sum = 0

while check:
    input_check = True
    while input_check:
        temp = input("Введите строку чисел через пробел, для выхода введите *: ")
        input_check = not_int_check(temp)

    if temp.find('*') >= 0:
        check_el = True
        temp_last = temp[:temp.index('*')]
        temp_last = temp_last.split()
        list_into_int(temp_last)
    temp = temp.split()
    index = 0
    if check_el:
        temp_last = sum(temp_last)
        temp_last += temp_sum
        check = False
        print(f"Sum of elements is {temp_last}")
    else:
        temp = list_into_int(temp)
        temp_sum += sum(temp)
        print(f"Sum of elements is {temp_sum}")