i = int(input("input your digit: "))
c = i % 10
while i > 0:
    if i % 10 > c:
        c = i % 10
    i = i // 10
print(f"max number in your digit is {c}")
