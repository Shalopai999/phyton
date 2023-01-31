import controller
import os

journal = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    path = './classes/'+ class_path + '.txt'

def view_files():
    path = '.\classes'
    rez = sorted(os.listdir(path))
    print('Список классов:')
    for n, item in enumerate(rez):        
        print(f"{n+1}. {item.split('.')[0]}")

def view_subject():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    i = 1
    print('Список предметов:')
    for subs in file:
        print(f"{i}. {subs.split(';')[0]}")
        i += 1        

def set_subject(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    print('Ученики: ')
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = study.split(':')[1].split()

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def get_journal():
    return journal

def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks