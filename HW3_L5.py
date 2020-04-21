with open('text_3_L5.txt', 'r', encoding='utf-8') as f:
   s_sum = []
   less = []
   line = f.read().split("\n")
   for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])
print(f'У сотрудника зарплата меньше 20 000:\n{less}.\nCредняя величина доходов сотрудников: {sum(map(float, s_sum))/ len(s_sum)}')

   #print(f"Сумма всех окладов {sum([int(value) for value in f.read().split(' ') if value.isdigit()])}")
   #не успела доработать этот момент.
