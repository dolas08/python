f = open("text_1.txt", "w+", encoding="utf-8")
while True:
    temp = input("Введите вашу строку или нажмите Enter чтобы завершить: ")
    if len(temp) > 0:
        print(f"{temp}", file=f)
    else:
        break
f.close()
