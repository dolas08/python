from random import randint


class Matrix:
    def __init__(self, my_list, n, m):
        """
        принимает список списков
        """
        self._my_list = my_list
        self._n = n
        self._m = m

    def __str__(self):
        """
        вывод матрицы в привычном виде
        """
        s = ''
        for _row in self._my_list:
            for _elem in _row:
                s += f"{_elem} "
            s += "\n"
        return s

    def __getitem__(self, item):
        return self._my_list[item]

    def __add__(self, other):
        """
        метод сложения матриц,
        на входе две матрицы,
        на выходе третья
        """
        m1 = list(self)
        m2 = list(other)
        m3 = []
        c = []
        i = 0
        while i < len(m1):
            for _x, _y in zip(m1[i], m2[i]):
                c += [int(_x) + int(_y)]
            # сложение с разными сторонами
            # la = len(m1[i])
            # lb = len(m2[i])
            # if la > lb:
            #     c += m1[la - lb + 1:]
            # elif la < lb:
            #     c += m2[lb - la + 1:]
            m3.append(c)
            c = []
            i += 1
        return Matrix(m3, self._n, self._m)


def ans_check(_str):
    """
    :return: возвращает int(arg) полученное с input
    """
    while True:
        try:
            arg = int(input(f"{_str}: "))
            return arg
        except ValueError:
            print(f"Вы ввели не число")


# я вводил эту функцию как метод класса Matrix и всё работало, но показалось что пока лучше вынести
def matrix_create_random(n, m, x):
    temp = [list() * n for i in range(0, m)]
    for row in range(0, n):
        for elem in range(0, m):
            temp[elem].append(randint(0, x))
    _temp = Matrix(temp, n, m)
    return temp


def not_int_check(arg_1):
    """
    :param arg_1: any list
    :return: result False if wrong symbols not found
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '}
    int_check = False
    j = 0
    while j < len(arg_1):
        if arg_1[j] in set_of_true:
            int_check = False
        else:
            int_check = True
            break
        j += 1
    if int_check:
        print(f"Был введён символ не являющийся числом или пробелом\n"
              f"Строка не будет засчитана, введите заново")
        return True
    else:
        return False


print("Введите 1 или 2, где:\n"
      "1: рандомные матрицы\n"
      "2: ручной ввод двух матриц")
x = ans_check("ваш выбор")
if x == 1:
    n = ans_check("Введите размер матрицы n*n")
    m = n
    x = ans_check("Введите максимальное число для элемента генерируемой матрицы")
    my_list_1 = Matrix(matrix_create_random(n, m, x), n, m)
    my_list_2 = Matrix(matrix_create_random(n, m, x), n, m)
elif x == 2:
    n = ans_check("Введите размер матрицы n*n")
    m = n
    my_list_1 = []
    my_list_2 = []
    for el in range(n):
        temp_check = True
        while temp_check:
            temp = input(f"{el + 1}-строка первой матрицы:").split()
            temp_check = not_int_check(temp)
            temp_n = len(temp)
            if m != temp_n:
                temp_check = True
                print("было введено несоответствующее количество символов")
            if not temp_check:
                my_list_1.append(temp)
    for el in range(n):
        temp_check = True
        while temp_check:
            temp = input(f"{el + 1}-строка Второй матрицы:").split()
            temp_check = not_int_check(temp)
            temp_n = len(temp)
            if m != temp_n:
                temp_check = True
                print("было введено несоответствующее количество символов")
            if not temp_check:
                my_list_2.append(temp)

# интересно, что на входе при рандомной генерации матрица хавает матрицу в следующих двух строках
# и проблем не возникает.
# это переопределение нужно чтобы создать матрицы после ручного ввода
my_matrix_1 = Matrix(my_list_1, n, m)
my_matrix_2 = Matrix(my_list_2, n, m)
print(f"Матрица 1:\n{my_matrix_1}")
print(f"Матрица 2:\n{my_matrix_2}")
print(f"Результат сложения матриц:\n{my_matrix_1 + my_matrix_2}")
