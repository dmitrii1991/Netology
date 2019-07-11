from datetime import datetime
import csv
import re
from pymongo import MongoClient

client = MongoClient()
db = client.tickets


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        tickets_data = []
        for line in reader:
            line['Цена'] = int(line['Цена'])
            date_str = line['Дата'] + f'.{datetime.now().year}'
            tickets_data.append(line)
        concert_tickets = db.concert
        concert_tickets.insert_many(tickets_data)



if __name__ == '__main__':
    read_data('artists.csv', db)

