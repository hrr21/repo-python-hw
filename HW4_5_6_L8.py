class StorageEquipment:
    def __init__(self):
        pass


class Equipment:
    def __init__(self, name, price, cost, *args):
        self.name = name
        self.price = price
        self.cost = cost
        self.my_storage_full = []
        self.my_storage = []
        self.my_unit = {"Модель устройства": self.name, "Цена за единицу": self.price, "Количество": self.cost}

    def save(self):
        symbol = False

        while symbol == False:
            try:
                user_name = input(f"Введите наименование товара: ")
                user_price = int(input(f"Введите цену за единицу товара: "))
                user_cost = int(input(f"Введите количество товара: "))
                user_storage = {"Модель устройства": user_name, "Цена за единицу": user_price, "Количество": user_cost}
                self.my_unit.update(user_storage)
                self.my_storage.append(self.my_unit)
                print(f"Новый список :\n {self.my_storage}")
            except ValueError:
                return f"Некорректно введены данные"
            print(f"Для прекращения ввода введите '#' для продолжения - 'Enter'")
            request = input(" ")
            if request != '#':
                symbol = False
                self.my_storage_full.append(self.my_storage)
                return Equipment.save(self)
            else:
                symbol = True
                print(f"Весь склад -\n {self.my_storage_full}")
                break


class Printer(Equipment):

    def to_print(self):
        return f"Я печатаю"


class Scanner(Equipment):
    def to_scan(self):
        return f"Я сканирую"


class Xerox(Equipment):
    def to_xerox(self):
        return f"Я копирую"



unit_1 = Printer('HP', 4650, 5)
unit_2 = Scanner('Canon', 2300, 5)
unit_3 = Xerox('Xerox', 3200, 12)

print(unit_1.save())
print(unit_2.save())
print(unit_3.save())
print(unit_1.to_print())
print(unit_3.to_xerox())
