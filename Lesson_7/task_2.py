from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v):
        self.v = v

    @abstractmethod
    def material_count(self):
        pass


class Coat(Clothes):
    @property
    def material_count(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    @property
    def material_count(self):
        return 2 * self.v + 0.3


def ans_check(str):
    """
    :return: возвращает int(arg) полученное с input
    """
    while True:
        try:
            arg = int(input(f"{str}: "))
            return arg
        except ValueError:
            print(f"Вы ввели не число")


v = ans_check("Введите размер (для пальто)")
h = ans_check("Введите рост (для костюма)")
a = Coat(v).material_count
b = Costume(h).material_count
print(f"Затраты ткани на костюм и пальто будут: {a + b}")
