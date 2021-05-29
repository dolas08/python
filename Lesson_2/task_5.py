my_list = [99, 88, 66, 4, 1]
print(f"Текущий рейтинг: {my_list}")
check = False
while check is False:
    try:
        el = int(input("Введите новую оценку: "))
        check = True
    except ValueError:
        print(f"Вы ввели не число")
        check = False
try:
    index = my_list.index(el)
    my_list.insert(index+1, el)
except ValueError:
    index = 0
    while index < len(my_list):
        if my_list[index] < el:
            my_list.insert(index, el)
            break
        index += 1
print(f"Новый рейтинг: {my_list}")
