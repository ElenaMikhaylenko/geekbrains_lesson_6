class Worker:
    #атрибуты класса
    name = "Ivan"
    surname = "Ivanov"
    position = "Economist"
    _income = {"wage": 30000, "bonus": 33000}

    def __init__(self, name = None):
        if name:
            self.name = name


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


work = Position()
print(work.get_full_name(), work.get_total_income())

