from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size


    @abstractmethod
    def cloth_area(self):
        pass

    def cloth_area_all(self):
        return int((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3))


class Coat(Clothes):

    def __init__(self, size):
        super().__init__(size)

    @property
    def cloth_area(self):
        print(f"На пошив пальто потребуется: {int(self.size / 6.5 + 0.5)} квадратных метров ткани.")


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def cloth_area(self):
        print(f"На пошив костюма потребуется: {int(self.height * 2 + 0.3)} квадратных метров ткани.")


a = Coat(12)
print(a.cloth_area)
b = Costume(12)
print(b.cloth_area)


