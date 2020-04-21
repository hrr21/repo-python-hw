class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
       #создан родитель


class RoadCalc(Road):
    def __init__(self, length, width, mass, height):
        super().__init__(length, width)
        self._mass = mass
        self._height = height

    def mass(self):
        mas = self._length * self._width * self._mass * self._height / 1000
        print(f"{mas} тонн асфальта понадобиться")

a = RoadCalc(20, 5000, 25, 5)
a.mass()

        # 20м * 5000м * 25кг * 5см = 12500т
