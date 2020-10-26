class Stationery:

    title = ""

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pen(Stationery):

    title = "Ручка"

    def draw(self):
        super().draw()
        print(f"Ручка? Ручка... Ручка!")


class Pencil(Stationery):

    title = "Карандаш"

    def draw(self):
        super().draw()
        print(f"Работает даже в космосе! (И без всяких разработок!)")


class Handle(Stationery):

    title = "Маркер"

    def draw(self):
        super().draw()
        print(f"Просто добавь немного воды.")


if __name__ == '__main__':
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
