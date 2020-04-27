class DivisionByZero:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.denominator = dividend

    @staticmethod
    def divide_by_zero(divider, dividend):
        try:
            return divider / dividend
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


div = DivisionByZero(0, 5)
print(DivisionByZero.divide_by_zero(5, 0))
print(DivisionByZero.divide_by_zero(6, 0.1))
print(div.divide_by_zero(8, 0))
print(DivisionByZero.divide_by_zero(0, 0))