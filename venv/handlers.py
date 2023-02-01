from loader import dp, bot
from aiogram import types
from random import randint

total = 150
p = 1

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!\n'
                            f'Я хочу поиграть с тобой в игру...\n'
                            f'На столе лежит {total} конфет.\n'
                            f'Возьми от 1 до 28 конфет так, что бы твой ход оказался последним.\n'
                            f'Помощь - /help')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    count = message.text.split()[1]
    total = int(count)
    await bot.send_message(message.from_user.id, f'Установил новое количество конфет в размере: {total}')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Ты можешь начать заново командой /start\n'
                           f'Либо установить своё количество конфет на столе командой /set (через пробел количество конфет)')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global p
    if message.text.isdigit():
        while total > 28:
            if int(message.text) > 0 and int(message.text) < 29:
                if p == 1:
                    total -= int(message.text)
                    await bot.send_message(message.from_user.id, f'Конфет осталось {total}')
                    p = 0
                else:
                    a = randint(1, 28)
                    await bot.send_message(message.from_user.id, f'А я возьму {a}!')
                    total -= a
                    await bot.send_message(message.from_user.id, f'Конфет осталось {total}')
                    p = 1
                    mes_all()
            else:
                await bot.send_message(message.from_user.id, f'Введи количество от 1 до 28!')
                mes_all()
    else:
        await bot.send_message(message.from_user.id, f'Введи число!')
        mes_all()
    if p == 1:
        await bot.send_message(message.from_user.id, f'Ты выиграл, молодец! Давай заново)')
        total = 150
        p = 1
    else:
        await bot.send_message(message.from_user.id, f'Выиграл я! Го еще)')
        total = 150
        p = 1
