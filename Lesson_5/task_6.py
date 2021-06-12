from itertools import count

with open('text_6.txt', 'r', encoding='utf-8') as f:
    n = len(f.readlines())
    f.seek(0)

    my_dict = dict()
    temp_list = []
    for i in count(1):
        temp = f.readline().split()
        temp_counter = 0
        for j in count(1):
            if temp[j] != '-':
                temp[j] = temp[j][0:temp[j].find('(')]
                temp_counter += int(temp[j])
            if j == 3:
                my_dict.setdefault(temp[0][0:len(temp[0])-1], temp_counter)
                break
        if i == n:
            break
print(my_dict)
