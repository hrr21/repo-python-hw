class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = "a + b * i"

    def __add__(self, other):
        # z1 + z2 = (a + b * i) + (c + d * i) = (a + c) + (b + d) * i
        print("Сумма комплексных чисел равна: ")
        return f"z1 + z2 = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        # z1 * z2 = (x1 + y1 * i) * (x2 + y2 * i) = (x1 * x2 − y1 * y2) + (x1 * y2 + x2 * y1) * i
        print("Произведение комплексных чисел равно: ")
        return f"z1 * z2 = {self.a * other.a - self.b * other.b} + {self.a * other.b + other.a * self.b} * i"

z_1 = ComplexNumber(2, 2)
z_2 = ComplexNumber(-3, 3)

print(z_1 + z_2)
print(z_1 * z_2)