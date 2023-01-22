import model
import view

def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
                new = list(view.new_contact())
                model.change_contact(new)                                
                view.change_contact()
            case 6:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
                model.delete_contact()
                view.delete_contact()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)