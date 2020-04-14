from itertools import count

с = 1
for el in count(int(input("Введите число для начала генерации: "))):
    if с > 20:
        break
    print(el)
    с += 1
