# class Date:
#     s = []
#
#     @staticmethod
#     def like_january(x):
#         # return true if x in [1..31]
#         if 1 <= x <= 31:
#             return True
#         else:
#             print("Введёно некорректное количество дней для нечетного месяца")
#             return False
#
#     @staticmethod
#     def like_april(x):
#         # return true if x in [1..30]
#         if 1 <= x <= 30:
#             return True
#         else:
#             print("Введёно некорректное количество дней для четного месяца")
#             return False
#
#     @staticmethod
#     def like_february(x):
#         # return true if x in [1..28]
#         if 1 <= x <= 28:
#             return True
#         else:
#             print("Введёно некорректное количество дней для февраля в НЕ високосном году")
#             return False
#
#     @staticmethod
#     def like_february_1(x):
#         # return true if x in [1..29]
#         if 1 <= x <= 29:
#             return True
#         else:
#             print("Введёно некорректное количество дней для февраля в високосном году")
#             return False
#
#     @classmethod
#     def clear(cls, _s):
#         _s = _s.split('-')
#         _s_1 = []
#         for i in range(len(_s)):
#             _s_1.append((int(_s[i])))
#         return _s_1
#
#     @staticmethod
#     def validate(_s):
#         if _s[2] % 4 != 0:
#             if 0 < _s[1] < 13:
#                 if _s[1] == 2:
#                     return Date.like_february(_s[0])
#                 elif _s[1] % 2 == 0:
#                     return Date.like_april(_s[0])
#                 else:
#                     return Date.like_january(_s[0])
#             else:
#                 print(f"В году всего 12 месяцев, а не {_s[1]}")
#                 return False
#         elif _s[2] % 4 == 0:
#             if 0 < _s[1] < 13:
#                 if _s[1] == 2:
#                     return Date.like_february_1(_s[0])
#                 elif _s[1] % 2 == 0:
#                     return Date.like_april(_s[0])
#                 else:
#                     return Date.like_january(_s[0])
#             else:
#                 print(f"В году всего 12 месяцев, а не {_s[1]}")
#                 return False
#
#
# def not_int_check(arg_1):
#     """
#     :param arg_1: any string
#     :return: result False if wrong symbols not found
#     """
#     set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'}
#     int_check = False
#     count = 0
#     j = 0
#     while j < len(arg_1):
#         if arg_1[j] in set_of_true:
#             int_check = False
#         else:
#             int_check = True
#             break
#         if arg_1[j] == '-':
#             count += 1
#         j += 1
#     if count != 2:
#         int_check = True
#     if int_check:
#         print(f"Был введён символ не являющийся числом, '-' или слишком много символов '-'.\n"
#               f"Строка не будет засчитана, введите заново")
#         return True
#     else:
#         return False
#
#
# while True:
#     s = input('Введите дату в формате день-месяц-год: ')
#     if not not_int_check(s):
#         a = Date.clear(s)
#         if Date.validate(a):
#             print(f'"{s}" это корректная дата')
#         else:
#             print(f'"{s}" это некорректная дата или не дата вовсе')
#         break

class Date:
    s = ''

    def __init__(self, s):
        self.s = s
        Date.s = self.s

    @classmethod
    def clear(cls):
        cls.s = cls.s.split('-')
        cls.s = [int(el) for el in cls.s]
        Date.s = cls.s

    @staticmethod
    def validate():
        """
        validate проверяет внутреннюю переменную s на корректность даты
        """
        temp = list(Date.s)
        if len(temp) == 3:
            if 0 < temp[1] < 13:
                if temp[2] % 4 == 0 and temp[1] == 2 and 0 < temp[0] < 30:
                    # если год високосный, месяц = февраль и день в пределах нормы
                    return "Date is fine"
                elif temp[1] == 2 and (temp[0] > 28 or temp[0] < 1):
                    # если год не високосный, месяц = февраль, а день не в порядке
                    return "Date is shit"
                else:
                    if temp[1] % 2 == 0 and 0 < temp[0] < 31:
                        # если месяц четный и день в порядке
                        return "Date is fine"
                    if temp[1] % 2 != 0 and 0 < temp[0] < 32:
                        # если месяц не четный и день не в порядке
                        return "Date is fine"
        else:
            return "Date is shit"


my_date = input('Введите дату в формате день-месяц-год: ')
set_of_true = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'}
n = 0
for el in my_date:
    if el not in set_of_true:
        print("Найден некорректный символ")
        break
    else:
        n += 1
if n == len(my_date):
    my_date = Date(my_date)
    my_date.clear()
    print(my_date.validate())
