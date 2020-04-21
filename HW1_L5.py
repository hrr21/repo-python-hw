f_1 = open("text_1_L5.txt", 'w', encoding="utf-8")
user_text = input("Введите текст \n")
while True:
    f_1.writelines(user_text + "\n")
    user_text = input("Введите текст, для прекращения ввода нажмите еще раз 'Enter' \n")
    if not user_text:
        break

f_1.close()
f_1 = open("text_1_L5.txt", "r", encoding="utf-8")
user_text = f_1.readlines()
print(user_text)
f_1.close()
