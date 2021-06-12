from itertools import count

f = open("text_2.txt", "r", encoding="utf-8")
my_dict = dict()
n = len(f.readlines())
f.seek(0)
for i in count(1):
    temp = f.readline().split()
    my_dict.setdefault(i, len(temp))
    if i == n:
        break
for each in my_dict:
    print(f"{each}-строка имеет {my_dict[each]} слов")
