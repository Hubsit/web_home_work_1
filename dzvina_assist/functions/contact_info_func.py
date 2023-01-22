from dzvina_assist.Classes.ConsoleView import ContactInfoView, AllContactsInfoView


def contact_info_func(book):
    return ContactInfoView.user_view(book)


def all_contact_info_func(book):
    return AllContactsInfoView(book)
