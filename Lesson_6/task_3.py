class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        _a = 0
        for el in self._income:
            _a += self._income.get(el)
        return _a


def ans_check():
    """
    :return: возвращает int(arg) полученное с input
    """
    while True:
        try:
            arg = int(input(": "))
            return arg
        except ValueError:
            print(f"Вы ввели не число")


worker_name = input("Введите имя работника: ")
worker_surname = input("Введите фамилию работника: ")
worker_position = input("Введите должность работника: ")
print("Введите зарплату работника", end='')
worker_wage = ans_check()
print("Введите премию работника", end="")
worker_bonus = ans_check()
a = Position(worker_name, worker_surname, worker_position, worker_wage, worker_bonus)
print(f"Работник {a.get_full_name()} получает {a.get_total_income()}")
