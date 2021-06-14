my_list = []
check = False
while check is False:
    index = input("введите количество элементов или str для ввода в строку: ")
    try:
        index = int(index)
        check = True
        amount = 1
        while amount < index + 1:
            el = input(f"{amount:02d}-й элемент: ")
            my_list.append(el)
            amount += 1
    except ValueError:
        if index == "str":
            check = True
            str_list = input("Введите ваш список в строку, используя пробел как разделитель элементов: ")
            my_list = str_list.split()
    index = len(my_list)
    if index < 2:
        print(f"необходимо ввести как минимум два элемента")
        check = False
print(f"your list is {my_list}")
amount = 0
while amount < index:
    my_list[amount], my_list[amount + 1] = my_list[amount + 1], my_list[amount]
    amount = amount + 2
    if amount + 1 == index:
        break
print(f" new list is {my_list}")
