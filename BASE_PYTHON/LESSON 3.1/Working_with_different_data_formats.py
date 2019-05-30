import json
from pprint import pprint

with open("newsafr.json", "r", encoding='utf-8') as datafile:
	json_data = json.load(datafile)

sum_words = {}

for i in range(len(json_data['rss']["channel"]["items"])):
	for word in json_data['rss']["channel"]["items"][i]['description'].split(" "):
		if len(word) > 6:
			if word.lower() not in sum_words.keys():
				sum_words[word.lower()] = 1
			else:
				sum_words[word.lower()] += 1

list_sum_words = list(sum_words.items())
list_sum_words.sort(key=lambda i: i[1])
list_sum_words.reverse()

for i in range(10):
	print("WORD: ",list_sum_words[i][0], "meet", list_sum_words[i][1], "times")

#------------------------------------------------------------------------------------------------------
import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")

sum_words = {}
print("")
items = tree.findall("channel/item/description")

for  item in items:
	for word in item.text.split(" "):
		if len(word) > 6:
				if word.lower() not in sum_words.keys():
					sum_words[word.lower()] = 1
				else:
					sum_words[word.lower()] += 1

list_sum_words = list(sum_words.items())

list_sum_words.sort(key=lambda i: i[1])
list_sum_words.reverse()

for i in range(10):
	print("WORD: ",list_sum_words[i][0], "meet", list_sum_words[i][1], "times")
