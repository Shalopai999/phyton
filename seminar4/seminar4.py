# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random
equation = {}
n = int(input('Введите максимальную степень: '))
for i in range(n+1):
    if i > 0:
        if i == n:
            while True:
                koef = random.randint(-99,100)
                if koef != 0:
                    break
            equation[i] = koef
        else:
            equation[i] = random.randint(-99,100)

new_list = list(equation.keys())
st = ''

if n > 0:
    for i in range(len(new_list)):

        if equation[new_list[i]] != 0:

            if equation[new_list[i]] < -1 and new_list[i] != 1:
                st += f'{equation[new_list[i]]}*x**{new_list[i]}'

            elif equation[new_list[i]] > 1 and new_list[i] != 1 and i != 0:
                st += f'+{equation[new_list[i]]}*x**{new_list[i]}'

            elif equation[new_list[i]] > 1 and new_list[i] != 1 and i == 0:
                st += f'{equation[new_list[i]]}*x**{new_list[i]}'

            elif new_list[i] == 1 and equation[new_list[i]] > 0 and i != 0:
                st += f'+{equation[new_list[i]]}*x'

            elif new_list[i] == 1 and equation[new_list[i]] > 0 and i == 0:
                st += f'{equation[new_list[i]]}*x'

            elif new_list[i] == 1 and equation[new_list[i]] < 0:
                st += f'{equation[new_list[i]]}*x'

            elif equation[new_list[i]] == 1 and i != 0:
                st += f'+x**{new_list[i]}|'

            elif equation[new_list[i]] == 1 and i == 0:
                st += f'x**{new_list[i]}|'

            elif equation[new_list[i]] == -1:
                st += f'-x**{new_list[i]}|'

    print(st + '=0')
else: 
    print('Нет такой степени')

