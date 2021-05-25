earnings = input("input your earnings: ")
costs = input("input your costs: ")
if int(earnings)-int(costs) > 0:
    print("You working with profit")
    print(f"Your rent is {(int(earnings)-int(costs))/(int(earnings))}")
    i = input("How many workers do you have?: ")
    print(f"your profit per worker is {(int(earnings)-int(costs))/int(i)}")
else:
    print("You working with loss")
