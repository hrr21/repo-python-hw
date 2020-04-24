class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f"Результат операции {self.quantity * '*'}"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity <= other.quantity:
            print("Проведена некорректная операция, вычитание не может быть произведено!")
        else:
            return self.quantity - other.quantity

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, row):
        orderly = ['*' * row for _ in range(self.quantity // row)]
        orderly.append('*' * (self.quantity % row))
        return f'\n'.join(orderly)


quantity_1 = Cell(12)
quantity_2 = Cell(5)

print(quantity_1)
print(quantity_2)
print(quantity_1 + quantity_2)
print(quantity_1 - quantity_2)
print(quantity_2.make_order(3))
print(quantity_1.make_order(4))
print(quantity_1 / quantity_2)
