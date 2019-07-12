from datetime import datetime
import csv
import re
from pymongo import MongoClient
from pprint import pprint

def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        tikets_list = []
        for line in reader:
            tikets_dict = {
                'Исполнитель': line['Исполнитель'],
                'Цена': int(line["Цена"]),
                'Место': line["Место"],
                'Дата': datetime.strptime(line["Дата"] + '.2019', '%d.%m.%Y')
            }
            tikets_list.append(tikets_dict)
        db.insert_many(tikets_list)
        return list(db.find())

def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    cheapest= db.aggregate(
        [
            {'$sort': {'Цена': 1}}
        ]
    )
    return list(cheapest)

def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """
    find_name = re.escape(name)
    regex = re.compile(find_name)
    result = db.find({'Исполнитель': regex })
    return list(result)


def find_by_date(date, db):
    """
     Cортировкa по дате мероприяти
     """
    start = datetime.strptime('01.' + date, '%d.%m.%Y')
    finish = datetime.strptime('31.' + date, '%d.%m.%Y')
    find_date = db.find(
             {'Дата':
                 {
                 '$gte': start,
                 '$lte': finish,
                 }
             }
    )
    return list(find_date)


if __name__ == '__main__':

    client = MongoClient()
    db = client.db
    tikets = db.tikets

    pprint(read_data('artists.csv', tikets))
    pprint(find_cheapest(tikets))
    pprint(find_by_name('T-Fest', tikets))
    pprint(find_by_date('12.2019', tikets))
