from random import randint

my_list = [el + randint(0, 8) for el in range(0, 10)]
print(f"my list is:\n{my_list}\nresult is:\n{[el for el in my_list[1:] if el > my_list[my_list.index(el) - 1]]}")

