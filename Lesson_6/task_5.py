class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисую ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисую карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисую маркером")


item = Stationery
item.draw(item)
item_1 = Pen
item_1.draw(item_1)
item_2 = Pencil
item_2.draw(item_2)
item_3 = Handle
item_3.draw(item_3)
