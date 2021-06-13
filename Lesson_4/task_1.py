# task_1 sys argv
from sys import argv

amount_hours, money_per_hour, bonus_money = argv[1:]
print(f"{(int(amount_hours) * int(money_per_hour)) + int(bonus_money)}")
