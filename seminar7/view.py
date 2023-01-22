def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = input('\nВведите пункт меню: ')
    if user_input.isdigit() and int(user_input)>0 and int(user_input)<9:
        return int(user_input)
    else: print('Введите корректные данные!')

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пуста или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер контакта: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    search = input('Введите строку для поиска: ')
    return search

def delete_contact():
    print('Контакт удален')

def change_contact():
    print('Контакт изменен')