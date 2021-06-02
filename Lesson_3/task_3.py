# по идее этот способ через ветвления
# тоже рабочий, но на всякий случай
# сделал ещё один вариант
# def my_func(*args):
#    my_list = list(*args)
#    n = len(my_list)
#    max_1 = my_list[0]
#    max_2 = my_list[1]
#    if max_1 < my_list[2]:
#        max_1 = my_list[2]
#        if my_list[0] > my_list[1]:
#            max_2 = my_list[0]
#    elif max_2 < my_list[2]:
#        max_2 = my_list[2]
#        if my_list[1] > my_list[0]:
#            max_1 = my_list[1]
#    return max_1 + max_2

def my_func(*args):
    """
    :param args: list
    :return: sum 2 max elements in list
    """
    temp = list(*args)
    max_1 = max(temp)
    if temp.count(max_1) > 1:
        return max_1 + max_1
    else:
        temp.pop(temp.index(max_1))
        max_2 = max(temp)
        return max_1 + max_2


index = 0
my_list_1 = []
print(f"Введите три числа, а я найду сумму двух максимальных.")
while index < 3:
    check = False
    while check is False:
        try:
            number = int(input(f"Введите {index+1} число: "))
            check = True
            my_list_1.append(number)
        except ValueError:
            print(f"Вы ввели не число")
            check = False
    index += 1
print(f"сумма двух максимальных чисел, что вы ввели: {my_func(my_list_1)}")
