my_list = ['a', 1, 'False', True, (3, 4), {1, 'a', 3.4}, [1, 2, 3], None]
n = 0
print(f"{my_list}")
for el in my_list:
    print(f"{my_list[n]} is {type(my_list[n])}")
    n += 1
