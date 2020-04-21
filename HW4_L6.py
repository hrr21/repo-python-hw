class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина поехала."

    def stop(self):
        return f"Машина {self.name} остановилась."

    def turn_left(self):
        return f"Машина {self.name} повернула налево."

    def turn_right(self):
        return f"Машина {self.name} повернула направо."

    def show_speed(self):
        return f'Текущая скорость машины {self.name}: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed}")

        if self.speed > 60:
            return f"Скорость машины {self.name} выше допустимых значений."
        else:
            return f"Скорость машины {self.name} в пределах нормы."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed}")

        if self.speed > 40:
            return f"Скорость машины {self.name} выше допустимых значений."
        else:
            return f"Скорость машины {self.name} в пределах нормы."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} - это полицейская машина"
        else:
            return f"{self.name} - это не полицейская машина"


mazda = SportCar(105, 'Красный', 'Mazda', False)
kia = TownCar(35, 'Серая', 'Kia', False)
lada = WorkCar(60, 'Белая', 'Lada', True)
ford = PoliceCar(100, 'Синяя', 'Ford', True)

print(lada.turn_right())
print(f'Когда {mazda.turn_left()}, {mazda.stop()}')
print(f'{kia.go()} {kia.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Эта машина {mazda.name} полицейская? {mazda.is_police}')
print(f'А эта машина {lada.name} полицейская? {lada.is_police}')
print(mazda.show_speed())
print(ford.police())
print(ford.show_speed())
