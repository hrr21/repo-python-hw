class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f"Все верно"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"

    def __str__(self):
        return f"Текущая дата {Data.extract(self.day_month_year)}"


my_day = Data("27 - 04 - 2020")

print(my_day)

print(Data.valid(10, 11, 2025))
print(my_day.valid(11, 13, 2008))
print(my_day.valid(33, 12, 2020))
print(Data.valid(1, 11, 2000))

print(Data.extract("27 - 04 - 2012"))
print(my_day.extract("27 - 04 - 2020"))
