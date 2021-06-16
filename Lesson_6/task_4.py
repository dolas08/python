# было очень весело работать над этой программой
from random import randint


class Car:
    speed = 0
    color = "цвет"
    name = "имя"
    is_police = False

    def go(self):
        print("Машина поехала")
        self.speed = randint(1, 100)

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Вы повернули {direction}")

    def show_speed(self):
        print(f"Текущая скорость машины {self.speed}")


class TownCar(Car):
    def __init__(self):
        self.name = "Ford"
        self.color = "синий"
        print(f"Ты сел в хорошую машину. это {self.name} окрашенная в {self.color} цвет\n"
              f"Рабочая лошадка за свои деньги. И в город, и на дачу или даже в какое-нибудь путешествие.\n"
              f"Ну что, поехали?\n"
              f"1: 'Конечно, выдвигаемся!'\n"
              f"2: 'Пожалуй, сегодня мне никуда не нужно ехать.")

    def show_speed(self):
        if self.speed > 60:
            print(f"Твоя скорость {self.speed} притормози, это нарушение правил!")
        else:
            print(f"Текущая скорость {self.speed}")


class SportCar(Car):
    def __init__(self):
        self.name = "Lexus"
        self.color = "Серебрянный"
        print(f"Ты сел в классную спортивную тачку. Это {self.name} окрашенная в {self.color} цвет.\n"
              f"Ну что, поехали?\n"
              f"1: 'Конечно, погнали!'\n"
              f"2: 'Пожалуй, я лучше пешком..")


class WorkCar(Car):
    def __init__(self):
        self.name = "KAMAZ"
        self.color = "зелёный"
        print(f"Ты сел в {self.name}, он окрашен в {self.color} цвет, но какая разница какой цвет?\n"
              f"Ведь это машина для работы. Поехали?\n"
              f"1: Опять работать..\n"
              f"2: К чёрту грузовики, как же они мне надоели...... ушёл менять работу..")

    def show_speed(self):
        if self.speed > 40:
            print(f"Твоя скорость - {self.speed} притормози!!!!, это нарушение правил!")
        else:
            print(f"Текущая скорость {self.speed}")


class PoliceCar(Car):
    def __init__(self):
        self.name = "Lada"
        self.color = "police skin"
        self.is_police = True
        print(f"Ты сел в свою рабочую машину. Это {self.name} окрашенная в {self.color},\n"
              f"Это абсолютно {self.is_police}, так как ты - сотрудник Полиции.\n"
              f"Пора выезжать на патруль\n"
              f"1: Поехали\n"
              f"2: Ой, забыл ключи в офисе, поеду в следующий раз.")


def ans_check():
    """
    функция ввода и проверки на int.
    :return: возвращает arg полученное с input
    """
    while True:
        try:
            arg = int(input(": "))
            if 0 < arg < 5:
                return arg
            else:
                print("Для продолжения необходимо ввести число из предоставленного выбора")
        except ValueError:
            print(f"Вы ввели не число")


def car_control(arg):
    """
    управление автомобилем, в зависимости от типа автомобиля
    :param arg: на входе число, означающее тип автомобиля
    :return: в функции возвращается 1, если нужно выйти из автомобиля
    """
    print(f"Машина в движении, что дальше?\n"
          f"1: Повернуть налево\n"
          f"2: Повернуть направо\n"
          f"3: Посмотреть на спидометр\n"
          f"4: Остановиться")
    _temp_choice = ans_check()
    # по-хорошему ветвление как-нибудь уменьшить, но я не придумал
    if arg == 1:
        if _temp_choice == 1:
            TownCar.turn(my_car, "налево")
        elif _temp_choice == 2:
            TownCar.turn(my_car, "направо")
        elif _temp_choice == 3:
            TownCar.show_speed(my_car)
        elif _temp_choice == 4:
            TownCar.stop(my_car)
            return 1
    if arg == 2:
        if _temp_choice == 1:
            SportCar.turn(my_car, "налево")
        elif _temp_choice == 2:
            SportCar.turn(my_car, "направо")
        elif _temp_choice == 3:
            SportCar.show_speed(my_car)
        elif _temp_choice == 4:
            SportCar.stop(my_car)
            return 1
    if arg == 3:
        if _temp_choice == 1:
            WorkCar.turn(my_car, "налево")
        elif _temp_choice == 2:
            WorkCar.turn(my_car, "направо")
        elif _temp_choice == 3:
            WorkCar.show_speed(my_car)
        elif _temp_choice == 4:
            WorkCar.stop(my_car)
            return 1
    if arg == 4:
        if _temp_choice == 1:
            PoliceCar.turn(my_car, "налево")
        elif _temp_choice == 2:
            PoliceCar.turn(my_car, "направо")
        elif _temp_choice == 3:
            PoliceCar.show_speed(my_car)
        elif _temp_choice == 4:
            PoliceCar.stop(my_car)
            return 1


while True:
    print("Выберете номер машины\n"
          "1: Простая, городская машина\n"
          "2: Спорткар\n"
          "3: Грузовой автомобиль\n"
          "4: Полицейская машина\n"
          "Итак, на чём поедем?")
    number = ans_check()
    if number == 1:
        my_car = TownCar()
        check = ans_check()
        if check == 2:
            break
        my_car.go()
        while True:
            if car_control(number) == 1:
                break
    elif number == 2:
        my_car = SportCar()
        check = ans_check()
        if check == 2:
            break
        my_car.go()
        while True:
            if car_control(number) == 1:
                break
    elif number == 3:
        my_car = WorkCar()
        check = ans_check()
        if check == 2:
            break
        my_car.go()
        while True:
            if car_control(number) == 1:
                break
    else:
        my_car = PoliceCar()
        check = ans_check()
        if check == 2:
            break
        my_car.go()
        while True:
            if car_control(number) == 1:
                break
    print(f"Вы вышли из машины и сами не поняли,\n"
          f"как оказались рядом со стоянкой автомобилей\n"
          f"1: Выбрать машину\n"
          f"2: Уйти")
    _temp = ans_check()
    if _temp == 1:
        continue
    elif _temp == 2:
        break
