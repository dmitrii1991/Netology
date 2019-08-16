import collections
import csv
import pprint

with open('inflation_russia.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';', )
    total_data = {}
    keys = list(reader.__iter__().__next__().keys())

    for raw in reader:
        data = {key: float(raw[key]) for key in keys[1:]}
        total_data[raw[keys[0]]] = data

    context = {'total_data': total_data}

    # for i, s in total_data.items():
    #     for w, e in s.items():
    #         print(e)
    #         break
    pprint.pprint(total_data)

