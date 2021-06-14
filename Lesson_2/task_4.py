my_str = input("Введите строку: ")
my_list = my_str.split()
for i, el in enumerate(my_list, 1):
    print(f"{i:02d} {el[0:10]}")
