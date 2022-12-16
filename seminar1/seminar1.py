# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num = int(input('Введите день недели: '))
# if num < 0 or num > 7:
#     print('Нет такого дня недели')
# else:
#     if num > 5 and num < 8:
#         print('Выходной день')
#     else:
#         print('Рабочий день')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату Х: '))
# y = int(input('Введите координату Y: '))
# if x == 0 or y == 0:
#     print('Точка не входит в четверть!')
# if x > 0 and y > 0:
#     print('Точка входит в первую четверть')
# if x < 0 and y > 0:
#     print('Точка входит во вторую четверть')
# if x > 0 and y < 0:
#     print('Точка входит в четвертую четверть')
# if x < 0 and y < 0:
#     print('Точка входит в третью четверть')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# ch = int(input('Введите номер четверти: '))
# if ch < 1 or ch > 4:
#     print('Такой четверти не существует!')
# if ch == 1:
#     print('Координаты точки Х больше 0, Y больше 0')
# if ch == 2:
#     print('Координаты точки Х меньше 0, Y больше 0')
# if ch == 3:
#     print('Координаты точки Х меньше 0, Y меньше 0')
# if ch == 4:
#     print('Координаты точки Х больше 0, Y меньше 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
x1 = int(input('Введите первую координату первой точки: '))
y1 = int(input('Введите вторую координату первой точки: '))
x2 = int(input('Введите первую координату второй точки: '))
y2 = int(input('Введите вторую координату второй точки: '))
distance = round(math.sqrt(((x2 - x1)*(x2 - x1))+((y2 - y1)*(y2 - y1))), 2)
print('Расстояние между точками равно: ',distance)
