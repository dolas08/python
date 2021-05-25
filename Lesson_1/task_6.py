a = input("Input sportsman achievement in km for 1st day: ")
b = input("How much km he should run?: ")
i = 1
while float(a) < float(b):
    i = i+1
    a = float(a)*0.1+float(a)
    #print(f"{i:02d}-day result is {a:.2f}")
print(f"{i}")
