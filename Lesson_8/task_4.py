class Warehouse:
    def __init__(self, my_class):
        self.a = f"{type(my_class)}"[f"{type(my_class)}".rfind('.') + 1:-2]
        _temp = [my_class]
        self.warehouse = dict()
        if my_class != 0:
            self.warehouse.update(dict.fromkeys([self.a], _temp))

    def __str__(self):
        return f"{self.warehouse}"

    def append(self, x):
        _temp = []
        _a = f"{type(x)}"[f"{type(x)}".rfind('.') + 1:-2]
        if self.warehouse.get(_a) is not None:
            _temp = self.warehouse.pop(_a)
            _temp.append(x)
            self.warehouse.update(dict.fromkeys([_a], _temp))

        else:
            _temp.append(x)
            self.warehouse.update(dict.fromkeys([_a], _temp))

    def transfer(self, other):
        # возможно нужно трансферить всё
        _temp = list(self.warehouse.keys())
        print("Какое оборудование будем передавать?")
        [print(f"{index + 1}: {el}") for index, el in zip(range(0, len(_temp)), _temp)]
        x = int(input("Ваш выбор: ")) - 1
        _temp_list = self.warehouse.get(_temp[x])
        print("Какую модель будем передавать?")
        [print(f"{index + 1}: {el}") for index, el in zip(range(0, len(_temp_list)), _temp_list)]
        z = int(input("Ваш выбор: ")) - 1
        print(f"Сколько " + f"{type(_temp_list[z])}"[
                            f"{type(_temp_list[z])}".rfind('.') + 1:-2] + f" будем отдавать (в шт)?")
        y = int(input("Ваш выбор: "))
        if _temp_list[x].show_amount() - y >= 0:
            _a = Scan(_temp_list[z].show_name(), y)
            other.append(_a)
            _temp_list[x] - y
        else:
            print("\033[31m {}".format("!!!У вас нет столько предметов!!!"), end='')
            print("\033[0m {}".format(""))
        if _temp_list[x].show_amount() == 0:
            _temp_list.pop(x)

    def show(self, key):
        try:
            return self.warehouse.get(key)
        except ValueError:
            print("No object with that key")


class OfficeEquipment:
    def __init__(self, name, amount):
        self.name = name
        self.amount = int(amount)
        self.unique_param = "first_param\nsecond_param\n"

    def __str__(self):
        return f'"{self.name}": {self.amount} шт'

    def __repr__(self):
        return f'"{self.name}": {self.amount} шт'

    def stats(self):
        return f"{type(self)}"[f"{type(self)}".rfind('.') + 1:-2] + f":\n{self.unique_param}"

    def __sub__(self, other):
        self.amount -= other

    def __add__(self, other):
        self.amount += other

    def show_amount(self):
        return self.amount

    def show_name(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.mass = 0


class Scan(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.width = 0
        self.height = 0
        self.length = 0


class Xerox(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.guarantee = True


a = Xerox(name=input("Name = "), amount=input(f"Amount= "))
s = f"{type(a)}"[f"{type(a)}".rfind('.') + 1:-2]
b = Xerox(name="Xerox_b", amount=f"{int(12)}")
warehouse = Warehouse(b)
warehouse.append(a)
a = Scan(name="Scan_a", amount="1")
b = Scan(name="Scan_b", amount="2")
warehouse.append(a)
warehouse.append(b)
print(warehouse)
print(warehouse.show("Scan")[0].stats())
warehouse_2 = Warehouse(0)
warehouse.transfer(warehouse_2)
print(f"Склад №1\n{warehouse}")
print(f"Склад №2\n{warehouse_2}")
