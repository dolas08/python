class NotComplexNumber(Exception):
    pass


class ComplexNumber:
    def __init__(self, arg):
        """
        :param arg: string
        """
        # self.arg = arg
        self.x = arg
        # должен заходить String, который мы проверим на правильность ввода
        # а потом, если нужно складывать или умножать комплексные числа, то
        # конвертить комплексное число в list, совершать операцию
        # отдавать ComplexNumber(string)

    def __add__(self, other):
        temp_1 = self.convert(self.x)
        temp_2 = other.convert(other.x)
        temp_3 = [int(temp_1[0]) + int(temp_2[0]), "+", int(temp_1[1]) + int(temp_2[1]), "i"]
        return ComplexNumber(''.join(map(str, temp_3)))

    def __mul__(self, other):
        temp_1 = self.convert(self.x)
        temp_2 = other.convert(other.x)
        temp_3 = [int(temp_1[0]) * int(temp_2[0]) + int(temp_1[1]) * int(temp_2[1]) * -1, "+",
                  int(temp_1[1]) * int(temp_2[0]) + int(temp_1[0]) * int(temp_2[1]), "i"]

        return ComplexNumber(''.join(map(str, temp_3)))

    def __str__(self):
        return f"{self.x}"

    @staticmethod
    def validate_input(arg):
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

    @staticmethod
    def complex_number_validate(my_string):
        """
        :arg my_string - описание для input
        :return temp, содержащий корректно введёное комплексное число
        """
        set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        temp_logic = True
        while temp_logic:
            temp = ''.join(input(f"{my_string}: ").split())
            try:
                if ComplexNumber.validate_input(temp) is False:
                    try:
                        if temp[0] == '(' and temp[-1] == ')':
                            temp = temp[1:-1]
                        elif temp[0] == '(' and temp[-1] != ')':
                            raise NotComplexNumber
                        elif temp[0] != '(' and temp[-1] == ')':
                            raise NotComplexNumber
                    except NotComplexNumber:
                        temp_logic = True
                        print('Неверный ввод комплексного числа (не хватает одной из скобок)')
                        # temp = "***"
                        continue
                    try:
                        if temp.count('+') > 1:
                            raise NotComplexNumber
                        elif temp.count('-') > 2:
                            raise NotComplexNumber
                        elif temp[0] == '-' and temp[1] == '-':
                            raise NotComplexNumber
                    except NotComplexNumber:
                        temp_logic = True
                        print("Введено слишком много операторов (+ или -)")
                        # temp = "***"
                        continue
                    if temp_logic:
                        try:
                            if temp[0] == '-':
                                if temp.find('+') != -1 and temp.find('-', 1) != -1:
                                    if temp.find('+') < temp.find('-', 1):
                                        temp_logic = False
                                    else:
                                        temp_logic = False
                                elif temp.find('+') == -1 and temp.find('-', 1) != -1:
                                    temp_logic = False
                                elif temp.find('+') != -1 and temp.find('-', 1) == -1:
                                    temp_logic = False
                                else:
                                    raise NotComplexNumber
                            elif temp[0] in set_of_true:
                                if temp.find('+') != -1 and temp.find('-') != -1:
                                    if temp.find('+') < temp.find('-', 1):
                                        temp_logic = False
                                    else:
                                        temp_logic = False
                                elif temp.find('+') == -1 and temp.find('-') != -1:
                                    temp_logic = False
                                elif temp.find('+') != -1 and temp.find('-') == -1:
                                    temp_logic = False
                                else:
                                    raise NotComplexNumber
                            else:
                                raise NotComplexNumber
                        except NotComplexNumber:
                            temp_logic = True
                            print("Комплексное число введено с ошибкой")
                            continue
                else:
                    raise NotComplexNumber
            except NotComplexNumber:
                temp_logic = True
                print("найдены некорректные символы")
                continue
        return temp

    @staticmethod
    def convert(my_string):
        """
        :param my_string: Комплексное число, проверенное в  complex_number_validate
        :return: список, содержащий цифры из комплексного числа взятого в input
                например: input = (2+1i) => list = [int(2),int(1)]
        """
        set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        temp_list = []
        temp = ''.join(my_string.split())
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


print("Ввод комплексных чисел\nПример ввода: (x+yi) / x+yi / (x + yi) / x + yi, где x и y это число, а i - буква")
arg_1 = ComplexNumber(ComplexNumber.complex_number_validate("Введите первое комплексное число"))
arg_2 = ComplexNumber(ComplexNumber.complex_number_validate("Введите второе комплексное число"))
print(f"Исходные комплексные числа: {arg_1} и {arg_2}\nИх сумма:\n{arg_1} + {arg_2} = {arg_1 + arg_2}\n"
      f"Их произведение:\n{arg_1} * {arg_2} = {arg_1 * arg_2}")

# print(f"arg_3 ={arg_1 * arg_2 * arg_1 * arg_2 * arg_1 * arg_2}")
# print(f"arg_3 ={arg_1 + arg_2 + arg_1 + arg_2 + arg_1 + arg_2}")
# print(f"arg_3 ={(arg_1 + arg_2) * (arg_1 + arg_2) * (arg_1 + arg_2)}")
