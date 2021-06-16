class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, _mass_for_1cm, _amount_cm):
        return self._length * self._width * _mass_for_1cm * _amount_cm / 1000


a = int(input("Введите Длину дороги в метрах: "))
b = int(input("Введите ширину дороги в метрах: "))
mass_for_1cm = int(input("Введите количество вещества на 1см (в килограммах): "))
amount_cm = int(input("Введите количество см: "))
print(f"Для покрытия заданного количества дороги необходимо "
      f"{Road(a, b).mass(mass_for_1cm, amount_cm)} тонн асфальта")
