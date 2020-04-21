class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


a = Position("Иван", "Петров", "Руководитель", 100000, 15000)

print(f"Фамилия Имя: {a.get_full_name()}")
print(f"Должность: {a.position}")
print(f"Доход (оклад + премия): {a.get_total_income()}")