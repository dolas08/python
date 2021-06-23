class Cell:
    def __init__(self, _a=10):
        self.cell_amount = _a

    def __add__(self, other):
        """
        сложение двух клеток
        """
        return Cell(self.cell_amount + other.cell_amount)

    def __sub__(self, other):
        """
        разность двух клеток
        """
        if self.cell_amount - other.cell_amount < 0:
            raise ValueError("разность клеток меньше ноля")
        else:
            return Cell(self.cell_amount - other.cell_amount)

    def __mul__(self, other):
        """
        умножение двух клеток
        """
        return Cell(self.cell_amount * other.cell_amount)

    def __truediv__(self, other):
        """
        целочисленное деление двух клеток
        """
        return Cell(self.cell_amount // other.cell_amount)

    def __str__(self):
        return f"{self.cell_amount}"

    def make_order(self, x):
        """
        Создание строки, в которой ячейки клетки
        разделены по x элементов на строку
        :param x: разграничитель ячеек в клетке
        :return: "отсортированная" строка s
        """
        s = []
        j = 1
        for i in range(self.cell_amount):
            s.append('*')
            if x * j == i + 1:
                s.append('\n')
                j += 1
        return ''.join(s)


def ans_check(_str="Ваш выбор"):
    """
    :return: возвращает int(arg) полученное с input
    """
    while True:
        try:
            arg = int(input(f"{_str}: "))
            return arg
        except ValueError:
            print(f"Вы ввели не число")


def ans_check_cell(_str):
    """
    :return: возвращает int(arg) полученное с input в пределах от 1 до 5
    """
    while True:
        try:
            arg = int(input(f"{_str}: "))
            if 0 < arg < 6:
                return arg
            else:
                print("Ваш выбор должен быть числом от 1 до 5 включительно")
        except ValueError:
            print(f"Вы ввели не число")


def cell_control(arg_1, arg_2):
    """
    управление операциями над клетками
    :param arg_1: клетка 1
    :param arg_2: клетка 2
    :return в зависимости от выборов одна из операций над клетками
    """
    print(f"Какую операцию будем делать?\n"
          f"1: Сложение клеток\n"
          f"2: Вычитание клеток\n"
          f"3: Умножение клеток\n"
          f"4: Деление клеток\n"
          f"5: Показать порядок клеток")
    temp_check = ans_check_cell("Ваш выбор")
    if temp_check == 1:
        return f"\nОтвет:{arg_1 + arg_2}\n"
    elif temp_check == 2:
        return f"\nОтвет:{arg_1 - arg_2}\n"
    elif temp_check == 3:
        return f"\nОтвет:{arg_1 * arg_2}\n"
    elif temp_check == 4:
        return f"\nОтвет:{arg_1 / arg_2}\n"
    else:
        x = ans_check("Введите количество ячеек в ряд для первой клетки")
        y = ans_check("Введите количество ячеек в ряд для второй клетки")
        print(f"Первая клетка:\n\n{a.make_order(x)}\n")
        print(f"Вторая клетка:\n\n{b.make_order(y)}\n")


def cell_input():
    _a = Cell(ans_check("Введите количество ячеек первой клетки"))
    _b = Cell(ans_check("Введите количество ячеек второй клетки"))
    return _a, _b


temp = 0
a, b = cell_input()
while True:
    if temp == 1:
        print(f"Ввести размер клеток заново?\n"
              f"1: Нет, продолжить с текущими\n"
              f"2: Да, нужны новые клетки")
        # принимается любое число для продолжения и только 2 для создания новых клеток
        temp = ans_check()
        if temp == 2:
            a, b = cell_input()
    print(f"{cell_control(a, b)}")
    print(f"Начать заново и выбрать другую операцию?\n"
          f"1: Да, хочу ещё\n"
          f"2: Нет, завершить программу")
    temp = ans_check()
    if temp == 2:
        break
