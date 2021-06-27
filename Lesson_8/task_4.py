class Warehouse:
    warehouse = dict()

    # warehouse = {
    # key == class_name == f"{class}"?
    # Key = f"{class}"[s.rfind('.')+1:-2]
    # value == [class,class,class .. class]
    # }"
    # количество = len(value)
    #
    # What class should include?
    # class.name = string
    # class.amount = ? считать количество одинаковых моделей принтеров ?
    # stats?
    def __init__(self, my_class):
        self.a = f"{type(my_class)}"[f"{type(my_class)}".rfind('.') + 1:-2]
        _temp = [my_class]
        # print(my_class)
        # print(_temp)
        # temp_dict = dict.fromkeys([self.a], _temp)
        # print(temp_dict)
        self.warehouse.update(dict.fromkeys([self.a], _temp))

    # если в в warehouse уже есть такой ключ
    # то достать значение == список
    # присоединить старый список к тому, что пришёл
    #
    # if self.warehouse.get(self.x[0]) is not None:
    #
    #     self.x[1] += self.warehouse.get(self.x[0])
    #     temp = self.x.pop(1)
    #     self.warehouse.update(dict.fromkeys(self.x, temp))
    # else:
    #     temp = self.x.pop(1)
    #     self.warehouse.update(dict.fromkeys(self.x, temp))
    @classmethod
    def append(cls, x):
        _temp = []
        _a = f"{type(x)}"[f"{type(x)}".rfind('.') + 1:-2]
        if cls.warehouse.get(_a) is not None:
            _temp = cls.warehouse.pop(_a)
            _temp.append(x)
            print(_temp)
            cls.warehouse.update(dict.fromkeys([_a], _temp))
        else:
            cls.warehouse.update(dict.fromkeys([_a], _temp := [].append(x)))

    def __str__(self):
        return f"{self.warehouse}"


class OfficeEquipment:
    type = ''

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: {self.amount}шт"


class Printer(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        name = self.name
        amount = self.amount


class Scan(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        name = self.name
        amount = self.amount


class Xerox(OfficeEquipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        name = self.name
        amount = self.amount


a = Xerox(name=input("Name = "), amount=input(f"Amount= "))

s = f"{type(a)}"[f"{type(a)}".rfind('.') + 1:-2]
b = Xerox(name="Xerox_b", amount=f"{int(12)}")
warehouse = Warehouse(b)
warehouse.append(a)
print(warehouse)
