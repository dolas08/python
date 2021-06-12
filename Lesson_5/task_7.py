from itertools import count
import json
import codecs

with open('text_7.txt', 'r', encoding='utf-8') as f, \
        codecs.open('text_7_output.json', 'w', encoding='utf-8') as f_output:
    n = len(f.readlines())
    f.seek(0)
    temp_count = 0
    temp_count_positive = 0
    profit_db = dict()
    for i in count(1):
        temp = f.readline().split()
        profit_db.setdefault(temp[0], int(temp[2]) - int(temp[3]))
        if int(temp[2]) - int(temp[3]) > 0:
            temp_count += int(temp[2]) - int(temp[3])
            temp_count_positive += 1
        if i == n:
            break
    avg_profit_db = dict()
    avg_profit_db.setdefault('average_profit', temp_count / temp_count_positive)
    json.dump([profit_db, avg_profit_db], f_output, ensure_ascii=False, sort_keys=False, indent=4)
