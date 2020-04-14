from sys import argv

scrip_salary, time, rate, bonus = argv
try:
    time = int(time)
    rate = int(rate)
    bonus = int(bonus)

    salary = (time * rate) + bonus

    print(f'Зарпата составила {salary} .')

except ValueError:
    print('Вы ввели неправильные параметры!')
