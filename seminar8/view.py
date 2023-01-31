import model

def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать?\nДля выхода введите 0: ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')