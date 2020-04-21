translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4_L5.txt', 'r') as f:

    for i in f:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + '  ' + i[1])
    print(new_file)

with open('new_text_4_L5.txt', 'w', encoding="utf-8") as f_2:
    f_2.writelines(new_file)
