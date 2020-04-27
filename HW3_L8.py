class MyException(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                user_number = int(input("Введите число: "))
                self.my_list.append(user_number)

            except:
                request = input(f"Попробовать еще раз? Yes/No ")
                if request == "Yes" or request == "yes":
                    print(try_except.my_input())
                elif request == "No" or request == "no":
                    return f"Вы завершили ввод,\nВаш список: {self.my_list}"
                else:
                    return f"Вы завершили ввод,\nВаш список: {self.my_list}"


try_except = MyException(1)

print(try_except.my_input())
