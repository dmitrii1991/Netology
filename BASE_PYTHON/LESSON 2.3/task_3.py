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


def out_name(documents):
	for document in documents:
		try:
			print(document["name"])
		except (KeyError) as e:
			print(f"{type(e)}, {e}")


command = str(input("Введите команду"))

if command == "o":
	out_name(documents)
else:
	print("нет такой команды")
