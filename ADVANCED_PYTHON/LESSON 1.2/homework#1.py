import json
import wikipedia

class Find_coun_wiki:
    def __init__(self, countries):
        self.countries = countries
        self.start = - 1
        self.end = len(countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.countries[self.start]["name"]["official"], wikipedia.page(self.countries[self.start]["name"]
                                                                              ["official"]).url


with open("countries.json", "r", encoding='utf-8') as datafile:
    json_counries = json.load(datafile)

    for country in Find_coun_wiki(json_counries):
        with open('countries.txt', 'w', encoding='utf-8') as data:
            print(country)
            print(country, file=data)
