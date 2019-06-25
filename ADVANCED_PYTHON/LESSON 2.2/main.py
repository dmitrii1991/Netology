from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f: # читаем адресную книгу в формате CSV в список contacts_list
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def opt_contact(contacts_list: list):
    number = r'(\+7|8)(\s?)(\()?(\d{3})(\)?)(\s?)(\-?)(\d{3}?)(\d{2})?(\d{2})?(\-?)(\d{2})(\-?)(\d{2})(\s?)(\()?([добавочный.]+\s?\d+)?(\))?'

    for contact in contacts_list[1:len(contacts_list)]:
        opt_mobile = re.sub(number, r"+7(\4)\8-\12-\14 \17", contact[5])
        contact[5] = opt_mobile  # приводим в соответствие моб тел
        contact[0], contact[1], contact[2], *args = " ".join(contact[0:3]).split(' ')  # разбиваем на позиции ФИО
        if len(contact) > 7:  # проверяем на лищние "ячейки"
            del contact[7:]
    print(len(contacts_list))

    ph_b = {}  # фильтр на повтор контакты и добавление недостающ данных
    for contact in contacts_list:
        if contact[0] not in ph_b.keys():
            ph_b[contact[0]] = contact[1:]
        else:
            for i, item in enumerate(contact[1:]):
                if ph_b[contact[0]][i - 6] == '':
                    ph_b[contact[0]][i - 6] = item

    opt_phone_list = []  # перепись в новый словарь
    for key, value in ph_b.items():
        new_contact = []
        new_contact.append(key)
        for _ in value:
            new_contact.append(_)
        opt_phone_list.append(new_contact)

    with open("phonebook.csv", "w", encoding="utf8") as ph_book:
        data = csv.writer(ph_book, delimiter=',')
        data.writerows(opt_phone_list)

    return opt_phone_list

pprint(opt_contact(contacts_list))
