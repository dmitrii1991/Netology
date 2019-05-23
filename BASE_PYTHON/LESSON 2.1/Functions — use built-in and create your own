documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# Задача №1
def people(numbers):
    for document in documents:
        i = 0
        if document["number"] == numbers:
            print(document["name"])
        else:
            i += 1
    if i != 0:
        print("Такого документа нет в Базе")


def list1(documents):
    li = []
    i = -1
    for document in documents:
        # print(document["type"],document["number"],document["name"])  #первое решение
        li = [document["type"], document["number"], document["name"]]
        print(li[0], li[1], li[2])


def shelf(numbers):
    _ = 0
    for i in range(len(directories)):
        ic = str(i + 1)
        if numbers in directories[ic]:
            print("номер полки", ic)
            _ += 1
    if _ == 0:
        print("номерa полки нет в Базе")


def add():
    type_doc = str(input("Тип документа"))
    number = str(input("Номер документа"))
    name = str(input("Имя ваше"))
    direct = str(input("Номер  полки"))
    try:
        directories[direct].append(number)
    except KeyError:
        print("нет такой полки! ")
    documents.append({"type": type_doc, "number": number, "name": name})
    return documents, directories


def delete(numbers):
    i = -1
    _ = 0
    __ = 0
    for document in documents:
        i += 1
        if document["number"] == numbers:
            del documents[i]
            _ += 1
    for icd in range(len(directories)):
        ic = str(icd + 1)
        if numbers in directories[ic]:
            ind = directories[ic].index(numbers)
            del directories[ic][ind]
            __ += 1
    if _ != 0 and __ != 0:
        return documents, directories
    else:
        print("Такого документа нет в Базе")


def move():
    _ = 0
    __ = 0

    numbers = str(input("Номер документа"))
    direct = str(input("Нужная полка"))

    for i in range(len(directories)):
        ic = str(i + 1)
        for number in directories[ic]:
            if number == numbers:
                ind = directories[ic].index(number)
                del directories[ic][ind]
                _ += 1
    if direct in directories.keys():
        __ += 1
    if _ != 0 and __ != 0:
        directories[direct].append(numbers)
        print(directories)
        print(_)
        return directories
    else:
        print("данные не корректны")


def add_shelf():
    direct = str(input("Номер новой полки"))
    if direct not in directories.keys():
        directories[direct] = []
        return directories
    else:
        print("Такая полка есть")


command = str(input("Введите команду"))

if command == "p":
    numbers = input("Введите номер документа")
    people(numbers)
elif command == "l":
    list1(documents)
elif command == "s":
    numbers = input("Введите номер документа")
    shelf(numbers)
elif command == "a":
    add()
elif command == "d":
    numbers = input("Введите номер документа")
    delete(numbers)
    print(directories)
elif command == "m":
    move()
elif command == "as":
    add_shelf()
    print(directories)
else:
    print("нет такой команды")
