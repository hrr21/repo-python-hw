from itertools import cycle

с = 1
my_list = [123, True, "Hello"]
for el in cycle(my_list):
    if с > 20:
        break
    print(el)
    с += 1