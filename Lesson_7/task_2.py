from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material_count(self):
        pass

    def __init__(self, _v):
        self.v = _v


class Coat(Clothes):
    @property
    def material_count(self):
        return Coat(self.v / 6.5 + 0.5)

    def __add__(self, other):
        return self.v + other.v


class Costume(Clothes):
    @property
    def material_count(self):
        return Costume(2 * self.v + 0.3)

    def __add__(self, other):
        return self.v + other.v


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


v = ans_check("Введите размер (для пальто)")
h = ans_check("Введите рост (для костюма)")
a = Coat(v).material_count
b = Costume(h).material_count
# a и b остаются классами Coat и Costume одновременно,
# но когда вычисляется формула, то внутренняя переменная,
# отвечающая за V или H (которая v в коде), теряется,
# так как создаётся новый объект Coat(v) или Costume(v)
# потеря переменной это не хорошо, но для одноразового выполнения кода - не мешает
print(f"Затраты ткани на костюм и пальто будут: {a + b}")
