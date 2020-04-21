f_2 = open('text_2_L5.txt', 'r', encoding='utf-8')
line = 0
for i in f_2:
    line += 1
    flag = 0
    word = 0
    for x in i:
        if x != ' ' and flag == 0:
            word += 1
            flag = 1
        elif x == ' ':
            flag = 0

    print(f"В {line}) строке : {len(i)} символов и {word} слов")
print(f'Количество строк в файле : {line}')
f_2.close()
