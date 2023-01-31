import model
import view

def start():
    model.view_files()
    model.set_class(view.input_class())
    model.view_subject()
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == '0':
            break
        mark = int(view.what_mark())
        if mark>5 or mark<1:
            print('Такой оценки не существует!')            
        else:
            model.student_mark(student, mark)
    model.save_file()