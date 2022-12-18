# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# sum = 0
# num = input('Введите число: ')
# for i in str(num):
#     if i != '.':
#         sum = sum + int(i)
# print(sum)

# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число: '))
# ch = 0
# sum = 0
# for i in range(1, n+1):
#     ch = round((1 + 1/i)**i, 2)
#     print(ch, end= ' ')
#     sum = sum + ch
# print(f'Сумма чисел равна: {sum}')

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random
n = int(input('Введите число: '))
my_list = []
my_list2 = []
for i in range(n, 0, -1):
    my_list.append(random.randint(0,99))
    j = random.randint(0, i)
    my_list2[j] = my_list[i]
print(my_list)
print(my_list2)
