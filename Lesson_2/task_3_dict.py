my_dict = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
           9: 'Осень', 10: 'Осень', 11: 'Осень'}
check = False
input_month = 0
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
print(f"Введённый месяц это {my_dict[input_month]}")
