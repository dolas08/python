from itertools import count
from googletrans import Translator

with open('text_4.txt', 'r', encoding='utf-8') as f, open('text_4_output.txt', 'w', encoding='utf-8') as f_output:
    n = len(f.readlines())
    f.seek(0)
    for i in count(1):
        temp = f.readline().split()
        translator = Translator()
        print(f"{translator.translate(temp[0], src='en', dest='ru').text} - {temp[2]}", file=f_output)
        if i == n:
            break
