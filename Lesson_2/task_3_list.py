my_list = [[12, 1, 2, "Зима"], [3, 4, 5, "Весна"], [6, 7, 8, "Лето"], [9, 10, 11, "Осень"]]
check = False
while check is False:
    try:
        input_month = int(input("Введите номер месяца от 1 до 12: "))
        if input_month < 1 or input_month > 12:
            check = False
        else:
            check = True
    except ValueError:
        print(f"Вы ввели не число")
        check = False
i = 0
while i < 4:
    check = False
    if input_month in my_list[i]:
        print(f"Введёный месяц это {my_list[i][3]}")
        break
    else:
        i += 1
