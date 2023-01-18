# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

# summ = int(input('Введите количество конфет на столе: '))
# p = randint(0, 1)
# kolvo1 = 0
# kolvo2 = 0
# print(p)
# while summ > 28:
#     if p == 1:
#         a = int(input('Возьмите от 1 до 28 конфет: '))
#         summ -= a
#         kolvo1 += a
#         p = 0
#         print(f'Вы взяли {a} конфет, у вас {kolvo1} конфет, на столе осталось {summ} конфет.')
#     else:
#         a = randint(1, 29)
#         summ -= a
#         kolvo2 += a
#         p = 1
#         print(f'Бот взял {a} конфет, у него {kolvo2} конфет, на столе осталось {summ} конфет.')
# if p == 1:
#     print('Вы выиграли!')
# else:
#     print('Выиграл бот!')

# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

desk = list(range(1, 10))
for i in range(3):
    print(desk[3*i+0],'|',desk[3*i+1],'|',desk[3*i+2])
    print('---------')

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# stroka = input('Введите строку типа 5a3b4c или aaaaabbbcccc : ')
# cod = ''
# e = stroka[0]
# c = ''
# decod = ''
# n = 1
# if stroka[0].isdigit():
#     for i in range(len(stroka)):
#         if stroka[i].isdigit():
#             c += stroka[i]
#         else:
#             decod += stroka[i] * int(c)
#             c = ''
#     print(decod)
# else:
#     for i in range(1, len(stroka)):
#         if stroka[i] == e:
#             n += 1
#         else:
#             cod += str(n) + e
#             e = stroka[i]
#             n = 1
#     cod += str(n) + e
#     print(cod)
