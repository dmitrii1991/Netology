
class Contact:

    def __init__(self, name, surname, number, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        if args == ():  # проверка на наличие args
            self.favourites = 'НЕТ'
        else:
            self.favourites = args
        if kwargs == {}:  # проверка на наличие kwargs
            self.add_info = 'НЕТ'
        else:
            self.add_info = kwargs

    def __str__(self):
        info = 'Имя: {}\nФамилия: {}\nТелефон: {}\nВ избранных: {}\nДополнительная информация:'.\
            format(self.name, self.surname, self.number, self.favourites)
        if self.add_info != 'НЕТ':
            for i in self.add_info.items():
                info += '\n\t{}'.format(i)
        else:
            info += '\nНЕТ'
        return info

class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.book = []

    def add_contact(self, contact):
        self.book.append(contact)

    def show_all(self):
        for _ in self.book:
            print(_)

    def del_contact_by_number(self, number):
        for contact in self.book[:]:
            if contact.number == number:
                self.book.remove(contact)

    def print_fav_con(self):
        for contact in self.book:
            if contact.favourites != 'НЕТ':
                print(contact)

    def search_by_name(self, name, surname=''):
        for contact in self.book:
            if name == contact.name:
                print(contact)
            elif surname == contact.surname:
                print(contact)


jhon = Contact('Jhon', 'Smith', '+71234567809',telegram='@jhony', email='jhony@smith.com')
dima = Contact('Dima', 'Rcdfe', '+718985684',vk='@j85', email='jerer@ser.com')
re = Contact('Re', 'Swe', '89854')
print(jhon)

ph = PhoneBook('new')

ph.add_contact(jhon)
ph.add_contact(dima)
ph.add_contact(re)
# ph.show_all()

ph.del_contact_by_number('+71234567809')
ph.show_all()

ph.print_fav_con()
ph.search_by_name('Dima', 'Rcdfe')



