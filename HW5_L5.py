try:
    with open('text_5_L5.txt', 'w+') as f:
        line = input('Введите числа через пробел:\n')
        f.writelines(line)
        my_numb = line.split()
        print(f"Сумма ваших числе равна :{sum(map(int, my_numb))}")
except ValueError:
    print('Ошибка ввода, нужно ввести цифры.')