class NotComplexNumber(Exception):
    pass


class ComplexNumber:
    def __init__(self, arg):
        self.arg = arg
        self.x = arg

    def __add__(self, other):
        return f"({int(self.x[0]) + int(other.x[0])} + {int(self.x[1]) + int(other.x[1])}i)"

    def __mul__(self, other):
        return f"({int(self.x[0]) * int(other.x[0]) + (int(self.x[1]) * int(other.x[1])) * -1} +" \
               f" {int(self.x[1]) * int(other.x[0]) + int(self.x[0]) * int(other.x[1])}i)"

    def __str__(self):
        return f"({self.arg[0]} + {self.arg[1]}i)"


def not_int_check(arg):
    """
    :param arg: any list
    :return: result False if wrong symbols not found
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', ' ', 'i', '(', ')'}
    int_check = False
    j = 0
    while j < len(arg):
        if arg[j] in set_of_true:
            int_check = False
        else:
            int_check = True
            break
        j += 1
    if int_check:
        return True
    else:
        return False


def ans_check(my_string):
    """
    :return: возвращает int(arg) полученное с input
    """
    set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    temp_list = []
    while True:
        temp = ''.join(input(f"{my_string}: ").split())
        try:
            if not_int_check(temp) is False:
                try:
                    if temp[0] == '(' and temp[-1] == ')':
                        temp = temp[1:-1]
                    elif temp[0] == '(' and temp[-1] != ')':
                        raise NotComplexNumber
                    elif temp[0] != '(' and temp[-1] == ')':
                        raise NotComplexNumber
                except NotComplexNumber:
                    print('Неверный ввод комплексного числа (не хватает одной из скобок)')
                    temp = "***"
                try:
                    if temp.count('+') > 1:
                        raise NotComplexNumber
                    elif temp.count('-') > 2:
                        raise NotComplexNumber
                    elif temp[0] == '-' and temp[1] == '-':
                        raise NotComplexNumber
                except NotComplexNumber:
                    print("Введено слишком много операторов (+ или -)")
                    temp = "***"
                if temp != "***":
                    try:
                        if temp[0] == '-':
                            if temp.find('+') != -1 and temp.find('-', 1) != -1:
                                if temp.find('+') < temp.find('-', 1):
                                    temp_list.append(int(temp[:temp.find('+')]))
                                    temp_list.append(int(temp[temp.find('-', 1):-1]))
                                else:
                                    temp_list.append(int(temp[:temp.find('-', 1)]))
                                    temp_list.append(int(temp[temp.find('+'):-1]) * -1)
                                return temp_list
                            elif temp.find('+') == -1 and temp.find('-', 1) != -1:
                                temp_list.append(int(temp[:temp.find('-', 1)]))
                                temp_list.append(int(temp[temp.find('-', 1):-1]))
                                return temp_list
                            elif temp.find('+') != -1 and temp.find('-', 1) == -1:
                                temp_list.append(int(temp[:temp.find('+')]))
                                temp_list.append(int(temp[temp.find('+'):-1]))
                                return temp_list
                            else:
                                raise NotComplexNumber
                        elif temp[0] in set_of_true:
                            if temp.find('+') != -1 and temp.find('-') != -1:
                                if temp.find('+') < temp.find('-', 1):
                                    temp_list.append(int(temp[:temp.find('+')]))
                                    temp_list.append(int(temp[temp.find('-'):-1]))
                                else:
                                    temp_list.append(int(temp[:temp.find('-')]))
                                    temp_list.append(int(temp[temp.find('+'):-1]) * -1)
                                return temp_list
                            elif temp.find('+') == -1 and temp.find('-') != -1:
                                temp_list.append(int(temp[:temp.find('-')]))
                                temp_list.append(int(temp[temp.find('-'):-1]))
                                return temp_list
                            elif temp.find('+') != -1 and temp.find('-') == -1:
                                temp_list.append(int(temp[:temp.find('+')]))
                                temp_list.append(int(temp[temp.find('+'):-1]))
                                return temp_list
                            else:
                                raise NotComplexNumber
                        else:
                            raise NotComplexNumber
                    except NotComplexNumber:
                        print("Комплексное число введено с ошибкой")
            else:
                raise NotComplexNumber
        except NotComplexNumber:
            print("найдены некорректные символы")


print("Ввод комплексных чисел\nПример ввода: (x+yi) / x+yi / (x + yi) / x + yi, где x и y это число, а i - буква")
arg_1 = ComplexNumber(ans_check("Введите первое комплексное число"))
arg_2 = ComplexNumber(ans_check("Введите второе комплексное число"))
print(f"Исходные комплексные числа: {arg_1} и {arg_2}\nИх сумма:\n{arg_1} + {arg_2} = {arg_1 + arg_2}\n"
      f"Их произведение:\n{arg_1} * {arg_2} = {arg_1 * arg_2}")
