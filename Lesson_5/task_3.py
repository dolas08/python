from itertools import count

salary_dict = dict()
temp_count = 0
with open('text_3.txt', 'r', encoding='utf-8') as f:
    n = len(f.readlines())
    f.seek(0)
    for i in count(1):
        temp = f.readline().split()
        salary_dict.setdefault(temp[0], temp[1])
        temp_count += float(temp[1])
        if float(temp[1]) < 20000:
            print(f"{temp[0]} получает меньше 20к!")
        if i == n:
            break
print(
    f"Средняя з/п сотрудника {temp_count / len(salary_dict)}")
